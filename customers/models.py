from django.db import models

# Create your models here.
class Customer(models.Model):
    customerid = models.CharField(max_length=100, primary_key=True, editable=False)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.IntegerField()
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip = models.IntegerField()
    country = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        if not self.customerid:
            last_customer = Customer.objects.order_by('-customerid').first()
            if last_customer:
                last_id = int(last_customer.customerid.split('-')[1])
                new_id = f"customer-{last_id + 1}"
            else:
                new_id = "customer-1"
            self.customerid = new_id
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username 