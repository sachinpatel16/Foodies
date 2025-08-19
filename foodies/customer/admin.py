from django.contrib import admin
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _
from .models import (
    CustomerProfile, DietaryRestriction, CuisineType,
    UserPreference, FoodRecommendation
)

@admin.register(CustomerProfile)
class CustomerProfileAdmin(admin.ModelAdmin):
    list_display = [
        'user_info', 'dietary_preferences', 'spice_tolerance',
        'preferred_cuisines_count', 'allergies_count', 'status'
    ]
    list_filter = [
        'is_vegetarian', 'is_vegan', 'is_gluten_free', 'is_dairy_free',
        'spice_tolerance', 'is_active', 'is_delete'
    ]
    search_fields = ['user__username', 'user__email', 'user__first_name', 'user__last_name']
    readonly_fields = ['create_time', 'update_time']
   
    fieldsets = (
        (_('User Information'), {
            'fields': ('user', 'is_active', 'is_delete')
        }),
        (_('Dietary Preferences'), {
            'fields': ('is_vegetarian', 'is_vegan', 'is_gluten_free', 'is_dairy_free', 'spice_tolerance')
        }),
        (_('Preferences'), {
            'fields': ('preferred_cuisines', 'preferred_areas', 'allergies')
        }),
        (_('Timestamps'), {
            'fields': ('create_time', 'update_time'),
            'classes': ('collapse',)
        }),
    )
   
    def user_info(self, obj):
        if obj.user:
            return format_html(
                '<strong>{}</strong><br><small>{}</small>',
                obj.user.get_full_name() or obj.user.username,
                obj.user.email or 'No email'
            )
        return 'No user'
    user_info.short_description = 'User Information'
   
    def dietary_preferences(self, obj):
        prefs = []
        if obj.is_vegetarian:
            prefs.append('Vegetarian')
        if obj.is_vegan:
            prefs.append('Vegan')
        if obj.is_gluten_free:
            prefs.append('Gluten-Free')
        if obj.is_dairy_free:
            prefs.append('Dairy-Free')
        return ', '.join(prefs) if prefs else 'None'
    dietary_preferences.short_description = 'Dietary Preferences'
   
    def preferred_cuisines_count(self, obj):
        return len(obj.preferred_cuisines) if obj.preferred_cuisines else 0
    preferred_cuisines_count.short_description = 'Cuisine Preferences'
   
    def allergies_count(self, obj):
        return len(obj.allergies) if obj.allergies else 0
    allergies_count.short_description = 'Allergies Count'
   
    def status(self, obj):
        if obj.is_delete:
            return format_html('<span style="color: red;">Deleted</span>')
        elif not obj.is_active:
            return format_html('<span style="color: orange;">Inactive</span>')
        else:
            return format_html('<span style="color: green;">Active</span>')
    status.short_description = 'Status'


@admin.register(DietaryRestriction)
class DietaryRestrictionAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'icon', 'status']
    list_filter = ['is_active', 'is_delete']
    search_fields = ['name', 'description']
    readonly_fields = ['create_time', 'update_time']
   
    fieldsets = (
        (_('Basic Information'), {
            'fields': ('name', 'description', 'icon')
        }),
        (_('Status'), {
            'fields': ('is_active', 'is_delete')
        }),
        (_('Timestamps'), {
            'fields': ('create_time', 'update_time'),
            'classes': ('collapse',)
        }),
    )
   
    def status(self, obj):
        if obj.is_delete:
            return format_html('<span style="color: red;">Deleted</span>')
        elif not obj.is_active:
            return format_html('<span style="color: orange;">Inactive</span>')
        else:
            return format_html('<span style="color: green;">Active</span>')
    status.short_description = 'Status'


@admin.register(CuisineType)
class CuisineTypeAdmin(admin.ModelAdmin):
    list_display = ['name', 'country_of_origin', 'description', 'icon', 'status']
    list_filter = ['country_of_origin', 'is_active', 'is_delete']
    search_fields = ['name', 'description', 'country_of_origin']
    readonly_fields = ['create_time', 'update_time']
   
    fieldsets = (
        (_('Basic Information'), {
            'fields': ('name', 'description', 'country_of_origin', 'icon')
        }),
        (_('Status'), {
            'fields': ('is_active', 'is_delete')
        }),
        (_('Timestamps'), {
            'fields': ('create_time', 'update_time'),
            'classes': ('collapse',)
        }),
    )
   
    def status(self, obj):
        if obj.is_delete:
            return format_html('<span style="color: red;">Deleted</span>')
        elif not obj.is_active:
            return format_html('<span style="color: orange;">Inactive</span>')
        else:
            return format_html('<span style="color: green;">Active</span>')
    status.short_description = 'Status'


