from . import db

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    roles_id = db.Column(db.Integer,db.Foreignkey('roless.id'))
    
    def __repr__(self):
        return f'User {self.username}'

#class Role
class Role(db.model):
    __table__ = 'roles'
    
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    users = db.relationship('User',backref = 'role',lazy="dynamic")
    
    return f'User {self.name}'
 