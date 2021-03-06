 # -*- coding: utf-8 -*-

from app import db
# from werkzeug.security import generate_password_has, check_password_hash

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nickname = db.Column(db.String(64), index = True, unique = True)
    email = db.Column(db.String(120), index = True, unique = True)
    comments1= db.relationship('Git_comment', backref = 'author', lazy = 'dynamic')
    comments2= db.relationship('Python_comment', backref = 'author', lazy = 'dynamic')
    comments3= db.relationship('Javascript_comment', backref = 'author', lazy = 'dynamic')
    password =db.Column(db.String(128))


    # @property
    # def password(self):
    #     raise AttributeError('password is not a readable attribute')
    
    # @password.setter
    # def password(self, password):
    #     self.password = generate_password(password)
    
    # def verify_password(self, password):
    #     return check_password(self.password, password)

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2
        except NameError:
            return str(self.id)  # python 3

    def __repr__(self):
        return '<User %r>' % (self.nickname)


class Git_comment(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Git_comment %r>' % (self.body)



class Python_comment(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Python_comment %r>' % (self.body)


class Javascript_comment(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Javascript_comment %r>' % (self.body)
