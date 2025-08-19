# 🍕 Food Finder Backend API

A comprehensive Django REST Framework backend for a food discovery platform that helps users find nearby restaurants and food items based on their preferences and location.

## 🎯 Project Overview

**Main Goal**: Create a food finder app where users can easily discover what famous food vendors are available nearby, whether they're active or not, making it simple for users to find the food they want without any hassle.

**Phase 1**: Focus on food discovery (no online delivery yet)

## ✨ Features

### For Merchants (Food Vendors)
- **Profile Management**: Create and manage business profiles
- **Multiple Outlets**: Manage multiple restaurant locations
- **Menu Management**: Create and update food items
- **Business Hours**: Set opening and closing times
- **Location Services**: Add coordinates for map integration

### For Customers (Food Seekers)
- **Food Discovery**: Search for food items by name, category, or location
- **Advanced Filtering**: Filter by dietary preferences, price, rating, and distance
- **Personalized Recommendations**: AI-powered food suggestions
- **Reviews & Ratings**: Rate and review food items
- **Favorites**: Save favorite food items
- **Search History**: Track search queries for better recommendations

### Core Functionality
- **Location-based Search**: Find food within specified radius
- **Category Management**: Organize food by types (Pizza, Burger, Indian, etc.)
- **Dietary Filters**: Vegetarian, vegan, gluten-free, spicy options
- **Rating System**: 5-star rating system with helpful votes
- **Image Support**: Multiple images for food items and reviews

## 🏗️ Architecture

### Technology Stack
- **Backend**: Django 5.2 + Django REST Framework
- **Database**: PostgreSQL with PostGIS for location queries
- **Authentication**: JWT-based authentication
- **Image Handling**: Django ImageField with media storage
- **API Documentation**: Swagger/OpenAPI integration
- **Permissions**: Role-based access control

### Project Structure
```
foodies/
├── merchant/           # Merchant and food vendor functionality
│   ├── models.py      # Category, MerchantProfile, Outlet, MenuItem, Review
│   ├── serializers.py # API serializers
│   ├── views.py       # API views and endpoints
│   └── admin.py       # Django admin configuration
├── customer/           # Customer and user functionality
│   ├── models.py      # CustomerProfile, UserPreference, Recommendations
│   ├── serializers.py # Customer API serializers
│   ├── views.py       # Customer API views
│   └── admin.py       # Customer admin configuration
├── custom_auth/        # User authentication and management
└── utils/              # Common utilities and helpers
```

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- PostgreSQL with PostGIS extension
- Virtual environment (recommended)

### Installation

1. **Clone the repository**
```bash
git clone <repository-url>
cd Foodies
```

2. **Create virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Environment Setup**
Create a `.env` file in the project root:
```bash
SECRET_KEY=your_secret_key_here
DEBUG=True
DATABASE_URL=postgresql://username:password@localhost:5432/foodies_db
API_KEY_SECRET=your_api_key_secret
```

5. **Database Setup**
```bash
# Create database
createdb foodies_db

# Run migrations
python manage.py makemigrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser
```

6. **Run the server**
```bash
python manage.py runserver
```

7. **Test the setup**
```bash
python test_models.py
```

## 📱 API Endpoints

### Base URL
```
http://localhost:8000/api/v1/
```

### Merchant Endpoints
- `GET /merchant/categories/` - Get food categories
- `POST /merchant/merchants/` - Create merchant profile
- `GET /merchant/outlets/` - Get outlets
- `POST /merchant/menu-items/` - Add menu items
- `GET /merchant/menu-items/search/` - Search food items
- `POST /merchant/reviews/` - Add reviews

### Customer Endpoints
- `POST /customer/profiles/` - Create customer profile
- `GET /customer/recommendations/personalized/` - Get recommendations
- `GET /customer/utilities/nearby_restaurants/` - Find nearby restaurants

### Authentication
```bash
# Get JWT token
POST /api/custom_auth/login/
{
    "email": "user@example.com",
    "password": "password"
}

# Use token in headers
Authorization: Bearer <your_jwt_token>
```

