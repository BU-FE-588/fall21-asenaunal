#!/usr/bin/env python
# coding: utf-8

# # Homework 3 and 4 due November December 21$^{st}$, 2021
# 
# The aim of this homework is to practice the concepts of objects and numpy module in Python. You are expected to use GitHub Classroom and present your work as an html file (i.e. web page) on your progress journals. You can use this jupyter notebook as template to provide your answers.
# 
# 
# ## Object-oriented programming concepts
# Tasks 1-6 require the definition of objects with init and sample uses to check if classes is defined as intented.

# ### Task 1
# Implement a Python program to create a course class with the course code, course name, credit information. Use this class to create a course object for FE588 and print instance attributes. Also check which class a given course object belongs to.
# 
# Hint: A sample template to create an object from this class can be as the following:
# 
# my_course=course('FE588', 'Python Programming for Financial Engineering')

# In[2]:


class Course:
    def __init__(self,course_code='',course_name='',credit_info=0):
        self.course_code=course_code
        self.course_name=course_name
        self.credit_info=credit_info
    def print_atributes(self):
        print(f'course_code : {self.course_code}')
        print(f'course_name : {self.course_name}')
        print(f'credit_info : {self.credit_info}')
    

my_course=Course('FE588', 'Python Programming for Financial Engineering',10)      
my_course.print_atributes()


# ### Task 2
# This part requires to create a student object with the name, id and grade attributes. You can assume name is string, id is an integer variable and grade is a list that can store multiple grades. 
# 
# Hint: A sample template to create an object from this class can be as the following:
# 
# mustafa=student('Mustafa', 123, grades=None)  
# or   
# mustafa=student('Mustafa', 123, grades=[85, 70, 100]) 

# In[3]:


class Student:
    def __init__(self,name='',student_id=0,grades=None):
        self.name=name
        self.grades=grades
        self.student_id=student_id
    def print_atributes(self):
        print(f'name : {self.name}')
        print(f'student_id : {self.student_id}')
        print(f'grades : {self.grades}')
    

mustafa=Student('Mustafa', 123, grades=None)  
mustafa.print_atributes()
mustafa=Student('Mustafa', 123, grades=[85, 70, 100]) 
mustafa.print_atributes()


# ### Task 3
# Let's modify the course class so that it can store the information of students as a list of student objects. 
# 
# Hint: A sample template to create an object from this class can be as the following:
# 
# mustafa=student('Mustafa', 123, grades=None)  
# ahmet=student('Ahmet', 124, grades=[90, 95, 87])  
# my_course=course('FE588', 'Python Programming for Financial Engineering', students=[mustafa, ahmet])

# In[4]:


class Course:
    def __init__(self,course_code='',course_name='',credit_info=0,students=None):
        self.course_code=course_code
        self.course_name=course_name
        self.credit_info=credit_info
        self.students=students
    def print_atributes(self):
        print(f'course_code : {self.course_code}')
        print(f'course_name : {self.course_name}')
        print(f'credit_info : {self.credit_info}')
        print(f'students : {[student.student_id for student in self.students]}')
    
my_course=Course('FE588', 'Python Programming for Financial Engineering',10)      

mustafa=Student('Mustafa', 123, grades=None)  
ahmet=Student('Ahmet', 124, grades=[90, 95, 87])  
my_course=Course('FE588', 'Python Programming for Financial Engineering', students=[mustafa, ahmet])

my_course.print_atributes()


# ### Task 4
# Implement a method for course object so that you can append new students to the roster.

# In[5]:


class Course:
    def __init__(self,course_code='',course_name='',credit_info=0,students=None):
        self.course_code=course_code
        self.course_name=course_name
        self.credit_info=credit_info
        self.students=students if students!=None else []
    def print_atributes(self):
        print(f'course_code : {self.course_code}')
        print(f'course_name : {self.course_name}')
        print(f'credit_info : {self.credit_info}')
        print(f'students : {[student.student_id for student in self.students]}')
    def add_student(self,student):
        self.students.append(student)
        return True
my_course=Course('FE588', 'Python Programming for Financial Engineering',10)      
my_course.add_student(Student('Ahmet', 124, grades=[90, 95, 87])  )
my_course.print_atributes()


# ### Task 5
# Implement a method for course object that you can calculate the average of the grades for each student. Print the averages for the students you have created in Task 3.

# In[6]:


class Course:
    def __init__(self,course_code='',course_name='',credit_info=0,students=None):
        self.course_code=course_code
        self.course_name=course_name
        self.credit_info=credit_info
        self.students=students if students!=None else []
    def print_atributes(self):
        print(f'course_code : {self.course_code}')
        print(f'course_name : {self.course_name}')
        print(f'credit_info : {self.credit_info}')
        print(f'students : {[student.student_id for student in self.students]}')
    def add_student(self,student):
        self.students.append(student)
        return True
    def calculate_average_grade(self):
        for student in self.students:
            print(f'student_name: {student.name}')
            print(f'student_average_grade: {sum(student.grades)/len(student.grades)if (student.grades) else 0 :.2f}')

my_course=Course('FE588', 'Python Programming for Financial Engineering',10)      
my_course.add_student(Student('Ahmet', 124, grades=[90, 95, 87])  )
my_course.print_atributes()
my_course.calculate_average_grade()


