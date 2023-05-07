from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from selenium import webdriver
import time
# import from webdriver_manager (using underscore)
from webdriver_manager.chrome import ChromeDriverManager 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.chrome.options import Options

from First_bot.models import Product,ProductDescription

def index(request):
#     #Product.objects.all().delete()
#     Product.objects.create(id=2,name="hello")
#     obj=Product.objects.all().values()
#     print("$$$$$$$$$$$$$$$$$ : ",obj)
#     id=Product.objects.values_list('id',flat=True)
#     print("$$$$$$$$$$$$$$$$$ idddddddddd : ",id)

#     #https://betterprogramming.pub/understanding-django-database-querysets-and-its-optimizations-1765cb9c36e5
#     for each in Product.objects.all():
#         print("each.name   :   ",each.name)


    option=Options()
    option.headless=True
    option.add_argument("window-size=1600x900")



    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    driver = webdriver.Chrome(options=chrome_options)

    driver = webdriver.Chrome(ChromeDriverManager().install())
    web = 'https://www.amazon.com/s?k=wireless+charger+iphone&crid=1ZF4TCRGDRXS8&sprefix=wireless+charger+iphone%2Caps%2C350&ref=nb_sb_noss_1'
    driver.get(web)
    #driver.maximize_window()
    name_l=[]


    last_page_num=int(driver.find_elements(By.CSS_SELECTOR,"span.s-pagination-item.s-pagination-disabled")[1].text)
    print("%%%%%%%%%%%%%%%%%%%%%%%%%%% last_page_num : ",last_page_num)

    box_l=[]

    c=0
    for _ in range(1,5):
        box=driver.find_elements(By.CSS_SELECTOR,"div.a-section.a-spacing-none.puis-padding-right-small.s-title-instructions-style")
        c=c+1
        print("ccccccccccccccccccccccccccccccc : ",c)
        for item in box:
            name=item.find_element(By.CSS_SELECTOR,"h2 a span").text
            #print("NNNNNNNNNNNNNNNNNNNNNNNNNNNName : ",name,"   ",c)
            
            name_l.append(name)
        time.sleep(5)
        new_page=driver.find_element(By.CSS_SELECTOR,"a.s-pagination-item.s-pagination-next.s-pagination-button.s-pagination-separator")
        new_page.click()
        time.sleep(3)
    
    print("****************************  name_l : ",name_l,"       ",len(name_l))

    driver.quit()
    # print("name_l : ",name_l,"         ",len(name_l))
    print("ccccccccccccccccccccccccccccccc : ",c)

    return HttpResponse("Hello, world. You're at the polls index.")