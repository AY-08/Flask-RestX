# from application import app, jwt, db
# from application.models import Role, User
# from flask_restx import Resource, fields, Api, reqparse
# from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required
# from flask import Flask, request, make_response, jsonify
# tokenAuth = {}
# access_token = ''
# #parser.add_argument('User-Agent', location='headers')


# # def token_required(f):
# #     @wraps(f)
# #     def decorated(*args, **kwargs):
# #         token = None
# #         # jwt is passed in the request header
# #         if 'Authorization' in request.headers:
# #             token = request.headers['Authorization']
# #         # return 401 if token is not passed
# #         print("token from header", token)
# #         if not token:
# #             return jsonify({'message': 'Token is missing !!'}), 401

# #         # try:
# #         #     # decoding the payload to fetch the stored details
# #         #     data = jwt.decode(token, app.config['SECRET_KEY'])
# #         #     current_user = User.query.filter_by(user_id=data['id']).first()

# #         # except:
# #         #     return jsonify({
# #         #         'message': 'Token is invalid !!'
# #         #     }), 401
# #         # returns the current logged in users contex to the routes
# #         # return f(current_user, *args, **kwargs)
# #         return token

# #     return decorated


# authorization = {
#     "jsonWebToken": {
#         "name": "Authorization",
#         "in": "header",
#         "type": "apiKey"
#     }

# }

# api = Api(app, title='Movie App Apis',
#           description='Adding CRUD operations in RestX framework', authorizations=authorization)

# role_model = api.model("Role", {
#     "role_id": fields.Integer,
#     "role_name": fields.String
# })

# user_model = api.model("User", {
#     "user_id": fields.Integer,
#     "user_name": fields.String,
#     "password": fields.String,
#     "role": fields.Nested(role_model),
# })
# update_user_model = api.model("UpdateUser", {
#     "password": fields.String
# })
# add_user_model = api.model("AddUser", {
#     "user_id": fields.Integer,
#     "user_name": fields.String,
#     "password": fields.String,
#     "role_id": fields.Integer

# })
# category_model = api.model("Cateory", {
#     "category_id": fields.Integer,
#     "category_name": fields.String
# })

# product_data_model = api.model("ProductModel", {
#     "categories": fields.Nested(category_model),
#     "product_id": fields.Integer,
#     "product_name": fields.String,
#     "price": fields.String,
#     "seller_id": fields.Integer
# })

# product_model = api.model('Product',{
#     "product_id": fields.Integer,
#     "product_name": fields.String,
#     "price": fields.String,
#     "user_product": fields.Nested(user_model),
#     "category_product":fields.Nested(category_model)



# })
# login_model = api.model("Login", {
#     "username": fields.String,
#     "password": fields.String
# })

# cart_model = ("Cart",{
#     "cart_id": fields.Integer,
#     "total_amount": fields.Float,
#     "user_cart": fields.Nested(user_model),
#     "cartproduct_cart": fields.Nested(cartproduct_model)
# }
    
# )

# cartproduct_model = ("CartProduct", {
#     "cp_id": fields.Integer,
#     "cart_cartproduct": fields.Nested(cart_model), 
#     "product_cartproduct": fields.Nested(product_model),
#     "quantity": fields.Integer

# }

# )


# @api.route("/api/role")
# class RoleResource(Resource):
#     @api.marshal_list_with(role_model)
#     def get(self):
#         result = db.session.query(Role).all()
#         return result, 200


# @api.route("/api/user")
# class UsersResource(Resource):
#     @api.marshal_list_with(user_model)
#     def get(self):
#         result = db.session.query(User).all()
#         return result, 201

#     @api.marshal_with(user_model)
#     @api.expect(add_user_model)
#     def post(self):
#         user_id = api.payload["user_id"]
#         user_name = api.payload["user_name"]
#         password = api.payload["password"]
#         role_id = api.payload["role_id"]
#         print(user_id)
#         print(user_name)
#         print(password)
#         print(role_id)
#         user = User(user_id=api.payload["user_id"], user_name=api.payload["user_name"],
#                     password=api.payload["password"], user_role=api.payload["role_id"])
#         db.session.add(user)
#         db.session.commit()
#         return user, 201


# @api.route("/api/user/<int:keyword>")
# class UserResource(Resource):
#     @api.marshal_list_with(user_model)
#     def get(self, keyword):
#         result = db.session.query(User).filter(User.user_id == keyword).all()

#         return result, 200

