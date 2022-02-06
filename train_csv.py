import csv

file_url='empty.csv'

with open(file_url,'r') as f :
    header=next(f)
    print(header.split(','))
    # for i in f :
    #     x=i.split()
    #     print(x)

with open (file_url,'a') as f:
    writer=csv.writer(f)
    writer.writerow(['mohsen','hamidi',63])
