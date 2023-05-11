
# Deployment to pythonanywhere
I have deployed this app to pythonanywhere free server. The link is : https://productdetails.pythonanywhere.com/
# Dependencies:

Django 

selenium

webdriver-manager

simplejson

Django REST framework

psycopg2

# Set up for Selenium Webdriver Running on Chrome Browser

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

# Datbase Connection


```bash
  DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'backend',
        'USER':'postgres',
        'PASSWORD':'1234',
        'HOST':'localhost',
        'PORT':'5432'
    }
}
```


# Propagating changes of models

```bash
  python manage.py makemigrations
  python manage.py migrate 
```

# To automatically search for a specific product on Amazon

```bash
    web = 'https://www.amazon.com'
    driver.get(web)
    driver.implicitly_wait(3)
    keyword = search
    search = driver.find_element(By.ID, 'twotabsearchtextbox')
    search.send_keys(keyword)
    search_button = driver.find_element(By.ID, 'nav-search-submit-button')
    search_button.click()
    driver.implicitly_wait(3)
```

# Scrape the list of products that match the search query

```bash
    last_page_num=int(driver.find_elements(By.CSS_SELECTOR,"span.s-pagination-item.s-pagination-disabled")[1].text)
    box_l=[]
    for _ in range(1,last_page_num):
        box=driver.find_elements(By.CSS_SELECTOR,"div.a-section.a-spacing-none.puis-padding-right-small.s-title-instructions-style")
        c=c+1
        for item in box:
            name=item.find_element(By.CSS_SELECTOR,"h2 a span").text
            link=item.find_element(By.CSS_SELECTOR,"h2 a")
            link=link.get_attribute('href')
            link_l.append(link)
            name_l.append(name)
        time.sleep(5)
        new_page=driver.find_element(By.CSS_SELECTOR,"a.s-pagination-item.s-pagination-next.s-pagination-button.s-pagination-separator")
        new_page.click()
        time.sleep(3)
```

# Store the list in the Product (first bot) table of  postgresql datbase

```bash
    count_= Product.objects.all().count()
    for i in range(0,count_):
        values=Product(id=i,link=link_l[i],name=name_l[i])
        values.save()
```

# Store the list in the ProductDescription (second bot) table of postgresql datbase

```bash
    for each in Product.objects.all():
        web=each.link
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
        except:
            rating=0
        try:
            if(driver.find_element(By.XPATH,'//*[@id="acrCustomerReviewText"]')):
                total_rating=driver.find_element(By.XPATH,'//*[@id="acrCustomerReviewText"]').text
        except:
            total_rating="Currently unavailable"
```



# Declaring Serializers
import necessary things for serializer
```bash
from First_bot.models import Product,ProductDescription
from rest_framework import serializers
```
For ProductSerializer table
```bash
  class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id','link','name']
```
For ProductDescriptionSerializer table
```bash
  class ProductDescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductDescription
        fields = '__all__'
```

# GenericAPIView Product (first bot) table
```bash
from First_bot.models import Product,ProductDescription
from First_bot.serializers import ProductSerializer,ProductDescriptionSerializer

class GenericApiView_Product(generics.GenericAPIView,class GenericApiView_Product(generics.GenericAPIView, 
                     mixins.ListModelMixin,
                     mixins.CreateModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.DestroyModelMixin):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    lookup_field="id"
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
```

# GenericAPIView ProductDescription (second bot) table
```bash
  class GenericApiView_Product_Description(generics.GenericAPIView, 
                     mixins.ListModelMixin,
                     mixins.CreateModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.DestroyModelMixin):
    queryset=ProductDescription.objects.all()
    serializer_class=ProductDescriptionSerializer
    lookup_field="id"
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
```

![Display all Product Detail](https://github.com/sohag-mbstu-ict/Backend_Developer_Assessment/blob/main/Screenshot/HTML.PNG)
