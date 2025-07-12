import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv('amazon_sales_data.csv', parse_dates=['Date'])

df['Month'] = df['Date'].dt.to_period('M').astype(str)

# ---------- 1. Monthly Sales Trend ----------
monthly_sales = df.groupby('Month')['Sales'].sum().reset_index()

plt.figure(figsize=(8,5))
sns.lineplot(data=monthly_sales, x='Month', y='Sales', marker='o')
plt.title('Monthly Sales Trend')
plt.xlabel('Month')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('monthly_sales_trend.png')
plt.close()

# ---------- 2. Category-wise Sales ----------
category_sales = df.groupby('Category')['Sales'].sum().reset_index().sort_values(by='Sales', ascending=False)

plt.figure(figsize=(10,6))
sns.barplot(data=category_sales, x='Sales', y='Category', palette='viridis')
plt.title('Category-wise Sales')
plt.tight_layout()
plt.savefig('category_sales.png')
plt.close()

# ---------- 3. Top Cities by Sales ----------
top_cities = df.groupby('City')['Sales'].sum().reset_index().sort_values(by='Sales', ascending=False).head(10)

plt.figure(figsize=(10,6))
sns.barplot(data=top_cities, y='City', x='Sales', palette='magma')
plt.title('Top 10 Cities by Sales')
plt.tight_layout()
plt.savefig('top_cities.png')
plt.close()

# ---------- 4. Top States by Sales ----------
top_states = df.groupby('State')['Sales'].sum().reset_index().sort_values(by='Sales', ascending=False).head(10)

plt.figure(figsize=(10,6))
sns.barplot(data=top_states, y='State', x='Sales', palette='coolwarm')
plt.title('Top 10 States by Sales')
plt.tight_layout()
plt.savefig('top_states.png')
plt.close()

