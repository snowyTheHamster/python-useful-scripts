# Compares a column in two csv files, remove duplicates, save to new csv file.
import csv
import time


set_a = set()
set_b = set()
list_unique = []


# get sku from csv and add to a set
with open('file_1.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        row = ', '.join(row)
        row = row.split(',')[1] # do neccesary string manipulation
        row = row.split('-')[0] + row.split('-')[1] # do neccesary string manipulation
        set_a.add(row) # append results in set_a


# get sku from csv and add to a set
with open('file_2.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        row = ', '.join(row)
        row = row.split(',')[-1] # do neccesary string manipulation
        set_b.add(row) # append results in set_b


# see which items are duplicates
duplicate_results = set_a.intersection(set_b)
print(f'duplicates in both sets: {duplicate_results}')


# merge two sets and append to list
set_c = set_a.union(set_b)
for item in set_c:
    list_unique.append(item)
list_unique.sort()


# write list to new csv file
with open('uniq_list.csv', mode='w', newline='') as new_file:
    new_writer = csv.writer(new_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for item in list_unique:
        print(f'writing {item} to new file')
        new_writer.writerow([item])