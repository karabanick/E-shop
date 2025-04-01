from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, FileField, SubmitField
from wtforms.validators import DataRequired, Length
from flask_wtf.file import FileAllowed

class CreateShopForm(FlaskForm):
    name = StringField('Shop Name', validators=[
        DataRequired(),
        Length(min=3, max=100)
    ])
    description = TextAreaField('Description', validators=[
        DataRequired(),
        Length(min=10, max=500)
    ])
    logo = FileField('Shop Logo', validators=[
        FileAllowed(['jpg', 'jpeg', 'png'], 'Images only!')
    ])
    banner = FileField('Shop Banner (Optional)', validators=[
        FileAllowed(['jpg', 'jpeg', 'png'], 'Images only!')
    ])
    submit = SubmitField('Create Shop')

class ProductForm(FlaskForm):
        name = StringField('Product Name', validators=[
            DataRequired(),
            Length(min=3, max=100)
        ])
        description = TextAreaField('Description', validators=[
            DataRequired(),
            Length(min=10, max=1000)
        ])
        price = StringField('Price', validators=[DataRequired()])
        quantity = StringField('Quantity', validators=[DataRequired()])
        image = FileField('Product Image', validators=[
            DataRequired(),
            FileAllowed(['jpg', 'jpeg', 'png'], 'Images only!')
        ])
        category = StringField('Category', validators=[
            DataRequired(),
            Length(min=2, max=50)
        ])
        submit = SubmitField('Save Product')

