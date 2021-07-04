
#CLASSES




#class MyNewClass():
#    '''my new class is class name'''
#    pass
#a = MyNewClass()
#print(a.__doc__)



class MyNewClass():   #class has inbuilt objects, eg; init

    '''my new class is class name'''
    b = 20
    def __init__(self):
        a = 10
        print(a)
        print(self.b)
        self.b = 15
        
    def hello(self, v):
        print(v)
        print(self.b)
        
'''y = MyNewClass()
print(y.b)
print(MyNewClass.b)
'''
'''
z = MyNewClass()
z.hello(6)
z.b = 50
z.hello(8)
'''


#INHERITANCE


#Single Inheritance:

'''
class Welcome(MyNewClass):   #MyNewClass-parent class, Welcome- child class
    def __init__(self):
        print(self.b)

    def hello(self, v):
        print(v+1)
        print(self.b+1)
        
x = Welcome()
x.hello(5)    # method overriding  #Child Class, Sub class  




class Welcome(MyNewClass):   
    def __init__(self):
        print(self.b)

    def hello(self, v):
        print(v+1)
        print(self.b+1)
        return super().hello(v)
        
x = Welcome()
x.hello(5)    


#Multilevel Inheritance


class good(Welcome):
    def __init__(self):
        print(self.b)
y= good()


#Multiple Inheritance

class K():
    p = 7
    pass

class New(MyNewClass,K):
    def __init__(self):
        print(self.b)
        print(self.p)
m = New()


#Hierarchical Inheritance


class hier(K):      #Hier class is the child of K Class
    pass


class NewHier(K):   #NewHier class is the child of K Class
    pass


'''


#Hybrid Inheritance

'''
class A:
    q = 5


class B(A):
    pass


class C(A):
    pass


class D(B,C):
    pass


z = D()
print(z.q)
'''


#EXAMPLEeeeee


class ClassRoom:
    class_name = "TEN"
    class_teacher = "ALOK"
    is_digital = True

class Student1(ClassRoom):
    student_name = "SOOREJ"
    student_id = 123

class Student2(ClassRoom):
    student_name = "SURYA"
    student_id = 321

x = Student1()
print(x.class_name)
