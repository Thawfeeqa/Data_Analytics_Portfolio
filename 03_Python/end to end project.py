import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_excel(
    r"C:\Users\user\Downloads\DataCoSupplyChainDataset.PROJECT.xlsx",
    sheet_name="DataCoSupplyChainDataset.PROJEC")
print(df.shape)
print(df.isnull().sum())
print(df.head())
print(df.describe())
print(df.info())
print(df.tail())
print("duplicate rows:",df.duplicated().sum())
print(df.dtypes)
print(df.nunique())
df = df.drop(columns=[
    'Product Description',
    'Order Zipcode',
    'Customer Email',
    'Customer Password',
    'Product Image',
    'Customer Street'
])
print("Shape after dropping columns:", df.shape)
print(df.columns)
df["Customer Lname"] = df["Customer Lname"].fillna("Unknown")
print(df["Customer Lname"].isnull().sum())
df['order date (DateOrders)'] = pd.to_datetime(
    df['order date (DateOrders)'],
    format='mixed',
    errors='coerce'
)

df['shipping date (DateOrders)'] = pd.to_datetime(
    df['shipping date (DateOrders)'],
    format='mixed',
    errors='coerce'
)
print(df['order date (DateOrders)'].isnull().sum())
print(df['shipping date (DateOrders)'].isnull().sum())
print(df[['order date (DateOrders)', 'shipping date (DateOrders)']].dtypes)
print(df[['order date (DateOrders)','shipping date (DateOrders)']].head())
df.to_excel("DataCoSupplyChain_Clean.xlsx",index=False)
print("successfully Data CLEANED")

Delivery_Status=df["Delivery Status"].value_counts()
print(Delivery_Status)
import matplotlib.pyplot as plt
plt.figure(figsize=(8,5))
Delivery_Status.plot(kind="bar",color="skyblue")
plt.title("Delivery_Status_Distribution")
plt.xlabel("Delivery_Status")
plt.ylabel("Number of Orders")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("Delivery_Status.png", dpi=300, bbox_inches="tight")
plt.show()


late=df["Late_delivery_risk"].value_counts()
print(late)
plt.figure(figsize=(6,4))
late.plot(kind="bar",color=["green","red"])
plt.title("Late Delivery Risk")
plt.xlabel("risk")
plt.ylabel("Number of Orders")
plt.xticks([0,1],["No Risk","Late Risk"],rotation=0)
plt.tight_layout()
plt.savefig("Late_Delivery_risk.png", dpi=300, bbox_inches="tight")
plt.show()

shipping = df['Shipping Mode'].value_counts()
print(shipping)
plt.figure(figsize=(8,5))
shipping.plot(kind='bar', color='orange')
plt.title('Orders by Shipping Mode')
plt.xlabel('Shipping Mode')
plt.ylabel('Number of Orders')
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("Shipping_Mode.png", dpi=300, bbox_inches="tight")
plt.show()


import seaborn as sns
import matplotlib.pyplot as plt
plt.figure(figsize=(8,5))
sns.histplot(df["Sales"],bins=30,kde=True)
plt.title("Sales Distribution")
plt.xlabel("Sales")
plt.ylabel("Count")
plt.savefig("Sales_Distribution.png", dpi=300, bbox_inches="tight")
plt.show()


















