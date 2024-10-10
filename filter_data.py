import pandas as pd


results = pd.read_csv('data/results.csv')
races = pd.read_csv('data/races.csv')


merged_data = results.merge(races[['raceId', 'year']], on='raceId')

START_YEAR = 2001
END_YEAR = 2024

filtered_data = merged_data[(merged_data['year'] >= START_YEAR) & (merged_data['year'] <= END_YEAR)]

print("\nFiltered Data (2001-2024):")
print(filtered_data.head())