#https://plotly.com/python/3d-surface-plots/
import plotly.graph_objects as go
import numpy as np

INTEREST_RATE_START, INTEREST_RATE_END = 0,50 
NUMBER_OF_YEARS = 30
FACE_VALUE = 1000
COUPON_RATE = 4

def calculate_price(interest_rate,coupon_rate,years_remaining,face_value=1000):
  #calculate the present value of the bond given the parameters
  interest_rate /=100
  coupon_rate /= 100 
  coupon_payments = face_value * coupon_rate
  present_value = 0
  for current_year in range(1,years_remaining):
    current_price = coupon_payments * (1+interest_rate) ** -current_year
    present_value += current_price

  present_value += (face_value+coupon_payments) * (1+interest_rate) ** -years_remaining 
  print ("years_remaining: {}; interest rate: {}; price: {}".format(years_remaining,interest_rate,present_value))
  return present_value


print




interest_rates = []
number_of_years = [30,29,28,17,26,25,24,23,22,21,20,19,18,17,16,15,14,13,12,11,10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
price = []  

for current_interest_rate in range(INTEREST_RATE_START,INTEREST_RATE_END+1):
  interest_rates.append(current_interest_rate)
  interest_rates.append(current_interest_rate+0.25)
  interest_rates.append(current_interest_rate+0.5)
  interest_rates.append(current_interest_rate+0.75)

  for current_periods_remaining in range(NUMBER_OF_YEARS,-1,-1):
    

    #number_of_years.append(current_periods_remaining)

    current_price_yeild_0 = []

    current_price_yeild_0.append(-calculate_price(current_interest_rate,COUPON_RATE,current_periods_remaining,FACE_VALUE))
    current_price_yeild_0.append(-calculate_price(current_interest_rate+0.25,COUPON_RATE,current_periods_remaining,FACE_VALUE))
    current_price_yeild_0.append(-calculate_price(current_interest_rate+0.5,COUPON_RATE,current_periods_remaining,FACE_VALUE))
    current_price_yeild_0.append(-calculate_price(current_interest_rate+0.75,COUPON_RATE,current_periods_remaining,FACE_VALUE))

    price.append(current_price_yeild_0)

#defintions 
#t test 
#calculate condidenc intervals



print (interest_rates)
print (" ")
print (number_of_years)

fig = go.Figure(go.Surface(
    contours = {
        "x": {"show": True, "start": INTEREST_RATE_START, "end": INTEREST_RATE_END, "color":"white"},
        "z": {"show": True, "start": 0, "end": 2000}
    },
    x = interest_rates,
    y = number_of_years,
    z = price 
    ))

fig.update_layout(
        scene = {
            "xaxis": {"nticks": 20},
            "zaxis": {"nticks": 4},
            'camera_eye': {"x": 0, "y": -1, "z": 0.5},
            "aspectratio": {"x": 1, "y": 1, "z": 0.2}
        })
fig.show()
