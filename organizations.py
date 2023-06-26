from .users import *
import csv
import os.path

class School:
	def __init__(self, name=None, address=None, phone=None, email="",
	num_stud=None, num_teachers=None):
		self.name = name
		self.address = address
		self.phone = phone
		self.email = email
		self.num_stud = num_stud
		self.num_teachers = num_teachers
		self.list_of_students = []
		self.list_of_teachers = []
		if os.path.exists(f"{self.name} report.csv"):
			with open(f"{self.name} report.csv", "r",
			newline = "", encoding = "UTF-8") as ofile:
				reader=list(csv.reader(ofile))
				self.name,self.address,self.phone,self.email,self.num_stud,self.num_teachers=reader[0]
				self.num_stud = int(self.num_stud)
				self.num_teachers = int(self.num_teachers)
				try:
					for row in range(1,self.num_stud+1):
						self.list_of_students.append(Student(name=reader[row][0],
						familyname=reader[row][1], age=reader[row][2], 
						gender=reader[row][3], nationality=reader[row][4], 
						school=self.name))
				except:
					self.set_num_stud(0)
				
				try:
					for row in range(self.num_stud+1,
					self.num_stud+self.num_teachers+1):
						self.list_of_teachers.append(Teacher(name=reader[row][0],
						familyname=reader[row][1], age=reader[row][2], 
						gender=reader[row][3], nationality=reader[row][4], 
						school=self.name, subject=reader[row][5]))
				except:
					self.set_num_teachers(0)
				

	def set_name(self, name):
		self.name = name

	def set_address(self, address):
		self.address = address

	def set_phone(self, phone):
		self.phone = phone

	def set_email(self, email):
		self.email = email

	def set_num_stud(self, num_stud):
		self.num_stud = num_stud

	def set_num_teachers(self, num_teachers):
		self.num_teachers = num_teachers

	def add_student(self, name=None, familyname=None, age=None,
	gender=None, nationality=None):
		if len(self.list_of_students)==0:
			self.set_num_stud(0)
		
		s1=Student(name=name,
		familyname=familyname, age=age, gender=gender, 
		nationality=nationality, school=self.name)
		
		
		if self.num_stud>0:
			print(self.list_of_students)
			for s in self.list_of_students:
				d1=s1.get_info()
				d=s.get_info()
				if d["name"]==d1["name"] and d["familyname"]==d1["familyname"]:
					return
		
		self.list_of_students.append(s1)
		self.set_num_stud(len(self.list_of_students))

	def add_teacher(self, name=None, familyname=None, age=None,
	gender=None, nationality=None, subject=None):
		if len(self.list_of_teachers)==0:
			self.set_num_teachers(0)
		
		t1=Teacher(name=name,
		familyname=familyname, age=age, gender=gender, 
		nationality=nationality, school=self.name, subject=subject)
		
		if self.num_teachers>0:
			for t in self.list_of_teachers:
				d1=t1.get_info()
				d=t.get_info()
				if d["name"]==d1["name"] and d["familyname"]==d1["familyname"]:
					return
		
		self.list_of_teachers.append(t1)
		self.set_num_teachers(len(self.list_of_teachers))

	def get_info(self):
		return {'name':self.name,
				'address':self.address,
				'phone':self.phone,
				'email':self.email,
				'num_stud':self.num_stud,
				'num_teachers':self.num_teachers}

	def get_report(self):
		with open(f"{self.name} report.csv", "w",
		newline = "", encoding = "UTF-8") as ofile:
			writer=csv.writer(ofile)
			writer.writerow(self.get_info().values())
			for row in range(len(self.list_of_students)):
				writer.writerow(self.list_of_students[row].get_info().values())
			
			for row in range(len(self.list_of_teachers)):
				writer.writerow(self.list_of_teachers[row].get_info().values())
