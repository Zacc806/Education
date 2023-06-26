class Human:
	def __init__(self, name=None, familyname=None, age=None, gender=None, 
	nationality=None):
		self.name = name
		self.familyname = familyname
		self.age = age
		self.gender = gender
		self.nationality = nationality
	
	def set_name(self, name):
		self.name = name
	
	def set_familyname(self, familyname):
		self.familyname = familyname
		
	def set_age(self, age):
		self.age = age
	
	def set_gender(self, gender):
		self.gender = gender
		
	def set_nationality(self, nationality):
		self.nationality = nationality
		
	def get_info(self):
		return {'name':self.name,
				'familyname':self.familyname,
				'age':self.age,
				'gender':self.gender,
				'nationality':self.nationality}
			
class Student(Human):
	def __init__(self, name=None, familyname=None, age=None, gender=None,
	nationality=None, school=None, list_of_subjects=None):
		super().__init__(name=name, familyname=familyname, age=age, 
		gender=gender, nationality=nationality)
		self.school = school
		self.list_of_subjects = []
	
	def set_school(self, school):
		self.school = school
	
	def add_subject(self, subject):
		self.list_of_subjects.append(subject)
		
	def get_info(self):
		return {'name':self.name,
				'familyname':self.familyname,
				'age':self.age,
				'gender':self.gender,
				'nationality':self.nationality,
				'list of subjects':self.list_of_subjects}
				
	def get_name(self):
		return self.name
		
class Teacher(Human):
	def __init__(self, name=None, familyname=None, age=None, gender=None,
	nationality=None, school=None, subject=None):
		super().__init__(name=name, familyname=familyname, age=age,
		gender=gender, nationality=nationality)
		self.school = school
		self.subject = subject
	
	def set_school(self, school):
		self.school = school
	
	def add_subject(self, subject):
		self.subject = subject
		
	def get_info(self):
		return {'name':self.name,
				'familyname':self.familyname,
				'age':self.age,
				'gender':self.gender,
				'nationality':self.nationality,
				'subject':self.subject}
	def get_name(self):
		return self.name
