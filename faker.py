import csv
import random


VALID_LOC_ENTRIES = {
    'YEL': 'Yelahanka', 'KRI': 'Krishnarajapuram', 'BYA': 'Byatarayanapura', 'YES': 'Yeshwantpur',
    'RAJ': 'Rajarajeshwarinagar', 'DAS': 'Dasarahalli', 'MAH': 'Mahalakshmi layout', 'MAL': 'Malleshwaram',
    'HEB': 'Hebbal', 'PUL': 'Pulakeshinagar', 'SAR': 'Sarvagnagar', 'CVR': 'CV Raman Nagar', 'SHI': 'Shivajinagar',
    'SHA': 'Shantinagar', 'GAN': 'Gandhinagar', 'GOV': 'Govindrajnagar', 'VIJ': 'Vijaynagar', 'CHA': 'Chamrajpet',
    'CHI': 'Chickpet', 'BAS': 'Basavanagudi', 'PAD': 'Padmanabhanagar', 'BTM': 'BTM Layout', 'JAY': 'Jayanagar',
    'MAH': 'Mahadevapura', 'BOM': 'Bommanahalli', 'BNS': 'Bangalore South', 'ANE': 'Anekal'
}

VALID_MOT_ENTRIES = {
    'C': 'Car', 'B': 'Bus', 'T': 'Two-wheeler', 'W': 'Walk', 'M': 'Miscellaneous'
}

def generate_fake_data(num_rows):
    with open('commute_data.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['LOC', 'MOT', 'CT (min)', 'DIST (km)'])

        for _ in range(num_rows):
            loc = random.choice(list(VALID_LOC_ENTRIES.values()))
            mot = random.choice(list(VALID_MOT_ENTRIES.values()))
            commute_time = random.randint(15, 120)  
            distance = int(random.uniform(1, 30)) 

            writer.writerow([loc, mot, commute_time, distance])

    print(f"{num_rows} rows of fake commute data have been generated and written to fake_commute_data.csv")

if __name__ == "__main__":
    num_rows = 50
    generate_fake_data(num_rows)
