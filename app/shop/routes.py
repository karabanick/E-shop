from flask import render_template, flash, redirect, url_for, request, current_app
from flask_login import login_required, current_user
from werkzeug.utils import secure_filename
import os
from app import db, photos
from app.shop import bp
from app.shop.forms import CreateShopForm, ProductForm
from app.models import Shop, Product

@bp.route('/create', methods=['GET', 'POST'])
@login_required
def create():
    if current_user.shop:
        return redirect(url_for('dashboard.index'))
    
    form = CreateShopForm()
    if form.validate_on_submit():
        # Handle file uploads
        logo_filename = None
        banner_filename = None

        if form.logo.data:
            logo_filename = photos.save(form.logo.data)
        if form.banner.data:
            banner_filename = photos.save(form.banner.data)

        shop = Shop(
            name=form.name.data,
            description=form.description.data,
            logo=logo_filename,
            banner=banner_filename,
            owner=current_user
        )
        db.session.add(shop)
        db.session.commit()
        flash('Your shop has been created!', 'success')
        return redirect(url_for('dashboard.index'))
    
    return render_template('shop/create.html', title='Create Shop', form=form)

@bp.route('/add_product', methods=['GET', 'POST'])
@login_required
def add_product():
    if not current_user.shop:
        return redirect(url_for('shop.create'))
    
    form = ProductForm()
    if form.validate_on_submit():
        image_filename = photos.save(form.image.data)
        product = Product(
            name=form.name.data,
            description=form.description.data,
            price=float(form.price.data),
            quantity=int(form.quantity.data),
            image=image_filename,
            category=form.category.data,
            shop=current_user.shop
        )
        db.session.add(product)
        db.session.commit()
        flash('Product added successfully!', 'success')
        return redirect(url_for('dashboard.products'))
    
    return render_template('shop/add_product.html', title='Add Product', form=form)

