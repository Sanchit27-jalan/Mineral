import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Create DataFrame from the CSR spending data
data = {
    'Financial Year': ['2019-20', '2020-21', '2021-22', '2022-23', '2023-24', '2024-25(Current)'],
    'Healthcare': [18.50, 26.44, 45.55, 35.72, 32.07, 13.40],
    'Education': [0.91, 4.74, 15.32, 12.77, 7.25, 5.12],
    'Water Supply': [0.69, 0.24, 0.00, 0.00, 0.00, 0.00],
    'Environmental Sustainability': [5.62, 0.11, 4.36, 0.42, 0.24, 1.09],
    'Rural Development': [1.94, 2.24, 5.14, 2.48, 6.54, 4.25],
    'Others': [56.99, 4.56, 9.45, 7.89, 6.97, 1.49],
    'Total': [84.65, 38.33, 79.82, 59.28, 53.07, 25.35]
}

df = pd.DataFrame(data)

# Set style for better visuals
sns.set(style="whitegrid")

# 1. Yearly Total Spending Visualization
plt.figure(figsize=(12, 6))
ax = sns.barplot(x='Financial Year', y='Total', data=df, palette='viridis')
plt.title('Yearly Total CSR Spending (Rs. in Crore)', fontsize=16, fontweight='bold')
plt.xlabel('Financial Year', fontsize=12)
plt.ylabel('Amount (Rs. in Crore)', fontsize=12)
plt.xticks(rotation=45)

# Add value labels on the bars
for i, val in enumerate(df['Total']):
    ax.text(i, val + 1, f'{val:.2f}', ha='center', fontweight='bold')

# Add gridlines for better readability
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()
# Save the yearly spending figure
plt.savefig('yearly_csr_spending.png', dpi=300, bbox_inches='tight')
plt.close()

# 2. Sector-wise Spending Visualization
# Calculate the total for each sector across all years
sectors = ['Healthcare', 'Education', 'Water Supply', 
           'Environmental Sustainability', 'Rural Development', 'Others']
sector_totals = df[sectors].sum().sort_values(ascending=False)

plt.figure(figsize=(12, 6))
bars = sns.barplot(x=sector_totals.index, y=sector_totals.values, palette='tab10')
plt.title('Total CSR Spending by Sector (Rs. in Crore)', fontsize=16, fontweight='bold')
plt.xlabel('Sector', fontsize=12)
plt.ylabel('Total Amount (Rs. in Crore)', fontsize=12)
plt.xticks(rotation=45, ha='right')

# Add value labels on the bars
for i, val in enumerate(sector_totals.values):
    bars.text(i, val + 2, f'{val:.2f}', ha='center', fontweight='bold')

# Add gridlines for better readability
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()
# Save the sector-wise spending figure
plt.savefig('sector_wise_csr_spending.png', dpi=300, bbox_inches='tight')
plt.close()

# 3. Sector-wise Pie Chart
plt.figure(figsize=(10, 8))
plt.pie(sector_totals, labels=sector_totals.index, autopct='%1.1f%%', 
        startangle=90, shadow=True, 
        colors=sns.color_palette('tab10', len(sectors)))
plt.axis('equal')  # Equal aspect ratio ensures the pie chart is circular
plt.title('Distribution of CSR Spending by Sector (2019-2024)', fontsize=16, fontweight='bold')

# Add a legend with absolute values
legend_labels = [f'{sector}: ₹{sector_totals[sector]:.2f} Cr' for sector in sector_totals.index]
plt.legend(legend_labels, loc='center left', bbox_to_anchor=(1, 0.5))

plt.tight_layout()
# Save the sector-wise pie chart
plt.savefig('sector_wise_pie_chart.png', dpi=300, bbox_inches='tight')

print("Visualizations have been created and saved as:")
print("1. yearly_csr_spending.png")
print("2. sector_wise_csr_spending.png")
print("3. sector_wise_pie_chart.png")