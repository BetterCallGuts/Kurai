from django.db import models
from datetime import datetime
import                os



class Category(models.Model):

    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Product(models.Model):

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    # Main
    name  = models.CharField (max_length=250)
    Price = models.FloatField(default=0)
    descr = models.TextField (blank=True, null=True)
    thumb = models.ImageField(upload_to="Product_thumbnails")
    # 
    # 
    quantity     = models.FloatField  (default=0)
    out_of_stock = models.BooleanField(default=True)
    on_sale      = models.BooleanField(default=False)
    old_price    = models.FloatField  (default=0, )

    at           = models.DateTimeField(default=datetime.now)


    def delete(self, *args, **kwargs):
        try:
            os.remove(self.thumb.path)
        except:
            pass
        return super().delete(*args, **kwargs)
    def __str__(self) :
        return self.name
    


class ProductImages(models.Model):
    prod   = models.ForeignKey(Product, on_delete=models.CASCADE)
    image  = models.ImageField(upload_to="Product_images")


    def delete(self, *args, **kwargs):
        try:
            os.remove(self.image.path)
        except:
            pass
        return super().delete(*args, **kwargs)

    def __str__(self):
        return self.prod.name + " - " + self.image.name



class Review(models.Model):

    product = models.ForeignKey   (Product, on_delete=models.CASCADE)
    user    = models.ForeignKey   ('auth.User', on_delete=models.CASCADE)  
    rating  = models.IntegerField (default=0, )
    comment = models.TextField    (blank=True, null=True)
    created = models.DateTimeField(default=datetime.now)
    updated = models.DateTimeField(default=datetime.now)
    
    def __str__(self):
        return self.product.name + " - " + "Comment"



class Cart(models.Model):
    user     = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    product  = models.ForeignKey(Product    , on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    is_done  = models.BooleanField(default=False)

    def __str__(self):
        return self.product.name + " - " + str(self.quantity)


class Pages(models.Model):
    name = models.CharField(max_length=250)
    image= models.ImageField(upload_to="Pages_image")

    def __str__(self):
        return self.name
    def delete(self, *args, **kwargs):
        try:
            os.remove(self.image.path)
        except:
            pass
        return super().delete(*args, **kwargs)