# Food Finder Backend API Documentation

## Overview
The Food Finder API is a comprehensive backend system built with Django REST Framework that allows users to discover food items from nearby restaurants and food vendors. The system supports both merchant (food vendor) and customer (food seeker) functionalities.

## Features
- **Merchant Management**: Create and manage food vendor profiles with multiple outlets
- **Menu Management**: Add, update, and manage food items with detailed information
- **Location-based Search**: Find food items based on user location and preferences
- **User Reviews & Ratings**: Comprehensive review system for food items
- **Personalized Recommendations**: AI-powered food suggestions based on user preferences
- **Advanced Filtering**: Filter by category, price, dietary restrictions, and more

## Technology Stack
- **Backend**: Django 5.2 + Django REST Framework
- **Database**: PostgreSQL with PostGIS for location-based queries
- **Authentication**: JWT-based authentication
- **Image Handling**: Support for multiple image uploads
- **API Documentation**: Swagger/OpenAPI integration

## API Base URL
```
https://yourdomain.com/api/v1/
```

## Authentication
All protected endpoints require JWT authentication. Include the token in the Authorization header:
```
Authorization: Bearer <your_jwt_token>
```

---

## Merchant API Endpoints

### 1. Categories
**Base URL**: `/api/v1/categories/`

#### Get All Categories
```http
GET /api/v1/categories/
```
**Response**:
```json
[
    {
        "id": 1,
        "name": "Pizza",
        "description": "Italian pizza varieties",
        "icon": "/media/categories/icons/pizza.png",
        "color": "#FF6B6B",
        "is_active": true,
        "create_time": "2024-01-15T10:30:00Z"
    }
]
```

#### Search Categories
```http
GET /api/v1/categories/?search=pizza
```

### 2. Merchant Profiles
**Base URL**: `/api/v1/merchants/`

#### Create Merchant Profile
```http
POST /api/v1/merchants/
Content-Type: application/json

{
    "user_id": 1,
    "business_name": "Pizza Palace",
    "business_description": "Best pizza in town",
    "opening_time": "09:00:00",
    "closing_time": "22:00:00",
    "business_phone": "+919876543210",
    "business_email": "info@pizzapalace.com"
}
```

#### Get Merchant Details
```http
GET /api/v1/merchants/{id}/
```

#### Update Merchant Profile
```http
PUT /api/v1/merchants/{id}/
```

#### Get Merchant Outlets
```http
GET /api/v1/merchants/{id}/outlets/
```

### 3. Outlets
**Base URL**: `/api/v1/outlets/`

#### Create Outlet
```http
POST /api/v1/outlets/
Content-Type: application/json

{
    "merchant_id": 1,
    "name": "Pizza Palace - Downtown",
    "address": "123 Main Street",
    "area": "Downtown",
    "city": "Mumbai",
    "state": "Maharashtra",
    "pin_code": "400001",
    "latitude": 19.0760,
    "longitude": 72.8777,
    "phone": "+919876543210",
    "opening_time": "09:00:00",
    "closing_time": "22:00:00",
    "is_dine_in": true,
    "is_takeaway": true
}
```

#### Get Outlet Menu
```http
GET /api/v1/outlets/{id}/menu/
```

#### Filter Menu by Category
```http
GET /api/v1/outlets/{id}/menu/?category=1
```

#### Filter Menu by Dietary Preferences
```http
GET /api/v1/outlets/{id}/menu/?vegetarian=true&spicy=false
```

### 4. Menu Items
**Base URL**: `/api/v1/menu-items/`

#### Create Menu Item
```http
POST /api/v1/menu-items/
Content-Type: application/json

{
    "outlet_id": 1,
    "category_id": 1,
    "name": "Margherita Pizza",
    "description": "Classic tomato and mozzarella pizza",
    "price": "299.00",
    "is_vegetarian": true,
    "is_spicy": false,
    "is_gluten_free": false,
    "calories": 800,
    "preparation_time": 20
}
```

#### Search Menu Items
```http
GET /api/v1/menu-items/search/?q=pizza&category=1&min_price=100&max_price=500&rating=4
```

#### Get Popular Items
```http
GET /api/v1/menu-items/popular/
```

#### Get Nearby Items
```http
GET /api/v1/menu-items/nearby/?lat=19.0760&lng=72.8777&radius=5
```

### 5. Reviews
**Base URL**: `/api/v1/reviews/`

#### Create Review
```http
POST /api/v1/reviews/
Content-Type: application/json

{
    "menu_item_id": 1,
    "rating": 5,
    "comment": "Excellent pizza! Best I've ever had.",
    "images": ["/media/reviews/review1.jpg", "/media/reviews/review2.jpg"]
}
```

#### Mark Review as Helpful
```http
POST /api/v1/reviews/{id}/helpful/
```

### 6. Favorites
**Base URL**: `/api/v1/favorites/`

