from django.db import models


# Create your models here.

# Create Company Models.
class Company(models.Model):
    company_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    about = models.TextField()
    type = models.CharField(max_length=100, choices=
    (
        ('IT', 'IT'),
        ('Non IT', 'Non IT'),
        ('Mobiles Phones', 'Mobiles Phones'),
    )
                            )
    added_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


# Create Models of Employee
class Employee(models.Model):
    emp_id = models.AutoField(primary_key=True)
    emp_name = models.CharField(max_length=100)
    profile = models.CharField(max_length=100)
    age = models.IntegerField()
    about = models.TextField()
    phone = models.CharField(max_length=10)
    datetime = models.DateTimeField(auto_now=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return self.emp_name
