from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os
import uuid

app = Flask(__name__)

if __name__ == '__main__':

    #app.run(host='127.0.0.1',port=8000,debug=True)
    app.run(debug=True)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
db = SQLAlchemy(app)


#################################################################
# USERS
#################################################################

class Admin(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  auid = db.Column(db.String(8), unique=True, nullable=False)
  first_name = db.Column(db.String(100), unique=False, nullable=False)
  last_name = db.Column(db.String(100), unique=False, nullable=False)

  def __init__(self, auid, first_name, last_name):
    self.first_name = first_name
    self.last_name = last_name
    self.auid = auid

db.create_all()

@app.route('/admin/<auid>', methods=['GET'])
def get_user(auid):
  user = Admin.query.get(auid)
  del user.__dict__['_sa_instance_state']
  return jsonify(user.__dict__)

@app.route('/admins', methods=['GET'])
def get_users():
  users = []
  for item in db.session.query(Admin).all():
    del item.__dict__['_sa_instance_state']
    users.append(item.__dict__)
  return jsonify(users)

@app.route('/admins', methods=['POST'])
def create_user():
  auid = uuid.uuid4().hex[:8] 
  body = request.get_json()
  db.session.add(Admin(auid, body['first_name'], body['last_name']))
  db.session.commit()
  return "Admin user created"

@app.route('/admins/<auid>', methods=['PUT'])
def update_user(auid):
  body = request.get_json()
  db.session.query(Admin).filter_by(auid=auid).update(dict(first_name=body['first_name'], last_name=body['last_name'], auid=body['auid']))
  db.session.commit()
  return "Admin user updated"


#################################################################
# STUDENTS
#################################################################

class Student(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  suid = db.Column(db.String(8), unique=True, nullable=False)
  first_name = db.Column(db.String(100), unique=False, nullable=False)
  last_name = db.Column(db.String(100), unique=False, nullable=False)
  time_status = df.Column(db.String(4), unique=False, nullable=False)
  nationality = db.Column(db.String(100), unique=False, nullable=False)
  gender = db.Column(db.String(100), unique=False, nullable=False)
  phone_number = db.column(db.String(30), unique=False, nullable=False)

  def __init__(self, suid, first_name, last_name, time_status, nationality, gender, phone_number):
    self.first_name = first_name
    self.last_name = last_name
    self.time_status = time_status
    self.nationality = nationality
    self.gender = gender
    self.phone_number = phone_number
    self.suid = suid
    
db.create_all()

@app.route('/student/<suid>', methods=['GET'])
def get_student_user(suid):
  user = Student.query.get(suid)
  del user.__dict__['_sa_instance_state']
  return jsonify(user.__dict__)

@app.route('/students', methods=['GET'])
def get_student_users():
  users = []
  for item in db.session.query(Student).all():
    del item.__dict__['_sa_instance_state']
    users.append(item.__dict__)
  return jsonify(users)

@app.route('/students', methods=['POST'])
def create_student_user():
  suid = uuid.uuid4().hex[:8] 
  body = request.get_json()
  db.session.add(Student(suid, body['first_name'], body['last_name'], body['time_status'], body['nationality'], body['gender'], body['phone_number']))
  db.session.commit()
  return "Student user created"

@app.route('/students/<suid>', methods=['PUT'])
def update_student_user(suid):
  body = request.get_json()
  db.session.query(Student).filter_by(suid=suid).update(dict(suid=suid, first_name=body['first_name'], last_name=body['last_name'], time_status=body['time_status'], nationality=body['nationality'], gender=body['gender'], phone_number=body['phone_number']))
  db.session.commit()
  return "Student user updated"

# ##############################################################################
# # classes
# ##############################################################################
# class StudentClass(db.Model):
  # id = db.Column(db.Integer, primary_key=True)
  # suid = db.Column(db.Integer, unique=False, nullable=False)
  # cid = db.Column(db.Integer, unique=False, nullable=False)
  # year = db.Column(db.Integer, unique=False, nullable=False)
  # semester = db.column(db.String(15), unique=False, nullable=False)

  # def __init__(self, suid, cid, year, semester):
    # self.suid = suid
    # self.cid = cid
    # self.year = year
    # self.semester = semester
    
# db.create_all()

# @app.route('/student/<suid>/classes', methods=['POST'])
# def create_student_class_user(suid):
  # body = request.get_json()
  
  # exists = db.session.query(Student.suid).filter_by(suid=suid).first() is not None
  # if not exists:
    # return "Student suid does not exist"
  
  # db.session.add(Student(body['first_name'], body['last_name'], body['status']))
  # db.session.commit()
  # return "User created"
  
  
  
# class Class(db.Model):
  # cid = db.Column(db.Integer, unique=False, nullable=False)
  # year = db.Column(db.Integer, unique=False, nullable=False)
  # semester = db.column(db.String(15), unique=False, nullable=False)

  # def __init__(self, id, cid, year, semester):
    # self.id = id
    # self.cid = cid
    # self.year = year
    # self.semester = semester
    
# db.create_all()