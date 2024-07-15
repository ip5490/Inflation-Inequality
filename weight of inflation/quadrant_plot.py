import pandas as pd
import os
import matplotlib.pyplot as plt

# Specify the folder path for the tables
folder_path = os.path.join(os.path.expanduser("~"), '…')

# Read the first table
first_table_path = os.path.join(folder_path, 'logestimatelistindirect.xlsx')
df_first = pd.read_excel(first_table_path)

# Read the second table
second_table_path = os.path.join(folder_path, 'logestimatelisttotal.xlsx')
df_second = pd.read_excel(second_table_path)

# Filter the first table to remove the extra rows
df_first_filtered = df_first[df_first['NACE'].isin(df_second['NACE'])]

# Merge the filtered first table with the second table on the 'NACE' column
merged_df = pd.merge(df_first_filtered, df_second, on='NACE', suffixes=('_indirect', '_total'))

# Compute the absolute difference of 'Estimate' columns
merged_df['Estimate_diff'] = merged_df['Estimate_total'].abs() - merged_df['Estimate_indirect'].abs()

# List of sectors to be moved
sectors_to_move_down_left = ['A01','A02','O84','C25']
sectors_to_move_down_right = ['C16','G46','M73','C33','D35','C20','C28']
sectors_to_move_left = ['M72','M74_M75']

# Create the plot
plt.figure(figsize=(10, 6))

# Define colors using RGB codes
light_green = (144/255, 202/255, 249/255)  # Light green
dark_green = (69/255, 117/255, 180/255)    # Dark green
light_red = (251/255, 128/255, 114/255)    # Light red
dark_red = (215/255, 48/255, 39/255)       # Dark red

# Draw background color for quadrants using RGB codes
plt.fill_between([0, 0.16], 0, 0.3, color=light_green, alpha=0.4)  # Upper Right Quadrant
plt.fill_between([-0.07, 0], 0, 0.3, color=light_green, alpha=0.2)  # Upper Left Quadrant
plt.fill_between([-0.07, 0], -0.1, 0, color=light_red, alpha=0.2)    # Lower Left Quadrant
plt.fill_between([0, 0.16], -0.1, 0, color=light_red, alpha=0.05)   # Lower Right Quadrant

# Plot the markers
plt.scatter(merged_df['Estimate_diff'], merged_df['Estimate_total'], c='black', alpha=0.4, marker='x', s=10)  # Reduced marker size

# Add labels next to the points
for i, row in merged_df.iterrows():
    if row['NACE'] in sectors_to_move_down_right:
        plt.text(row['Estimate_diff'], row['Estimate_total'], row['NACE'], fontsize=6, ha='left', va='top')  # Adjusted position for specific sectors
    elif row['NACE'] in sectors_to_move_down_left:
        plt.text(row['Estimate_diff'], row['Estimate_total'], row['NACE'], fontsize=6, ha='right', va='top')  # Adjusted position for specific sectors
    elif row['NACE'] in sectors_to_move_left:
        plt.text(row['Estimate_diff'], row['Estimate_total'], row['NACE'], fontsize=6, ha='right', va='bottom')  # Adjusted position for specific sectors
    else:
        plt.text(row['Estimate_diff'], row['Estimate_total'], row['NACE'], fontsize=6, ha='left', va='bottom')  # For other points, position labels at the bottom right

# Manually specify the distance shown on x and y axis
plt.xlim(-0.07, 0.16)
plt.ylim(-0.1, 0.3)

# Draw x and y axes through the origin
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)

# Add text to each quadrant with transparency
plt.text(-0.068, 0.01, 'equalizing\namplifying', fontsize=12, fontweight='bold', fontname='Arial', color=dark_green, rotation=0, linespacing=2.5, alpha=0.75)
plt.text(0.05, 0.01, 'equalizing\ndampening', fontsize=12, fontweight='bold', fontname='Arial', color=dark_green, rotation=0, linespacing=2.5, alpha=0.75)
plt.text(0.05, -0.055, 'disequalizing\ndampening', fontsize=12, fontweight='bold', fontname='Arial', color=dark_red, rotation=0, linespacing=2.5, alpha=0.75)
plt.text(-0.068, -0.055, 'disequalizing\namplifying', fontsize=12, fontweight='bold', fontname='Arial', color=dark_red, rotation=0, linespacing=2.5, alpha=0.75)

# labels
plt.xlabel('Mediating Effect Size', fontsize=12, fontname='Helvetica')
plt.ylabel('Estimate Total Effect', fontsize=12, fontname='Helvetica')
plt.title('Production Network Effect on Inflation Inequality', fontsize=14, fontname='Helvetica')

# Remove the frame
plt.box(False)

# Save plot as PDF to desktop
plt.savefig(os.path.join(os.path.expanduser("~"), 'Desktop', 'plot.pdf'))

# Show plot
plt.tight_layout()
plt.show()
