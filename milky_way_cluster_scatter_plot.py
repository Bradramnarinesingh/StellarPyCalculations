import pandas as pd
import matplotlib.pyplot as plt

# Adjust the path to where the file is located on your system
file_path = 'Project 2 Data.xlsx'

# Load the data
open_clusters = pd.read_excel(file_path, sheet_name='Open Cluster Coordinates')
globular_clusters = pd.read_excel(file_path, sheet_name='Globular Cluster Coordinates')

# Plotting Open Clusters with adjusted scales
plt.figure(figsize=(10, 6))
plt.scatter(open_clusters['Galactic Longitude (deg)'], open_clusters['Galactic Latitude (deg)'], color='blue', alpha=0.5, label='Open Clusters')
plt.title('Galactic Longitude vs. Latitude for Open Clusters')
plt.xlabel('Galactic Longitude (deg)')
plt.ylabel('Galactic Latitude (deg)')
plt.xlim(-180, 180)  # Assuming you want the full range for longitude for consistency, adjust if needed
plt.ylim(-100, 100)  # Adjusted as per your requirement

# Adding x-axis and y-axis lines
plt.axhline(0, color='black', linewidth=1)  # Adds a horizontal line at y=0
plt.axvline(0, color='black', linewidth=1)  # Adds a vertical line at x=0

plt.legend()
plt.grid(True)
plt.savefig('open_clusters_plot_adjusted.png')  # Saves the plot as a PNG file with adjusted scales
plt.show()

# Plotting Globular Clusters with adjusted scales
plt.figure(figsize=(10, 6))
plt.scatter(globular_clusters['Galactic Longitude (deg)'], globular_clusters['Galactic Latitude (deg)'], color='red', alpha=0.5, label='Globular Clusters')
plt.title('Galactic Longitude vs. Latitude for Globular Clusters')
plt.xlabel('Galactic Longitude (deg)')
plt.ylabel('Galactic Latitude (deg)')
plt.xlim(-180, 180)  # Adjusted for consistency with the open clusters plot
plt.ylim(-100, 100)  # Adjusted as per your requirement

# Adding x-axis and y-axis lines
plt.axhline(0, color='black', linewidth=1)  # Adds a horizontal line at y=0
plt.axvline(0, color='black', linewidth=1)  # Adds a vertical line at x=0

plt.legend()
plt.grid(True)
plt.savefig('globular_clusters_plot_adjusted.png')  # Saves the plot as a PNG file with adjusted scales
plt.show()

# Calculate the average distance for open clusters
average_distance_open = open_clusters['Distance (ly)'].mean()

# Calculate the average distance for globular clusters
average_distance_globular = globular_clusters['Distance (ly)'].mean()

print(f"Average distance to open clusters: {average_distance_open} light-years")
print(f"Average distance to globular clusters: {average_distance_globular} light-years")
