from application import db, app
from flask_restx import Resource, Api, fields
from flask import Flask, request, jsonify
from application.models import User
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity

authorization = {
    "jsonWebToken": {
        "name": "Authorization",
        "in": "header",
        "type": "apiKey"
    }

}
# # authenticate and response with status code and  JWT

# # decorator for verifying the JWT

api = Api(app, description="Rest Apis", authorizations=authorization)
login_model = api.model("Login", {
    "username": fields.String,
    "password": fields.String
})
# def token_required(f):
#     @wraps(f)
#     def decorated(*args, **kwargs):
#         token = None
#         # jwt is passed in the request header
#         if 'x-access-token' in request.headers:
#             token = request.headers['x-access-token']
#         # return 401 if token is not passed
#         if not token:
#             return jsonify({'message': 'Token is missing !!'}), 401

#         # try:
#         #     # decoding the payload to fetch the stored details
#         #     data = jwt.decode(token, app.config['SECRET_KEY'])
#         #     current_user = User.query.filter_by(user_id=data['id']).first()

#         # except:
#         #     return jsonify({
#         #         'message': 'Token is invalid !!'
#         #     }), 401
#         # returns the current logged in users contex to the routes
#         # return f(current_user, *args, **kwargs)
#         return token

#     return decorated


@api.route('/login')
class LoginView(Resource):
    @api.expect(login_model)
    def post(self):
        name = api.payload["username"]
        password = api.payload["password"]
        print(name)
        print(password)
        query = db.session.query(User).filter(
            User.user_name == name, User.password == password).all()
        print(query)
        if not query:
            # print("Wrong Username or password")
            return {"message": "Invalid credentials"}, 401
        else:
            access_token = create_access_token(identity=name)
            tokenAuth = {'access_token': access_token}

        #  tokenAuth.update({"Authorization": "Bearer "+access_token})

        return tokenAuth, 200


# Protected resource that requires Bearer Token authentication


@api.route('/protected')
class ProtectedView(Resource):
    @jwt_required()
    @api.doc(security="jsonWebToken")
    def get(self):
        current_user = get_jwt_identity()
        print("current user", current_user)
        return {'message': f"Hello, {current_user}"}
        # if current_user:
        #     data = {
        #         'message': f"Hello, {current_user}"}
        #     return data, 200
        # else:
        #     return {"message": "Missing Authorization Header"}, 401
