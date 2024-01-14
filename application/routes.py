from application import app, db
from flask_restx import Resource, Api, fields
from application.models import Role, User
from flask_jwt_extended import JWTManager, create_access_token, get_jwt_identity, jwt_required

authorization = {
    "jsonwebtoken": {
        "name": "Authorization",
        "in": "header",
        "type": "apiKey"
    }
}

api = Api(app, decsription= "Apis", authorizations = authorization)

role_model = api.model('Role',{
      "role_id": fields.Integer,
      "role_name": fields.String
})

user_model = api.model('User', {
    "user_id": fields.Integer,
    "user_name": fields.String,
     "password": fields.String,
     "role": fields.Nested(role_model)

})

login_model = api.model('Login', {
    "username": fields.String,
    "password": fields.String
})

add_user_model = api.model('Add_User', {
    "user_name": fields.String,
    "password": fields.String,
    "user_role": fields.Integer

})
@api.route('/users')
class Users(Resource):
    @api.marshal_list_with(user_model)
    def get(self):
        query = db.session.query(User).all()

        return query, 200


# login
@api.route('/login')
class Login(Resource):
    @api.expect(login_model)
    def post(self):
        username = api.payload["username"]
        password = api.payload["password"]
        credentials =  db.session.query(User).filter(username == username and password == password)
        if credentials:
            access_token = create_access_token(identity = username)

            return {"message": access_token}, 200
        else:
            return {"message": "Invalid Credentials"}, 401
            


@api.route('/protected')
class Protected(Resource):
    @jwt_required()
    @api.doc(security ="jsonwebtoken")
    def get(self):
        current_user = get_jwt_identity()
        if current_user == 'bob':
            return {"messsage":f"Welcome, {current_user}"}, 200

        else:
            return {"message":"Login with admin id"}, 401

    @api.expect(add_user_model)
    @api.marshal_list_with(user_model)
    @jwt_required()
    @api.doc(security= "jsonwebtoken")
    def post(self):
        print(api.payload)
        currentuser = get_jwt_identity()
        if currentuser == 'bob':
            user = User(user_name = api.payload["user_name"], password = api.payload["password"], user_role = api.payload["user_role"])
            db.session.add(user)
            db.session.commit()

            return user, 200 

        else: 
            return {"message": "Login from bob id to add user"},401


@api.route('/delete/<int:keyword>')  
class delete(Resource):      
    @jwt_required()
    @api.doc(security="jsonwebtoken")
    def delete(self, keyword):
        currentuser = get_jwt_identity()
        if currentuser == 'bob':
            user = db.session.query(User).filter(User.user_id == keyword).one_or_none()
            print(user)
            db.session.delete(user)
            db.session.commit()
            return {"message": "user deleted!!!"}


        
        else: 
            {"message": "Login using bob id to delete user"}