#### Add to Favorites
```http
POST /api/v1/favorites/
Content-Type: application/json

{
    "menu_item_id": 1
}
```

#### Get User Favorites
```http
GET /api/v1/favorites/my_favorites/
```

### 7. Search History
**Base URL**: `/api/v1/search-history/`

#### Get Search History
```http
GET /api/v1/search-history/
```

#### Clear Search History
```http
DELETE /api/v1/search-history/clear_history/
```

---

## Customer API Endpoints

### 1. Customer Profiles
**Base URL**: `/api/v1/profiles/`

#### Create Customer Profile
```http
POST /api/v1/profiles/
Content-Type: application/json

{
    "is_vegetarian": true,
    "is_vegan": false,
    "is_gluten_free": false,
    "spice_tolerance": "medium",
    "preferred_cuisines": ["Italian", "Indian"],
    "allergies": ["nuts"],
    "preferred_areas": ["Downtown", "Bandra"]
}
```

#### Get My Profile
```http
GET /api/v1/profiles/my_profile/
```

#### Update Preferences
```http
POST /api/v1/profiles/{id}/update_preferences/
Content-Type: application/json

{
    "is_vegetarian": false,
    "spice_tolerance": "hot"
}
```

### 2. User Preferences
**Base URL**: `/api/v1/preferences/`

#### Create User Preferences
```http
POST /api/v1/preferences/
Content-Type: application/json

{
    "min_price": "50.00",
    "max_price": "1000.00",
    "max_distance": 10,
    "min_rating": 4.0,
    "email_notifications": true,
    "push_notifications": true
}
```

#### Update Settings
```http
POST /api/v1/preferences/{id}/update_settings/
Content-Type: application/json

{
    "max_distance": 15,
    "min_rating": 3.5
}
```

### 3. Food Recommendations
**Base URL**: `/api/v1/recommendations/`

#### Get Personalized Recommendations
```http
GET /api/v1/recommendations/personalized/?lat=19.0760&lng=72.8777
```

#### Mark as Viewed
```http
POST /api/v1/recommendations/{id}/mark_viewed/
```

#### Mark as Clicked
```http
POST /api/v1/recommendations/{id}/mark_clicked/
```

### 4. Utility Endpoints
**Base URL**: `/api/v1/utilities/`

#### Get Nearby Restaurants
```http
GET /api/v1/utilities/nearby_restaurants/?lat=19.0760&lng=72.8777&radius=5
```

#### Get Food Suggestions
```http
GET /api/v1/utilities/food_suggestions/
```

---

## Data Models

### Core Models

#### Category
```python
{
    "id": "Auto-generated ID",
    "name": "Category name (e.g., Pizza, Burger)",
    "description": "Category description",
    "icon": "Icon image URL",
    "color": "Hex color code",
    "is_active": "Boolean status",
    "create_time": "Creation timestamp"
}
```

#### MerchantProfile
```python
{
    "id": "Auto-generated ID",
    "user": "Associated user ID",
    "business_name": "Business name",
    "business_description": "Business description",
    "business_logo": "Logo image URL",
    "business_license": "License number",
    "tax_id": "Tax identification",
    "opening_time": "Opening time (HH:MM:SS)",
    "closing_time": "Closing time (HH:MM:SS)",
    "business_phone": "Business phone",
    "business_email": "Business email",
    "website": "Website URL",
    "is_verified": "Verification status",
    "is_featured": "Featured status",
    "is_active": "Active status"
}
```

#### Outlet
```python
{
    "id": "Auto-generated ID",
    "merchant": "Merchant profile ID",
    "name": "Outlet name",
    "address": "Full address",
    "area": "Area/locality",
    "city": "City name",
    "state": "State name",
    "pin_code": "PIN code",
    "latitude": "Latitude coordinate",
    "longitude": "Longitude coordinate",
    "phone": "Outlet phone",
    "opening_time": "Opening time",
    "closing_time": "Closing time",
    "is_active": "Active status",
    "is_dine_in": "Dine-in available",
    "is_takeaway": "Takeaway available"
}
```

#### MenuItem
```python
{
    "id": "Auto-generated ID",
    "outlet": "Outlet ID",
    "category": "Category ID",
    "name": "Food item name",
    "description": "Food description",
    "price": "Price in decimal",
    "primary_image": "Main image URL",
    "images": "Additional images array",
    "is_vegetarian": "Vegetarian status",
    "is_spicy": "Spicy status",
    "is_gluten_free": "Gluten-free status",
    "is_available": "Availability status",
    "calories": "Calorie count",
    "preparation_time": "Prep time in minutes",
    "total_orders": "Total order count",
    "average_rating": "Average rating (0-5)",
    "total_reviews": "Total review count",
    "is_favorited": "User favorite status"
}
```

