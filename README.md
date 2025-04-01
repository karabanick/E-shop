An e-commerce platform with:
- Multi-tenant architecture(multiple shops)
- Customer and shop owner roles
- Comprehensive dshboard and management features.
Using Python/Flask for back-end and front-end.
UI | UX enabled.

## TECHNOLOGY STACK ##
Back-end: Python/Flask
Database: SQLite (dev)
Front-end: HTML5, CSS3, Javascript
Authentication: Flask-login
File Uploads: Flask-Uploads
Payments: Mock implementation (can integrate Stripe/Paypal)
Image Storage: Local filesystem (can migrate to S3)

## Core Application Files ##
app/__init__.py - Flask app initialization
   /routes.py - All application routes
   /models.py - Database models
   /forms.py - WTForms definitions
   /templates/ - All HTML templates
   /static/ - CSS/JS/Images
config.py - Configuration settings

## Main Features Modules ##
app/auth/ - Authentication system
   /shop/ - Shop management
   /products/ - Product management
   /orders/ - Order processing
   /dashboard/ - Owner dashboard

##  Implementation steps ##
1. Setup and configuration:
	Initialize Flask application structure
	Configure database (SQLAlchemy)
	Setup authentication system(Flask-Login)
	Configure file upload handling
	Create base templates with modern UI framework (Bootstrap 5)
2. Authentication System:
	User registration/login forms
	Password hashing
	Role management (customer/shop owner)
	Profile management
	Session handling
3. Shop Creation flow:
	Shop registration form
	Logo/banner upload
	Initial product setup
	Shop activation logic
4. Product management:
	Product CRUD operations
	Image upload handling
	Inventory tracking
	Category/tag system
5. Order Processing:
	Cart functionality
	Checkout process
	Order status tracking
	Notification system
6. Dashboard features:
	Sales analytics
	Inventory alerts
	Order management
	Review system
7. Market Features:
	Shop discovery
	Product search/filter
	Customer reviews
	Purchase history

