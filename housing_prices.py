import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read CSV
df = pd.read_csv('Housing.csv') 

# Scale the price values to millions
df['price'] = df['price'] / 1_000_000

# Define number of subplots for #1,#2, #3
fig, axs = plt.subplots(1, 3, figsize=(16, 5)) 

###### 1. Price vs Area 2D Histogram
hist1 = axs[0].hist2d(df['area'], df['price'], bins=[30, 30], cmap='Blues')
fig.colorbar(hist1[3], ax=axs[0], label='Counts')
axs[0].set_title('Price vs Area 2D Histogram')
axs[0].set_xlabel('Area (sqft)')
axs[0].set_ylabel('Price (Million)')

###### 2. Price vs Bedrooms 2D Histogram
hist2 = axs[1].hist2d(df['bedrooms'], df['price'], bins=[10, 30], cmap='Greens')
fig.colorbar(hist2[3], ax=axs[1], label='Counts')
axs[1].set_title('Price vs Bedrooms 2D Histogram')
axs[1].set_xlabel('Number of Bedrooms')
axs[1].set_ylabel('Price (Million)')

###### 3. Price vs Stories 2D Histogram
hist3 = axs[2].hist2d(df['stories'], df['price'], bins=[10, 30], cmap='Reds')
fig.colorbar(hist3[3], ax=axs[2], label='Counts')
axs[2].set_title('Price vs Stories 2D Histogram')
axs[2].set_xlabel('Number of Stories')
axs[2].set_ylabel('Price (Million)')

plt.tight_layout()
plt.show()


# Define number of subplots for #4, #5
fig, axs = plt.subplots(1, 2, figsize=(12, 5)) 

###### 4. AVERAGE PRICES ACCORDING TO BATHROOMS (
avg_price_by_bathrooms = df.groupby('bathrooms')['price'].mean()

sns.barplot(ax=axs[0], x=avg_price_by_bathrooms.index, y=avg_price_by_bathrooms.values)  # Use axs[0] for the first subplot
axs[0].set_title('Average House Prices According to Number of Bathrooms', fontsize=14)
axs[0].set_xlabel('Number of Bathrooms', fontsize=12)
axs[0].set_ylabel('Average Price (million)', fontsize=12)

####### 5. AVERAGE PRICES ACCORDING TO FURNISHING STATUS 
avg_price_by_furnishingStatus = df.groupby('furnishingstatus')['price'].mean()

sns.barplot(ax=axs[1], x=avg_price_by_furnishingStatus.index, y=avg_price_by_furnishingStatus.values)  # Use axs[1] for the second subplot
axs[1].set_title('Average House Prices According to Furnishing Status', fontsize=14)
axs[1].set_xlabel('Furnishing Status', fontsize=12)
axs[1].set_ylabel('Average Price (million)', fontsize=12)


plt.tight_layout()  # Adjust spacing between subplots
plt.show()

###### 6. CORRELATION MATRIX HEATMAP

# Mapping 'Yes/No' to binary values
df['mainroad'] = df['mainroad'].map({'yes': 1, 'no': 0})
df['guestroom'] = df['guestroom'].map({'yes': 1, 'no': 0})
df['basement'] = df['basement'].map({'yes': 1, 'no': 0})
df['hotwaterheating'] = df['hotwaterheating'].map({'yes': 1, 'no': 0})
df['airconditioning'] = df['airconditioning'].map({'yes': 1, 'no': 0})
df['prefarea'] = df['prefarea'].map({'yes': 1, 'no': 0})
df['furnishingstatus'] = df['furnishingstatus'].map({'unfurnished': 0, 'semi-furnished': 1, 'furnished': 2})

# Select only numeric columns for correlation
numeric_df = df.select_dtypes(include='number')
corr_matrix = numeric_df.corr()

# Heatmap Visualization
plt.figure(figsize=(8, 5))
sns.heatmap(corr_matrix, annot=True, fmt=".2f", cmap='coolwarm', linewidths=0.5)
plt.title('Correlation Matrix Heatmap', fontsize=16)
plt.xticks(rotation=45, ha='right') 
plt.yticks(rotation=0)  
plt.tight_layout() 
plt.show()