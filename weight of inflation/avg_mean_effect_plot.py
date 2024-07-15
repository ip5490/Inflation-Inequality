import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Specify the folder path
folder_path = os.path.join(os.path.expanduser("~"), '…')

# Specify the file name for the table
file_name = 'meantable.xlsx'

# Read the data from the Excel file
file_path = os.path.join(folder_path, file_name)
data = pd.read_excel(file_path, header=None)

# Extract the columns
sectors = data[0]
col1_values = data[1]
col2_values = data[2]

# Define the colors with specified RGB values
blue_color = (144/255, 202/255, 249/255)
red_color = (251/255, 128/255, 114/255)

# Sectors to be colored in red
red_sectors = [
    "Real estate activities",
    "Electricity, gas (..)",
    "Manuf. of food products (..)",
    "Construction",
    "Crop & animal production (..)",
    "(..) Waste management services",
    "Fishing & aquaculture"
]

# Create a figure and axis for the plot
fig, ax = plt.subplots(figsize=(10, len(sectors) * 0.3))

# Define index for positioning
index = np.arange(len(sectors))

# Plot col1 and col2 values in a stacked manner with specified colors and alpha values
for i in range(len(sectors)):
    if sectors[i] in red_sectors:
        ax.barh(index[i], col1_values[i], label='Column 1' if i == 0 else "", color=red_color, alpha=1)
        ax.barh(index[i], col2_values[i], left=col1_values[i], label='Column 2' if i == 0 else "", color=red_color, alpha=0.7)
    else:
        ax.barh(index[i], col1_values[i], label='Column 1' if i == 0 else "", color=blue_color, alpha=0.7)
        ax.barh(index[i], col2_values[i], left=col1_values[i], label='Column 2' if i == 0 else "", color=blue_color, alpha=0.4)

# Add sector descriptions as y-axis labels
ax.set_yticks(index)
ax.set_yticklabels(sectors)

# Add labels and title
ax.set_xlabel('Values')
ax.set_ylabel('Sectors')
ax.set_title('Stacked Bar Plot of Column 1 and Column 2 for Each Sector')
ax.legend()

# Adjust layout and display the plot
plt.tight_layout()
plt.show()
