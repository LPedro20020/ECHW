#Students
class Student:
    #to create student profile, must name student, the current year, and create a list of classes already enrolled
    #list must be created separately before the student object. It can be an empty list.
    #List can then be assigned to a variable, which would be what is inputted as a parameter here
    def __init__(self, name, year, enrolledClasses):
        self.name = name
        self.year = year
        self.enrolledClasses = enrolledClasses

    def __repr__(self):
        return (f'Student({self.name})')
    
#Get Student Info
    #Get Advisor
    @classmethod
    def getAdvisor(cls, stu):
        #Insert Student and advisor data. Must be entered individually 
        #in this version
        advisorStuPairList = {"Student1":"Advisor1"}
        return advisorStuPairList[str(stu)]


#NOTE: I am using dictionaries for most of my methods for quick 
#and easy retrieval of information with keys. Figuring out how to
#utilize objects in said dictionaries.
#Dictionaries consist of placeholders for now, of an example of an entry
#Thought about making it knox specific but I don't know the laws
#about copying and pasting course descriptions and typing names in
#But makes this generic for any "school" aplication

    #Placeholder fot a possible Declare Major Method?
    
    #Get Major
    @classmethod
    def getMajor(cls, stud):
        #Insert Student and Major Data here.
        #With a declare method, it could be possible to edit this list.
        #Would require this to become a static method
        #Might have to move the list to __init__
        stuMajorPairList = {"Student1":"Major1"}
        return stuMajorPairList[str(stud)]
    
    #Get Enrolled Classes
    #Might need to move these to __init__
    #Would allow editing with add/drop methods
    #However would require individual lists to be made 
    #before student object initialization
    #and this would need to be a static method
    #I would move the if conditionals to the add drop methods though
    @classmethod
    def getEnrolledClassList(cls, stude, term):
        if term == "Fall":
            fallStuClassList = {"Stu1":"Classes1"}
            return fallStuClassList[str(stude, term)]
        elif term == "Winter":
            winterStuClassList = {"Stu1":"Classes1"}
            return winterStuClassList[str(stude, term)]
        elif term == "Spring":
            springStuClassList = {"Stu1":"Classes1"}
            return springStuClassList[str(stude, term)]    

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
class Courses(Student):
    def __init__(self, cours):
        self.name = cours

#Get Offered courses
    @classmethod
    def getCurrentCourses(cls, year):
        courseList = {"year":"Courses offered"}
        return courseList[str(year)]

#Get Course Requirements, Prereqs
    @classmethod
    def getCourseReqs(cls, course):
        courseListA = {"course1":"course reqs1"}
        return courseListA[str(course)]


#Classes
class Classes:
    def __init__(self, name):
        self.name = name

#Get Available term Classes  
    @classmethod
    def available(cls, term):
        classList = {"term":"classes"}
        return classList[str(term)]

#Get Class capacity and seats filled
    @classmethod
    def classCap(cls, class4Cap):
        classListA = {"class":"student capacity and seats filled"}
        return classListA[str(class4Cap)]

#Get Class student list
    @classmethod
    def clasStu(cls, clas1):
        clasStu = {"Class":"Student roster"}
        return clasStu[str(clas1)]


#Professors
class Professors(Classes):
    def __init__(self, name):
        self.name = name

#Get Professor's Advisee
    @classmethod
    def getAdvisee(cls, advi):
        adviProfPairList = {"1":"Africana Studies", "2":"American Studies", "3":"Anthropology & Sociology"}
        return adviProfPairList[str(advi)]

#Get roster of a specific class
    @classmethod
    def getRoster(cls, roster):
        classListR = {"1":"Africana Studies", "2":"American Studies", "3":"Anthropology & Sociology"}
        return classListR[str(roster)]


#Majors
class Majors:
    def __init__(self, major1):
        self.major = major1

#Get Major Description
    @classmethod    
    def majorInfo(cls, major):
        mj = {"1":"Africana Studies", "2":"American Studies", "3":"Anthropology & Sociology"}
        return mj[str(major)]
    
#Get Major Requirements
    @classmethod
    def majorReqs(cls, major2):
        reqList = {"1":"Africana Studies", "2":"American Studies", "3":"Anthropology & Sociology"}
        return reqList[str(major2)]
    
