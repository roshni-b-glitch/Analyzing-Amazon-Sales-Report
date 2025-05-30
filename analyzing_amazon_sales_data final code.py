# -*- coding: utf-8 -*-
"""Analyzing Amazon Sales Data.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ogAyGK_1-IEDR3l6m2i9TPWkrRJwuKUY
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

pd.read_csv('/content/Amazon Sale Report.csv')

df=pd.read_csv('/content/Amazon Sale Report.csv')

df.head()

df.tail()

df.info()# checking for datatype information

df.isnull()#cheking for null values.



"""Here we got True and False. True means it has null values and False means i do not have any null values.
If we are facing a lot of null values then probably the column is of no use for us, or else if e have some null values we can probably assign it "unknown" or "others".

New and Pendings column has a lot of null values so will drop it.
"""

#dropping the null values.
df.drop(['New','PendingS'],axis=1,inplace=True) #axis tells to drop column not rows

#after dropping check if the column is dropped?
df.info()

"""Here the two columns are dropped and now if we see fullfilled-by column we can find that some of the values of NAN so instead of dropping the whole column we can simply put "others" in place of NAN.

We are doing it because in analysis of our project fullfilled by Easy Ship is done by amazon's logistic service , so here we can compare amazon's logistic services with others they may be a other country or may be the data was not recorded.
"""

df['fulfilled-by'].fillna('others',inplace=True)

#check if the NAN is filled by others in fulfilled-by column or not?
df.head()

"""Now as we did df.info() above it is given that our date is in object datatype. if date is in object datatype Python treats it as plain text, making it difficult to analyze. so converting it into datetime format will help us to make datetime as our index which will hwlp in analysis"""

df["Date"]=pd.to_datetime(df["Date"])

#checking if the object is converted to datetime or not?
df.info()

#set datetime as index
df.set_index('Date',inplace=True)

df.info()

df['ship-postal-code'] = df['ship-postal-code'].astype(str)

df.head()

#dropping the original index
df.drop(columns=['index'],inplace=True)

df.info()

print(df.index)

"""here we have successfullu checked for the index column"""

df.info()

#check for null values again
df.isnull().sum()

"""Here we have 35 missing values in ship-city,ship-state,ship-postal-code,ship-country, so we can safely drop the null values as they are not a big deal in much data."""

df = df.dropna(subset=['ship-city', 'ship-state', 'ship-postal-code', 'ship-country'])

df.isnull().sum()

df.isnull().sum()

df.info()

df.head()

# Set Date as index
df.set_index('Date', inplace=True)

print(df.info())

# Check for duplicate rows
duplicates = df[df.duplicated()]
print(duplicates)

# Check for exact duplicates
df.duplicated().sum()

!git config --global user.name "roshni-b-glitch"
!git config --global user.email "roshnibarua83@gmail.com"

!git clone https://github.com/roshni-b-glitch/Analyzing-Amazon-Sales-Report.

print(df.columns.tolist())  # Check again

df.index

df.isnull().sum()

df[df['Amount'].isnull()].head()

df.isnull().sum()

df[df['Amount'].isnull()]['Courier Status'].value_counts()

df['Amount'].fillna(0, inplace=True)
df['currency'].fillna('NA', inplace=True)
#let's fill NA in place of missing values it will be useful whenever we need toanalyx=ze cancellation of order

df.isnull().sum()

df.describe()

"""Here the count of amount and qty are same that means that there are no further missing values, and for each quantity there is a amount present.

mean tells us that People almost buy  1 item per order and also on average people spend Rs.609 ON Per order.

(Mean is the average value, it sums up all the values and divided by total numbers)

Std is the Standard deviation , it  shows how much the values vary from the average (mean).
it tells us how spread out the data is !!

here the qty is close to one means there is not much variation, if we see the amiunt then mean=609 and std=313, means spending is around 600 more or less.

25% of orders were of around 413, 50% of order was around 583 also known as the median and 75% o order was around 717.

