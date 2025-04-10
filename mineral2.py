import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set style for plots
plt.style.use('seaborn-v0_8')
sns.set_palette("muted")
plt.rcParams.update({'font.size': 12})

# Data
coal_areas = ['Bagdeva', 'Balagi', 'Banki', 'Dhelwadih', 'Ghurdeva', 'Korba', 
              'Manikpur', 'Pawan', 'Rajgamar', 'Singhali', 'Surakachar']

nutrients_data = {
    'Coal_Area': coal_areas,
    'Calorie': [3383.4, 3813.5, 3412.4, 3612.6, 3730.9, 3590.4, 3690.4, 2832.8, 2413.9, 2458.3, 3973],
    'Protein': [33.89, 41.93, 42.9, 28.56, 36.56, 43.21, 39.49, 37.36, 20.11, 31.55, 43.71],
    'Fats': [20.1, 21.73, 22.4, 15.7, 22, 25, 15.8, 15.3, 15.5, 13.5, 12.21],
    'Calcium': [345, 438, 284, 326, 371, 511, 283, 401, 375, 283, 391],
    'Iron': [11.3, 20.1, 22.3, 10.2, 9.67, 10.66, 11.82, 8.78, 10.52, 9.66, 9.6],
    'Thiamine': [2.9, 3.3, 2.9, 3.1, 3.2, 3.1, 3.2, 2.5, 2.1, 2, 3.4],
    'Riboflavin': [2.1, 2.4, 2.2, 2.2, 2.5, 2.1, 2.2, 1.6, 1.3, 1.7, 2.5],
    'Niacin': [28.1, 31.7, 28.7, 31.3, 31.1, 30.3, 30.8, 24.6, 20.3, 18.9, 33.9],
    'Vitamin_C': [46.21, 60.55, 52.81, 33.55, 44.36, 37.73, 50.11, 62.91, 49, 36.45, 56.72],
    'Zinc': [7.1, 8.3, 5.8, 7.9, 10.2, 8.9, 11.4, 6.8, 9.2, 7.4, 9.3]
}

recommended = {
    'Calorie': 3800,
    'Protein': 60,
    'Fats': 20,
    'Calcium': 400,
    'Iron': 28,
    'Thiamine': 1.6,
    'Riboflavin': 1.9,
    'Niacin': 21,
    'Vitamin_C': 40,
    'Zinc': 9.5
}

# Create DataFrame
df = pd.DataFrame(nutrients_data)
average_values = df.mean(numeric_only=True)

# === Figure 1: Bar chart comparing recommended and actual intake ===
fig, ax = plt.subplots(figsize=(12, 7))
nutrients_to_compare = ['Calorie', 'Protein', 'Fats', 'Calcium', 'Iron', 'Zinc']
bar_width = 0.35
nutrient_indices = np.arange(len(nutrients_to_compare))

recommended_vals = [recommended[n] for n in nutrients_to_compare]
actual_vals = [average_values[n] for n in nutrients_to_compare]
percentages = [actual / rec * 100 for actual, rec in zip(actual_vals, recommended_vals)]

bars1 = ax.bar(nutrient_indices - bar_width/2, recommended_vals, bar_width, label='Recommended')
bars2 = ax.bar(nutrient_indices + bar_width/2, actual_vals, bar_width, label='Actual')

for i, perc in enumerate(percentages):
    ax.text(i + bar_width/2, actual_vals[i] + max(actual_vals)*0.02, f"{perc:.1f}%", ha='center')

ax.set_xlabel('Nutrients')
ax.set_ylabel('Amount')
ax.set_title('Comparison of Recommended vs. Actual Nutrient Intake')
ax.set_xticks(nutrient_indices)
ax.set_xticklabels(nutrients_to_compare)
ax.legend()
plt.tight_layout()
plt.savefig('nutrient_comparison.png')
plt.close()

# === Figure 2: Heatmap of nutrient adequacy ===
plt.figure(figsize=(14, 10))
heatmap_data = df.copy()
for nutrient in recommended.keys():
    if nutrient in heatmap_data.columns:
        heatmap_data[nutrient] = (heatmap_data[nutrient] / recommended[nutrient] - 1) * 100

heatmap_cols = [col for col in recommended.keys() if col in heatmap_data.columns]
heatmap_data = heatmap_data.set_index('Coal_Area')[heatmap_cols]

sns.heatmap(heatmap_data, cmap="RdBu_r", center=0, annot=True, fmt=".1f",
            vmin=-50, vmax=100, cbar_kws={'label': '% Difference from Recommended'})
plt.title('Nutrient Adequacy Across Coal Mining Areas (% Difference from Recommended)')
plt.tight_layout()
plt.savefig('nutrient_heatmap.png')
plt.close()

# === Figure 3: BMI Distribution (horizontal bar chart) ===
bmi_categories = ['CED III (Severe)', 'CED II (Moderate)', 'CED I (Mild)', 
                  'Low weight normal', 'Normal', 'Obese grade I', 'Obese grade II']
