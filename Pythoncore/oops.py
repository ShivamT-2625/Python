# nums = [7,9,3,5,0]

# def solution(nums):
#     if not nums:
#         return None
#     nums_sorted = sorted(nums)
#     return nums_sorted[-2]
# print(solution(nums))


# class Student :
#     name = "karan kumar"
# s1= Student()
# print(s1)
# print(s1.name)

                    ####
#constructor 
# __init__ function

class Student:
    #default constructor
    def __init__(self):
        pass
    #parameterized constructor
    def __init__(self,fullname,marks):
        self.name=fullname
        self.marks=marks
        print(f"Adding {fullname} student in {marks} database")
s1 = Student("Shivam",97)
#output = Adding new student in database

#self is reference to the object 

s2 = Student("Arjun",94)


                                    ####
# Class and Instance Attribute

# Class.attr
# obj.attr

class Modi:
    college_name ="Abc"
    def __init__(self,name):
        self.name=name
        print(name)
    def welcome(self):
        print("welcome students",self.name)
s3=Modi("Shivam")
print(s3.college_name)
s3.welcome()


#same name ka class attribute and object attribute , then object attribute is given preference



class Students:
    def __init__(self,physics,chemistry,maths):
        self.physics=physics
        self.maths=maths
        self.chemistry=chemistry
        print(f"Here are the marks:{physics},{chemistry},{maths}")
        
    @staticmethod
    def hello():
        print("Hello")
    def find_avg(self):
        sum = self.physics +self.maths+ self.chemistry
        avg = sum / 3
        print("Average is ",avg)
s4 = Students(45,46,48)
s4.find_avg() 



class Account:
    def __init__(self,account_no , balance):
        self.account=account_no
        self.balance=balance

    def debit(self):
        self.balance -= 1
        return f"Balance reduced to {self.balance} on {self.account}"
    def credit(self):
        self.balance += 1
        return f"Credited money on {self.account}"
    def check_balance(self):
        return self.balance

s5 = Account(12006,506)
print(s5.debit())
print(s5.credit())
print(s5.check_balance())
        