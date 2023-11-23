from application import db

class Role(db.Model):
    __tablename__ = 'Role'
    role_id = db.Column(db.Integer, primary_key = True)
    role_name = db.Column(db.String)
    user = db.relationship("User", back_populates = 'role')


class User(db.Model):
    __tablename__ = 'User'
    user_id = db.Column(db.Integer, primary_key = True)
    user_name = db.Column(db.String)
    password = db.Column(db.String)
    user_role = db.Column(db.Integer, db.ForeignKey('Role.role_id'))
    role = db.relationship('Role', back_populates = 'user')
    cart_user = db.relationship('Cart', back_populates = 'user_cart')
    product_user = db.relationship('Product', back_populates = 'user_product')

class Cart(db.Model):
    __tablename__ = 'Cart'
    cart_id = db.Column(db.Integer, primary_key = True)
    total_amount = db.Column(db.Float)
    user_id = db.Column(db.Integer, db.ForeignKey('User.user_id'))
    user_cart = db.relationship('User', back_populates = 'cart_user')
    cartproduct_cart = db.relationship('CartProduct', back_populates = 'cart_cartproduct')

class Category(db.Model):
    __tablename__ = 'Category'
    category_id = db.Column(db.Integer, primary_key = True)
    category_name = db.Column(db.String)
    product_category = db.relationship('Product', back_populates = 'category_product')


class Product(db.Model):
    __tablename__ = 'Product'
    product_id = db.Column(db.Integer, primary_key = True)
    product_name = db.Column(db.String)
    price = db.Column(db.Float)
    seller_id = db.Column(db.Integer, db.ForeignKey('User.user_id'))
    user_product = db.relationship('User', back_populates = 'product_user')
    category_id = db.Column(db.Integer, db.ForeignKey('Category.category_id'))
    category_product = db.relationship('Category', back_populates = 'product_category')
    cartproduct_product = db.relationship('CartProduct', back_populates = 'product_cartproduct')

class CartProduct(db.Model):
    __tablename__ = 'CartProduct'
    cp_id = db.Column(db.Integer, primary_key = True)
    cart_id = db.Column(db.Integer, db.ForeignKey('Cart.cart_id'))
    cart_cartproduct = db.relationship('Cart', back_populates = 'cartproduct_cart')
    product_id = db.Column(db.Integer, db.ForeignKey('Product.product_id'))
    product_cartproduct = db.relationship('Product', back_populates = 'cartproduct_product')
    quantity = db.Column(db.Integer)

    
