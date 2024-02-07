from dataorg import *
import numpy as np

def main():
    print("Commute time statistics: ")
    commute_time_mean = round(np.mean(base_df['CT (min)']),2)
    print(f"Average Commute time = {commute_time_mean} min")

    commute_time_median = round(np.median(base_df['CT (min)']),2)
    print(f"Median of Commute time = {commute_time_median} min")

    commute_time_var = round(np.var(base_df['CT (min)']),2)
    print(f"Variance of Commute time = {commute_time_var} min")

    commute_time_std = round(np.std(base_df['CT (min)']),2)
    print(f"Standard deviation of Commute time = {commute_time_std} min")

    commute_time_range = round(np.max(base_df['CT (min)']) - np.min(base_df['CT (min)']),2)
    print(f"Range of Commute time = {commute_time_range} min")

    print('\n')

    print("Distance statistics: ")
    dist_mean = round(np.mean(base_df['DIST (km)']),2)
    print(f"Average Distance travelled = {dist_mean} km")

    dist_median = round(np.median(base_df['DIST (km)']),2)
    print(f"Median of Distance travelled = {dist_median} km")

    dist_var = round(np.var(base_df['DIST (km)']),2)
    print(f"Variance of Distance travelled = {dist_var} km")

    dist_std = round(np.std(base_df['DIST (km)']),2)
    print(f"Standard Deviation of Distance travelled = {dist_std} km")

    dist_range = round(np.max(base_df['DIST (km)']) - np.min(base_df['DIST (km)']),2)
    print(f"Range of Distance travelled = {dist_range} km")


