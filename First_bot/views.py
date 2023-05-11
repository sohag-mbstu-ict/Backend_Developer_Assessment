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
import simplejson as json

from First_bot.models import Product,ProductDescription
from First_bot.serializers import ProductSerializer,ProductDescriptionSerializer
from django.template import loader

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
    # mydata = ProductDescription.objects.all().values()
    # template = loader.get_template('display.html')
    # context = {
    #     'mymembers': mydata,
    # }
    # return HttpResponse(template.render(context, request))
    return render(request,'search.html')
    

def index(request):
    #Product.objects.all().delete()

    if(request.method=='POST'):
        search=request.POST["search"]
        print("Search &&&&&&&&&&&&&&&&&&&& ",search)
    else:
        print("ERORRRRRRRRRRRRRRRRRRRRRRRRR")

    option=Options()
    option.add_argument("enable-automation")
    option.add_argument("--headless")
    option.add_argument("--window-size=1920,1080")
    option.add_argument("--no-sandbox")
    option.add_argument("--disable-extensions")
    option.add_argument("--dns-prefetch-disable")
    option.add_argument("--disable-gpu")
    option.page_load_strategy = 'normal'
    driver = webdriver.Chrome(options=option)
    web = 'https://www.amazon.com'
    driver.get(web)
    #driver = webdriver.Chrome(ChromeDriverManager().install())


    driver.implicitly_wait(2)
    keyword = search
    search = driver.find_element(By.ID, 'twotabsearchtextbox')
    search.send_keys(keyword)
    # click search button
    search_button = driver.find_element(By.ID, 'nav-search-submit-button')
    search_button.click()

    driver.implicitly_wait(2)



    #driver.maximize_window()
    name_l=[]
    link_l=[]


    last_page_num=int(driver.find_elements(By.CSS_SELECTOR,"span.s-pagination-item.s-pagination-disabled")[1].text)
    print("%%%%%%%%%%%%%%%%%%%%%%%%%%% last_page_num : ",last_page_num)

    box_l=[]

    c=0
    
    box=driver.find_elements(By.CSS_SELECTOR,"div.a-section.a-spacing-none.puis-padding-right-small.s-title-instructions-style")
    c=c+1
    print("ccccccccccccccccccccccccccccccc : ",c)
    for item in box:
        name=item.find_element(By.CSS_SELECTOR,"h2 a span").text
        #print("NNNNNNNNNNNNNNNNNNNNNNNNNNNName : ",name,"   ",c)
        link=item.find_element(By.CSS_SELECTOR,"h2 a")
        #https://stackoverflow.com/questions/36476861/selenium-webelement-object-has-no-attribute-get-attribute
        link=link.get_attribute('href')
        # print("  Linkkkkkkkkkkkkk : ",link)
            
        link_l.append(link)
        name_l.append(name)
    #time.sleep(5)
    # new_page=driver.find_element(By.CSS_SELECTOR,"a.s-pagination-item.s-pagination-next.s-pagination-button.s-pagination-separator")
    # new_page.click()
    # time.sleep(3)
    
    #print("****************************  name_l : ",link_l,"       ",len(link_l))

    Product.objects.all().delete()
    #Product.objects.create(id=2,name="hello")
    for i in range(0,6):
        #Product.objects.create(id=i,link=link_l[i],name=name_l[i])
        values=Product(id=i,link=link_l[i],name=name_l[i])
        values.save()

    count= Product.objects.all().count()
    print("count /////////////////////// ",count)
    
    # print("name_l : ",name_l,"         ",len(name_l))
    #print("ccccccccccccccccccccccccccccccc : ",c)

