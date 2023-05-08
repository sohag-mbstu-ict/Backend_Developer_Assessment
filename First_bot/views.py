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

from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_framework.views import APIView
from django.http import Http404

from rest_framework.renderers import TemplateHTMLRenderer

from rest_framework import generics
from rest_framework import mixins
from rest_framework import serializers

from First_bot.models import Product,ProductDescription
from First_bot.serializers import ProductSerializer,ProductDescriptionSerializer

#################    GenericApiView based API     #################
#https://www.django-rest-framework.org/api-guide/generic-views/
#https://www.django-rest-framework.org/tutorial/3-class-based-views/
class GenericApiView_Product(generics.GenericAPIView, 
                     mixins.ListModelMixin,
                     mixins.CreateModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.DestroyModelMixin):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    lookup_field="id"

    #https://www.django-rest-framework.org/tutorial/3-class-based-views/
    def get(self,request,id=None):
        if id:
            return self.retrieve(request,id)
        else:
            return self.list(request)
        
    def post(self,request):
        return self.create(request)
    
    def put(self,request,id=None):
        return self.update(request,id)
    
    def delete(self,request,id=id):
        return self.destroy(request,id)
    
class GenericApiView_Product_Description(generics.GenericAPIView, 
                     mixins.ListModelMixin,
                     mixins.CreateModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.DestroyModelMixin):
    queryset=ProductDescription.objects.all()
    serializer_class=ProductDescriptionSerializer
    lookup_field="id"

    #https://www.django-rest-framework.org/tutorial/3-class-based-views/
    def get(self,request,id=None):
        if id:
            return self.retrieve(request,id)
        else:
            return self.list(request)
        
    def post(self,request):
        return self.create(request)
    
    def put(self,request,id=None):
        return self.update(request,id)
    
    def delete(self,request,id=id):
        return self.destroy(request,id)


###########################################################
def home(request):
    return render(request,'search.html')

def index(request):
    #Product.objects.all().delete()

    if(request.method=='POST'):
        search=request.POST["search"]
        print("Search &&&&&&&&&&&&&&&&&&&& ",search)
    else:
        print("ERORRRRRRRRRRRRRRRRRRRRRRRRR")



    


    option=Options()
    option.headless=True
    option.add_argument("window-size=1600x900")



    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    driver = webdriver.Chrome(options=chrome_options)

    driver = webdriver.Chrome(ChromeDriverManager().install())
    # web = 'https://www.amazon.com'
    # driver.get(web)



    # driver.implicitly_wait(3)
    # keyword = search
    # search = driver.find_element(By.ID, 'twotabsearchtextbox')
    # search.send_keys(keyword)
    # # click search button
    # search_button = driver.find_element(By.ID, 'nav-search-submit-button')
    # search_button.click()

    # driver.implicitly_wait(3)



    # #driver.maximize_window()
    # name_l=[]
    # link_l=[]


    # last_page_num=int(driver.find_elements(By.CSS_SELECTOR,"span.s-pagination-item.s-pagination-disabled")[1].text)
    # print("%%%%%%%%%%%%%%%%%%%%%%%%%%% last_page_num : ",last_page_num)

    # box_l=[]

    # c=0
    # for _ in range(1,2):
    #     box=driver.find_elements(By.CSS_SELECTOR,"div.a-section.a-spacing-none.puis-padding-right-small.s-title-instructions-style")
    #     c=c+1
    #     print("ccccccccccccccccccccccccccccccc : ",c)
    #     for item in box:
    #         name=item.find_element(By.CSS_SELECTOR,"h2 a span").text
    #         #print("NNNNNNNNNNNNNNNNNNNNNNNNNNNName : ",name,"   ",c)
    #         link=item.find_element(By.CSS_SELECTOR,"h2 a")
    #         #https://stackoverflow.com/questions/36476861/selenium-webelement-object-has-no-attribute-get-attribute
    #         link=link.get_attribute('href')
    #         # print("  Linkkkkkkkkkkkkk : ",link)
            
    #         link_l.append(link)
    #         name_l.append(name)
    #     time.sleep(5)
    #     new_page=driver.find_element(By.CSS_SELECTOR,"a.s-pagination-item.s-pagination-next.s-pagination-button.s-pagination-separator")
    #     new_page.click()
    #     time.sleep(3)
    
    # #print("****************************  name_l : ",link_l,"       ",len(link_l))

    # Product.objects.all().delete()
    # #Product.objects.create(id=2,name="hello")
    # for i in range(0,len(link_l)):
    #     Product.objects.create(id=i,link=link_l[i],name=name_l[i])
    #     # values=Product(name=name_l[i],link=link_l[i])
    #     # values.save()


    # driver.quit()
    # # print("name_l : ",name_l,"         ",len(name_l))
    # #print("ccccccccccccccccccccccccccccccc : ",c)

