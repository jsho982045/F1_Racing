import pandas as pd

results = pd.read_csv('data/results.csv')
races = pd.read_csv('data/races.csv')
drivers = pd.read_csv('data/drivers.csv')

driver_names = drivers[['driverId', 'forename', 'surname']]

merged_data = results.merge(races[['raceId', 'year']], on='raceId')

results_2024 = merged_data[merged_data['year'] == 2024]

active_driver_ids = results_2024['driverId'].unique()

print("\nActive Drivers in 2024:", active_driver_ids)

active_drivers_data = merged_data[merged_data['driverId'].isin(active_driver_ids)]

earliest_years = active_drivers_data.groupby('driverId')['year'].min()

earliest_years_with_names = earliest_years.reset_index().merge(
    driver_names, on='driverId'
)

earliest_years_with_names['name'] = (
    earliest_years_with_names['forename'] + " " + earliest_years_with_names['surname'] 
)

result = earliest_years_with_names[['name', 'year']]

print("\nEarliest Year for Each Active Driver with Names:")
print(result)