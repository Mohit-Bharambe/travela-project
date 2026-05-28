from django.shortcuts import render, redirect
from django.contrib import auth, messages
from django.contrib.auth import logout as auth_logout
from .forms import BookingForm, ContactForm, UserRegistrationForm
from .models import Destination, Package, Testimonial

# Create your views here.

def index(request):
    # Get featured destinations and packages for homepage
    destinations = Destination.objects.filter(featured=True)[:6]
    packages = Package.objects.filter(featured=True)[:6]
    testimonials = Testimonial.objects.filter(is_approved=True)[:6]
    
    context = {
        'destinations': destinations,
        'packages': packages,
        'testimonials': testimonials,
    }
    return render(request, 'index.html', context)


def about(request):
    return render(request, 'about.html')


def blog(request):
    return render(request, 'blog.html')


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you for contacting us! We will get back to you soon.')
            return redirect('contact')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = ContactForm()
    
    return render(request, 'contact.html', {'form': form})


def booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking_obj = form.save(commit=False)
            # Associate with logged-in user if available
            if request.user.is_authenticated:
                booking_obj.user = request.user
            booking_obj.save()
            messages.success(request, 'Your booking has been submitted successfully! We will contact you soon.')
            return redirect('booking')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = BookingForm()
        # Pre-fill name and email if user is logged in
        if request.user.is_authenticated:
            form.initial['name'] = request.user.get_full_name() or request.user.username
            form.initial['email'] = request.user.email
    
    return render(request, 'booking.html', {'form': form})


def destination(request):
    destinations = Destination.objects.all()
    return render(request, 'destination.html', {'destinations': destinations})


def gallery(request):
    return render(request, 'gallery.html')


def guides(request):
    return render(request, 'guides.html')


def packages(request):
    packages = Package.objects.all()
    return render(request, 'packages.html', {'packages': packages})


def services(request):
    return render(request, 'services.html')


def testimonial(request):
    testimonials = Testimonial.objects.filter(is_approved=True)
    return render(request, 'testimonial.html', {'testimonials': testimonials})


def tour(request):
    return render(request, 'tour.html')


def error(request):
    return render(request, 'error.html')


def login(request):
    if request.method == 'POST':
        un = request.POST.get('uname')
        p1 = request.POST.get('pass')
        user = auth.authenticate(username=un, password=p1)
        if user is not None:
            auth.login(request, user)
            messages.success(request, f'Welcome back, {user.username}!')
            return redirect('/')
        else:
            messages.error(request, 'Invalid username or password. Please try again.')
            return redirect('/login/')
    return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Account created successfully! You can now log in.')
            return redirect('login')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = UserRegistrationForm()
    
    return render(request, 'register.html', {'form': form})


def logout(request):
    auth_logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('/')
