# Analyzing-Amazon-Sales-Report.

Before Analyzing a Data we should understand the data first .
We need to now and understand its columns, what the data is about and what is meant by every columns?
Columns plays a major role also if we wanted to understand terms. They helps you to understand and get close to the objective.


In this dataset each term in column plays a special role , example: B2B as Trur or False will tell you about the business to business or business to consumer relationship.
as it can affect the profit ans sales margin and also can drive decisions and insights on the sales VS quantity !!!




PERFORMING EDA(Exploratory Data Analysis)


df.describe() will let us know about the numeric values for mean,median,maximum and standard deviation.
here what i got:
Here the count of amount and qty are same that means that there are no further missing values, and for each quantity there is a amount present.

mean tells us that People almost buy 1 item per order and also on average people spend Rs.609 ON Per order.

(Mean is the average value, it sums up all the values and divided by total numbers)

Std is the Standard deviation , it shows how much the values vary from the average (mean). it tells us how spread out the data is !!

here the qty is close to one means there is not much variation, if we see the amiunt then mean=609 and std=313, means spending is around 600 more or less.

25% of orders were of around 413, 50% of order was around 583 also known as the median and 75% o order was around 717.

Max tells us that one of the largest order is around Rs.5584, it may be in bulk.

