from flask import  render_template, flash, redirect, url_for
from flask_login import login_required, current_user
from app import db
from app.dashboard import bp
from app.models import Shop, Product, Order

@bp.route('/')
@login_required
def index():
    if not current_user.shop:
        return redirect(url_for('shop.create'))
    
    shop = current_user.shop
    products = shop.products.order_by(Product.created_at.desc()).limit(5).all()
    orders = Order.query.filter_by(shop_id=shop.id).order_by(Order.created_at.desc()).limit(5).all()

    # Sample analylitsics data (replaceable with real data queries)
    analytics = {
        'total_sales': 100,
        'revenue': 2,
        'top_products': [
            {'name': 'Product A', 'sales': 15},
            {'name': 'Product B', 'sales': 12},
            {'name': 'Product C', 'sales': 8}
        ],
        'order_status': {
            'pending': 3,
            'processing': 2,
            'completed': 7
        }
    }

    return render_template('dashboard/index.html',
                           shop=shop,
                           products=products,
                           orders=orders,
                           analytics=analytics)

@bp.route('/products')
@login_required
def products():
    if not current_user.shop:
        return redirect(url_for('shop.create'))
    
    products = current_user.shop.products.order_by(Product.created_at.desc()).all()
    return render_template('dashboard/products.html', products=products)

@bp.route('/orders')
@login_required
def orders():
    if not current_user.shop:
        return redirect(url_for('shop.create'))
    
    orders = Order.query.filter_by(shop_id=current_user.shop.id).order_by(Order.created_at.desc()).all()
    return render_template('dashboard/orders.html', orders=orders)

@bp.route('/view_shop')
@login_required
def view_shop():
    if not current_user.shop:
        return redirect(url_for('shop.create'))
    
    shop = current_user.shop
    return render_template('dashboard/view_shop.html', shop=shop)