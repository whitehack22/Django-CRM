from django.db import models


class Record(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=100)
    county = models.CharField(max_length=50)
    sub_county = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=20)

    def __str__(self):
        return(f"{self.first_name} {self.last_name}")
   
    
