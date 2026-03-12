from django.db import models
from customers.models import Customer
from products.models import Product
# Create your models here.
class Orders(models.Model):
    orderid = models.CharField(max_length=100, primary_key=True, editable=False)
    customerid = models.ForeignKey(Customer, on_delete=models.CASCADE)
    productid = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.IntegerField()
    total = models.IntegerField()
    order_date = models.DateField()
    order_status = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        if not self.orderid:
            last_order = Orders.objects.order_by('-orderid').first()
            if last_order:
                last_id = int(last_order.orderid.split('-')[1])
                new_id = f"order-{last_id + 1}"
            else:
                new_id = "order-1"
            self.orderid = new_id
        super().save(*args, **kwargs)

    def __str__(self):
        return self.orderid 
