from bs4 import BeautifulSoup
import csv
import urllib.request

with open('tes.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for line in csv_reader:
        url = line[0]
        print("membaca url")
        filename = line[1] + ".jpg"
        print("membaca nama file")
        html = urllib.request.urlopen(url).read()
        print("mengambil html")
        soup = BeautifulSoup(html, 'html.parser')
        print("membuka html parser")
        for i in range(1, 21):
            img_tag = soup.find('a', {'title': f'Product Image 1/{i}'})
            if img_tag is not None:
                break
        print(img_tag)
        print("mencari tag a")
        if img_tag:
            img_url = img_tag['href']
            print("mengambil href")
            print(img_url)
            urllib.request.urlretrieve(img_url, filename)
            print(f'{filename} has been downloaded.')
        else:
            print(f'No image found on {url}')
