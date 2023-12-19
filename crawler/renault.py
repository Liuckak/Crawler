from lxml.etree import HTML
from requests import get
import csv
#crawlinam web
def csv_rasymas():
  fieldnames=['Pavadinimas', 'Img', 'Linkas', 'Aprasymas']
  with open("Renault.csv", "w", encoding='utf-8', newline='') as file_writer:
    csv_write = csv.DictWriter(file_writer, fieldnames, delimiter = ',')
    csv_write.writeheader()
    for i in range(len(car_name)):
        csv_write.writerow({"Pavadinimas": car_name[i], "Img": car_img[i], "Linkas": car_link[i],"Aprasymas": car_resume[i]}) 

def get_url():
  data= get("https://www.renault.lt/index.html?CAMPAIGN=lt-lt-r-t-def-brand-all_products-ice-go-classic--&ORIGIN=SEA&ds_rl=1297188&ds_rl=1297188&gclid=CjwKCAiA-P-rBhBEEiwAQEXhH_TEgbNrfO3zZD6J7VAtZ4yzwQ5H9pn37wQqVQ2HNROD48nfQBX5CxoCSbkQAvD_BwE&gclsrc=aw.ds").text
  return HTML(data)

 

data= get_url()

#isirenkam is nucrawlinto saito data apie auto pavadinimus
car_name=data.xpath("//a/img/@alt")
#linkai i nuotraukas
car_img=[]
for link in data.xpath("//a/img/@src"):
    car_img.append("https://www.renault.lt/" + link)

#linkai i aprasymus
car_link=[]
for link in data.xpath("//a[@class='vehicle-item fp-cta-gtm']/@href"):
    car_link.append("https://www.renault.lt/" + link)

#gaunam aprasymu reiksmes
car_atributes=[]
for i in car_link:
  parse_url= get(i).text
  parse_url= HTML(parse_url)
  car_atributes.append(parse_url.xpath("//div[contains(@class,'col-md-3')]//span"))

#gaunam aprasymu pavadinimus
car_atributes_title=[]
for i in car_link:
  parse_url= get(i).text
  parse_url= HTML(parse_url)
  car_atributes_title.append(parse_url.xpath("//div[@class='wysiwyg-block wysiwyg-block--16 wysiwyg-block--center']")) 

#spausdinam aprasymus su ju pavadinimais
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
for i in range(len(car_atributes)):
  car_resume.append("")
  for z in range(len(car_atributes[i])):
    car_resume[i]=car_resume[i]+f"{c_atributes_list_t[z].replace("\r\n", "").strip()}: {c_atributes_list[z].strip()}"
print(car_resume)
csv_rasymas()
