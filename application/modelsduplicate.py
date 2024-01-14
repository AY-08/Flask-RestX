from application import db
import datetime

class Test(db.Model):
    id = db.Column(db.Integer, primary_key= True) 
    date_time = db.Column(db.DateTime, default = datetime.datetime.utcnow)
    date_only = db.Column(db.Date, default = datetime.date.today)
    tzinfo = db.Column(db.String)
