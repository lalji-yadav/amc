from django.db import models

# Create your models here.


class Amc(models.Model):
    # AMC_TYPE = (
    #     ('', 'Select'),
    #     ('Quarterly', 'Quarterly'),
    #     ('Half yearly', 'Half yearly'),
    #     ('Annual', 'Annual'),
    # )

    CustomerName = models.CharField(max_length=30)
    AmcType = models.CharField(max_length=30)
    AmcWarrenty =models.CharField(max_length=30)
    MaxFeeServices = models.IntegerField()
    StartDate = models.DateField(max_length=30)
    EndDate = models.DateField(max_length=30)
    email = models.EmailField(max_length=50)