#     @api.marshal_with(user_model)
#     @api.expect(update_user_model)
#     def put(self, keyword):
#         print(keyword)
#         result = db.session.query(User).filter(
#             User.user_id == keyword).one_or_none()
#         result.password = api.payload["password"]
#         db.session.commit()
#         if result:
#             return result, 200
#         else:
#             return "error", 400

#     def delete(self, keyword):
#         result = db.session.query(User).filter(
#             User.user_id == keyword).one_or_none()
#         db.session.delete(result)
#         db.session.commit()
#         return "user deleted", 200


# @api.route("/api/category")
# class RoleResource(Resource):
#     @api.marshal_list_with(category_model)
#     def get(self):
#         result = db.session.query(Category).all()
#         if result:
#             return result, 200
#         else:
#             return "error", 400

#     @api.expect(category_model)
#     @api.marshal_with(category_model)
#     def post(self):
#         category = Category(
#             category_id=api.payload["category_id"], category_name=api.payload["category_name"])
#         db.session.add(category)
#         db.session.commit()
#         return category, 200


# @api.route("/api/category/<int:keyword>")
# class CategoryResource(Resource):
#     @api.marshal_with(category_model)
#     @api.expect(category_model)
#     def put(self, keyword):
#         updatec_cate = db.session.query(Category).filter(
#             Category.category_id == keyword).one_or_none()
#         updatec_cate.category_id = api.payload["category_id"]
#         updatec_cate.category_name = api.payload["category_name"]
#         db.session.commit()
#         return updatec_cate, 200

#     def delete(self, keyword):
#         result = db.session.query(Category).filter(
#             Category.category_id == keyword).one_or_none()
#         db.session.delete(result)
#         db.session.commit()
#         return "deleted record", 200


# @api.route("/api/public/product/search/<string:keyword>")
# class Products(Resource):
#     @api.marshal_list_with(product_data_model, code=200)
#     @api.response(400, 'Validation error')
#     def get(self, keyword):
#         result = db.session.query(Product).filter(
#             Product.product_name == keyword).all()
#         return result


# @api.route("/api/public/login")
# class Login(Resource):
#     @api.expect(login_model)
#     def post(self):
#         name = api.payload["username"]
#         password = api.payload["password"]
#         print(name)
#         print(password)
#         query = db.session.query(User).filter(
#             User.user_name == name, User.password == password).all()
#         print(query)
#         if not query:
#             print("Invalid credentials")
#             return {"message": "Invalid credentials"}, 401

#         else:
#             access_token = create_access_token(identity=name)
#             # tokenAuth = {'Authorization': 'Bearer {}'.format(access_token)}

#           #  tokenAuth.update({"Authorization": "Bearer "+access_token})

#             return {"access_token": access_token}, 200


# # @api.route("/api/currentuser")
# # class CurrentUser(Resource):
# #     @api.doc(security='api_key')
# #     @token_required
# #     def get(self):
# #         currentusr = get_jwt_identity()
# #         return currentusr


# @api.route("/api/welcomeuser")
# class Welcome(Resource):
#     @jwt_required()
#     @api.doc(security="jsonWebToken")
#     def get(self):
#         currentuser = get_jwt_identity()
#         # currentuser.encode_auth_token
#         if currentuser == 'apple':
#             return {"message": f"Hello, {currentuser}"}, 200
#         else:
#             return {"message": "Missing Authorization Header"}, 401


# @api.route('/testing/<int:id>', endpoint='api')
# @api.doc(header={'id': 'An ID'})
# class MyResource(Resource):
#     def get(self, id):
#         return {}

#     # @api.doc(responses={403: 'Not Authorized'})
#     # def post(self, id):
#     #     api.abort(403)


# # class LoginAPI(MethodView):
# #     """
# #     User Login Resource
# #     """

# #     def post(self):
# #         # get the post data
# #         post_data = request.get_json()
# #         try:
# #             # fetch the user data
# #             user = User.query.filter_by(
# #                 email=post_data.get('email')
# #             ).first()
# #             auth_token = user.encode_auth_token(user.id)
# #             if auth_token:
# #                 responseObject = {
# #                     'status': 'success',
# #                     'message': 'Successfully logged in.',
# #                     'auth_token': auth_token.decode()
# #                 }
# #                 return make_response(jsonify(responseObject)), 200
# #         except Exception as e:
# #             print(e)
# #             responseObject = {
# #                 'status': 'fail',
# #                 'message': 'Try again'
# #             }
# #             return make_response(jsonify(responseObject)), 500
