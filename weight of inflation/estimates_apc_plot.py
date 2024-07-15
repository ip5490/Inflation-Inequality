import os
import pandas as pd
import matplotlib.pyplot as plt

# Specify the folder path
folder_path = os.path.join(os.path.expanduser("~"), '…')

# Specify the file names for the merged table
file_name = ['logestimatesmergedapc.xlsx']

# Read merged table
estimatesmerged_df = pd.read_excel(os.path.join(folder_path, file_name[0]))

# Sort the dataframe by 'Estimate Total' in descending order
estimatesmerged_df = estimatesmerged_df.sort_values(by='Estimate Total', ascending=False)

# Remove sectors with out total effect estimates
estimatesmerged_df = estimatesmerged_df.iloc[:-3]

# Set figure size
plt.figure(figsize=(10, 18))

# Layout
for i, sector in enumerate(estimatesmerged_df['Sector']):
    plt.axhline(y=i, color='lightgrey', linewidth=0.5, zorder=0)

# Point plot
plt.errorbar(estimatesmerged_df['Estimate Direct'], estimatesmerged_df['Sector'], 
             xerr=[estimatesmerged_df['Estimate Direct'] - estimatesmerged_df['Direct Confi -'], 
                   estimatesmerged_df['Direct Confi +'] - estimatesmerged_df['Estimate Direct']], 
             fmt='o', color='#FF5733', label='Estimate Direct Effect')  # Orange color

plt.errorbar(estimatesmerged_df['Estimate Indirect'], estimatesmerged_df['Sector'], 
             xerr=[estimatesmerged_df['Estimate Indirect'] - estimatesmerged_df['Indirect Confi -'], 
                   estimatesmerged_df['Indirect Confi +'] - estimatesmerged_df['Estimate Indirect']], 
             fmt='o', color='#377EB8', label='Estimate Production Network Effect')  # Blue color

plt.errorbar(estimatesmerged_df['Estimate Total'], estimatesmerged_df['Sector'], 
             xerr=[estimatesmerged_df['Estimate Total'] - estimatesmerged_df['Total Confi -'], 
                   estimatesmerged_df['Total Confi +'] - estimatesmerged_df['Estimate Total']], 
             fmt='o', color='black', label='Estimate Total Effect', zorder=3)

# Add vertical markers at the end of the whiskers
for i, (_, row) in enumerate(estimatesmerged_df.iterrows()):    
    plt.plot([row['Direct Confi -'], row['Direct Confi -']], [i - 0.2, i + 0.2], color='#FF5733', linewidth=1, linestyle='-')  # Orange color
    plt.plot([row['Direct Confi +'], row['Direct Confi +']], [i - 0.2, i + 0.2], color='#FF5733', linewidth=1, linestyle='-')  # Orange color
    
    plt.plot([row['Indirect Confi -'], row['Indirect Confi -']], [i - 0.2, i + 0.2], color='#377EB8', linewidth=1, linestyle='-')  # Blue color
    plt.plot([row['Indirect Confi +'], row['Indirect Confi +']], [i - 0.2, i + 0.2], color='#377EB8', linewidth=1, linestyle='-')  # Blue color
    
    plt.plot([row['Total Confi -'], row['Total Confi -']], [i - 0.2, i + 0.2], color='black', linewidth=1, linestyle='-')
    plt.plot([row['Total Confi +'], row['Total Confi +']], [i - 0.2, i + 0.2], color='black', linewidth=1, linestyle='-')

# Add dashed line at 0.0 mark
plt.axvline(x=0, color='grey', linestyle='--')

# Add whisker with vertical markers to legend
plt.plot([], [], color='black', linewidth=1, linestyle='-', label='95% Confidence Interval')

plt.xlabel('Estimates of Income-dependent Inflation Exposure',fontsize=16)
plt.ylabel('Sector',fontsize=16)
plt.tick_params(axis='y', labelsize=14)
plt.tick_params(axis='x', labelsize=14)
plt.legend(fontsize=12)

# Export the plot to a pdf file
plt.savefig(os.path.join(folder_path, 'Merged Estimates of Income-dependent Inflation Exposure APC.pdf'), bbox_inches='tight')

plt.show()
 