Max tells us that one of the largest order is around Rs.5584, it may be in bulk
"""

df.describe(include='object')  # For categorical columns

#Row	Meaning (Took the help of Website).
#count	How many rows (orders) there are — here, 128,941.
#unique	How many different values each column has.
#top	The most common (frequent) value in that column.
#freq	How many times that top value appears.

# Group sales by date
daily_sales = df.groupby(df['order-date'].dt.date)['Amount'].sum()

print(df.columns)

df.rename(columns={'Date': 'order-date'}, inplace=True)

#Sales Trend over Time
df['Amount'].resample('M').sum().plot(figsize=(12,6), title='Monthly Sales Trend')
plt.ylabel("Total Sales Amount")
plt.show()

#Top Categories/Product by sales
top_products.plot(kind='bar', title='Top 10 Categories by Sales')
plt.ylabel("Sales Amount")
plt.xticks(rotation=45)#to prevent overlapping we used rotation.
plt.show()

#order by fulfillment type
df['fulfilled-by'].value_counts().plot(kind='pie',autopct='%1.0f%%',title='Fulfillment Type Distribution')
plt.ylabel('')
plt.show()
#autopct will show the percentage in our pie chart.

#Sales by State/Country
df.groupby('ship-state')['Amount'].sum().sort_values(ascending=False).head(10).plot(kind='bar', title='Top States by Sales')
plt.xticks(rotation=45)
plt.ylabel("Sales Amount(Rs)")
plt.show()

# Extract Year, Month, and Weekday into new columns
df['Year'] = df.index.year
df['Month'] = df.index.month
df['Weekday'] = df.index.day_name()

print(df.columns)

#identify the top selling products.
top_selling_by_qty = df.groupby('Category')['Qty'].sum().sort_values(ascending=False).head(10)
print(top_selling_by_qty)

"""Conclusion:- T-shirt is among the top selling products, followed by shirts and blazzer.
Most low sell product includes Watch followed by shoes, socks wallet and perfumes.
"""

# Top-selling by category and state
df.groupby(['Category', 'ship-state'])['Qty'].sum().sort_values(ascending=False).head(5)

# Top-selling by month
df.groupby(['Category', 'Month'])['Qty'].sum().sort_values(ascending=False).head(5)

#Visualization for top 10 selling products by quantity

top_selling_by_qty.plot(kind='bar', title='Top 10 Selling Products by Quantity', ylabel='Total Quantity', figsize=(10,5))
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

"""Conclusion:- The top selling Category is T-shirt and the least selling category is watch."""

df['Total_Revenue'] = df['Qty'] * df['Amount']

# Print the new column
print(df[['Qty', 'Amount', 'Total_Revenue']].head())

#Total revenue by category
total_revenue_by_category = df.groupby('Category')['Total_Revenue'].sum().sort_values(ascending=False)
print(total_revenue_by_category)

"""Revenue refers to the total income a business earns from selling goods or services before any expenses are deducted."""

#Visualization for total revenue by category.
total_revenue_by_category.plot(kind='bar', figsize=(9,6), title='Total Revenue by Category')
plt.ylabel('Revenue')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

"""Here are some business questions we can now figure out:-

1. Which caategory brings the highest Revenue?
---->T-shirt category brings the highest revenue.

2. What is top selling product by quantity?
-----> T-shirt is the top selling product by quantity
       of more than 40,000

3.  Which is the lowest selling product by quantity
   and category?
-----> Watch is the lowest selling product by category
      and quantity.

4.  Give the percentage of fulfillment type
   distribution by others and Easy Ship?
------> It's around 30% by Easy Ship and 70% by
      others.        

5. Arrange top 10 category by sales in Descending
   Order?
 -------> T-shirt > Shirt > Blazzer > Trousers > Perfume > Wallet > Socks > Shoes > Watch  .

6. Give the name for top 2 states by sales?
-----> Maharashtra and Karnataka are top 2 states by sales .

7. Give the name for the 2 states with the least sales?
-----> Andhra Pradesh and Haryana are the states ith the lowest sales.


"""

print(df['B2B'].unique())

# Group by 'B2B' column and sum the 'Amount' (total sales)
sales_by_b2b_b2c = df.groupby('B2B')['Amount'].sum()

# Or count the number of occurrences for each category (count of sales)
count_by_b2b_b2c = df['B2B'].value_counts()
print(sales_by_b2b_b2c)
print(count_by_b2b_b2c)

# Group and sum sales by 'B2B' and 'B2C'
sales_by_b2b_b2c = df.groupby('B2B')['Amount'].sum()

# Or just count the number of occurrences
count_by_b2b_b2c = df['B2B'].value_counts()

sales_by_b2b_b2c.plot(kind='bar', title='Total Sales by B2B vs B2C')
plt.xticks([0, 1], ['B2C', 'B2B'], rotation=0)
plt.ylabel('Total Sales (₹)')
plt.tight_layout()
plt.show()

count_by_b2b_b2c.plot(kind='bar', title='Order Count by B2B vs B2C')
plt.xticks([0, 1], ['B2C', 'B2B'], rotation=0)
plt.ylabel('Number of Orders')
plt.tight_layout()
plt.show()

# Group by 'B2B' and sum the 'Amount' to get total sales for B2B and B2C
sales_by_b2b_b2c = df.groupby('B2B')['Amount'].sum()

# Plot the bar chart
ax = sales_by_b2b_b2c.plot(kind='bar', title='Total Sales by B2B vs B2C', color=['skyblue', 'lightgreen'])

# Set labels and title
plt.xticks([0, 1], ['B2C', 'B2B'], rotation=0)
plt.ylabel('Total Sales (₹)')
plt.tight_layout()

# Add sales amounts on top of each bar
for i, v in enumerate(sales_by_b2b_b2c):
    ax.text(i, v + 1000, f'₹{v:,.0f}', ha='center', va='bottom', fontsize=12)

# Show the plot
plt.show()

"""Here we can move to a conclusion that B2B has a total sales around Rs.77,979,068 with B2C having total sales of around Rs. 591,480.

Business to Customer demand is high rather than Business to Business, Which is usually in bulk purchase.
"""

sales_over_time = df.groupby('Month')['Amount'].sum()
print(sales_over_time)

# Plotting the sales over time
plt.figure(figsize=(10,6))
sales_over_time.plot(kind='line', marker='o', color='b', title='Sales Over Time (Monthly)')
plt.xlabel('Month')
plt.ylabel('Total Sales (₹)')
plt.grid(True)
plt.xticks(rotation=45)  # Rotate month labels for better readability
plt.tight_layout()
plt.show()

