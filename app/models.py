from app import db

class User(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   nickname = db.Column(db.String(64),index=True,unique=True)
   email = db.Column(db.String(120),index=True,unique=True)
   task = db.relationship('Task',lazy='dynamic')
   @property 
   def is_authenticated(self):
      return True
   @property
   def is_active(self):
      return True
   @property
   def is_anonymous(self):
      return False
   
   def get_id(self):
      try:
         return unicode(self.id)
      except:
         return str(self.id) 

   def __repr__(self):
      return '<User %r>' % (self.nickname)

class Task(db.Model):
   id = db.Column(db.Integer,primary_key=True)
   title = db.Column(db.String(64))
   description = db.Column(db.String(140))
   ###Add a due date 
   ###Add other stuff
   user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
   
   def __repr__(self):
       return '<Task %r>' % (self.descrption)
