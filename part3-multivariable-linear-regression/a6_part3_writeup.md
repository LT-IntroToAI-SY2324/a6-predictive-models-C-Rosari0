# Part 3 - Multivariable Linear Regression Writeup

After completing `a6_part3.py` answer the following questions

## Questions to answer

1. What is the R Squared coefficient for your model? What does that mean about the model in relation to your data?
he r squared coefficient is 0.85. This means that a larger proportion of the variance in the targe can be explained by the independent features in the model

2. Is your model accurate? Why or why not?
i say its pretty accurate if my predicted prices are close to the actual prices 

3. What does the model predict a 10-year-old car with 89000 miles is worth? What about a car that is 20 years old with 150000 miles?
Predicted price for Car 1: $8983.56
Predicted price for Car 2: $1912.18


4. You may notice that some of your predicted results are negative. This is occurring when the value of age and the mileage of the car are very high. Why do you think this is happening?

The model is reading passed the data wall 