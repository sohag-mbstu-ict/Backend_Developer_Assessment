
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





