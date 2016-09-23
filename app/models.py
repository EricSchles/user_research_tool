from app import db

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String())
    password = db.Column(db.String())

    def __init__(self,username,password):
        self.username = username
        self.password = password

#To do - make this a join
class Notes(db.Model):
    __tablename__ = 'notes'
    id = db.Column(db.Integer, primary_key=True)
    note = db.Column(db.String())
    username = db.Column(db.String())
    
    def __init__(self,note,username):
        self.note = note
        self.username = username

