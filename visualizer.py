import matplotlib.pyplot as plt
from dataorg import *

location_counts.plot(x = 'LOC', y = 'n', kind = "bar", color = "lime", width = 0.8)
plt.title('Number of commuters to RIT from various areas in Bangalore')
plt.xlabel('Locations -->')
plt.ylabel('Number of commuters -->')
plt.xticks(rotation=45)
plt.show()

mode_counts.plot(x = 'MOT', y = 'n', kind = "bar", color = "skyblue", width = 0.8)
plt.title('Number of commuters using various modes of transportation on their commute to RIT')
plt.xlabel('Mode of transportation -->')
plt.ylabel('Number of commuters -->')
plt.xticks(rotation=45)
plt.show()

average_commute_time_byloc.plot(x = 'LOC', y = 'CT (min)', kind = 'bar', color = "crimson", width = 0.8)
plt.title('Average Commute time by Location of commuter origin')
plt.xlabel('Locations -->')
plt.ylabel('Average Commute time -->')
plt.xticks(rotation=45)
plt.show()

average_commute_time_bymot.plot(x = 'MOT', y = 'CT (min)', kind = 'bar', color = "orange", width = 0.8)
plt.title('Average Commute time by Mode of transport of commute')
plt.xlabel('Modes of transport -->')
plt.ylabel('Average Commute time -->')
plt.xticks(rotation=45)
plt.show()

mode_usage_by_location.plot(kind='bar', stacked=True, figsize=(10, 6))
plt.title('Mode of Transportation Distribution by Location')
plt.xlabel('Location')
plt.ylabel('Number of Commuters')
plt.xticks(rotation=45)
plt.show()

