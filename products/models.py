import uuid
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

class Book(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)

    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    cover = models.ImageField(upload_to='covers/', blank=True)

    class Meta:
        indexes = [
            models.Index(fields=['id'], name='id_index'),
        ]

        permissions = [
            ('special_status', 'Can read all books'),
        ]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book_detail', args=[str(self.id)])

class Review(models.Model):
    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        related_name='reviews',
    )
    review = models.CharField(max_length=255)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.review

class Product(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)

    sku = models.CharField(max_length=100)
    itemGroupId = models.CharField(max_length=200, blank=True)
    url = models.URLField(name="base_url", blank=True)
    name = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to='products/', height_field=None, width_field=None, blank=True)
    startPrice = models.DecimalField(max_digits=8,decimal_places=2, blank=True)
    toPrice = models.DecimalField(max_digits=8,decimal_places=2, blank=True)
    price = models.CharField(max_length=200)
    salePrice = models.DecimalField(max_digits=8,decimal_places=2, blank=True)
    currency = models.CharField(max_length=10)
    discount = models.FloatField(blank=True, default=0)
    shortDesc = models.CharField(max_length=200, blank=True)
    desc = models.TextField(blank=True, default="Description goes here")
    category = models.CharField(max_length=200,blank=True)
    listCategory = models.CharField(max_length=200, blank=True)
    other = models.CharField(max_length=200, blank=True)
    otherAttributeToIndex = models.CharField(max_length=200, blank=True)
    inStock = models.CharField(max_length=200, default=True)
    rating = models.PositiveIntegerField(blank=True)
    customerReview = models.CharField(max_length=200, blank=True)
   
        
    def __str__(self):
        return self.sku
    

