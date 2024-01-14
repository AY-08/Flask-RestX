from application import db, app
from flask_sqlalchemy import *
from flask import Flask,request
from flask_restx import Resource, Api, fields
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity 
#from application.models import Role, User, Product, Cart, CartProduct, Category 
from application.models import Test
from datetime import datetime, date
import pytz



authorization = {
    "JsonWebToken": {
        "name": "Authorization",
        "in":"header",
        "type": "apiKey"
    }
}


api = Api(app, description = "Api testing", authorizations = authorization)
testpost_model = api.model("Test Post Model",{
    "id": fields.Integer,
    "tzinfo": fields.String

})
test_model = api.model("Test",{
    "id": fields.Integer,
    "date_time": fields.DateTime,
    "date_only": fields.Date,
    "tzinfo": fields.String
})
# loginModel = api.model("Login", {
#     "username": fields.String,
#     "password" : fields.String

# })

# @api.route('/api/login')
# class LoginView(Resource):
#     @api.expect(LoginView)
#     def post(self):
#         username = api.payload["username"]
#         password = api.payload["password"]

#         result = db.session.query(User).filter(_and(User.user_name == username, User.password == password)).first()
#         if not result:
#             return {"message": "wrong credentials"}, 401
#         else:
#             print("username", result.username)
#             access_token = create_access_token(identity = result.username)



@api.route('/datetime')
class Datetime(Resource):
    def get(self):
        date_time = datetime.datetime(year = 2023, month = 6,
         day = 25, hour = 5, minute = 30, second = 34, microsecond = 435,
          tzinfo = pytz.timezone("Asia/Kolkata"))
        print(date_time.year)
        print(date_time.month)
        print(date_time.day)

        return date_time.year

    @api.expect(test_model)
    @api.marshal_list_with(test_model)
    def post(self):
        id = api.payload["id"]
        tzinfo = api.payload["tzinfo"] 
        test = Test(id = id, tzinfo = tzinfo)
        db.session.add(test)
        db.session.commit()

        return test, 200
        


        # jsondata = request.get_json()
        # date_time = jsondata.get("date_time")
        # print("request json date_time:",date_time)
        # datedata = jsondata.get("date")
        # print("request json date:",datedata)
        # datetime_str= api.payload["date_time"]
        # format_datetime = "YYYY-MM-DDTHH:mm:ss.SSSZ"
        
        # payload_datetime = datetime.strptime(datetime_str, format_datetime)
        # format_date =date.strftime('%Y-%m-%d')
        # date_str = api.payload["Date"]
        # date_data = date.strptime(date_str, format_date)
    
        # print("payload payload_datetime:", type(payload_datetime))
        # print("date data", type(date_data))
        

        # test = Test(id = jsondata.get("id"), date_time = datetime(date_time.year, date_time.month, date_time.day, date_time.hour, date_time.minute, date_time.second, date_time.microsecond),
        #                   date = date(datedata.year, datedata.month, datedata.day),
        #                    tzinfo = jsondata.get("tzinfo"))
        # test = Test(id = api.payload['id'], date_time = datetime(year = payload_datetime.year,
        #  month = payload_datetime.month, day = payload_datetime.day, hour = payload_datetime.hour,minute = payload_datetime.minute, second = payload_datetime.second, microsecond = payload_datetime.microsecond),
        #  date = date(day = date_data.year, month = date_data.month, day = date_data.day, tzinfo = api.payload['tzinfo'] ))
        # db.session.add(test)
        # db.session.commit()
        # return test, 200




       
