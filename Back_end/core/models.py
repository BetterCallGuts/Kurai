from django.db import models





class Product(models.Model):
    # Main
    name = models.CharField (max_length=250)
    Price= models.FloatField(default=0)
    descr= models.TextField (blank=True, null=True)
    thumb= models.ImageField(upload_to="thumbnails")


    # 
    quantity     = models.FloatField  (default=0)
    out_of_stock = models.BooleanField(default=True)
    on_sale      = models.BooleanField(default=False)
    old_price    = models.FloatField  (default=0, )

    def __str__(self) :
        return self.name
    

class ProductImages(models.Model):
    prod   = models.ForeignKey(Product, on_delete=models.CASCADE)
    pass