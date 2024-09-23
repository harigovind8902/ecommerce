from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Products(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    products_image = models.ImageField(upload_to='Products')
    category = models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self):
        return self.name
