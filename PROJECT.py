import pandas as pd
import matplotlib.pyplot as plt

url = 'C:/Users/Gaurav Vishwakarma/Desktop/MFDS/Train.csv'
df = pd.read_csv(url)
skew_value = df['Item_Outlet_Sales'].skew()
print(f"Skewness value for Item_Outlet_Sales :- {skew_value}")

kurt_value = df['Item_Outlet_Sales'].kurt()
print(f"Kurotosis value for Item_Outlet_Sales :- {kurt_value}")

sales = df['Item_Outlet_Sales']

plt.hist(sales,'auto',ec='black')
plt.title('Sales Distribution')
plt.xlabel('Item_Outline_Sales')
plt.ylabel('Count')
plt.show()