# ### Task 6
# Implement a method for course object that you can find the student with maximum average grade and print the student's name and average grade.

# In[10]:


class Course:
   def __init__(self,course_code='',course_name='',credit_info=0,students=None):
       self.course_code=course_code
       self.course_name=course_name
       self.credit_info=credit_info
       self.students=students if students!=None else []
   def print_atributes(self):
       print(f'course_code : {self.course_code}')
       print(f'course_name : {self.course_name}')
       print(f'credit_info : {self.credit_info}')
       print(f'students : {[student.student_id for student in self.students]}')
   def add_student(self,student):
       self.students.append(student)
       return True
   def calculate_average_grade(self):
       for student in self.students:
           print(f'student_name: {student.name}')
           print(f'student_average_grade: {sum(student.grades)/len(student.grades)if (student.grades) else 0 :.2f}')
   def find_top_student(self):
       if not self.students:
           print('No Students')
           return False
       else:
           topstudent=(self.students[0],sum(self.students[0].grades)/len(self.students[0].grades)if (self.students[0].grades) else 0)
           for student in self.students[1:]:
               avg=sum(student.grades)/len(student.grades)if (student.grades) else 0 
               if avg>topstudent[1]:
                   topstudent=(student,avg)
           print(f'TopStudent!!: {topstudent[0].name} {topstudent[1] :.2f}')
           return True
           
my_course=Course('FE588', 'Python Programming for Financial Engineering',10)      
my_course.add_student(Student('Ahmet', 124, grades=[90, 95, 87])  )
my_course.add_student(Student('Mehmet', 124, grades=[91, 95, 87])  )
my_course.add_student(Student('Ali', 124, grades=[92, 95, 87])  )
my_course.add_student(Student('Asena', 124, grades=[93, 95, 87])  )




my_course.print_atributes()
my_course.calculate_average_grade()
my_course.find_top_student()


# ## Matrix manipulation on images
# In this exercise, you are requested to perform certain operations on images. The aim is to develop matrix manipulation skills.
# 
# Here is a background information about how a grayscale image is represented on our computers. A grayscale image is basically a matrix where each matrix entry shows the intensity (brightness) level. In other words, when you take a picture with a digital camera, the image is represented by a numerical matrix where the matrix size is defined by the resolution setting of your camera. If your resolution setting is 1280x720, then your image is represented by 1280x720= 921600 pixel values (Actually that is why higher resolution provides better quality pictures). When you have a color image, the image stores the information of multiple channels depending on the image type. The most famous one is RGB type where R, G and B stand for “red”, “green” and “blue” respectively. Hence, you have a matrix as in greyscale images representing the intensity for each channel. Combining these matrices generates the color image.
# 
# Below is the steps you need to follow for this task:
# - Take a picture of yours and save it as *.jpg or *.jpeg file.
# - Using an image editor (i.e. Paint in Windows), crop your head from the image and save it as separate image file (again *.jpg or *.jpeg). The resulting image is expected to be a square (i.e. has the same length and width), hence you should crop the image accordingly.
# - Resize the cropped image to size 512x512 px (pixel) using an image editor. This image is the one that you will use for this exercise.

# ### Task 7
# Read image as numpy array in Python. You can use matplotlib module. If your environment does not have this module, please install using 'pip install matplotlib'. You can use 'asarray' function from numpy to transform your image contents to numpy array.
# 
# What is the structure of the variable that stores the image? What is the dimension? Display the image. 
# 
# Hint: You can use the following set of scripts to read the image.   
# from matplotlib import image   
# from matplotlib import pyplot    
# from numpy import asarray
# 
# image = image.imread('your_image.jpg')  
# data = asarray(image)

# In[19]:


from PIL import Image
Img=Image.open('asena.jpg')
Img


# In[ ]:





# In[20]:


print("image store as : {}".format(type(data)))
print("array shape is : {}".format(data.shape))


# ### Task 8
# Display each channel as separate image

# In[23]:


G=Img[:,:,1]
plt.imshow(G)


# ### Task 9
# For each channel, calculate the average, maximum and minimum of the columns and store it in three variables using numpy methods defined for numpy objects. What is the structure of the variables storing the average, max and min information.
# 

# In[25]:


print("R max_min_avg shape {}".format(R_max_min_avg.shape))
R_max_min_avg


# ### Task 10
# For each channel, subtract one half of the image from the other half (choice of halves is up to you
# but dividing the head image vertically into two parts make more sense). If you observe negative pixel
# values, you can make them equal to zero. Then:
# - Display the new image.
# - Display each channel separately as separate image.

# In[30]:


contrast_image=Img[:,561:]- Img[:,:561]
plt.imshow(contrast_image)


# ### Tasks 11-12
# 
# In order to create a noisy image, add a random noise from normal distribution for alternative mean and standard deviation settings to each pixel value for each channel of original image. You can try $\mu \in \{5,10\}$ and $\sigma \in \{1,2\}$. So two types of noise are expected: mean=2 and st. dev=1, mean=10 and st.dev=2.
# - Display the new image.
# - Display each channel separately as separate image.

# In[ ]:




