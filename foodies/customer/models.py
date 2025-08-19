from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from foodies.custom_auth.models import BaseModel

User = get_user_model()


class CustomerProfile(BaseModel):
    """Extended customer profile with food preferences"""
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='customer_profile')
    
    # Dietary preferences
    is_vegetarian = models.BooleanField(default=False)
    is_vegan = models.BooleanField(default=False)
    is_gluten_free = models.BooleanField(default=False)
    is_dairy_free = models.BooleanField(default=False)
    
    # Spice tolerance
    SPICE_LEVELS = [
        ('mild', 'Mild'),
        ('medium', 'Medium'),
        ('hot', 'Hot'),
        ('extra_hot', 'Extra Hot'),
    ]
    spice_tolerance = models.CharField(max_length=20, choices=SPICE_LEVELS, default='medium')
    
    # Cuisine preferences
    preferred_cuisines = models.JSONField(default=list, blank=True, help_text='List of preferred cuisine types')
    
    # Allergies and restrictions
    allergies = models.JSONField(default=list, blank=True, help_text='List of food allergies')
    
    # Location preferences
    preferred_areas = models.JSONField(default=list, blank=True, help_text='List of preferred areas for food search')
    
    class Meta:
        verbose_name = _('Customer Profile')
        verbose_name_plural = _('Customer Profiles')
    
    def __str__(self):
        return f"{self.user.get_full_name()} - Customer Profile"


class DietaryRestriction(BaseModel):
    """Common dietary restrictions for food filtering"""
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    icon = models.CharField(max_length=50, blank=True, null=True, help_text='Icon class or emoji')
    
    class Meta:
        verbose_name = _('Dietary Restriction')
        verbose_name_plural = _('Dietary Restrictions')
        ordering = ['name']
    
    def __str__(self):
        return self.name


class CuisineType(BaseModel):
    """Different cuisine types for categorization"""
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    country_of_origin = models.CharField(max_length=100, blank=True, null=True)
    icon = models.CharField(max_length=50, blank=True, null=True, help_text='Icon class or emoji')
    
    class Meta:
        verbose_name = _('Cuisine Type')
        verbose_name_plural = _('Cuisine Types')
        ordering = ['name']
    
    def __str__(self):
        return self.name


class UserPreference(BaseModel):
    """User's food preferences and settings"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='food_preferences')
    
    # Price range preference
    min_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    max_price = models.DecimalField(max_digits=10, decimal_places=2, default=1000.00)
    
    # Distance preference (in km)
    max_distance = models.PositiveIntegerField(default=10, help_text='Maximum distance in kilometers')
    
    # Rating preference
    min_rating = models.DecimalField(max_digits=3, decimal_places=2, default=0.00)
    
    # Notification preferences
    email_notifications = models.BooleanField(default=True)
    push_notifications = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = _('User Preference')
        verbose_name_plural = _('User Preferences')
        unique_together = ['user']
    
    def __str__(self):
        return f"{self.user.get_full_name()} - Preferences"


class FoodRecommendation(BaseModel):
    """AI-powered food recommendations for users"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='food_recommendations')
    menu_item = models.ForeignKey('merchant.MenuItem', on_delete=models.CASCADE, related_name='recommendations')
    
    # Recommendation metadata
    confidence_score = models.DecimalField(max_digits=3, decimal_places=2, help_text='AI confidence score (0-1)')
    reason = models.CharField(max_length=200, blank=True, null=True, help_text='Why this item was recommended')
    
    # User interaction
    is_viewed = models.BooleanField(default=False)
    is_clicked = models.BooleanField(default=False)
    
    class Meta:
        verbose_name = _('Food Recommendation')
        verbose_name_plural = _('Food Recommendations')
        unique_together = ['user', 'menu_item']
        ordering = ['-confidence_score']
    
    def __str__(self):
        return f"{self.user.get_full_name()} → {self.menu_item.name} ({self.confidence_score})"
