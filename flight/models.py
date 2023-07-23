from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Flight(models.Model):
    
    AİRLİNES = (
        ("THY","TÜRK HAVAYOLLARI"),
        ("PHT","PEGASUS HAVA TAŞIMACILIĞI"),
        ("AJH","ATLAS JET HAVACILIK"),
        ("OİT","ONUR AİR TAŞIMACILIK")
    )
    
    flight_number = models.CharField(max_length=50)  #(UÇUŞ NUMARASI)
    operation_airlines = models.CharField(max_length=50,choices=AİRLİNES) #(İŞLETME HAVAYOLU)
    departure_city =models.CharField(max_length=50) #(KALKIŞ ŞEHRİ)
    arrival_city= models.CharField(max_length=50) #(VARIŞ ŞEHRİ)
    date_of_departure=models.DateField() #(UÇAĞIN KALKIŞ GÜNÜ)
    estimated_time_of_departure = models.TimeField() #(UÇAĞIN KALKIŞ SAATİ)
    
    def __str__(self):
        return f"{self.flight_number}-{self.operation_airlines}-{self.departure_city}-{self.arrival_city}-{self.date_of_departure}-{self.estimated_time_of_departure}"
    
    class Meta : 
        
        verbose_name_plural = ("Uçuş Bilgileri")
    
class Passenger(models.Model):
    
    firstName=models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    phoneNumber = models.PositiveSmallIntegerField()
    updateDate = models.DateTimeField(auto_now=True)
    createDate = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.firstName}-{self.last_name}-{self.email}-{self.phoneNumber}"
    
    class Meta : 
        ordering = ('firstName'),
        verbose_name_plural = ("Yolcu Bilgileri")

    

class Rezervation(models.Model):
    
    flight = models.ForeignKey(Flight, on_delete=models.SET_NULL ,null=True,related_name='rezervations')
    user = models.ForeignKey(User, on_delete=models.PROTECT ,null=True,)
    passenger = models.ManyToManyField(Passenger,related_name='passengers')
    
    def __str__(self):
        return f"{self.flight}"
    
    
    class Meta : 
        
        verbose_name_plural = ("Rezervasyon Bilgileri")