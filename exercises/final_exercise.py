import csv
with open('../exercises/llc-workshop-data.csv') as workshop_file:
    workshop_data = csv.DictReader(workshop_file)
    national_count = 0
    kids_or_girls_count = 0
    youth_count = 0
    for workshop in workshop_data:
        if workshop['Event Name'].find('National Learn to Code Day') >= 0:
            national_count += 1
        if workshop['Event Name'].find('Kids Learning Code') >= 0 or \
                        workshop['Event Name'].find('Girls Learning Code') >= 0:
            kids_or_girls_count += 1
        if workshop['Event Name'].find('National Learn to Code Day') >= 0 and \
                        workshop['Event Name'].find('Teens 13-16') >= 0:
            youth_count += 1


    print("Total number of people who registered for the National Learn to Code Day was: " + str(national_count))
    print("Total number of people registered for Kids Learning Code or Girls Learning Code was: " + str(kids_or_girls_count))
    print("Total number people involved in youth-oriented National Learn to Code Day was: " + str(youth_count))
