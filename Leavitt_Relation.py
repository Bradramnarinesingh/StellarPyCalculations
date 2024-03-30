import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

# Set the file path
file_path = 'C:/Users/brad5/Downloads/Project 2 Data.xlsx'

# Load the data for Milky Way Cepheids
cepheids_data = pd.read_excel(file_path, sheet_name='Milky Way Cepheids')

# Assuming the DataFrame has columns 'Period (days)', 'Parallax (arcsec)', and 'Brightness (W/m2)'
# Convert Brightness and Distance to Luminosity, then calculate logarithms
cepheids_data['Distance (pc)'] = 1 / cepheids_data['Parallax (arcsec)']
cepheids_data['Distance (m)'] = cepheids_data['Distance (pc)'] * 3.086e+16
cepheids_data['Luminosity (W)'] = cepheids_data['Brightness (W/m2)'] * 4 * np.pi * (cepheids_data['Distance (m)'] ** 2)
cepheids_data['log_Period'] = np.log10(cepheids_data['Period (days)'])
cepheids_data['log_Luminosity'] = np.log10(cepheids_data['Luminosity (W)'])

# Fit a linear regression to the log-log data
slope, intercept, r_value, p_value, std_err = stats.linregress(cepheids_data['log_Period'], cepheids_data['log_Luminosity'])

# Plotting the Leavitt Law with trendline
plt.figure(figsize=(10, 6))
plt.scatter(cepheids_data['log_Period'], cepheids_data['log_Luminosity'], color='blue', alpha=0.5)
plt.plot(cepheids_data['log_Period'], slope*cepheids_data['log_Period'] + intercept, 'r-', label=f'Fit: log(L) = {slope:.2f}log(P) + {intercept:.2f}')

plt.title('Leavitt Law for Milky Way Cepheids (Log-Log Plot)')
plt.xlabel('Log(Period in days)')
plt.ylabel('Log(Luminosity in Watts)')
plt.legend()
plt.grid(True)
plt.show()

print(f"Slope (a): {slope:.2f}, Intercept (b): {intercept:.2f}")
print(f"Coefficient of Determination (R^2): {r_value**2:.2f}")


galaxy_x_data = pd.read_excel(file_path, sheet_name='Cepheids in Galaxy X')

# Apply the derived relationship to calculate log(luminosity)
galaxy_x_data['log_Luminosity'] = slope * np.log10(galaxy_x_data['Period (days)']) + intercept

# Convert log(luminosity) back to luminosity (W)
galaxy_x_data['Luminosity (W)'] = 10**galaxy_x_data['log_Luminosity']

# Calculate distance (m)
galaxy_x_data['Distance (m)'] = np.sqrt(galaxy_x_data['Luminosity (W)'] / (4 * np.pi * galaxy_x_data['Brightness (W/m^2)']))

# Convert distance from meters to light-years for readability
galaxy_x_data['Distance (ly)'] = galaxy_x_data['Distance (m)'] / (9.461e+15)

# Calculate the average distance to Galaxy X Cepheids in light-years
average_distance_ly = galaxy_x_data['Distance (ly)'].mean()

print(f"Average distance to Galaxy X Cepheids: {average_distance_ly} light-years")
