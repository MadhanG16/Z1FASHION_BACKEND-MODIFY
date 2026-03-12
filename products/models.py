from django.db import models

# Create your models here.
class Product(models.Model):
    productid = models.CharField(max_length=100, primary_key=True, editable=False)
    product_name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    size = models.CharField(max_length=100)
    stock = models.IntegerField()
    cost_price = models.IntegerField()
    selling_price = models.IntegerField()
    image = models.ImageField(upload_to='product_images/')

    def save(self, *args, **kwargs):
        if not self.productid:
            last_product = Product.objects.order_by('-productid').first()
            if last_product:
                last_id = int(last_product.productid.split('-')[1])
                new_id = f"product-{last_id + 1}"
            else:
                new_id = "product-1"
            self.productid = new_id
        super().save(*args, **kwargs)

    def __str__(self):
        return self.product_name 