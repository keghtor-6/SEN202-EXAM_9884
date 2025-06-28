from django.db import models

# Create your models here.
class StaffBase(models.Model):
    street_address = models.CharField(max_length=255)
    phone_number=models.CharField(max_length=10)
    house_number = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=10)
    
    def str(self):
        return f"{self.street1_address}, {self.phone_number}, {self.house_number},
          {self.city}, {self.state}, {self.country}, {self.postal_code}, "
class Meta:
    abstract=True

class Manager(StaffBase):
    street1_address = models.CharField(max_length=255)
    phone_number=models.CharField(max_length=10)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=10)
    department=models.CharField(max_length=100)
    has_company_card=models.BooleanField
    
    def str(self):
        return f"{self.street1_address}, {self.phone_number}, {self.city},
           {self.state}, {self.country}, {self.postal_code},{self.department},{self.has_company_card} "


class Intern(StaffBase):
     phone_number=models.CharField(max_length=10)
     name=models.CharField(max_length=100)
     address=models.CharField(max_length=100)
     school=models.CharField(max_length=100)
     mentor=models.Manager()
     internship_end=models.DateField()
     

     def str(self):
        return f"{self.name}, {self.phone_number}, {self.address},
           {self.school}, {self.mentor},{self.internship_end} "  
     
     class Address(models.Model):
         city=models.CharField(max_length=100)
         street=models.CharField(max_length=100)
         postal_code=models.CharField(max_length=10)
         country=models.CharField(max_length=100)

         def __str__ (self):
             return f"{self.city},{self.street},{self.postal_code},{self.country}"
#admin logs username=keghtorchileh@gmail.com password=1234567890