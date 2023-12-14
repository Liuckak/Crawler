from lxml.etree import HTML
from requests import get
import csv

data= get("https://www.dacia.lt/index.html").text
data= HTML(data)
car_name= data.xpath("//a/img[contains(@class, 'img-responsive')]/@alt")

car_image=data.xpath("//a/img[contains(@class, 'img-responsive')]/@src")
car_image_url=[]
for link in data.xpath("//a/img[contains(@class, 'img-responsive')]/@src"):
    car_image_url.append("https://www.dacia.lt/" + link)

car_page=data.xpath("//a[contains(@class,'vehicle-item fp-cta-gtm')]/@href")
car_page_url=[]
for link in data.xpath("//a[contains(@class,'vehicle-item fp-cta-gtm')]/@href"):
    car_page_url.append("https://www.dacia.lt/" + link)

with open("Cars.csv", "w") as file_writer:
    fieldnames=['Pavadinimas', 'Img', 'Linkas']
    csv_write = csv.DictWriter(file_writer, fieldnames, delimiter = ',')
    csv_write.writeheader()
    #csv_write.writerow
    for i in range(len(car_name)):
        csv_write.writerow({"Pavadinimas": car_name[i], "Img": car_image_url[i], "Linkas": car_page_url[i]})
