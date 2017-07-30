# Import the csv library
import csv

# Open the 'llc-chapters.csv' file
with open('../exercises/llc-chapters.csv') as chapters_file:
    # Convert it to a csv_data structure
    chapters = csv.DictReader(chapters_file)
    # Loop through each of the rows
    for chapter in chapters:
        # Compare the 'City' in the row with your city
        if chapter['City'] == 'Ottawa':
            # Print a thank you message to your chapter lead(s)
            print('Thank you ' + chapter['Chapter Lead(s)'])
