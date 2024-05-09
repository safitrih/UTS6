from django.db import models

class CookieType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Cookie(models.Model):
    name = models.CharField(max_length=100)
    cookie_type = models.ForeignKey(CookieType, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class Order(models.Model):
    cookie = models.ForeignKey(Cookie, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    date_ordered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.quantity} x {self.cookie.name}"
