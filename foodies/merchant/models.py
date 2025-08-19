from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.translation import gettext_lazy as _
from foodies.custom_auth.models import BaseModel

User = get_user_model()


class Category(BaseModel):
    """Food categories like Pizza, Burger, Indian, Chinese, etc."""
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    icon = models.ImageField(upload_to='categories/icons/', blank=True, null=True)
    color = models.CharField(max_length=7, default='#FF6B6B', help_text='Hex color code')
    
    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')
        ordering = ['name']
    
    def __str__(self):
        return self.name


class MerchantProfile(BaseModel):
    """Merchant profile for food vendors"""
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='merchant_profile')
    business_name = models.CharField(max_length=200)
    business_description = models.TextField(blank=True, null=True)
    business_logo = models.ImageField(upload_to='merchants/logos/', blank=True, null=True)
    business_license = models.CharField(max_length=100, blank=True, null=True)
    tax_id = models.CharField(max_length=100, blank=True, null=True)
    
    # Business hours
    opening_time = models.TimeField()
    closing_time = models.TimeField()
    
    # Contact info
    business_phone = models.CharField(max_length=20, blank=True, null=True)
    business_email = models.EmailField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    
    # Status
    is_verified = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)
    
    class Meta:
        verbose_name = _('Merchant Profile')
        verbose_name_plural = _('Merchant Profiles')
    
    def __str__(self):
        return f"{self.business_name} - {self.user.get_full_name()}"


class Outlet(BaseModel):
    """Multiple outlets for a merchant"""
    merchant = models.ForeignKey(MerchantProfile, on_delete=models.CASCADE, related_name='outlets')
    name = models.CharField(max_length=200)
    address = models.TextField()
    area = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pin_code = models.CharField(max_length=10)
    
    # Location coordinates for map integration (using simple decimal fields)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    
    # Outlet specific details
    phone = models.CharField(max_length=20, blank=True, null=True)
    opening_time = models.TimeField()
    closing_time = models.TimeField()
    
    # Status
    is_active = models.BooleanField(default=True)
    is_dine_in = models.BooleanField(default=True)
    is_takeaway = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = _('Outlet')
        verbose_name_plural = _('Outlets')
        ordering = ['name']
    
    def __str__(self):
        return f"{self.name} - {self.merchant.business_name}"


class MenuItem(BaseModel):
    """Individual food items in the menu"""
    outlet = models.ForeignKey(Outlet, on_delete=models.CASCADE, related_name='menu_items')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='menu_items')
    
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    # Images
    primary_image = models.ImageField(upload_to='menu/primary/', blank=True, null=True)
    images = models.JSONField(default=list, blank=True, help_text='List of additional image URLs')
    
    # Food details
    is_vegetarian = models.BooleanField(default=False)
    is_spicy = models.BooleanField(default=False)
    is_gluten_free = models.BooleanField(default=False)
    is_available = models.BooleanField(default=True)
    
    # Nutritional info (optional)
    calories = models.PositiveIntegerField(blank=True, null=True)
    preparation_time = models.PositiveIntegerField(blank=True, null=True, help_text='Preparation time in minutes')
    
    # Popularity metrics
    total_orders = models.PositiveIntegerField(default=0)
    average_rating = models.DecimalField(max_digits=3, decimal_places=2, default=0.00)
    
    class Meta:
        verbose_name = _('Menu Item')
        verbose_name_plural = _('Menu Items')
        ordering = ['category', 'name']
        unique_together = ['outlet', 'name']
    
    def __str__(self):
        return f"{self.name} - {self.outlet.name}"


class Review(BaseModel):
    """User reviews for menu items"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE, related_name='reviews')
    
    rating = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        help_text='Rating from 1 to 5'
    )
    comment = models.TextField(blank=True, null=True)
    images = models.JSONField(default=list, blank=True, help_text='List of review image URLs')
    
    # Review metadata
    is_verified_purchase = models.BooleanField(default=False)
    helpful_votes = models.PositiveIntegerField(default=0)
    
    class Meta:
        verbose_name = _('Review')
        verbose_name_plural = _('Reviews')
        unique_together = ['user', 'menu_item']
        ordering = ['-create_time']
    
    def __str__(self):
        return f"{self.user.get_full_name()} - {self.menu_item.name} ({self.rating}★)"


class SearchHistory(BaseModel):
    """Track user search history for recommendations"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='search_history')
    query = models.CharField(max_length=500)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    location = models.CharField(max_length=200, blank=True, null=True)
    
    class Meta:
        verbose_name = _('Search History')
        verbose_name_plural = _('Search History')
        ordering = ['-create_time']
    
    def __str__(self):
        return f"{self.user.get_full_name()} - {self.query}"


class FavoriteItem(BaseModel):
    """User's favorite menu items"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorite_items')
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE, related_name='favorited_by')
    
    class Meta:
        verbose_name = _('Favorite Item')
        verbose_name_plural = _('Favorite Items')
        unique_together = ['user', 'menu_item']
    
    def __str__(self):
        return f"{self.user.get_full_name()} ❤️ {self.menu_item.name}"
