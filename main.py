#Students
class Student:
    #to create student profile, must name student, the current year, and create a list of classes already enrolled
    #list must be created separately before the student object. It can be an empty list.
    #List can then be assigned to a variable, which would be what is inputted as a parameter here
    def __init__(self, name, year, enrolledClasses):
        self.name = name
        self.year = year
        self.enrolledClasses = enrolledClasses
    
#Get Student Info
    #Get Advisor
    def getAdvisor(cls):
        #Insert Student and advisor data. Must be entered individually 
        #in this version
        advisorStuPairList = {"Student1":"Advisor1", "bobert":"success:)"}
        print(advisorStuPairList[cls.name])


#NOTE: I am using dictionaries for most of my methods for quick 
#and easy retrieval of information with keys. Figuring out how to
#utilize objects in said dictionaries.
#Dictionaries consist of placeholders for now, of an example of an entry
#Thought about making it knox specific but I don't know the laws
#about copying and pasting course descriptions and typing names in
#But makes this generic for any "school" aplication

    #Placeholder fot a possible Declare Major Method?
    
    #Get Major
    def getMajor(cls):
        #Insert Student and Major Data here.
        #With a declare method, it could be possible to edit this list.
        #Would require this to become a static method
        #Might have to move the list to __init__
        stuMajorPairList = {"Student1":"Major1", "bobert":"getmayor is good"}
        print(stuMajorPairList[cls.name])
    
    #Get Enrolled Classes
    #Might need to move these to __init__
    #Would allow editing with add/drop methods
    #However would require individual lists to be made 
    #before student object initialization
    #and this would need to be a static method
    #I would move the if conditionals to the add drop methods though

    def getEnrolledClassList(cls, term):
        if term == "Fall":
            fallStuClassList = {"Stu1":"Classes1","bobert":"fall is a go"}
            print(fallStuClassList[str(cls.name)])
        elif term == "Winter":
            winterStuClassList = {"Stu1":"Classes1"}
            print(winterStuClassList[str(cls.name)])
        elif term == "Spring":
            springStuClassList = {"Stu1":"Classes1"}
            print(springStuClassList[str(cls.name)])    

#Add drop functions are meant to edit list of enrolled courses
#which was created at student object creation  
  
#Add courses
    def addCourse(self, clase):
        #clase is the course intending to enroll in
        self.enrolledClasses.append(clase)
    
#Drop courses
    def dropCourse(self, classe):
        #classe is the class attempting to drop
        self.enrolledClasses.remove(classe)
    

#Courses
class Courses:
    def __init__(self, cours):
        self.name = str(cours)

#Get Offered courses
    @classmethod
    def getCurrentCourses(cls, year):
        courseList = {"year":"Courses offered", "2022":"Check the catalog"}
        return courseList[str(year)]

#Get Course Requirements, Prereqs
    @classmethod
    def getCourseReqs(cls, course):
        courseListA = {"course1":"course reqs1"}
        return courseListA[str(course)]


#Classes
class Classes(Student):
    def __init__(self, name):
        self.name = str(name)

#Get Available term Classes  
    
    def available(term):
        classList = {"term":"classes"}
        print(classList[term])

#Get Class capacity and seats filled
    @classmethod
    def classCap(cls, class4Cap):
        classListA = {"class":"student capacity and seats filled"}
        print(classListA[str(class4Cap)])

#Get Class student list
    @classmethod
    def clasStu(cls, clas1):
        clasStu = {"Class":"Student roster"}
        print(clasStu[str(clas1)])


#Professors
class Professors(Classes, Student):
    def __init__(self, name, classT):
        self.name = str(name)
        self.classT = str(classT)

#Get Professor's Advisee
    @classmethod
    def getAdvisee(cls, prof):
        adviProfPairList = {"Advisor1":"Students"}
        print(adviProfPairList[str(prof)])

#list of classes they currently teach
    @classmethod
    def classInstructed(cls, proff):
        profClassList = {"Professor1":"Classes Taught"}
        print(profClassList[str(proff)])


#Get roster of a specific class
    @classmethod
    def getRoster(cls, profe):
        classListR = {"Professor1":"Students1"}
        print(classListR[str(profe)])


#Majors
class Majors:
    def __init__(self, major1):
        self.major = str(major1)

#Get Major Description
    @classmethod    
    def majorInfo(cls, major):
        mj = {"Course":"Course Descriptions"}
        print(mj[str(major)])
    
#Get Major Requirements
#INSERT data from any school in the dictionary. 
    @classmethod
    def majorReqs(cls, major2):
        reqList = {"major":"reqlist"}
        print(reqList[str(major2)])
    

def main():
    #EXAMPLES HERE
    print("hello world!")
    
    #Student Object Test
    enrolledClasses1 = []
    bob = Student("bobert", 2022, enrolledClasses1)
    bob.getAdvisor()
    bob.getMajor()
    bob.getEnrolledClassList("Fall")
    bob.addCourse("Bio")
    print(enrolledClasses1)
    bob.addCourse("potions")
    print(enrolledClasses1)
    bob.dropCourse("Bio")
    print(enrolledClasses1)
    
    #Courses Object Test
    Courses.getCurrentCourses(2022)
    Courses.getCourseReqs("course1")
    
    #Classes Object Test
    Classes.available("term")
    Classes.classCap("class")
    Classes.clasStu("Class")
    
    #Professors Object Test
    Professors.getAdvisee("Advisor1")
    Professors.classInstructed("Professor1")
    Professors.getRoster("Professor1")
    
    #Majors Object Test
    Majors.majorInfo("Course")
    Majors.majorReqs("major")
    
    #Objects Succesful
    #The next step in this project would be to use the inheritance I have set 
    #up between these classes to have classes call eachother. For example, my getRoster method. 
    #It would be set up to parse the student registered classes list to to see what students are registered for the professors classes.
    #This could expand on the detail in each dictionary as well, as the courses lists could have what professor teaches it.
    #This would make it a very dynamic set of classes that could be applied to any school and stay on top of all the changes that happen in them. 


main()