from django.db import models

# Create your models here.
class AdminUser(models.Model):
    name = models.CharField(max_length=16)
    password = models.CharField(max_length=16)


    class Meta:
        db_table='AdminUser'