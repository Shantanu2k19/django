from django.db import models

# Create your models here.
class menu(models.Model):
    item= models.CharField(max_length = 64)
    code = models.CharField(max_length = 3)
    price = models.IntegerField()

    #what the object should look like, terminal or page
    def __str__(self):
        return f" {self.item}, code: {self.code} costing {self.price}Rs. \n"

class customer(models.Model):
    name = models.CharField(max_length=64)
    order= models.ForeignKey(menu, on_delete=models.CASCADE, related_name = "cu_orders")
    bill = models.IntegerField() 

    def __str__(self):
        return f" {self.name} ordered {self.order.item} with bill {self.bill}Rs. \n"