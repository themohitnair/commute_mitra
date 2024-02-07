import pandas as pd
from tabulate import tabulate 

base_df = pd.read_csv('commute_data.csv')
location_counts = base_df.groupby('LOC').size().reset_index(name='n')
mode_counts = base_df.groupby('MOT').size().reset_index(name='n')
average_commute_time_byloc = base_df.groupby('LOC')['CT (min)'].mean().reset_index()
average_commute_time_bymot = base_df.groupby('MOT')['CT (min)'].mean().reset_index()
mode_usage_by_location = base_df.groupby(['LOC', 'MOT']).size().unstack(fill_value=0)

def main():
    print("Data used: ")
    print(tabulate(base_df, headers="keys", tablefmt="psql"))
    print('\n')
    print("Number of commuters to RIT from various areas in Bangalore: ")
    print(tabulate(location_counts, headers="keys", tablefmt="psql"))
    print('\n')
    print("Number of commuters using various modes of transportation on their commute to RIT: ")
    print(tabulate(base_df, headers="keys", tablefmt="psql"))
    print('\n')
    print("Average Commute time by Location of commuter origin: ")
    print(tabulate(base_df, headers="keys", tablefmt="psql"))
    print('\n')
    print("Average Commute time by Mode of transport of commute: ")
    print(tabulate(base_df, headers="keys", tablefmt="psql"))
    print('\n')
    print("Mode of Transportation Distribution by Location: ")
    print(tabulate(base_df, headers="keys", tablefmt="psql"))
    print('\n')

if __name__ == "__main__":
    main()




