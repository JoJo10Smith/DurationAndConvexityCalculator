# DurationAndConvexityCalculator
A VBA and excel workbook that calculates the Macaulay and Modified durations and convexities for bonds, stocks, level perpetuities, and annutities

***Excel and VBA component***

The duration and convexity of an asset is useful for an investor to know since it will tell them how much they can expect to lose/gain when interest rates change. I was able to build an excel workbook that uses user input and calculates both the Modified and Macaulay durations and convexities for a wide range of assets. After getting user input, the workbook is able to calculate all the values and ouput them in the excel sheet.

***Graphing Component***

I found during my analysis that the price yeild curve changes over time - the price-yeild curve for a bond is not the same throughout the life of the bond. To show the relationship between the price-yeild curve and time I wrote a python program that plots the different price-yeild curve and connects them to create a price-yeild-time curve. I found that some bonds - depending on the interest rate - changed a lot during the life of the bond as illustated in the graph below

![Price-yeild-time curve image #1](https://github.com/JoJo10Smith/DurationAndConvexityCalculator/blob/main/Example_Images/price-yeild-time_1.JPG)

While other bonds did not change as drastically to changes in interest rate. An example of a bond is given by the price-yeild-time curve below. 

![Price-yeild-time curve image #2](https://github.com/JoJo10Smith/DurationAndConvexityCalculator/blob/main/Example_Images/price-yeild-time_2.JPG)

From this it is clear to see that some bonds protect their holder better against changes in interest rate over time when compared to other bonds. If you as an investor predict that there will be a change in interest rates before your bonds maturity date then you need to precedt the value of that bond. Using this tool you can easily visualize which bonds would reduce your risk to changes in interest rate.

If you have any questions or suggestions please email me at: jsmith58@bryant.edu
