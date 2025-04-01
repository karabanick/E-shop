from app import create_app, db
from app.models import User, Shop, Product, Order, OrderItem

app = create_app()

def init_db():
    with app.app_context():
        # Create all database tables
        db.create_all()

        # Create a test user
        if not User.query.filter_by(username='admin').first():
            user = User(username='admin', email='admin@example.com', is_shop_owner=True)
            user.set_password('password')
            db.session.add(user)
            db.session.commit()

            # Create a test shop
            shop = Shop(name='Test Shop', description='A test shop', owner=user)
            db.session.add(shop)
            db.session.commit()

            # Create a test products
            products = [
                Product(name='Product 1', description='First test description',price=9.99, quantity=10, shop=shop),
                Product(name='Product 2', description='Second test product', price=19.99, quantity=5, shop=shop),
                Product(name='Product 3', description='Third test product', price=29.99, quantity=2, shop=shop),
            ]
            db.session.add_all(products)
            db.session.commit()

if __name__=='__main__':
    init_db()
    print("Database initialized successfully!")