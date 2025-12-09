# Travela - Django Travel Booking Website

A fully functional travel booking website built with Django 5.2, featuring destination browsing, tour packages, online booking, contact forms, and user authentication.

## Features

- **User Authentication**: Login, registration, and logout functionality
- **Destination Browsing**: View featured travel destinations with details
- **Tour Packages**: Browse and explore various tour packages
- **Online Booking**: Submit booking requests with date, destination, and preferences
- **Contact Form**: Get in touch with the travel agency
- **Admin Panel**: Comprehensive admin interface to manage bookings, contacts, destinations, packages, and testimonials
- **Responsive Design**: Mobile-friendly interface
- **Testimonials**: Display customer reviews and ratings

## Tech Stack

- **Backend**: Django 5.2.4
- **Database**: SQLite (development), easily configurable for PostgreSQL/MySQL (production)
- **Frontend**: HTML5, CSS3, JavaScript, Bootstrap 5
- **Image Processing**: Pillow
- **Static Files**: WhiteNoise for production

## Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Setup Instructions

1. **Clone or navigate to the project directory**
   `ash
   cd "c:\Users\Laser cote\OneDrive\Desktop\college project\Mohit"
   `

2. **Activate the virtual environment**
   `ash
   Scripts\activate
   `

3. **Install dependencies**
   `ash
   pip install -r requirements.txt
   `

4. **Navigate to the project directory**
   `ash
   cd Scripts\MiProject
   `

5. **Run migrations**
   `ash
   python manage.py makemigrations
   python manage.py migrate
   `

6. **Create a superuser (admin account)**
   `ash
   python manage.py createsuperuser
   `
   Follow the prompts to set username, email, and password.

7. **Run the development server**
   `ash
   python manage.py runserver
   `

8. **Access the application**
   - Website: http://127.0.0.1:8000/
   - Admin Panel: http://127.0.0.1:8000/admin/

## Usage

### For Users

1. **Browse Destinations**: Visit the homepage to see featured destinations
2. **Book a Tour**: Navigate to the booking page, fill out the form with your details
3. **Contact Us**: Use the contact form to send inquiries
4. **Register/Login**: Create an account to track your bookings

### For Administrators

1. **Login to Admin Panel**: Go to /admin/ and login with superuser credentials
2. **Manage Destinations**: Add, edit, or delete travel destinations
3. **Manage Packages**: Create tour packages linked to destinations
4. **View Bookings**: See all booking requests and update their status
5. **Manage Contacts**: Read and respond to contact form submissions
6. **Approve Testimonials**: Review and approve customer testimonials

## Project Structure

`
MiProject/
 App2/                   # Main Django app
    models.py          # Database models
    views.py           # View functions
    forms.py           # Django forms
    urls.py            # URL routing
    admin.py           # Admin configuration
 MiProject/             # Project settings
    settings.py        # Django settings
    urls.py            # Main URL configuration
    wsgi.py            # WSGI configuration
 template/              # HTML templates
 static/                # Static files (CSS, JS, images)
 db.sqlite3             # SQLite database
 manage.py              # Django management script
`

## Deployment

### Environment Variables

For production, create a .env file based on .env.example:

`env
SECRET_KEY=your-production-secret-key
DEBUG=False
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
`

### Production Checklist

1. Set DEBUG=False in environment variables
2. Configure ALLOWED_HOSTS with your domain
3. Use a production database (PostgreSQL/MySQL)
4. Collect static files: python manage.py collectstatic
5. Set up proper web server (Gunicorn + Nginx)
6. Enable HTTPS
7. Configure email backend for contact form notifications

### Collect Static Files

`ash
python manage.py collectstatic
`

## Models

- **Destination**: Travel destinations with pricing and details
- **Package**: Tour packages linked to destinations
- **Booking**: Customer booking requests
- **Contact**: Contact form submissions
- **Testimonial**: Customer reviews and ratings

## Contributing

This is a college project. For any issues or suggestions, please contact the project maintainer.

## License

This project is created for educational purposes.

## Support

For any questions or issues, please use the contact form on the website or reach out to the administrator.
