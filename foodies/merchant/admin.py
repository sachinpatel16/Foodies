from django.contrib import admin
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _
from .models import (
    Category, MerchantProfile, Outlet, MenuItem,
    Review, SearchHistory, FavoriteItem
)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'icon_preview', 'color_preview', 'status']
    list_filter = ['is_active', 'is_delete']
    search_fields = ['name', 'description']
    readonly_fields = ['create_time', 'update_time']
   
    fieldsets = (
        (_('Basic Information'), {
            'fields': ('name', 'description')
        }),
        (_('Visual Elements'), {
            'fields': ('icon', 'color')
        }),
        (_('Status'), {
            'fields': ('is_active', 'is_delete')
        }),
        (_('Timestamps'), {
            'fields': ('create_time', 'update_time'),
            'classes': ('collapse',)
        }),
    )
   
    def icon_preview(self, obj):
        if obj.icon:
            return format_html(
                '<img src="{}" style="max-height: 30px; max-width: 30px;" />',
                obj.icon.url
            )
        return 'No icon'
    icon_preview.short_description = 'Icon'
   
    def color_preview(self, obj):
        if obj.color:
            return format_html(
                '<div style="background-color: {}; width: 30px; height: 20px; border: 1px solid #ccc;"></div>',
                obj.color
            )
        return 'No color'
    color_preview.short_description = 'Color'
   
    def status(self, obj):
        if obj.is_delete:
            return format_html('<span style="color: red;">Deleted</span>')
        elif not obj.is_active:
            return format_html('<span style="color: orange;">Inactive</span>')
        else:
            return format_html('<span style="color: green;">Active</span>')
    status.short_description = 'Status'


@admin.register(MerchantProfile)
class MerchantProfileAdmin(admin.ModelAdmin):
    list_display = [
        'business_info', 'contact_info', 'business_hours',
        'verification_status', 'status'
    ]
    list_filter = [
        'is_verified', 'is_featured', 'is_active', 'is_delete'
    ]
    search_fields = [
        'business_name', 'user__username', 'user__email',
        'business_phone', 'business_email'
    ]
    readonly_fields = ['create_time', 'update_time']
   
    fieldsets = (
        (_('Business Information'), {
            'fields': ('user', 'business_name', 'business_description', 'business_logo')
        }),
        (_('Business Details'), {
            'fields': ('business_license', 'tax_id')
        }),
        (_('Business Hours'), {
            'fields': ('opening_time', 'closing_time')
        }),
        (_('Contact Information'), {
            'fields': ('business_phone', 'business_email', 'website')
        }),
        (_('Status'), {
            'fields': ('is_verified', 'is_featured', 'is_active', 'is_delete')
        }),
        (_('Timestamps'), {
            'fields': ('create_time', 'update_time'),
            'classes': ('collapse',)
        }),
    )
   
    def business_info(self, obj):
        logo_html = ''
        if obj.business_logo:
            logo_html = format_html(
                '<img src="{}" style="max-height: 30px; max-width: 30px; margin-right: 10px;" />',
                obj.business_logo.url
            )
       
        return format_html(
            '{}<strong>{}</strong><br><small>{}</small>',
            logo_html,
            obj.business_name,
            obj.business_description[:50] + '...' if obj.business_description and len(obj.business_description) > 50 else obj.business_description or 'No description'
        )
    business_info.short_description = 'Business Information'
   
    def contact_info(self, obj):
        return format_html(
            '<strong>{}</strong><br><small>Phone: {} | Email: {}</small>',
            obj.user.get_full_name() or obj.user.username,
            obj.business_phone or 'No phone',
            obj.business_email or 'No email'
        )
    contact_info.short_description = 'Contact Information'
   
    def business_hours(self, obj):
        return f"{obj.opening_time.strftime('%H:%M')} - {obj.closing_time.strftime('%H:%M')}"
    business_hours.short_description = 'Business Hours'
   
    def verification_status(self, obj):
        if obj.is_verified:
            return format_html('<span style="color: green;">✓ Verified</span>')
        else:
            return format_html('<span style="color: orange;">✗ Not Verified</span>')
    verification_status.short_description = 'Verification'
   
    def status(self, obj):
        if obj.is_delete:
            return format_html('<span style="color: red;">Deleted</span>')
        elif not obj.is_active:
            return format_html('<span style="color: orange;">Inactive</span>')
        else:
            return format_html('<span style="color: green;">Active</span>')
    status.short_description = 'Status'


