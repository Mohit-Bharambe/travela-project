from django.contrib import admin
from .models import Destination, Package, Booking, Contact, Testimonial

# Register your models here.

@admin.register(Destination)
class DestinationAdmin(admin.ModelAdmin):
    list_display = ['name', 'country', 'price', 'duration', 'featured', 'created_at']
    list_filter = ['featured', 'country', 'created_at']
    search_fields = ['name', 'country', 'description']
    list_editable = ['featured']
    ordering = ['-featured', '-created_at']


@admin.register(Package)
class PackageAdmin(admin.ModelAdmin):
    list_display = ['name', 'destination', 'price', 'duration', 'max_persons', 'featured', 'created_at']
    list_filter = ['featured', 'destination', 'created_at']
    search_fields = ['name', 'description', 'destination__name']
    list_editable = ['featured']
    ordering = ['-featured', '-created_at']


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'destination', 'datetime', 'persons', 'status', 'created_at']
    list_filter = ['status', 'category', 'created_at']
    search_fields = ['name', 'email', 'destination']
    list_editable = ['status']
    ordering = ['-created_at']
    readonly_fields = ['created_at', 'updated_at']
    
    actions = ['mark_confirmed', 'mark_cancelled', 'mark_completed']
    
    def mark_confirmed(self, request, queryset):
        updated = queryset.update(status='confirmed')
        self.message_user(request, f'{updated} booking(s) marked as confirmed.')
    mark_confirmed.short_description = 'Mark selected bookings as Confirmed'
    
    def mark_cancelled(self, request, queryset):
        updated = queryset.update(status='cancelled')
        self.message_user(request, f'{updated} booking(s) marked as cancelled.')
    mark_cancelled.short_description = 'Mark selected bookings as Cancelled'
    
    def mark_completed(self, request, queryset):
        updated = queryset.update(status='completed')
        self.message_user(request, f'{updated} booking(s) marked as completed.')
    mark_completed.short_description = 'Mark selected bookings as Completed'


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'is_read', 'created_at']
    list_filter = ['is_read', 'created_at']
    search_fields = ['name', 'email', 'subject', 'message']
    list_editable = ['is_read']
    ordering = ['-created_at']
    readonly_fields = ['created_at']
    
    actions = ['mark_read', 'mark_unread']
    
    def mark_read(self, request, queryset):
        updated = queryset.update(is_read=True)
        self.message_user(request, f'{updated} contact(s) marked as read.')
    mark_read.short_description = 'Mark selected contacts as Read'
    
    def mark_unread(self, request, queryset):
        updated = queryset.update(is_read=False)
        self.message_user(request, f'{updated} contact(s) marked as unread.')
    mark_unread.short_description = 'Mark selected contacts as Unread'


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ['name', 'profession', 'rating', 'is_approved', 'created_at']
    list_filter = ['is_approved', 'rating', 'created_at']
    search_fields = ['name', 'profession', 'message']
    list_editable = ['is_approved']
    ordering = ['-created_at']
    readonly_fields = ['created_at']
    
    actions = ['approve_testimonials', 'unapprove_testimonials']
    
    def approve_testimonials(self, request, queryset):
        updated = queryset.update(is_approved=True)
        self.message_user(request, f'{updated} testimonial(s) approved.')
    approve_testimonials.short_description = 'Approve selected testimonials'
    
    def unapprove_testimonials(self, request, queryset):
        updated = queryset.update(is_approved=False)
        self.message_user(request, f'{updated} testimonial(s) unapproved.')
    unapprove_testimonials.short_description = 'Unapprove selected testimonials'
