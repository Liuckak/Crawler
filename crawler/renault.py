
"""
# apsibrėžti klasę Humanm, kuri turi klasės atributą number_of_humans
# objektų atributus, name, age, gender
import time
class Human:
    number_of_humans= 0
    def __init__ (self, name :str, age: int, gender: str):
        if type(name) != str:
            raise ValueError("irasyti stringa i name")
        self.name=name
        if type(age) != int:
            raise ValueError("irasyti int tipa i age")
        self.age=age
        if type(gender) != str:
            raise ValueError("irasyti stringa i gender")
        self.gender=gender
        self.stringas= ""+ name+ " "+ gender

        

# Apsirašyti klasę Developer, kuri paveldi Human, ir turi papildomus laukelius
# salary, work_hours
class Developer(Human):
    def __init__(self, name: str, age: int, gender: str, salary: float, work_hours:int):
        super().__init__(name, age, gender)
        self.salary=salary
        self.work_hours= work_hours
        self.uzdarbis=salary*work_hours


zmogus= Human("juozas", 23, "vyras")
developer=Developer("vytas", 45, "Vyrukas", 2, 40)
#print(developer.uzdarbis)

def print_time(funk):
    def wrapper(*args, **kwargs):
        prad_t= time.time()
        result=funk(*args, *kwargs)
        pabg_t=time.time()
        print("wraperis")
        kiek +=1
        print(kiek)
        return pabg_t - prad_t
    return wrapper

@print_time
def suma():
        print("Wrappinta funkcija")
        suma1=0
        for i in range(35):
            suma1+=i
        print(suma1)
        return suma1

print(suma())

class Human:
  number_of_humans = 0
  def __init__(self, name:str, age:int, gender:str) -> None:
    self.name = name
    self.age = age
    self.gender = gender
    if not isinstance(self.name, str):
      raise ValueError("Name must be a string")
    if not isinstance(self.age, int):
      raise ValueError("Age must be an integer")
    if not isinstance(self.gender, str):
      raise ValueError("Gender must be a string")

class Developer(Human):
  def __init__(self, name:str, age:int, gender:str, salary:float, work_hours:int) -> None:
    super().__init__(name, age, gender)
    self.salary:float = salary
    self.work_hours:int = work_hours
    if not isinstance(self.salary, float):
      raise ValueError("Salary must be a float")
    if not isinstance(self.work_hours, int):
      raise ValueError("Work hours must be an integer")
"""


"""
import requests
from lxml.etree import HTML
from selenium import webdriver
from pyshadow.main import Shadow
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#driver = webdriver.Chrome(webdriver.ChromeOptions())
#shadow = Shadow(driver)
#z = shadow.chrome_driver.get("https://www.mercedes-benz.lt/passengercars.html?group=all&subgroup=see-all&view=BODYTYPE")
#element = shadow.find_element("owc-simple-teaser")
#text = element.text
driver.get("https://www.mercedes-benz.lt/passengercars.html?group=all&subgroup=see-all&view=BODYTYPE")
shadow_root= driver.find_element(By.XPATH,"owc-simple-teaser").shadow_root

shadow_text= shadow_root.find_element(By.XPATH,"//div").text
#aaa =html.xpath("//div/span[contains(@class, 'dh-io-vmos_2pz0m')]")
print(shadow_text)

options= webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver= webdriver.Chrome(options=options)
url=driver.get("https://www.mercedes-benz.lt/passengercars.html?group=all&subgroup=all.estate&view=BODYTYPE")
driver.implicitly_wait(10)

#shadow_root= driver.find_element(By.XPATH, "//div/owc-simple-teaser").shadow_root
#shadow_text= shadow_root.find_element(By.XPATH,"//div[contains(@class,'dh-io-vmos_2QU0g')]").text
#print(shadow_text)
#shadow_root= driver.find_element(By.XPATH, "//div/owc-simple-teaser")
#shadow_html= shadow_root.execute_script('return arguments[0].shadowRoot',shadow_root)
#shadow_html= shadow_root.get_attribute('innerHTML')
##shadow_host1 = driver.find_element(By.XPATH , "//div/owc-simple-teaser")
#shadow_host1=driver.find_element(By.CSS_SELECTOR, "#shadow_host")
#shadow_root1 = driver.execute_script("return arguments[0].shadowRoot", shadow_host1)
#document.querySelector('dh-io-vmos').shadowRoot.querySelector('div')
#shadow_root11=shadow_root1.find_element(By.XPATH, "//div//span")
shadow_root1 = driver.execute_script("return document.querySelector('dh-io-vmos').shadowRoot.querySelector(div.formatted-text')")
divv= shadow_root1.text
html=HTML(divv)
print(shadow_root1)
"""


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
