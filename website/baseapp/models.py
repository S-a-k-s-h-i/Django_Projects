from django.db import models

# Create your models here.
class Category(models.Model):
    sub_category = models.CharField(max_length=30)
    def __str__(self):
        return self.sub_category

class Book_Product(models.Model):
    name=models.CharField(max_length=80)
    desc=models.TextField()
    price=models.IntegerField()
    img=models.ImageField(upload_to='pics')
    offer=models.BooleanField()
    author_name=models.CharField(max_length=80)
    sub_categories=models.ManyToManyField('Category',related_name='books')

    def __str__(self):
        return self.name