bmi_percentages = [1.6, 0.0, 8.2, 4.9, 45.9, 26.2, 13.1]

plt.figure(figsize=(12, 7))
colors = ['#d73027', '#f46d43', '#fdae61', '#fee090', '#e0f3f8', '#abd9e9', '#74add1']

bars = plt.barh(bmi_categories, bmi_percentages, color=colors)
plt.xlabel('Percentage (%)')
plt.title('BMI Distribution of Coal Mine Workers')
plt.gca().invert_yaxis()

for bar in bars:
    width = bar.get_width()
    plt.text(width + 0.5, bar.get_y() + bar.get_height() / 2,
             f'{width:.1f}%', va='center', fontsize=11)

plt.tight_layout()
plt.savefig('bmi_distribution_bar.png')
plt.close()

# === Figure 4: Subplots for nutrient variation across areas ===
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('Key Nutrient Variation Across Coal Mining Areas', fontsize=16)

axes[0, 0].bar(coal_areas, df['Calorie'])
axes[0, 0].axhline(y=recommended['Calorie'], color='r', linestyle='--', label='Recommended')
axes[0, 0].set_title('Calorie Intake')
axes[0, 0].tick_params(axis='x', rotation=45)
axes[0, 0].legend()

axes[0, 1].bar(coal_areas, df['Protein'], color='#d95f02')
axes[0, 1].axhline(y=recommended['Protein'], color='r', linestyle='--', label='Recommended')
axes[0, 1].set_title('Protein Intake')
axes[0, 1].tick_params(axis='x', rotation=45)
axes[0, 1].legend()

axes[1, 0].bar(coal_areas, df['Iron'], color='#7570b3')
axes[1, 0].axhline(y=recommended['Iron'], color='r', linestyle='--', label='Recommended')
axes[1, 0].set_title('Iron Intake')
axes[1, 0].tick_params(axis='x', rotation=45)
axes[1, 0].legend()

axes[1, 1].bar(coal_areas, df['Calcium'], color='#e7298a')
axes[1, 1].axhline(y=recommended['Calcium'], color='r', linestyle='--', label='Recommended')
axes[1, 1].set_title('Calcium Intake')
axes[1, 1].tick_params(axis='x', rotation=45)
axes[1, 1].legend()

plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.savefig('nutrient_variation.png')
plt.close()

# === Figure 5: Radar chart ===
nutrient_names = list(recommended.keys())
avg_percentages = [average_values[nutrient] / recommended[nutrient] * 100 for nutrient in nutrient_names]

angles = np.linspace(0, 2 * np.pi, len(nutrient_names), endpoint=False)
avg_percentages.append(avg_percentages[0])
angles = np.append(angles, angles[0])
nutrient_names.append(nutrient_names[0])

fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))
ax.plot(angles, [100] * len(angles), color='red', linestyle='--', label='Recommended (100%)')
ax.plot(angles, avg_percentages, linewidth=2, linestyle='solid', label='Actual (% of recommended)')
ax.fill(angles, avg_percentages, alpha=0.25)

ax.set_thetagrids(angles[:-1] * 180 / np.pi, nutrient_names[:-1])
ax.set_ylim(0, 200)
ax.set_yticks([0, 50, 100, 150, 200])
ax.set_yticklabels(['0%', '50%', '100%', '150%', '200%'])
ax.grid(True)
plt.title('Nutrient Intake as Percentage of Recommended Values', size=15)
plt.legend(loc='upper right')
plt.tight_layout()
plt.savefig('nutrient_radar.png')
plt.close()

# === Summary ===
print("===== Summary of Coal Mine Worker Nutrition =====")
print(f"Average calorie intake: {average_values['Calorie']:.1f} kcal ({average_values['Calorie']/recommended['Calorie']*100:.1f}% of recommended)")
print(f"Average protein intake: {average_values['Protein']:.1f} g ({average_values['Protein']/recommended['Protein']*100:.1f}% of recommended)")
print(f"Average iron intake: {average_values['Iron']:.1f} mg ({average_values['Iron']/recommended['Iron']*100:.1f}% of recommended)")
print(f"Average calcium intake: {average_values['Calcium']:.1f} mg ({average_values['Calcium']/recommended['Calcium']*100:.1f}% of recommended)")

print("\nAreas with best nutrition status:")
print(f"Highest calorie intake: {df.loc[df['Calorie'].idxmax(), 'Coal_Area']} ({df['Calorie'].max()} kcal)")
print(f"Highest protein intake: {df.loc[df['Protein'].idxmax(), 'Coal_Area']} ({df['Protein'].max()} g)")

print("\nAreas with worst nutrition status:")
print(f"Lowest calorie intake: {df.loc[df['Calorie'].idxmin(), 'Coal_Area']} ({df['Calorie'].min()} kcal)")
print(f"Lowest protein intake: {df.loc[df['Protein'].idxmin(), 'Coal_Area']} ({df['Protein'].min()} g)")
