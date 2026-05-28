from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Destination(models.Model):
    '''Model for travel destinations'''
    name = models.CharField(max_length=200)
    country = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='destinations/', blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, help_text="Price in USD")
    duration = models.CharField(max_length=50, help_text="e.g., '5 Days 4 Nights'")
    featured = models.BooleanField(default=False, help_text="Show on homepage")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-featured', '-created_at']

    def __str__(self):
        return f"{self.name}, {self.country}"


class Package(models.Model):
    '''Model for tour packages'''
    name = models.CharField(max_length=200)
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE, related_name='packages')
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, help_text="Price in USD")
    duration = models.CharField(max_length=50, help_text="e.g., '3 Days 2 Nights'")
    includes = models.TextField(help_text="What's included in the package")
    image = models.ImageField(upload_to='packages/', blank=True, null=True)
    max_persons = models.IntegerField(default=10)
    featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-featured', '-created_at']

    def __str__(self):
        return f"{self.name} - {self.destination.name}"


class Booking(models.Model):
    '''Model for tour bookings'''
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
        ('completed', 'Completed'),
    ]
    
    CATEGORY_CHOICES = [
        ('kids', 'Kids'),
        ('adults', 'Adults'),
        ('family', 'Family'),
        ('couple', 'Couple'),
    ]

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='bookings')
    name = models.CharField(max_length=200)
    email = models.EmailField()
    datetime = models.DateTimeField()
    destination = models.CharField(max_length=200)
    persons = models.IntegerField(validators=[MinValueValidator(1)])
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='adults')
    special_request = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Booking by {self.name} for {self.destination} on {self.datetime.date()}"


class Contact(models.Model):
    '''Model for contact form submissions'''
    name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(max_length=300)
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Contact from {self.name} - {self.subject}"


class Testimonial(models.Model):
    '''Model for customer testimonials'''
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=200)
    profession = models.CharField(max_length=100, blank=True)
    message = models.TextField()
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        default=5,
        help_text="Rating from 1 to 5"
    )
    image = models.ImageField(upload_to='testimonials/', blank=True, null=True)
    is_approved = models.BooleanField(default=False, help_text="Show on website")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Testimonial by {self.name} - {self.rating} stars"
