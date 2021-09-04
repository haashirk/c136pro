# IMPORT MODULE
import csv

# EXTARCT DATA FROM CSV
rows = []

with open("upgrade.csv",'r') as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        rows.append(row)

headers = rows[0]
star_data = rows[1:]

# MAKE A FINAL DATA SET FROM THE CSV
final_dict = []

for data in star_data:
    temp_dict = {
        "name":data[2],
        "distance":data[3],
        "mass":data[4],
        "radius":data[5],
        "luminosity":data[6],
        "solar_mass":data[7],
        "solar_radius":data[8],
        "apparent_magnitude":data[9],
        "gravity":data[10]
    }
    

    final_dict.append(temp_dict)

print(list(final_dict))
