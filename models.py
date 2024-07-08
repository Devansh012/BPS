from django.db import models
# from colorfield.fields import ColorField

import datetime

# Create your models here.
class Project(models.Model):

    CHOICES = (
        ('Nos','Nos'),
        ('Meter','Meter'),
    )
    name = models.CharField(max_length=100)
    # description = models.TextField()
    baseComponent = models.BooleanField(default=False)
    serialNumber = models.IntegerField( null=True)
    project = models.CharField(max_length=20 , null=True)
    weightage = models.DecimalField(max_digits=10, decimal_places=1 ,null=True)
    parentComponent = models.CharField(max_length=20,null=True)
    quantity = models.DecimalField(max_digits=10, decimal_places=1,null=True)
    unit = models.CharField(max_length=20, choices = CHOICES , null=True)
    progress = models.DecimalField(max_digits=10, decimal_places=1,null=True)
    description = models.TextField(null=True)
    baseStartDate = models.DateField(("Date"), null=True)
    baseEndDate = models.DateField(("Date"), null=True)
    actualStartDate = models.DateField(("Date"), null=True)
    actualEndDate = models.DateField(("Date"), null = True)
    # color = ColorField(verbose_name="Color",default="#000000")
    hasSegments = models.BooleanField(default=False)
    subContracts = models.CharField(max_length=30, null=True)
    completed = models.BooleanField(default=False)
    fieldQuantity = models.DecimalField(max_digits=10, decimal_places=1,null=True)
    principalMaterial = models.CharField(max_length=30 , null=True)

    def __str__(self):
        return self.name
