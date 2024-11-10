from django.db import models

# Create your models here.
class Client(models.Model):
    username = models.CharField(max_length=50)
    email =models.EmailField()
    password = models.CharField(max_length=50)
    shipping_address = models.CharField(max_length=50)
    billing_address = models.IntegerField(null=5)
    order_history =models.CharField(max_length=50)
    cart = models.CharField(max_length=60)
    payment_information = models.CharField(max_length=50)


    def __str__(self):
        return self.username
class Products(models.Model):
        pimage = models.ImageField(upload_to='product_images/', null=True, blank=True)
        pname = models.CharField(max_length=50)
        pprice = models.DecimalField(max_digits=4,decimal_places=2,null=True)
        pdescription = models.TextField(default="no description")

        def __str__(self):
             return self.pname




    