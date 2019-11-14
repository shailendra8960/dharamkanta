from django.db import models

# Create your models here.

class Product(models.Model):
    p_id = models.AutoField(primary_key=True)
    p_name = models.CharField(max_length=100,default="")
    p_category = models.CharField(max_length=100,default="")
    p_desc = models.CharField(max_length=300, default="")
    p_price = models.CharField(max_length=100,default="")
    p_upload_date = models.DateField()
    p_capacity = models.CharField(max_length=100,default="")
    p_division = models.CharField(max_length=100,default="")
    p_pan_size = models.CharField(max_length=100,default="")
    p_img = models.ImageField(upload_to='images')

    def __str__(self):
        return self.p_name