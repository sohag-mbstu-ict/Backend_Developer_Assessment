

# Dependencies:

Django 

selenium

webdriver-manager

simplejson

Django REST framework

psycopg2

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

# Store the list of products in first bot of  postgresql datbase

```bash
    count_= Product.objects.all().count()
    for i in range(0,count_):
        values=Product(id=i,link=link_l[i],name=name_l[i])
        values.save()
```

# Store the list of products in postgresql datbase

```bash
  D
```

# Store the list of products in postgresql datbase

```bash
  D
```
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
Starting development server at http://127.0.0.1:8000/


# Propagating changes of models

```bash
  python manage.py makemigrations
  python manage.py migrate 
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
