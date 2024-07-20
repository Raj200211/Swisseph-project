import matplotlib.pyplot as plt

# Data for plotting
celestial_bodies = ['Sun', 'Moon']
longitudes = [123.45, 234.56]

# Plotting the data
plt.figure(figsize=(10, 6))
plt.bar(celestial_bodies, longitudes, color=['orange', 'silver'])
plt.xlabel('Celestial Body')
plt.ylabel('Longitude (°)')
plt.title('Longitudinal Positions of Sun and Moon on July 15, 2023, 12:00 UTC')
plt.show()

