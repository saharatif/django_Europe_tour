from django.db import models

# Create your models here.

class Trip(models.Model):
    #id = models.AutoField(primary_key=True)
    origin= models.CharField(max_length=64)
    destination= models.CharField(max_length=64)
    nights= models.IntegerField()
    price= models.IntegerField()

    def __str__(self):
        return f"{self.id} - {self.origin} To {self.destination} for {self.nights} and costs {self.price} EUROS"
    

