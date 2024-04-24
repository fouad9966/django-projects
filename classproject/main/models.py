from django.db import models

# Create your models here.
class Banks(models.Model):
    bank_name = models.CharField(max_length=30)
    no_of_staffs = models.IntegerField(null=True)

    def __str__(self):
        return self.bank_name
    
class Skills(models.Model):
    skill_name= models.CharField(max_length=40)
    
class Employee(models.Model):
    staff_name = models.CharField(max_length=50)
    staff_level = models.IntegerField(null=True)
    staff_age = models.IntegerField(null=True)
    bank_name = models.ForeignKey(Banks, on_delete=models.CASCADE)
    skill = models.ManyToManyField(Skills)

    def __str__(self):
        return self.staff_name
    
class Women(models.Model):
    name = models.CharField(max_length=50)
    marital_status = models.CharField(max_length=20)
    age = models.IntegerField(null=True)
    employment_status = models.CharField(max_length=40)
    no_of_kids = models.IntegerField(null=True)
    
    def __str__(self):
        return self.name

    
