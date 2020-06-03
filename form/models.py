from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.db.models.signals import pre_save
from django.dispatch import receiver

# Create your models here.


class Emp(models.Model):
    author = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    Emp_ID = models.IntegerField()
    First_Name = models.CharField(max_length=50)
    Last_Name = models.CharField(max_length=50)
    Email = models.EmailField()
    Phone = models.CharField(max_length=11)
    Job_Title = models.CharField(max_length=100)
    Department = models.CharField(max_length=100)
    Address = models.CharField(max_length=100)
    City = models.CharField(max_length=100)
    Zipcode = models.CharField(max_length=100)
    Country = models.CharField(max_length=100)
    Salary = models.DecimalField(decimal_places=2, max_digits=15)
    slug = models.SlugField(blank=True, unique=True)

    def __str__(self):
        return self.Email

    class Meta:
        verbose_name_plural = "Record"


def pre_save_item(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.author.username + "-" + str(instance.Emp_ID))


pre_save.connect(pre_save_item, sender=Emp)
