from flask import render_template, current_app 
from flask_login import login_required
from app.models import Shop, Product
from app.main import bp

@bp.route('/')
def index():
    shops = Shop.query.all()
    return render_template('main/index.html', shops=shops)

@bp.route('/home')
def home():
    return render_template('main/home.html')

@bp.route('/home2')
def home2():
    return render_template('main/home2.html', title='Home')

@bp.route('/marketplace')
def marketplace():
    shops = Shop.query.order_by(Shop.created_at.desc()).limit(8).all()
    products = Product.query.order_by(Product.created_at.desc()).limit(12).all()
    return render_template('main/marketplace.html',
                           shops=shops,
                           products=products)
    
@bp.route('/shop/<shop_name>')
def shop_detail(shop_name):
    shop = Shop.query.filter_by(name=shop_name).first_or_404()
    products = shop.products.order_by(Product.created_at.desc()).all()
    return render_template('main/shop_detail.html', shop=shop, products=products)

@bp.route('/product/<int:product_id>')
def product_detail(product_id):
    product = Product.query.get_or_404(product_id)
    return render_template('main/product_detail.html', product=product)