import csv

VALID_LOC_ENTRIES = {
    'YEL': 'Yelahanka', 
    'KRI': 'Krishnarajapuram', 
    'BYA': 'Byatarayanapura', 
    'YES': 'Yeshwantpur',
    'RAJ': 'Rajarajeshwarinagar', 
    'DAS': 'Dasarahalli', 
    'MAH': 'Mahalakshmi layout', 
    'MAL': 'Malleshwaram',
    'HEB': 'Hebbal', 
    'PUL': 'Pulakeshinagar', 
    'SAR': 'Sarvagnagar', 
    'CVR': 'CV Raman Nagar', 
    'SHI': 'Shivajinagar',
    'SHA': 'Shantinagar', 
    'GAN': 'Gandhinagar', 
    'GOV': 'Govindrajnagar', 
    'VIJ': 'Vijaynagar', 
    'CHA': 'Chamrajpet',
    'CHI': 'Chickpet', 
    'BAS': 'Basavanagudi', 
    'PAD': 'Padmanabhanagar', 
    'BTM': 'BTM Layout', 
    'JAY': 'Jayanagar',
    'MAH': 'Mahadevapura', 
    'BOM': 'Bommanahalli', 
    'BNS': 'Bangalore South', 
    'ANE': 'Anekal'
}

VALID_MOT_ENTRIES = {
    'C': 'Car', 
    'B': 'Bus', 
    'T': 'Two-wheeler', 
    'W': 'Walk', 
    'M': 'Miscellaneous'
}

def main():
    with open('commute_data.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['LOC', 'MOT', 'CT (min)', 'DIST (km)'])
        
        while True:
            loc = input("Enter location (LOC - Valid entries: {}): ".format(', '.join(VALID_LOC_ENTRIES.keys())))
            while loc.upper() not in VALID_LOC_ENTRIES:
                print("Invalid location entry. Please choose from the valid entries.")
                loc = input("Enter location (LOC - Valid entries: {}): ".format(', '.join(VALID_LOC_ENTRIES.keys())))
            
            mot = input("Enter mode of transportation (MOT - Valid entries: {}): ".format(', '.join(VALID_MOT_ENTRIES.keys())))
            while mot.upper() not in VALID_MOT_ENTRIES:
                print("Invalid mode of transportation entry. Please choose from the valid entries.")
                mot = input("Enter mode of transportation (MOT - Valid entries: {}): ".format(', '.join(VALID_MOT_ENTRIES.keys())))
            
            commute_time = input("Enter commute time in minutes (CT): ")
            distance = input("Enter distance between college and point of origin in kilometers (DIS): ")
            
            writer.writerow([VALID_LOC_ENTRIES[loc.upper()], VALID_MOT_ENTRIES[mot.upper()], commute_time, distance])
            
            add_more = input("Do you want to add more commute data? (yes/no): ").lower()
            if add_more != 'yes' and add_more != 'y':
                break

if __name__ == "__main__":
    main()