#### Review
```python
{
    "id": "Auto-generated ID",
    "user": "User ID",
    "menu_item": "Menu item ID",
    "rating": "Rating (1-5)",
    "comment": "Review comment",
    "images": "Review images array",
    "is_verified_purchase": "Purchase verification",
    "helpful_votes": "Helpful vote count"
}
```

### Customer Models

#### CustomerProfile
```python
{
    "id": "Auto-generated ID",
    "user": "User ID",
    "is_vegetarian": "Vegetarian preference",
    "is_vegan": "Vegan preference",
    "is_gluten_free": "Gluten-free preference",
    "is_dairy_free": "Dairy-free preference",
    "spice_tolerance": "Spice level (mild/medium/hot/extra_hot)",
    "preferred_cuisines": "Preferred cuisine types array",
    "allergies": "Food allergies array",
    "preferred_areas": "Preferred areas array"
}
```

#### UserPreference
```python
{
    "id": "Auto-generated ID",
    "user": "User ID",
    "min_price": "Minimum price preference",
    "max_price": "Maximum price preference",
    "max_distance": "Maximum distance in km",
    "min_rating": "Minimum rating preference",
    "email_notifications": "Email notification preference",
    "push_notifications": "Push notification preference"
}
```

---

## Search and Filtering

### Location-based Search
All location-based endpoints accept these parameters:
- `lat`: Latitude coordinate
- `lng`: Longitude coordinate
- `radius`: Search radius in kilometers (default: 10km)

### Menu Item Filtering
```http
GET /api/v1/menu-items/?category=1&is_vegetarian=true&min_price=100&max_price=500&rating=4
```

**Available Filters**:
- `category`: Category ID
- `outlet`: Outlet ID
- `is_vegetarian`: Boolean
- `is_spicy`: Boolean
- `is_gluten_free`: Boolean
- `min_price`: Minimum price
- `max_price`: Maximum price
- `rating`: Minimum rating

### Advanced Search
```http
GET /api/v1/menu-items/search/?q=pizza&category=1&outlet=2&min_price=100&max_price=500&rating=4&vegetarian=true
```

**Search Parameters**:
- `q`: Search query text
- `category`: Category ID
- `outlet`: Outlet ID
- `min_price`: Minimum price
- `max_price`: Maximum price
- `rating`: Minimum rating
- `vegetarian`: Vegetarian filter

---

## Error Handling

### Standard Error Response
```json
{
    "error": "Error message description",
    "detail": "Detailed error information",
    "status_code": 400
}
```

### Common HTTP Status Codes
- `200`: Success
- `201`: Created
- `400`: Bad Request
- `401`: Unauthorized
- `403`: Forbidden
- `404`: Not Found
- `500`: Internal Server Error

---

## Rate Limiting
- **Public endpoints**: 100 requests per minute
- **Authenticated endpoints**: 1000 requests per minute
- **Search endpoints**: 50 requests per minute

---

## Pagination
All list endpoints support pagination with these parameters:
- `page`: Page number
- `page_size`: Items per page (default: 20, max: 100)

**Response Format**:
```json
{
    "count": 150,
    "next": "https://api.example.com/endpoint/?page=3",
    "previous": "https://api.example.com/endpoint/?page=1",
    "results": [...]
}
```

---

## Image Upload
- **Supported formats**: JPEG, PNG, WebP
- **Maximum size**: 5MB per image
- **Storage**: Media files stored in `/media/` directory
- **Image optimization**: Automatic resizing and compression

---

## Testing the API

### Using cURL

#### Get All Categories
```bash
curl -X GET "https://yourdomain.com/api/v1/categories/" \
  -H "Authorization: Bearer YOUR_JWT_TOKEN"
```

#### Create Menu Item
```bash
curl -X POST "https://yourdomain.com/api/v1/menu-items/" \
  -H "Authorization: Bearer YOUR_JWT_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "outlet_id": 1,
    "category_id": 1,
    "name": "Margherita Pizza",
    "description": "Classic tomato and mozzarella pizza",
    "price": "299.00",
    "is_vegetarian": true
  }'
```

### Using Postman
1. Import the API endpoints
2. Set the base URL
3. Add JWT token in Authorization header
4. Test each endpoint with appropriate data

---

## Deployment Considerations

### Environment Variables
```bash
SECRET_KEY=your_secret_key
DEBUG=False
ALLOWED_HOSTS=yourdomain.com
DATABASE_URL=postgresql://user:password@localhost:5432/foodies
```

### Database Setup
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

### Static Files
```bash
python manage.py collectstatic
```

---

## Support and Contact
For API support and questions:
- **Email**: support@foodfinder.com
- **Documentation**: https://docs.foodfinder.com
- **GitHub**: https://github.com/foodfinder/backend

---

## Version History
- **v1.0.0**: Initial release with core functionality
- **v1.1.0**: Added advanced search and filtering
- **v1.2.0**: Added personalized recommendations
- **v1.3.0**: Added review and rating system

---

*Last updated: January 2024*