## 🗄️ Database Models

### Core Models
- **Category**: Food categories (Pizza, Burger, etc.)
- **MerchantProfile**: Business profiles for food vendors
- **Outlet**: Restaurant locations with coordinates
- **MenuItem**: Individual food items with details
- **Review**: User reviews and ratings
- **CustomerProfile**: User food preferences
- **UserPreference**: Search and filter preferences

### Key Features
- **Location-based queries** using PostGIS
- **Soft delete** with `is_delete` flag
- **Audit trails** with `create_time` and `update_time`
- **Status management** with `is_active` flags
- **Image handling** for food items and reviews

## 🔍 Search & Filtering

### Location-based Search
```bash
GET /api/v1/merchant/menu-items/nearby/?lat=19.0760&lng=72.8777&radius=5
```

### Advanced Filtering
```bash
GET /api/v1/merchant/menu-items/?category=1&is_vegetarian=true&min_price=100&max_price=500&rating=4
```

### Text Search
```bash
GET /api/v1/merchant/menu-items/search/?q=pizza&category=1&outlet=2
```

## 🧪 Testing

### Run Model Tests
```bash
python test_models.py
```

### Run Django Tests
```bash
python manage.py test foodies.merchant
python manage.py test foodies.customer
```

### API Testing
Use the included test script or tools like:
- **Postman**: Import the API collection
- **cURL**: Use the examples in the documentation
- **Swagger UI**: Available at `/swagger/`

## 📊 Admin Interface

Access the Django admin at `/admin/` to manage:
- Food categories and merchants
- Restaurant outlets and menus
- User reviews and ratings
- Customer profiles and preferences
- System settings and configurations

## 🔧 Configuration

### Settings Files
- `config/settings/base.py` - Base settings
- `config/settings/development.py` - Development environment
- `config/settings/production.py` - Production environment

### Key Settings
- **Database**: PostgreSQL with PostGIS
- **Media Files**: Local storage in `/media/` directory
- **Static Files**: Collected to `/staticfiles/` directory
- **CORS**: Configured for frontend integration
- **JWT**: Token-based authentication

## 🚀 Deployment

### Production Setup
1. Set `DEBUG=False` in production settings
2. Configure production database
3. Set up static file serving
4. Configure media file storage
5. Set up proper CORS settings

### Docker Support
```bash
# Build and run with Docker
docker-compose up --build
```

### Environment Variables
```bash
SECRET_KEY=your_production_secret_key
DEBUG=False
ALLOWED_HOSTS=yourdomain.com
DATABASE_URL=postgresql://user:password@host:5432/dbname
```

## 📚 API Documentation

Comprehensive API documentation is available in:
- **FOOD_FINDER_API_DOCUMENTATION.md** - Detailed API reference
- **Swagger UI** - Interactive API documentation at `/swagger/`
- **Code comments** - Inline documentation in views and serializers

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📝 License

This project is licensed under the MIT License.

## 🆘 Support

For support and questions:
- Check the API documentation
- Review the code comments
- Open an issue on GitHub
- Contact the development team

## 🔮 Future Enhancements

### Phase 2 (Planned)
- **Online Ordering**: Food delivery and pickup
- **Payment Integration**: Multiple payment gateways
- **Real-time Tracking**: Order status updates
- **Push Notifications**: Order updates and offers

### Phase 3 (Planned)
- **AI Recommendations**: Machine learning for better suggestions
- **Analytics Dashboard**: Business insights for merchants
- **Multi-language Support**: Internationalization
- **Mobile Apps**: Native iOS and Android applications

---

## 🎉 Getting Started Checklist

- [ ] Clone the repository
- [ ] Set up virtual environment
- [ ] Install dependencies
- [ ] Configure environment variables
- [ ] Set up PostgreSQL database
- [ ] Run migrations
- [ ] Create superuser
- [ ] Test the models
- [ ] Start the development server
- [ ] Access the admin interface
- [ ] Test the API endpoints

**Happy coding! 🚀**
