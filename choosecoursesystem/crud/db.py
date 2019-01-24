#!/usr/bin/python3
# -*-encoding:utf-8-*-
# Author: wuxiaobo
# @Time: 2019/1/24 

from choosecoursesystem.entity.entity import *
import choosecoursesystem.tools.tools as Tools
import pickle
import os


class DB:
    '''
    此类用于操作实体对象
    '''
    filename = os.path.abspath(os.path.dirname(os.path.dirname(__file__)) + "\\db\\sc.data")
    data = {
        "school":[],
        "teacher":[],
        "course":[],
        "grade":[],
        "student":[],
        "user":[],
    }

    def __init__(self,filename,pickle_obj):
        self.filename = filename
        self.data = pickle_obj


    #封装初始化函数
    @staticmethod
    def get_db():
        #首次创建
        if not os.path.exists(DB.filename):
            pickle.dump(DB.data,open(DB.filename,"wb"))

        pickle_obj = pickle.load(open(DB.filename,"rb"))
        return DB(DB.filename,pickle_obj)

    def save(self):
        pickle.dump(self.data,open(self.filename,"wb"))

    #增
    def create_school(self,id,name,addr):
        self.data["school"].append(School(id,name,addr))

    def create_course(self,id,name,price,period,school_id):
        self.data["course"].append(Course(id,name,price,period,school_id))

    def create_teacher(self,id,name,age,salary,school_id,user_id):
        self.data["teacher"].append(Teacher(id,name,age,salary,school_id,user_id))

    def create_grade(self,id,name,start_time,teacher_id,course_id,school_id):
        self.data["grade"].append(Grade(id,name,start_time,teacher_id,course_id,school_id))

    def create_student(self,id,name,age,school_id,grade_id,user_id):
        self.data["student"].append(Student(id,name,age,school_id,grade_id,user_id))

    def create_user(self,id,pwd,role):
        self.data["user"].append(User(id,pwd,role))
    #删
    #改
    #查

    def get_school_All(self,school_=""):
        return self.data["school"]

    #获取学校
    def get_schoolId_by_squenceid(self,school_squenceid):
        return self.data["school"][school_squenceid].id

    #获取老师
    def get_teachers_byschoolId(self,school_id):
        res = []
        teacher_list = self.data["teacher"]
        for teacher in teacher_list:
            if teacher.school_id == school_id:
                res.append(teacher)
        return res

    def get_teacherId_by_squenceid(self,teacher_squenceid):
        return self.data["teacher"][teacher_squenceid].id

    def get_teacher_by_userId(self,id):
        for teacher in self.data["teacher"]:
            if id == teacher.user_id:
                return teacher
    #获取课程
    def get_courses_byschoolId(self, school_id):
        res = []
        course_list = self.data["course"]
        for course in course_list:
            if course.school_id == school_id:
                res.append(course)
        return res

    def get_courseId_by_squenceid(self, course_squenceid):
        return self.data["course"][course_squenceid].id

    def get_grades_byschoolId(self, school_id):
        res = []
        grade_list = self.data["grade"]
        for grade in grade_list:
            if grade.school_id == school_id:
                res.append(grade)
        return res
    def get_gradeId_by_squenceid(self, grade_squenceid):
        return self.data["grade"][grade_squenceid].id

    def get_grades_byteacherId(self, teacher_id):
        res = []
        grade_list = self.data["grade"]
        for grade in grade_list:
            if grade.teacher_id == teacher_id:
                res.append(grade)
        return res

    def get_grade_bystudentId(self, student_id):
        student_list = self.data["student"]
        for student in student_list:
            if student.id == student_id:
                return student.grade_id

    #通过grade_id 找到grade
    def get_grade_bygradeId(self,grade_id):
        grade_list = self.data["grade"]
        for grade in grade_list:
            if grade.id == grade_id:
               return grade
    #获取学生
    #通过用户名
    def  get_student_by_userId(self,id):
        for student in self.data["student"]:
            if id == student.user_id:
                return student
    # id取用户
    def get_user_byId(self, id):
        user_list = self.data["user"]
        for user in user_list:
            if id == user.id:
                return user


if __name__ == "__main__":
    DB = DB.get_db()
    #初始化一个管理员
    DB.create_user("admin","123","admin")
    DB.save()
