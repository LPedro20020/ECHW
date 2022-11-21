# ECHW

Extra Credit Python HW Attempt

INSTRUCTIONS:
Write a series of Python classes to model students, professors, course, classes, and majors. Implement as many of the magic methods as make sense for your model. Submit a git repo with a readme describing how to use your classes.
I will leave the specifics up to you but you should implement things like add/drop class, get_advisor/advisee, course requirements, major requirements.

Note that a class is a specific term offering of a course which is a more general description.

The standard for 10% extra credit would be a barebones model with a readme ~100-150 lines of code. 20% would include a full demo and documentation ~500+ lines of code.
____________________________________________________

CLASSES INSTRUCTIONS:
There are a total of five classes in this file: Students, Courses, Classes, Professors, and Majors.
Each is pretty self explanatory, but here are some basic instructions.

Students:
    The purpose of this class is to create objects as student profiles. These can be used to check enrolled classes and edit said list. It is just a tool for very basic information.

    To create a student profile, one must call 

        Student(name, year, enrolledClasses)

    ***NOTE: the enrolled classes list must be initialized separately before entered as a parameter. Just create a simple list 

        list = []

    Then assign it to a variable. and insert that into the parameter for pretty looking code. 

    The list can be empty, as it can be edited through the class. ***

    This will initialize a basic student profile to be accessed and edited. This class is first in the code so that it can be accessed by other classes. Schools center around students, it is only logical this code should too. 

    The class is intended to have the following methods: getAdvisor, declareMajor, getMajor, getEnrolledClassList, addCourse, dropCourse. 

    Each method should be pretty straightforward in stating what it does. 

Courses:
    The courses class is meant to create course objects to make a dictionary of currently offered courses and another of their requirements.

    The two methods in this class are: getCurrentCourses and getCourseReqs. 

    getCurrentCourses takes in the year parameter to use it as a key and return a list of what courses have and are offered each year. 

    getCourseReqs takes in a course name as a parameter and uses it as a key to return a list of it's requisites. 

Classes:
    The classes class is meant to create class objects to make dictionaries with them.

    The methods in this class are: available, classCap, and clasStu. 

    available takes in the parameter of term which returns a lis of the classes available during a specific term. 

    These classes are not to be confused with courses. Courses describe the general subject and level while classes describe the specific focus that is being taken by a specific section. For example, SPANISH 230 is a course. It has the classes A to D, so a class of SPAN 230 can be SPAN 230B. 

    The difference in courses and classes is subtle but important, which is why I thought that the best way to effectively differentiate them was to give them both their own class. 

    classCap takes in the name of a class as a parameter, using it to extract the maximum number of students allowed and returning how many of those seats have been filled. 

    clasStu takes in a class name as a parameter to use it as a key in a dictionary to return a list of the students registered for the class. 

Professors:
    This class is intended to create a profile for professors in a similar regard to students. It is meant to show who their advisees are, what classes they teach, and what their student rosters are.

    The ethods in this class include: getAdvisee, classInstructed, and getRoster. 

    getAdvisee does exactly that, takes in the name of a professor and shows the list of advisees they have. 

    classInstructed takes in the name of a professor and returns a list of classes that they currently teach. 

    getRoster takes in the name of a profesor and returns a list of students that they are currently instructing. 

Majors:
    This class is meant to build objects for majors. And by extension, a simple profile of them.

    The methods in this class are majorInfo and majorReqs. 

    majorInfo takes in the name of a major and uses it as a key in a dictionary to return the description of the course. 

    majorReqs takes in the name of a major and returns a list of requiremnts for taking and passing the course.
