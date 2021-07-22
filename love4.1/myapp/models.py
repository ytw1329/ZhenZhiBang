from django.db import models

# Create your models here.
class User(models.Model):
    name=models.CharField(max_length=20,null=True)
    password=models.CharField(max_length=20)
    tel=models.CharField(max_length=20)

    class Meta:
        db_table='User'

class Admin(models.Model):
    name=models.CharField(max_length=20)
    password=models.CharField(max_length=20)


    class Mete:
        db_table='Admin'


#志愿活动数据库
class activity(models.Model):
    title=models.CharField(max_length=50)
    context=models.CharField(max_length=50)
    time=models.CharField(max_length=50)
    place=models.CharField(max_length=50)
    Organizer=models.CharField(max_length=50)
    qualifications=models.CharField(max_length=50)

    class Meta:
        db_table='activity'

class activity2(models.Model):
    title=models.CharField(max_length=50)
    context=models.CharField(max_length=50)
    time=models.CharField(max_length=50)
    place=models.CharField(max_length=50)
    Organizer=models.CharField(max_length=50)
    qualifications=models.CharField(max_length=50)

    class Meta:
        db_table='activity2'

class Canyu(models.Model):

    name = models.CharField(max_length=20, null=True)
    title = models.CharField(max_length=50)
    context = models.CharField(max_length=50)
    time = models.CharField(max_length=50)
    place = models.CharField(max_length=50)
    Organizer = models.CharField(max_length=50)
    qualifications = models.CharField(max_length=50)
    sex = models.CharField(max_length=3)
    tel = models.CharField(max_length=20)


    class Meta:
        db_table = 'Canyu'

class activity3(models.Model):
    title=models.CharField(max_length=50)
    context=models.CharField(max_length=50)
    time=models.CharField(max_length=50)
    place=models.CharField(max_length=50)
    Organizer=models.CharField(max_length=50)
    qualifications=models.CharField(max_length=50)
    state=models.CharField(max_length=50)


    class Meta:
        db_table='activity3'

class Child(models.Model):

    name=models.CharField(max_length=20)
    sex=models.CharField(max_length=3)
    birthday=models.CharField(max_length=20)
    place=models.CharField(max_length=50)
    time=models.CharField(max_length=20)
    detaile=models.CharField(max_length=100)

    class Meta:
        db_table='Child'

class Childimg(models.Model):
    img=models.ImageField(upload_to='static/pictures/')
    name=models.CharField(max_length=20)
    sex=models.CharField(max_length=3)
    birthday=models.CharField(max_length=20)
    place=models.CharField(max_length=50)
    time=models.CharField(max_length=20)
    detaile=models.CharField(max_length=100)

    class Meta:
        db_table='Childimg'

class Testimg(models.Model):
    img=models.ImageField(upload_to='static/pictures/')

    class Meta:
        db_table='Testimg'

#志愿捐款数据库
class donate(models.Model):
    dproject=models.CharField(max_length=50)
    damount=models.CharField(max_length=50)
    dname=models.CharField(max_length=50)
    dtel=models.CharField(max_length=50)
    dtext=models.CharField(max_length=50)
    dway=models.CharField(max_length=50)

    class Meta:
        db_table='donate'

class Sum1(models.Model):
    sum=models.CharField(max_length=50)

    class Meta:
        db_table='Sum1'