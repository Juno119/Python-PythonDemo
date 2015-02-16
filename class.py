__author__ = 'YiTao'
#coding=utf-8

class Employee:
    '自定义类'
    empCount = 0
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
        Employee.empCount+=1

    def __del__(self):
        class_name=self.__class__
        print("%s destroyed" % class_name)

    def displayCount(self):
        print("Total Employee %d" % Employee.empCount)

    def displayEmployee(self):
        print("Name:%s \nSalary:%d\nCount:%d" % (self.name,self.salary,Employee.empCount))
    def buildConnectionString(self,params):
        """build Connection String"""
        return ";".join(["%s=%s" % (k,v) for k,v in params.items()])

class Child(Employee):
    '继承类Employee'
    def __init__(self):
        print("child constructor")

    def childMethod(self):
        print("This is child Method")


emp1 = Employee("mike",2000)
emp2 = Employee("zhangshan",3000)

emp1.displayCount()
emp1.displayEmployee()

emp2.displayCount()
emp2.displayEmployee()

print(Employee.empCount)

#添加一个属性
emp1.age = 23
print(emp1.age)
#修改属性
emp1.age = 33
print(emp1.age)
#删除属性
del emp1.age

print(hasattr(emp2, 'age'))    # 如果存在 'age' 属性返回 True。
print(setattr(emp2, 'age', 8)) # 添加属性 'age' 值为 8
print(getattr(emp2, 'age'))    # 返回 'age' 属性的值
print(delattr(emp2, 'age'))    # 删除属性 'age'

#类的属性（包含一个字典，由类的数据属性组成）
print(emp1.__dict__)
#类的文档字符串
print(emp1.__doc__)

print(emp1.__module__)

print(emp1.__class__)



child = Child()
child.childMethod()

if __name__=="__main__":
    myParams={"server":"10.8.8.50",
              "database":"Ets",
              "uid":"sa",
              "pwd":"dev_master"
              }
    employee = Employee("mike",33)
    print(employee.buildConnectionString(myParams))
    print(employee.buildConnectionString.__doc__)