@admin.register(Outlet)
class OutletAdmin(admin.ModelAdmin):
    list_display = [
        'outlet_info', 'location_info', 'services', 'business_hours', 'status'
    ]
    list_filter = [
        'city', 'state', 'is_active', 'is_dine_in', 'is_takeaway', 'is_delete'
    ]
    search_fields = [
        'name', 'merchant__business_name', 'address', 'area', 'city', 'state'
    ]
    readonly_fields = ['create_time', 'update_time']
   
    fieldsets = (
        (_('Outlet Information'), {
            'fields': ('merchant', 'name', 'address')
        }),
        (_('Location'), {
            'fields': ('area', 'city', 'state', 'pin_code', 'latitude', 'longitude')
        }),
        (_('Contact & Hours'), {
            'fields': ('phone', 'opening_time', 'closing_time')
        }),
        (_('Services'), {
            'fields': ('is_dine_in', 'is_takeaway')
        }),
        (_('Status'), {
            'fields': ('is_active', 'is_delete')
        }),
        (_('Timestamps'), {
            'fields': ('create_time', 'update_time'),
            'classes': ('collapse',)
        }),
    )
   
    def outlet_info(self, obj):
        return format_html(
            '<strong>{}</strong><br><small>{}</small>',
            obj.name,
            obj.merchant.business_name if obj.merchant else 'No merchant'
        )
    outlet_info.short_description = 'Outlet Information'
   
    def location_info(self, obj):
        return format_html(
            '<strong>{}</strong><br><small>{}, {}</small>',
            obj.area,
            obj.city,
            obj.state
        )
    location_info.short_description = 'Location'
   
    def services(self, obj):
        services = []
        if obj.is_dine_in:
            services.append('Dine-in')
        if obj.is_takeaway:
            services.append('Takeaway')
        return ', '.join(services) if services else 'None'
    services.short_description = 'Services'
   
    def business_hours(self, obj):
        return f"{obj.opening_time.strftime('%H:%M')} - {obj.closing_time.strftime('%H:%M')}"
    business_hours.short_description = 'Business Hours'
   
    def status(self, obj):
        if obj.is_delete:
            return format_html('<span style="color: red;">Deleted</span>')
        elif not obj.is_active:
            return format_html('<span style="color: orange;">Inactive</span>')
        else:
            return format_html('<span style="color: green;">Active</span>')
    status.short_description = 'Status'


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = [
        'item_info', 'category', 'price', 'food_details', 'popularity', 'status'
    ]
    list_filter = [
        'category', 'is_vegetarian', 'is_spicy', 'is_gluten_free',
        'is_available', 'is_active', 'is_delete'
    ]
    search_fields = [
        'name', 'description', 'outlet__name', 'outlet__merchant__business_name'
    ]
    readonly_fields = ['create_time', 'update_time']
   
    fieldsets = (
        (_('Basic Information'), {
            'fields': ('outlet', 'category', 'name', 'description', 'price')
        }),
        (_('Images'), {
            'fields': ('primary_image', 'images')
        }),
        (_('Food Details'), {
            'fields': ('is_vegetarian', 'is_spicy', 'is_gluten_free', 'is_available')
        }),
        (_('Additional Info'), {
            'fields': ('calories', 'preparation_time')
        }),
        (_('Status'), {
            'fields': ('is_active', 'is_delete')
        }),
        (_('Timestamps'), {
            'fields': ('create_time', 'update_time'),
            'classes': ('collapse',)
        }),
    )
   
    def item_info(self, obj):
        image_html = ''
        if obj.primary_image:
            image_html = format_html(
                '<img src="{}" style="max-height: 30px; max-width: 30px; margin-right: 10px;" />',
                obj.primary_image.url
            )
       
        return format_html(
            '{}<strong>{}</strong><br><small>{}</small>',
            image_html,
            obj.name,
            obj.outlet.name if obj.outlet else 'No outlet'
        )
    item_info.short_description = 'Item Information'
   
    def food_details(self, obj):
        details = []
        if obj.is_vegetarian:
            details.append('🥬 Veg')
        if obj.is_spicy:
            details.append('🌶️ Spicy')
        if obj.is_gluten_free:
            details.append('🌾 GF')
        return ' '.join(details) if details else 'Standard'
    food_details.short_description = 'Food Details'
   
    def popularity(self, obj):
        return format_html(
            '<strong>Orders:</strong> {} | <strong>Rating:</strong> {}★',
            obj.total_orders,
            obj.average_rating
        )
    popularity.short_description = 'Popularity'
   
    def status(self, obj):
        if obj.is_delete:
            return format_html('<span style="color: red;">Deleted</span>')
        elif not obj.is_active:
            return format_html('<span style="color: orange;">Inactive</span>')
        elif not obj.is_available:
            return format_html('<span style="color: gray;">Unavailable</span>')
        else:
            return format_html('<span style="color: green;">Available</span>')
    status.short_description = 'Status'


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = [
        'user_info', 'menu_item_info', 'rating_display', 'comment_preview', 'status'
    ]
    list_filter = [
        'rating', 'is_verified_purchase', 'is_active', 'is_delete'
    ]
    search_fields = [
        'user__username', 'user__email', 'menu_item__name', 'comment'
    ]
    readonly_fields = ['create_time', 'update_time']
   
    fieldsets = (
        (_('Review Details'), {
            'fields': ('user', 'menu_item', 'rating', 'comment')
        }),
        (_('Media'), {
            'fields': ('images',)
        }),
        (_('Metadata'), {
            'fields': ('is_verified_purchase', 'helpful_votes')
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
   
    def rating_display(self, obj):
        stars = '★' * obj.rating + '☆' * (5 - obj.rating)
        return format_html(
            '<span style="color: gold; font-size: 16px;">{}</span> ({})',
            stars,
            obj.rating
        )
    rating_display.short_description = 'Rating'
   
    def comment_preview(self, obj):
        if obj.comment:
            return obj.comment[:50] + '...' if len(obj.comment) > 50 else obj.comment
        return 'No comment'
    comment_preview.short_description = 'Comment'
   
    def status(self, obj):
        if obj.is_delete:
            return format_html('<span style="color: red;">Deleted</span>')
        elif not obj.is_active:
            return format_html('<span style="color: orange;">Inactive</span>')
        else:
            return format_html('<span style="color: green;">Active</span>')
    status.short_description = 'Status'


@admin.register(SearchHistory)
class SearchHistoryAdmin(admin.ModelAdmin):
    list_display = ['user_info', 'query', 'category', 'location', 'search_time', 'status']
    list_filter = ['category', 'is_active', 'is_delete']
    search_fields = ['query', 'location', 'user__username', 'user__email']
    readonly_fields = ['create_time', 'update_time']
   
    fieldsets = (
        (_('Search Details'), {
            'fields': ('user', 'query', 'category', 'location')
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
   
    def search_time(self, obj):
        return obj.create_time.strftime('%Y-%m-%d %H:%M')
    search_time.short_description = 'Search Time'
   
    def status(self, obj):
        if obj.is_delete:
            return format_html('<span style="color: red;">Deleted</span>')
        elif not obj.is_active:
            return format_html('<span style="color: orange;">Inactive</span>')
        else:
            return format_html('<span style="color: green;">Active</span>')
    status.short_description = 'Status'


@admin.register(FavoriteItem)
class FavoriteItemAdmin(admin.ModelAdmin):
    list_display = ['user_info', 'menu_item_info', 'favorite_time', 'status']
    list_filter = ['is_active', 'is_delete']
    search_fields = [
        'user__username', 'user__email', 'menu_item__name',
        'menu_item__outlet__name'
    ]
    readonly_fields = ['create_time', 'update_time']
   
    fieldsets = (
        (_('Favorite Details'), {
            'fields': ('user', 'menu_item')
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
                '<strong>❤️ {}</strong><br><small>{}</small>',
                obj.menu_item.name,
                obj.menu_item.outlet.name if obj.menu_item.outlet else 'No outlet'
            )
        return 'No menu item'
    menu_item_info.short_description = 'Favorite Item'
   
    def favorite_time(self, obj):
        return obj.create_time.strftime('%Y-%m-%d %H:%M')
    favorite_time.short_description = 'Favorited On'
   
    def status(self, obj):
        if obj.is_delete:
            return format_html('<span style="color: red;">Deleted</span>')
        elif not obj.is_active:
            return format_html('<span style="color: orange;">Inactive</span>')
        else:
            return format_html('<span style="color: green;">Active</span>')
    status.short_description = 'Status'


