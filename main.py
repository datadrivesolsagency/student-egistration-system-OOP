print("******************************************************Welcome to Student Registration System*****************************************************")

class People:
    def __init__(self, name, surname, number):
        self.name = name
        self.surname = surname
        self.number = number

p1 = People(input("Enter your name: "), input("Enter your surename: "), input("YOUr contact Info"))
print(p1.name)
print(p1.surname)
print(p1.number)
print("***********************************Detail of Student**********************************")
class Student(People):
    def __init__(self, id, course,semester, majors, *args, **kwargs):
        self.id = id
        #self.student_type = student_type
        self.course= course
        self.semester = semester
        self.majors = majors

    def login(self):
        return f"the {self.id} can log in by using id of {self.id}"
    
    def courses(self):
        return f"{self.id} is registered in {self.course}"
    
    def term(self):
        return f" Department of {self.course} consisting of {self.semester}"
    
    def major(self):
        return f"{self.id} is enrolled {self.course} so planning to have majors in {self.majors}"
    
stud = Student(input('Enter student Id: '),input("Enter the Name of Course: "), input("Semester: "), input("Majors:"))
print(stud.login())
print(stud.courses())
print(stud.term())
print(stud.major())
print("\n***********************************************Course Registration*****************************************\n")


class courses():
    def __init__(self,course_id1,course_id2,course_id3,course_id4,course_name1,course_name2,course_name3,course_name4,credits,*args, **kwargs):
        self.course_name1 = course_name1
        self.courses_id1 = course_id1
        self.course_name2 = course_name2
        self.courses_id2 = course_id2
        self.course_name3 = course_name3
        self.courses_id4 = course_id3
        self.course_name4 = course_name4
        self.courses_id4 = course_id4
        self.credit_hours = credits
        
           
    def getcourseid(self):
        print("The id for",self.course_name1 ,"is", self.courses_id1)
        
    def setcourseid(self):
        return f"Course Id for {self.course_name2} is {self.courses_id2}"
    
    def getcoursename(self):
        print("The course name of", self.courses_id3 ,"is", self.course_nam3e)
    
    def setcoursename(self):
        return f"The course name for course id {self.courses_id4} is {self.course_name4}"


course = courses(input("Enter Course Number one: "), int(input("Enter its course code: ")),input("Enter Course Number Two: "), int(input("Enter its course code: ")),input("Enter Course Number Three: "), int(input("Enter its course code: ")),input("Enter Course Number Four: "), int(input("Enter its course code: ")), int(input("Please Enter no. of credit hours: ")))
print(course.setcoursename())
print(course.getcourseid())
print(course.setcourseid())
print(course.credit_hours)
print("**************************************************Advisor Allocation****************************************")
class Advisor(People):     
    def __init__(self, name, department, faculty_name):
        super().__init__(name,  department, faculty_name)
        self.name = name
        self.department = department
        self.faculty_name = faculty_name
    def advisor_assigned(self):
        return f"{self.name} is assigned with {self.faculty_name} for consultation"

adv = Advisor(input("Enter the name of student: ") ,input("Enter departmentt: "), "Mr. Joseph Warren")
print(adv.advisor_assigned())
print("*********************************************************COllege Details*************************************")
class college:
    def __init__(self, id, department, college_name, year):
        self.id = id
        self.department = department
        self.college_name = college_name
        self.year = year
        

    def get_admission_in_college(self):
        print(self.id, "is got select in", {self.college_name}, "for the year", {self.year}, "in the department of", {self.department})
        
        
colg = college(input("Re-enter your student Id: "), input("Re-enter your department"),"Zayed University",input("Enter Academic Year: "))
print(colg.get_admission_in_college())        

print("---------------------------------------Registration Process is completed---------------------------------------")
