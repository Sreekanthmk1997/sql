

from django.db import models

class Employee(models.Model):
    employee_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    email = models.EmailField(unique=True)
    number = models.CharField(max_length=15)
    hire_date = models.DateField()
    job = models.CharField(max_length=50)
    department = models.CharField(max_length=50)

    salary = models.DecimalField(max_digits=10, decimal_places=2)
    manager_id = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.first_name
