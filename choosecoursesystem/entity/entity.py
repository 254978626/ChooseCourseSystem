#!/usr/bin/python3
# -*-encoding:utf-8-*-
# Author: wuxiaobo
# @Time: 2019/1/23


class School:
    filename = "school.data"
    def __init__(self,id,name,addr):
        self.id = id
        self.name = name
        self.addr = addr

    def __str__(self):
        return "school_id: %s,school_name:%s,school_addr: %s" %(self.id,self.name,self.addr)

class Course:
    def __init__(self,id,name,price,period,school_id):
        self.id = id
        self.name = name
        self.period = period
        self.price = price
        self.school_id = school_id

    def __str__(self):
        return "course_id: %s,course_name:%s,course_period: %s,course_period: %s,school_id: %s" \
               %(self.id,self.name,self.period,self.price,self.school_id)

class Teacher:
    def __init__(self,id,name,age,salary,school_id,user_id):
        self.id = id
        self.name = name
        self.age = age
        self.salary = salary
        self.school_id = school_id
        self.user_id = user_id

    def __str__(self):
        return "teacher_id: %s,teacher_name:%s,teacher_age: %s,teacher_salary:%s,school_id: %s"\
               %(self.id,self.name,self.age,self.salary,self.school_id)

class Grade:
    def __init__(self,id,name,start_time,teacher_id,course_id,school_id):
        self.id = id
        self.name = name
        self.start_time = start_time
        self.teacher_id = teacher_id
        self.course_id = course_id
        self.school_id = school_id

    def __str__(self):
        return "grade_id: %s,grade_name:%s,grade_start: %s,teacher_id:%s,course_id: %s"\
               %(self.id,self.name,self.start_time,self.teacher_id,self.course_id)

class Student:
    def __init__(self,id,name,age,school_id,grade_id,user_id):
        self.id = id
        self.name = name
        self.age = age
        self.school_id = school_id
        self.grade_id = grade_id
        self.user_id = user_id

    def __str__(self):
        return "student_id: %s,student_name:%s,student_age: %s,school_id:%s,grade_id: %s"\
               %(self.id,self.name,self.age,self.school_id,self.grade_id)

class User:
    def __init__(self,id,pwd,role):
        self.id = id
        self.pwd = pwd
        self.role = role

    def __str__(self):
        return "user_id: %s,user_role:%s" %(self.id,self.role)

if __name__ == "__main__":
    pass




