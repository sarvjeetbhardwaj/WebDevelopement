from django.db import models

class Record(models.Model):
    created_at = models.DateField(auto_now_add=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    address = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'