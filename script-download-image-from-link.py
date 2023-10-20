import csv
import urllib.request

with open('tes.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for line in csv_reader:
        url = line[0]
        filename = line[1] + ".jpg"
        urllib.request.urlretrieve(url, filename)
        print(f'{filename} has been downloaded.')
