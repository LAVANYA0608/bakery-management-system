from django.db import models

class Admin(models.Model):
    admin_id = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=50, unique=True)
    password = models.CharField(max_length=50, blank=False, null=False)

    def __str__(self):
        return self.email

class Customer(models.Model):
    c_id = models.AutoField(primary_key=True)
    c_name = models.CharField(max_length=50)
    c_email = models.EmailField(max_length=50, unique=True)
    password = models.CharField(max_length=50, blank=False, null=False)
    address = models.CharField(max_length=100)
    mobile_no = models.CharField(max_length=15)

    def __str__(self):
        return self.c_name

class Product(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to='product_images/')  # ✅ Uploads to `media/product_images/`
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name