##################################################################################################
    # #Product.objects.all().delete()
    # #Product.objects.create(id=2,name="hello")
    #obj=Product.objects.all().values()
    #print("$$$$$$$$$$$$$$$$$ obj obj : ",obj)
    #id=Product.objects.values_list('id',flat=True)
    #print("$$$$$$$$$$$$$$$$$ idddddddddd : ",id)

    # #https://betterprogramming.pub/understanding-django-database-querysets-and-its-optimizations-1765cb9c36e5
    c=0
    ProductDescription.objects.all().delete()
    for each in Product.objects.all():
        c=c+1
        if(c>5):
            break
        #print("each.link   :   ",each.link)
        idd=each.id
        a=each.link
        #break  
        print("cccccccccccccccccccccccccc   :   ",c)
        print("web web  web web web web web web   :   ",a)
        web=a
        #web = 'https://www.amazon.com/Apple-MHXH3AM-A-MagSafe-Charger/dp/B08L5NP6NG/ref=sr_1_4?keywords=wireless+charger&qid=1683472286&sr=8-4'
        driver.get(web)
        time.sleep(5)
        
        try:
            if(driver.find_element(By.XPATH,'//*[@id="productTitle"]')):
                name=driver.find_element(By.XPATH,'//*[@id="productTitle"]').text
        except:
            name="Currently unavailable"

        try:
            if(driver.find_element(By.XPATH,'//*[@id="availability"]/span')):
                availability=driver.find_element(By.XPATH,'//*[@id="availability"]/span').text
        except:
            availability="Currently unavailable"
        
        try:
            if(driver.find_element(By.XPATH,'//*[@id="acrPopover"]/span[1]/a/span')):
                rating=float(driver.find_element(By.XPATH,'//*[@id="acrPopover"]/span[1]/a/span').text)
                print("   rating gggggg  : ",rating,"    type   : ",type(rating))
        except:
            rating=0
        
        try:
            if(driver.find_element(By.XPATH,'//*[@id="acrCustomerReviewText"]')):
                total_rating=driver.find_element(By.XPATH,'//*[@id="acrCustomerReviewText"]').text
        except:
            total_rating="Currently unavailable"

        #First XPATH price
        ck_price=0
        try:
            if(driver.find_element(By.XPATH,'//*[@id="corePriceDisplay_desktop_feature_div"]/div[1]/span[2]/span[2]/span[2]')):
                price=float(driver.find_element(By.XPATH,'//*[@id="corePriceDisplay_desktop_feature_div"]/div[1]/span[2]/span[2]/span[2]').text)
                ck_price=1
        except:
          price=0

        #Second XPATH for price
        if(ck_price==0):
            try:
                if(driver.find_element(By.XPATH,'//*[@id="corePriceDisplay_desktop_feature_div"]/div[1]/span[1]/span[2]/span[2]')):
                        price=float(driver.find_element(By.XPATH,'//*[@id="corePriceDisplay_desktop_feature_div"]/div[1]/span[1]/span[2]/span[2]').text)
            except:
                price=0

        
        try:
            if(driver.find_element(By.XPATH,'//*[@id="amazonGlobal_feature_div"]/span[1]')):
                shipping_import_details=driver.find_element(By.XPATH,'//*[@id="amazonGlobal_feature_div"]/span[1]').text
        except:
            shipping_import_details="Currently unavailable" 
            
        try:
            if(driver.find_element(By.XPATH,'//*[@id="mir-layout-DELIVERY_BLOCK-slot-PRIMARY_DELIVERY_MESSAGE_LARGE"]/span/span[1]')):
                delivery=driver.find_element(By.XPATH,'//*[@id="mir-layout-DELIVERY_BLOCK-slot-PRIMARY_DELIVERY_MESSAGE_LARGE"]/span/span[1]').text
        except:
            delivery="Currently unavailable" 
        
        #First XPATH of brand
        ck_brand=0
        try:
            if(driver.find_element(By.XPATH,'//*[@id="poExpander"]/div[1]/div/table/tbody/tr[1]/td[2]/span')):
                brand=driver.find_element(By.XPATH,'//*[@id="poExpander"]/div[1]/div/table/tbody/tr[1]/td[2]/span').text
                ck_brand=1
        except:
            brand="Currently unavailable"

        #Second XPATH for brand
        if(ck_brand==0):
            try:
                if(driver.find_element(By.XPATH,'//*[@id="productOverview_feature_div"]/div/table/tbody/tr[1]/td[2]/span')):
                        brand=driver.find_element(By.XPATH,'//*[@id="productOverview_feature_div"]/div/table/tbody/tr[1]/td[2]/span').text
            except:
                brand="Currently unavailable"

        try:
            if(driver.find_element(By.XPATH,'//*[@id="poExpander"]/div[1]/div/table/tbody/tr[2]/td[2]/span')):
                connectivity_technology=driver.find_element(By.XPATH,'//*[@id="poExpander"]/div[1]/div/table/tbody/tr[2]/td[2]/span').text
        except:
            connectivity_technology="Currently unavailable"

        try:
            if(driver.find_element(By.XPATH,'//*[@id="poExpander"]/div[1]/div/table/tbody/tr[3]/td[2]/span')):
                connector_type=driver.find_element(By.XPATH,'//*[@id="poExpander"]/div[1]/div/table/tbody/tr[3]/td[2]/span').text
        except:
            connector_type="Currently unavailable"

        try:
            if(driver.find_element(By.XPATH,'//*[@id="poExpander"]/div[1]/div/table/tbody/tr[4]/td[2]/span[1]/span/span[2]')):
                compatible_device=driver.find_element(By.XPATH,'//*[@id="poExpander"]/div[1]/div/table/tbody/tr[4]/td[2]/span[1]/span/span[2]').text
        except:
            compatible_device="Currently unavailable"

        try:
            if(driver.find_element(By.XPATH,'//*[@id="poExpander"]/div[1]/div/table/tbody/tr[5]/td[2]/span[1]/span/span[2]')):
                compatible_models=driver.find_element(By.XPATH,'//*[@id="poExpander"]/div[1]/div/table/tbody/tr[5]/td[2]/span[1]/span/span[2]').text
        except:
            compatible_models="Currently unavailable"

        # try:
        #     if(driver.find_element(By.XPATH,'//*[@id="poExpander"]/div[1]/div/table/tbody/tr[7]/td[2]/span')):
        #         special_features=driver.find_element(By.XPATH,'//*[@id="poExpander"]/div[1]/div/table/tbody/tr[7]/td[2]/span').text
        # except:
        #     special_features="Currently unavailable"

        # try:
        #     if(driver.find_element(By.XPATH,'//*[@id="poExpander"]/div[1]/div/table/tbody/tr[8]/td[2]/span')):
        #         color=driver.find_element(By.XPATH,'//*[@id="poExpander"]/div[1]/div/table/tbody/tr[8]/td[2]/span').text
        # except:
        #     color="Currently unavailable"

        # try:
        #     if(driver.find_element(By.XPATH,'//*[@id="poExpander"]/div[1]/div/table/tbody/tr[9]/td[2]/span')):
        #         input_voltage=driver.find_element(By.XPATH,'//*[@id="poExpander"]/div[1]/div/table/tbody/tr[9]/td[2]/span').text
        # except:
        #     input_voltage="Currently unavailable"

        # try:
        #     if(driver.find_element(By.XPATH,'//*[@id="poExpander"]/div[1]/div/table/tbody/tr[10]/td[2]/span')):
        #         mounting_type=driver.find_element(By.XPATH,'//*[@id="poExpander"]/div[1]/div/table/tbody/tr[10]/td[2]/span').text
        # except:
        #     mounting_type="Currently unavailable"

        try:
            if(driver.find_element(By.XPATH,'//*[@id="feature-bullets"]/ul')):
                about_this_item=driver.find_element(By.XPATH,'//*[@id="feature-bullets"]/ul').text
        except:
            about_this_item="Currently unavailable"

        #https://stackoverflow.com/questions/1110153/what-is-the-most-efficient-way-to-store-a-list-in-the-django-models
        #https://stackoverflow.com/questions/65531814/extract-all-the-src-attribute-from-the-images-of-amazon-product-page-in-selenium
        img_l=[]
        my_img=ProductDescription()
        #for my_elem in WebDriverWait(driver, 20).until(EC.visibility_of_all_elements_located((By.XPATH, "//div[@id='altImages']/ul//li[@data-ux-click]//img"))):
        time.sleep(2)
        for my_elem in driver.find_elements(By.CSS_SELECTOR,'#a-autoid-4-announce >img'):
            img_l.append(my_elem.get_attribute("src"))
        #my_img.img=json.dumps(img_l)
        #driver.find_elements(By.CSS_SELECTOR,

        #ProductDescription.objects.all().delete()
        print("1111111111nameeeeeeeee name : ",rating)
        values_=ProductDescription (genre_id=c,id=c,name=name,availability=availability,rating=rating,
                    total_rating=total_rating,price=price,shipping_import_details=shipping_import_details,
                    delivery=delivery,brand=brand,about_this_item=about_this_item,img=json.dumps(img_l),
                    connectivity_technology=connectivity_technology,connector_type=connector_type,
                    compatible_device=compatible_device,compatible_models=compatible_models)
        values_.save()

        print("1111111111nameeeeeeeee name : ",rating)
        #break
    driver.quit()

    mydata = ProductDescription.objects.all().values()
    template = loader.get_template('display.html')
    context = {
        'mymembers': mydata,
    }
    return HttpResponse(template.render(context, request))