@admin.register(UserPreference)
class UserPreferenceAdmin(admin.ModelAdmin):
    list_display = [
        'user_info', 'price_range', 'max_distance', 'min_rating',
        'notifications', 'status'
    ]
    list_filter = [
        'email_notifications', 'push_notifications', 'is_active', 'is_delete'
    ]
    search_fields = ['user__username', 'user__email', 'user__first_name', 'user__last_name']
    readonly_fields = ['create_time', 'update_time']
   
    fieldsets = (
        (_('User Information'), {
            'fields': ('user', 'is_active', 'is_delete')
        }),
        (_('Price Preferences'), {
            'fields': ('min_price', 'max_price')
        }),
        (_('Location & Rating'), {
            'fields': ('max_distance', 'min_rating')
        }),
        (_('Notifications'), {
            'fields': ('email_notifications', 'push_notifications')
        }),
        (_('Timestamps'), {
            'fields': ('create_time', 'update_time'),
            'classes': ('collapse',)
        }),
    )
   
    def user_info(self, obj):
        if obj.user:
            return format_html(
                '<strong>{}</strong><br><small>{}</small>',
                obj.user.get_full_name() or obj.user.username,
                obj.user.email or 'No email'
            )
        return 'No user'
    user_info.short_description = 'User Information'
   
    def price_range(self, obj):
        return f"₹{obj.min_price} - ₹{obj.max_price}"
    price_range.short_description = 'Price Range'
   
    def notifications(self, obj):
        notifs = []
        if obj.email_notifications:
            notifs.append('Email')
        if obj.push_notifications:
            notifs.append('Push')
        return ', '.join(notifs) if notifs else 'None'
    notifications.short_description = 'Notifications'
   
    def status(self, obj):
        if obj.is_delete:
            return format_html('<span style="color: red;">Deleted</span>')
        elif not obj.is_active:
            return format_html('<span style="color: orange;">Inactive</span>')
        else:
            return format_html('<span style="color: green;">Active</span>')
    status.short_description = 'Status'


@admin.register(FoodRecommendation)
class FoodRecommendationAdmin(admin.ModelAdmin):
    list_display = [
        'user_info', 'menu_item_info', 'confidence_score',
        'interaction_status', 'reason', 'status'
    ]
    list_filter = [
        'confidence_score', 'is_viewed', 'is_clicked', 'is_active', 'is_delete'
    ]
    search_fields = [
        'user__username', 'user__email', 'menu_item__name', 'reason'
    ]
    readonly_fields = ['create_time', 'update_time']
   
    fieldsets = (
        (_('Recommendation Details'), {
            'fields': ('user', 'menu_item', 'confidence_score', 'reason')
        }),
        (_('User Interaction'), {
            'fields': ('is_viewed', 'is_clicked')
        }),
        (_('Status'), {
            'fields': ('is_active', 'is_delete')
        }),
        (_('Timestamps'), {
            'fields': ('create_time', 'update_time'),
            'classes': ('collapse',)
        }),
    )
   
    def user_info(self, obj):
        if obj.user:
            return format_html(
                '<strong>{}</strong><br><small>{}</small>',
                obj.user.get_full_name() or obj.user.username,
                obj.user.email or 'No email'
            )
        return 'No user'
    user_info.short_description = 'User Information'
   
    def menu_item_info(self, obj):
        if obj.menu_item:
            return format_html(
                '<strong>{}</strong><br><small>{}</small>',
                obj.menu_item.name,
                obj.menu_item.outlet.name if obj.menu_item.outlet else 'No outlet'
            )
        return 'No menu item'
    menu_item_info.short_description = 'Menu Item'
   
    def interaction_status(self, obj):
        if obj.is_clicked:
            return format_html('<span style="color: green;">Clicked</span>')
        elif obj.is_viewed:
            return format_html('<span style="color: blue;">Viewed</span>')
        else:
            return format_html('<span style="color: gray;">Not Viewed</span>')
    interaction_status.short_description = 'Interaction'
   
    def status(self, obj):
        if obj.is_delete:
            return format_html('<span style="color: red;">Deleted</span>')
        elif not obj.is_active:
            return format_html('<span style="color: orange;">Inactive</span>')
        else:
            return format_html('<span style="color: green;">Active</span>')
    status.short_description = 'Status'

