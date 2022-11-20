#Students
class Student:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return (f'Student({self.name})')
    
#Get Student Info
    #Get Advisor
    @classmethod
    def getAdvisor(stu):
        advisorStuPairList = {"1":"Africana Studies", "2":"American Studies", "3":"Anthropology & Sociology"}
        return advisorStuPairList[str(stu)]

    #Get Major
    @classmethod
    def getMajor(cls, stud):
        stuMajorPairList = {"1":"Africana Studies", "2":"American Studies", "3":"Anthropology & Sociology"}
        return stuMajorPairList[str(stud)]
    
    #Get Enrolled Classes
    @classmethod
    def enrolledClassList(cls, stude, term):
        stuClassList = {"Fall":"Classes"}
        return stuClassList[str(stude, term)]
    
    
#Add courses
    @classmethod
    def addCourse(cls, clase):
        stuClassList = ["nose"]
        return stuClassList[str(clase)]
    
    
#Drop courses
    @classmethod
    def dropCourse(classe):
        stuClassListA = ["nose"]
        return stuClassListA[str(classe)]


#Professors
class Professors:
    def __init__(self, name):
        self.name = name

#Get Professor's Advisee
    @classmethod
    def getAdvisee(advi):
        adviProfPairList = {"1":"Africana Studies", "2":"American Studies", "3":"Anthropology & Sociology"}
        return adviProfPairList[str(advi)]

#Get roster of a specific class
    @classmethod
    def getRoster(roster):
        classListR = {"1":"Africana Studies", "2":"American Studies", "3":"Anthropology & Sociology"}
        return classListR[str(roster)]
    

#Courses
class Courses:
    def __init__(self, name):
        self.name = name

#Get Offered courses
    @classmethod
    def getCurrentCourses(year):
        courseList = {"1":"Africana Studies", "2":"American Studies", "3":"Anthropology & Sociology"}
        return courseList[str(year)]

#Get Course Requirements, Prereqs
    @classmethod
    def getCourseReqs(course):
        courseListA = {"1":"Africana Studies", "2":"American Studies", "3":"Anthropology & Sociology"}
        return courseListA[str(course)]


#Classes
class Classes:
    def __init__(self, name):
        self.name = name

#Get Available term Classes  
    @classmethod
    def available(term):
        classList = {"1":"Africana Studies", "2":"American Studies", "3":"Anthropology & Sociology"}
        return classList[str(term)]

#Get Class capacity and seats filled
    @classmethod
    def classCap(class4Cap):
        classListA = {"1":"Africana Studies", "2":"American Studies", "3":"Anthropology & Sociology"}
        return classListA[str(class4Cap)]

#Get Class student list
    @classmethod
    def clasStu(clas1):
        clasStu = {"1":"Africana Studies", "2":"American Studies", "3":"Anthropology & Sociology"}
        return clasStu[str(clas1)]


#Majors
class Majors:
    def __init__(self, major1):
        self.major = major1

#Get Major Description
    @classmethod    
    def majorInfo(major):
        mj = {"1":"Africana Studies", "2":"American Studies", "3":"Anthropology & Sociology"}
        return mj[str(major)]
    
#Get Major Requirements
    @classmethod
    def majorReqs(major2):
        reqList = {"1":"Africana Studies", "2":"American Studies", "3":"Anthropology & Sociology"}
        return reqList[str(major2)]