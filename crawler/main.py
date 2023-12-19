from lxml.etree import HTML
from requests import get
import csv


def csv_rasymas():
    fieldnames=['Pavadinimas', 'Img', 'Linkas']
    with open("Cars.csv", "w", encoding='utf-8', newline='') as file_writer:
        csv_write = csv.DictWriter(file_writer, fieldnames, delimiter = ',')
        csv_write.writeheader()
        for i in range(len(car_name)):
            csv_write.writerow({"Pavadinimas": car_name[i].strip(), "Img":car_image_url[i].strip(), "Linkas":car_page_url[i].strip()})

#crawlinam web
data= get("https://www.dacia.lt/index.html").text
data= HTML(data)

#isirenkam is nucrawlinto saito data apie auto pavadinimus
car_name=[link for link in data.xpath("//a/img[contains(@class, 'img-responsive')]/@alt")]
#isirenkam is nucrawlinto saito data apie auto paveiksliukus
car_image=[link for link in data.xpath("//a/img[contains(@class, 'img-responsive')]/@src")]
car_image_url=[]

#dadedam priekius kad gautusi linkas
for link in car_image:
    car_image_url.append("https://www.dacia.lt/" + link)

#isirenkam is nucrawlinto saito data apie auto puslapius
car_page=[link for link in data.xpath("//a[contains(@class,'vehicle-item fp-cta-gtm')]/@href")]
car_page_url=[]

#dadedam priekius kad gautusi linkas
for link in car_page:
    car_page_url.append(f"https://www.dacia.lt/{link}")


#//div[contains(@class, 'col-xs-12 col-sm-6 col-sm-6--clear-third col-md-3')]//span
print(car_page_url)
kainos=[]
for i in car_page_url:
    data= get(i).text
    dataa=HTML(data)
    #print(dataa.xpath("//div/span[contains(@class, 'prices_price')]"))
    kainos.append([link.text for link in dataa.xpath("//div/span[contains(@class,'prices_price')]")])
    #for u in dataa.xpath("//div/span[contains(@class,'prices_price')]"):
       #if u.text != "":
        #print(u.text)
    #else:
       #print("tuscia")
print(kainos)
csv_rasymas()