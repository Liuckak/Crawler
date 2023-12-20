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
  fieldnames=['Pavadinimas', 'Img', 'Linkas', 'Aprasymas']
  with open("Renault.csv", "w", encoding='utf-8', newline='') as file_writer:
    csv_write = csv.DictWriter(file_writer, fieldnames, delimiter = ',')
    csv_write.writeheader()
    for i in range(len(car_name)):
        csv_write.writerow({"Pavadinimas": car_name[i], "Img": car_img[i], "Linkas": car_link[i],"Aprasymas": car_resume[i]}) 

def get_url():
  """
  Grazina data is nuorodos
  """
  data= get("https://www.renault.lt/index.html?CAMPAIGN=lt-lt-r-t-def-brand-all_products-ice-go-classic--&ORIGIN=SEA&ds_rl=1297188&ds_rl=1297188&gclid=CjwKCAiA-P-rBhBEEiwAQEXhH_TEgbNrfO3zZD6J7VAtZ4yzwQ5H9pn37wQqVQ2HNROD48nfQBX5CxoCSbkQAvD_BwE&gclsrc=aw.ds").text
  return HTML(data)

def car_im():
  car_img=[]
  for link in data.xpath("//a/img/@src"):
      car_img.append("https://www.renault.lt/" + link)
  return car_img

def car_lin():
  car_link=[]
  for link in data.xpath("//a[@class='vehicle-item fp-cta-gtm']/@href"):
      car_link.append("https://www.renault.lt/" + link)
  return car_link

def car_atribute():
  car_atributes=[]
  for i in car_link:
    parse_url= get(i).text
    parse_url= HTML(parse_url)
    car_atributes.append(parse_url.xpath("//div[contains(@class,'col-md-3')]//span"))
  return car_atributes


def car_atribute_titl():
  car_atributes_title=[]
  for i in car_link:
    parse_url= get(i).text
    parse_url= HTML(parse_url)
    car_atributes_title.append(parse_url.xpath("//div[@class='wysiwyg-block wysiwyg-block--16 wysiwyg-block--center']")) 
  return car_atributes_title

def car_resum(car_atributes_title, car_atributes):
  c_atributes_list=[]
  for c_a_set in car_atributes:
    for i in c_a_set:
      c_atributes_list.append(i.text)
  c_atributes_list_t=[]
  for c_a_set_a in car_atributes_title:
    for i in c_a_set_a:
      c_atributes_list_t.append(i.text)
  car_resume=[]
  for i in range(len(car_atributes_title)):
    car_resume.append("")
    for z in range(len(car_atributes[i])):
      car_resume[i]=car_resume[i]+f"{c_atributes_list_t[z].replace("\r\n", "").strip()}: {c_atributes_list[z].strip()};   "
  return car_resume

data= get_url()

#isirenkam is nucrawlinto saito data apie auto pavadinimus
car_name=data.xpath("//a/img/@alt")
#linkai i nuotraukas
car_img=car_im()
#for link in data.xpath("//a/img/@src"):
    #car_img.append("https://www.renault.lt/" + link)

#linkai i aprasymus
car_link=car_lin()
#for link in data.xpath("//a[@class='vehicle-item fp-cta-gtm']/@href"):
    #car_link.append("https://www.renault.lt/" + link)

#gaunam aprasymu reiksmes
car_atributes=car_atribute()
#for i in car_link:
  #parse_url= get(i).text
  #parse_url= HTML(parse_url)
  #car_atributes.append(parse_url.xpath("//div[contains(@class,'col-md-3')]//span"))

#gaunam aprasymu pavadinimus
car_atributes_title=car_atribute_titl()
#for i in car_link:
  #parse_url= get(i).text
  #parse_url= HTML(parse_url)
  #car_atributes_title.append(parse_url.xpath("//div[@class='wysiwyg-block wysiwyg-block--16 wysiwyg-block--center']")) 

#spausdinam aprasymus su ju pavadinimais
"""
c_atributes_list=[]
for c_a_set in car_atributes:
  for i in c_a_set:
    c_atributes_list.append(i.text)
c_atributes_list_t=[]
for c_a_set_a in car_atributes_title:
  for i in c_a_set_a:
    c_atributes_list_t.append(i.text)

#sudarom aprasyma
car_resume=[]
for i in range(len(car_atributes_title)):
  car_resume.append("")
  for z in range(len(car_atributes[i])):
    car_resume[i]=car_resume[i]+f"{c_atributes_list_t[z].replace("\r\n", "").strip()}: {c_atributes_list[z].strip()};   "
"""
car_resume=car_resum(car_atributes_title, car_atributes)

csv_rasymas()
