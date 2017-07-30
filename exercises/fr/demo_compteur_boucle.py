import csv
import os

with open(os.path.join(os.pardir, 'llc-chapters.csv')) as csv_file:
    csv_data = csv.DictReader(csv_file)

    count = 0
    for row in csv_data:
        count += 1

    print("Il y a " + str(count) + " chapitres")