##################################################################################################
    # #Product.objects.all().delete()
    # #Product.objects.create(id=2,name="hello")
    obj=Product.objects.all().values()
    #print("$$$$$$$$$$$$$$$$$ obj obj : ",obj)
    id=Product.objects.values_list('id',flat=True)
    #print("$$$$$$$$$$$$$$$$$ idddddddddd : ",id)

    # #https://betterprogramming.pub/understanding-django-database-querysets-and-its-optimizations-1765cb9c36e5
    c=0
    for each in Product.objects.all():
        #print("each.link   :   ",each.link)
        a=each.link
        c=c+1
        break
        # if(c==2):
        #     break
    print("aaaaaaaaaaaaaaaaaaaaaaaa web   :   ",a)
    web=a
    #web = 'https://www.amazon.com/gp/slredirect/picassoRedirect.html/ref=pa_sp_atf_aps_sr_pg1_1?ie=UTF8&adId=A0300086DVV103RTJFEJ&qualifier=1683472286&id=5670395769173738&widgetName=sp_atf&url=%2FiOttie-Compatible-Midnight-Charging-Including%2Fdp%2FB0C1DHHG9N%2Fref%3Dsr_1_2_sspa%3Fkeywords%3Dwireless%2Bcharger%26qid%3D1683472286%26sr%3D8-2-spons%26psc%3D1'
    time.sleep(3)
    driver.implicitly_wait(7)
    driver.get(web)
    time.sleep(15)
    driver.implicitly_wait(15)
    name= WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR,"span#productTitle.a-size-medium.product-title-word-break.product-title-resize"))).text
    #name=driver.find_element(By.CSS_SELECTOR,"span#productTitle.a-size-medium.product-title-word-break.product-title-resize").text
    time.sleep(2)
    availability=driver.find_element(By.CSS_SELECTOR,"span.a-size-medium.a-color-success").text
    time.sleep(2)
    rating=WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="acrPopover"]/span[1]/a/span'))).text
    #time.sleep(2)
    total_rating=driver.find_element(By.XPATH,'//*[@id="acrCustomerReviewText"]').text
    #time.sleep(2)
    price=driver.find_element(By.CSS_SELECTOR,"span.a-price-whole").text
    #time.sleep(2)
    shipping_import_details=driver.find_element(By.XPATH,'//*[@id="amazonGlobal_feature_div"]/span[1]').text
    #time.sleep(2)
    delivery=driver.find_element(By.XPATH,'//*[@id="mir-layout-DELIVERY_BLOCK-slot-PRIMARY_DELIVERY_MESSAGE_LARGE"]/span/span[1]').text
    #time.sleep(2)
    brand=driver.find_element(By.XPATH,'//*[@id="poExpander"]/div[1]/div/table/tbody/tr[1]/td[2]/span').text
    #time.sleep(2)
    connectivity_technology=driver.find_element(By.XPATH,'//*[@id="poExpander"]/div[1]/div/table/tbody/tr[2]/td[2]/span').text

    connector_type=driver.find_element(By.XPATH,'//*[@id="poExpander"]/div[1]/div/table/tbody/tr[3]/td[2]/span').text

    compatible_device=driver.find_element(By.XPATH,'//*[@id="poExpander"]/div[1]/div/table/tbody/tr[4]/td[2]/span').text

    compatible_models=driver.find_element(By.XPATH,'//*[@id="poExpander"]/div[1]/div/table/tbody/tr[5]/td[2]/span[1]/span/span[2]').text
    time.sleep(2)
    #special_features=driver.find_element(By.XPATH,'//*[@id="poExpander"]/div[1]/div/table/tbody/tr[7]/td[2]/span[1]/span/span[2]').text
    #time.sleep(2)
    # color=driver.find_element(By.XPATH,'//*[@id="poExpander"]/div[1]/div/table/tbody/tr[8]/td[2]/span').text
    # time.sleep(2)
    # input_voltage=driver.find_element(By.XPATH,'//*[@id="poExpander"]/div[1]/div/table/tbody/tr[9]/td[2]/span').text
    # time.sleep(2)
    # mounting_type=driver.find_element(By.XPATH,'//*[@id="poExpander"]/div[1]/div/table/tbody/tr[10]/td[2]/span').text
    # time.sleep(2)
    about_this_item=driver.find_element(By.XPATH,'//*[@id="feature-bullets"]/ul').text


    ProductDescription.objects.all().delete()
    values_=ProductDescription(genre_id=1,name=name,availability=availability,rating=rating,
                total_rating=total_rating,price=price,shipping_import_details=shipping_import_details,
                delivery=delivery,brand=brand,connectivity_technology=connectivity_technology,
                connector_type=connector_type,compatible_device=compatible_device,
                compatible_models=compatible_models,about_this_item=about_this_item)
    values_.save()

    print("1111111111nameeeeeeeee name : ",rating)

    return HttpResponse("Hello, world. You're at the polls index.")