import csv
import whois

# with open(player.txt, mode='r') as csv_file:
#     csv_reader: csv.DictReader(csv_file)
#     line_count = 0
#     for row in csv_reader:
#         print(f'Player Name {",".join(row)}')o
#         line_count += 1


w = whois.whois('charchitdahal.com')

try:
    w.creation_date
except NameError:
    print("False")
else:
    print("True")

print(w.creation_date)

# (1)I want to remove any spaces between last name and first name
# (2)identify middle name (usually an initial with . end) and remove it
# (3) check if the fistnamelastname.com is available


