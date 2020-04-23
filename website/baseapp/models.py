from django.db import models

# Create your models here.
class Book_Product(models.Model):
    name=models.CharField(max_length=80)
    desc=models.TextField()
    price=models.IntegerField()
    img=models.ImageField(upload_to='pics')
    offer=models.BooleanField()
    author_name=models.CharField(max_length=80)
    category=models.CharField(max_length=80)

    def __str__(self):
        return self.name
