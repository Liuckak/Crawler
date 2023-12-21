from lxml.etree import HTML
from requests import get
import csv

headers = {
    "authority": "www.renault.lt",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-language": "en-US,en;q=0.9",
    "cache-control": "max-age=0",
    "referer": "https://www.renault.lt/index.html?CAMPAIGN=lt-lt-r-t-def-brand-all_products-ice-go-classic--&ORIGIN=SEA&ds_rl=1297188&ds_rl=1297188&gclid=CjwKCAiAvoqsBhB9EiwA9XTWGYn9d-fOz2dfYASlQUOhVpFARDe5IPET0ijoJVnjrAnPHTGQ42l3YRoCjdQQAvD_BwE&gclsrc=aw.ds",
    "sec-ch-ua": '"Chromium";v="119", "Not?A_Brand";v="24"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Linux"',
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-origin",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
}
#crawlinam web
def csv_rasymas():
  """
  irasom i csv faila
  """
  fieldnames=['Pavadinimas', 'Img', 'Linkas', 'Kaina']
  with open("Renault.csv", "w", encoding='utf-8', newline='') as file_writer:
    csv_write = csv.DictWriter(file_writer, fieldnames, delimiter = ',')
    csv_write.writeheader()
    for i in range(len(car_name)):
        csv_write.writerow({"Pavadinimas": car_name[i], "Img": car_img[i], "Linkas": car_link[i],"Kaina": car_price[i]}) 

def get_url():
  """
  Grazina data is nuorodos
  """
  data= get("https://www.renault.lt/index.html?CAMPAIGN=lt-lt-r-t-def-brand-all_products-ice-go-classic--&ORIGIN=SEA&ds_rl=1297188&ds_rl=1297188&gclid=CjwKCAiA-P-rBhBEEiwAQEXhH_TEgbNrfO3zZD6J7VAtZ4yzwQ5H9pn37wQqVQ2HNROD48nfQBX5CxoCSbkQAvD_BwE&gclsrc=aw.ds").text
  return HTML(data)

def car_im():
  """
  Grazina paveiksleliu nuorodas
  """
  car_img=[]
  for link in data.xpath("//a/img/@src"):
      car_img.append("https://www.renault.lt/" + link)
  return car_img

def car_lin():
  """
  Grazina sarasa i konkreciu automobiliu puslapius
  """
  car_link=[]
  for link in data.xpath("//a[@class='vehicle-item fp-cta-gtm']/@href"):
      car_link.append("https://www.renault.lt/" + link)
  return car_link

def kaina(scraperis):
  """
  Grazina kainas formatu kaina: xxxxxx
  """
  kainos=[]
  for scraperis in car_link:
    data=get(scraperis).text
    data=HTML(data)
    text=data.xpath("//div/span[@class='prices_price']/span/text()")
    price=data.xpath("//div/span[@class='prices_price']/text()")
    if len(text) >0 and len(price) >= 2:
      formated=price[1].strip()
      formated1=str(formated[:-3]).replace("\xa0", "")
      kainos.append(f"{text[0].strip().capitalize()}: {formated1} €")
    else:
     kainos.append("Nenurodyta")
  return kainos



data= get_url()

#isirenkam is nucrawlinto saito data apie auto pavadinimus
car_name=data.xpath("//a/img/@alt")
#linkai i nuotraukas
car_img=car_im()

#linkai i aprasymus
car_link=car_lin()

#gaunam aprasymu reiksmes

car_price=kaina(car_link)

csv_rasymas()
