import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Create the dataframe from the extracted data
data = {
    'Year': [2016, 2017, 2018, 2019, 2020, 2021, 2022],
    'Fatal_Accidents': [2, 2, 11, 3, 6, 2, 4],
    'Serious_Accidents': [4, 4, 2, 6, 0, 1, 4],
    'Killed_Below_Ground': [1, 1, 5, 1, 3, 1, 0],
    'Killed_Opencast': [1, 1, 7, 2, 3, 1, 3],
    'Killed_Above_Ground': [0, 0, 1, 0, 0, 0, 1],
    'Total_Killed': [2, 2, 13, 3, 6, 2, 4],
    'Injured_Below_Ground': [0, 1, 2, 2, 0, 0, 0],
    'Injured_Opencast': [3, 2, 0, 3, 1, 1, 2],
    'Injured_Above_Ground': [1, 1, 1, 1, 0, 0, 2],
    'Total_Injured': [4, 4, 3, 6, 1, 1, 4]
}

df = pd.DataFrame(data)

# Set up the figure with a professional style
plt.style.use('seaborn-v0_8-whitegrid')
fig = plt.figure(figsize=(16, 12))

# Create a 2x2 grid for our charts
gs = fig.add_gridspec(2, 2)

# Chart 1: Accidents Over Time
ax1 = fig.add_subplot(gs[0, 0])
accidents_data = df[['Year', 'Fatal_Accidents', 'Serious_Accidents']]
accidents_data_melted = pd.melt(accidents_data, id_vars=['Year'],
                                var_name='Accident Type',
                                value_name='Count')

sns.barplot(x='Year', y='Count', hue='Accident Type', data=accidents_data_melted, ax=ax1,
            palette=['#d62728', '#1f77b4'])
ax1.set_title('Fatal and Serious Accidents in Korba Coal Mines (2016-2022)', fontsize=14, fontweight='bold')
ax1.set_xlabel('Year', fontsize=12)
ax1.set_ylabel('Number of Accidents', fontsize=12)
ax1.legend(title='Type', title_fontsize=12)

# Chart 2: Fatalities by Location
ax2 = fig.add_subplot(gs[0, 1])
fatalities_data = df[['Year', 'Killed_Below_Ground', 'Killed_Opencast', 'Killed_Above_Ground']]
fatalities_data_melted = pd.melt(fatalities_data, id_vars=['Year'],
                                var_name='Location',
                                value_name='Count')
fatalities_data_melted['Location'] = fatalities_data_melted['Location'].str.replace('Killed_', '')

sns.lineplot(x='Year', y='Count', hue='Location', data=fatalities_data_melted, ax=ax2,
             marker='o', linewidth=2.5, markersize=10, palette='dark')
ax2.set_title('Fatalities by Location in Korba Coal Mines (2016-2022)', fontsize=14, fontweight='bold')
ax2.set_xlabel('Year', fontsize=12)
ax2.set_ylabel('Number of Fatalities', fontsize=12)
ax2.legend(title='Location', title_fontsize=12)

# Chart 3: Serious Injuries by Location
ax3 = fig.add_subplot(gs[1, 0])
injuries_data = df[['Year', 'Injured_Below_Ground', 'Injured_Opencast', 'Injured_Above_Ground']]
injuries_data_melted = pd.melt(injuries_data, id_vars=['Year'],
                             var_name='Location',
                             value_name='Count')
injuries_data_melted['Location'] = injuries_data_melted['Location'].str.replace('Injured_', '')

sns.lineplot(x='Year', y='Count', hue='Location', data=injuries_data_melted, ax=ax3,
             marker='o', linewidth=2.5, markersize=10, palette='colorblind')
ax3.set_title('Serious Injuries by Location in Korba Coal Mines (2016-2022)', fontsize=14, fontweight='bold')
ax3.set_xlabel('Year', fontsize=12)
ax3.set_ylabel('Number of Serious Injuries', fontsize=12)
ax3.legend(title='Location', title_fontsize=12)

# Chart 4: Total Fatalities vs Total Injuries
ax4 = fig.add_subplot(gs[1, 1])
totals_data = df[['Year', 'Total_Killed', 'Total_Injured']]
totals_data_melted = pd.melt(totals_data, id_vars=['Year'],
                           var_name='Type',
                           value_name='Count')
totals_data_melted['Type'] = totals_data_melted['Type'].str.replace('Total_', '')

sns.barplot(x='Year', y='Count', hue='Type', data=totals_data_melted, ax=ax4,
            palette=['#d62728', '#2ca02c'])
ax4.set_title('Total Fatalities vs Serious Injuries in Korba Coal Mines (2016-2022)', fontsize=14, fontweight='bold')
ax4.set_xlabel('Year', fontsize=12)
ax4.set_ylabel('Count', fontsize=12)
ax4.legend(title='Type', title_fontsize=12)

# Add a title to the entire figure
plt.suptitle('Korba Coal Mine Safety Data Analysis (2016-2022)', fontsize=18, fontweight='bold', y=0.98)

# Adjust layout
plt.tight_layout(rect=[0, 0, 1, 0.95])

# Add data source note
plt.figtext(0.5, 0.01, 'Data Source: Coal Mine Casualty/Serious Injury Reports 2016-2022',
            ha='center', fontsize=10, style='italic')

# Save the figure
plt.savefig('korba_coal_mine_safety_analysis.png', dpi=300, bbox_inches='tight')

# Show the plot
plt.show()
