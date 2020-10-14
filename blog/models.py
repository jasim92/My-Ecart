from django.db import models

# Create your models here.
class Blogposts(models.Model):
    post_id = models.AutoField(primary_key = True)
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50, default="")
    region = models.CharField(max_length=50, default="World")
    heading = models.CharField(max_length=50, default="")
    cheading = models.CharField(max_length=5000, default="")
    subheading1 = models.CharField(max_length=50, default="")
    cheading1 = models.CharField(max_length=5000, default="")
    subheading2 = models.CharField(max_length=50, default="")
    cheading2 = models.CharField(max_length=5000, default="")
    pub_date = models.DateField()
    thumbnail = models.ImageField(upload_to="shop/images", default="")

    def __str__(self):
        return self.title

