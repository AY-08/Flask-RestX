from application import db

# one to many relation implmementation


class Role(db.Model):
    role_id = db.Column(db.Integer, primary_key=True)
    role_name = db.Column(db.String)
    users = db.relationship('User', backref='role')


class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String)
    password = db.Column(db.String)
    user_role = db.Column(db.Integer, db.ForeignKey('role.role_id'))
    carts = db.relationship('Cart', backref='user')


class Cart(db.Model):
    cart_id = db.Column(db.Integer, primary_key=True)
    total_amount = db.Column(db.Float)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))


class Category(db.Model):
    category_id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String)

# class Category(db.Model):
#     category_id = db.Column(db.Integer, primary_key=True)
#     category_name = db.Column(db.String)
#     products = db.relationship('Product', back_populates='categories')


# class User(db.Model):
#     user_id = db.Column(db.Integer, primary_key=True)
#     user_name = db.Column(db.String)
#     password = db.Column(db.String)
#     user_role = db.Column(db.ForeignKey('role.role_id'))
#     roles = db.relationship('Role', back_populates='users')
# #     cart = db.relationship('Cart', backref='user')
# #     product = db.relationship('Product', backref='user')


# class Product(db.Model):
#     __tablename__ = 'product'
#     product_id = db.Column(db.Integer, primary_key=True)
#     product_name = db.Column(db.String)
#     price = db.Column(db.Float)
#     seller_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
#     category_id = db.Column(db.Integer, db.ForeignKey('category.category_id'))
# #     # user = db.relationship('User', back_populates='product')
#     categories = db.relationship('Category', back_populates='products')


# # class Cart(db.Model):
# #     cart_id = db.Column(db.Integer, primary_key=True)
# #     total_amount = db.Column(db.Float)
# #     user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
# #     cartproduct = db.relationship('CartProduct', backref='cart')
# #     user = db.relationship('User', back_populates='cart')


# # class CartProduct(db.Model):
# #     cp_id = db.Column(db.Integer, primary_key=True)
# #     cart_id = db.Column(db.String, db.ForeignKey('cart.cart_id'))
# #     product_id = db.Column(db.Integer, db.ForeignKey('product.product_id'))
# #     quantity = db.Column(db.Integer)
# #     cart = db.relationship('Cart', back_populates='cartproduct')
