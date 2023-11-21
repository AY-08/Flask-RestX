from application import db

class Role(db.Model):
    __tablename__ = 'Role'
    role_id = db.Column(db.Integer, primary_key = True)
    role_name = db.Column(db.String)
    users = db.relationship("User", back_populates = 'roles')


class User(db.Model):
    __tablename__ = 'User' 
    user_id = db.Column(db.Integer, primary_key = True)
    user_name = db.Column(db.String, nullable = False, unique = True)
    password = db.Column(db.String, nullable = False)
    user_role = db.Column(db.String, db.ForeignKey('Role.role_id'))
    roles = db.relationship("Role", back_populates = 'users')
    carts = db.relationship("Cart", back_populates = 'cart_users')
    products = db.relationship("Product", back_populates = 'product_users')


class Cart(db.Model):
    __tablename__ = 'Cart'
    cart_id = db.Column(db.Integer, primary_key = True)
    total_amount = db.Column(db.Float)
    user_id = db.Column(db.Integer, db.ForeignKey('User.user_id'))
    cart_users = db.relationship("User", back_populates = 'carts')
    

    

class Category(db.Model):
    __tablename__ = 'Category'
    category_id = db.Column(db.Integer, primary_key = True)
    category_name = db.Column(db.Integer)
    products_cat = db.relationship('Product', back_populates = 'category')


class Product(db.Model):
    __tablename__ = 'Product'
    product_id = db.Column(db.Integer, primary_key = True)
    product_name = db.Column(db.String)
    price = db.Column(db.Float)
    seller_id = db.Column(db.Integer, db.ForeignKey('User.user_id'))  
    product_users = db.relationship('User', back_populates = 'products')  
    category_id = db.Column(db.Integer, db.ForeignKey('Category.category_id'))
    category = db.relationship('Category', back_populates = 'products_cat')
