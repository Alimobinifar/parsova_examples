import csv

file_url='empty.csv'

# Read Csv File 

with open(file_url,'r') as f :
    header=next(f)
    print(header.split(','))

# Write on csv as append
with open (file_url,'a') as f:
    writer=csv.writer(f)
    writer.writerow(['mohsen','hamidi',63])
