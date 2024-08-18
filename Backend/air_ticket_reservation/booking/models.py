from django.db import models
from django.contrib.auth.models import User

class Flight(models.Model):
    flight_number = models.CharField(max_length=10)
    airline = models.CharField(max_length=50)
    departure_city = models.CharField(max_length=100)
    arrival_city = models.CharField(max_length=100)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    description = models.TextField(null=True, blank=True)
    slug=models.SlugField()

    def __str__(self):
        return f"{self.flight_number} - {self.airline}"


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    booking_date = models.DateTimeField(auto_now_add=True)
    number_of_tickets = models.PositiveIntegerField()
    price=models.PositiveBigIntegerField()

    def __str__(self):
        return f"Booking by {self.user.username} for {self.flight.flight_number}"


class Passenger(models.Model):
    MEMBERSHIP_Economy_class='E'
    MEMBERSHIP_Buisness_class= 'B'
    MEMBERSHIP_First_class = 'F'

    MEMBERSHIP_CHOICES = [
        (MEMBERSHIP_Economy_class, 'Economy Class'),
        ( MEMBERSHIP_Buisness_class, 'Buisness Class'),
        (MEMBERSHIP_First_class, 'First Class'),
    ]
    membership = models.CharField(
        max_length=1, choices=MEMBERSHIP_CHOICES, default=MEMBERSHIP_Economy_class)
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    passport_number = models.CharField(max_length=20)
    date_of_birth = models.DateField()
    phone = models.CharField(max_length=255)
    seat_number = models.CharField(max_length=10, blank=True, null=True)
    
    
    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.passport_number}"

class Order(models.Model):
    PAYMENT_STATUS_PENDING = 'P'
    PAYMENT_STATUS_COMPLETE = 'C'
    PAYMENT_STATUS_FAILED = 'F'
    PAYMENT_STATUS_CHOICES = [
        (PAYMENT_STATUS_PENDING, 'Pending'),
        (PAYMENT_STATUS_COMPLETE, 'Complete'),
        (PAYMENT_STATUS_FAILED, 'Failed')
    ]
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    placed_at = models.DateTimeField(auto_now_add=True)
    passenger=models.ForeignKey(Passenger,on_delete=models.PROTECT)
    
    
    def __str__(self):
        return f"Payment {self.id} - {self.status}"
