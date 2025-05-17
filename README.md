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


Here are some business questions we can now figure out:-

1.Which caategory brings the highest Revenue?
---->T-shirt category brings the highest revenue.

2.What is top selling product by quantity?
-----> T-shirt is the top selling product by quantity of more than 40,000

3.Which is the lowest selling product by quantity and category?
-----> Watch is the lowest selling product by category and quantity.

4.Give the percentage of fulfillment type distribution by others and Easy Ship?
------> It's around 30% by Easy Ship and 70% by others.

5.Arrange top 10 category by sales in Descending Order? -------> T-shirt > Shirt > Blazzer > Trousers > Perfume > Wallet > Socks > Shoes > Watch .

6.Give the name for top 2 states by sales?

-----> Maharashtra and Karnataka are top 2 states by sales .

7.Give the name for the 2 states with the least sales?
-----> Andhra Pradesh and Haryana are the states ith the lowest sales.

8. Among B2B and B2C which has the most toal sales and what could be the reason?
-----> B2B has a total sales around Rs.77,979,068 with B2C having total sales of around Rs. 591,480.
   the reason could be because customers are making small purchases but it is making the sales high , instead of purchasing in bulk.

   1.Amazon is primarily a B2C platform
   
   2.B2C customers make frequent small purchases.
   
   3.B2B buyers often purchase through procurement platforms, not retail channels.
   
   4.B2B purchases are usually bulk but less frequent, so total volume may look smaller depending on the time frame.
   
   5.B2B buyers may prefer dedicated wholesale platforms or direct vendor relationships.








   RECOMMENDATIONS:-

   1.  Geographic Focus on High Revenue States
Maharashtra and Karnataka are top-performing states.
Recommendation: Target ads and faster delivery in these states for better ROI.

   2.   Customer Segment TargetingExpand Fulfillment via Easy Ship
Only 30% of orders are fulfilled by Easy Ship.
Recommendation: Leverage Amazon Easy Ship more to ensure timely deliveries and better customer experience.


  3.  B2B customers contribute significantly to sales.
 Recommendation: Offer special deals or subscriptions for B2B clients.

  4.   T-shirts have the highest sales volume and revenue.
Recommendation: Increase inventory and run promotions for T-shirts and other top-selling categories.


  5.    Discontinue or Discount Low-Selling Items
Watches are the lowest selling category.
Recommendation: Consider discontinuing or offering heavy discounts on watches to clear inventory.

