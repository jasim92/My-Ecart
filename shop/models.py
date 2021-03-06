from django.db import models

# Create your models here.
class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, default="")
    subcategory = models.CharField(max_length=50, default="")
    price = models.IntegerField(default=0)
    product_desc = models.CharField(max_length=1000)
    publish_date = models.DateField()
    image = models.ImageField(upload_to="shop/images", default="")


    def __str__(self):
        return self.product_name

class Contact(models.Model):
    msg_id = models.AutoField(primary_key = True)
    name = models.CharField(max_length=15)
    email = models.CharField(max_length=20, default="")
    phone = models.IntegerField(max_length=12, default="")
    desc = models.CharField(max_length=500, default="")

    def __str__(self):
        return self.name
class Orders(models.Model):
    order_id = models.AutoField(primary_key = True)
    items_json = models.CharField(max_length=5000)
    name = models.CharField(max_length=20)
    # total_amount = models.IntegerField(default=0)
    email = models.CharField(max_length=20)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    zip_code = models.IntegerField(max_length=6)
    phone = models.IntegerField(max_length=12, default="")

    def __str__(self):
        return self.name

class OrderUpdate(models.Model):
    update_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField(default="")
    update_desc = models.CharField(max_length=5000)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.update_desc[0:7] + "..."

