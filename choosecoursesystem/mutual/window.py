#!/usr/bin/python3
# -*-encoding:utf-8-*-
# Author: wuxiaobo
# @Time: 2019/1/24


import choosecoursesystem.tools.tools as Tools
from choosecoursesystem.crud.db import DB

class Window:
    '''
    此类用于交互中的子单元
    '''
    def __init__(self,db):
        self.db = db

    @staticmethod
    def get_window():
        db_obj = DB.get_db()
        return Window(db_obj)

    #增
    def create_school(self,name,addr):
        id = Tools.create_id()
        self.db.create_school(id, name, addr)

    def create_course(self,name,price,period,school_id):
        id = Tools.create_id()
        self.db.create_course(id,name,price,period,school_id)

    def create_teacher(self,user_id,user_pwd,school_id,name,age,salary):
        #创建用户
        id = user_id
        pwd = user_pwd
        role = "teacher"
        self.db.create_user(id, pwd, role)
        #创建老师
        id = Tools.create_id()
        self.db.create_teacher(id,name,age,salary,school_id,user_id)

    def create_grade(self,name,start_time,teacher_id,course_id,school_id):
        id = Tools.create_id()
        self.db.create_grade(id,name,start_time,teacher_id,course_id,school_id)

    #学生注册
    def register_student(self,user_id,user_pwd,school_id,grade_id,name,age):
        id = user_id
        pwd = user_pwd
        role = "student"
        #创建用户
        self.db.create_user(id,pwd,role)
        #创建学生
        id = Tools.create_id()
        self.db.create_student(id,name,age,school_id,grade_id,user_id)
        self.save_data()
        print("注册完成！")

    #查询
    def get_schoolId_by_squenceid(self,school_squenceid):
        return self.db.get_schoolId_by_squenceid(school_squenceid)
    def get_teacherId_by_squenceid(self,teacher_squenceid):
        return self.db.get_schoolId_by_squenceid(teacher_squenceid)
    def get_courseId_by_squenceid(self, course_squenceid):
        return self.db.get_courseId_by_squenceid(course_squenceid)
    def get_gradeId_by_squenceid(self, grade_squenceid):
        return self.db.get_gradeId_by_squenceid(grade_squenceid)

    #用户信息，用于交互界面信息传输
    def get_user_info(self,user_id):
        user = self.db.get_user_byId(user_id)
        if user.role == 'student':
            student = self.db.get_student_by_userId(user_id)
            id = student.id
            name = student.name
        elif user.role == 'teacher':
            teacher = self.db.get_teacher_by_userId(user_id)
            id = teacher.id
            name = teacher.name
        else:
            id ='admin'
            name = 'admin'
        #传递用户信息
        return  {"id":id,"name": name,"role": user.role}

    def login(self,user_id,user_pwd):
        user = self.db.get_user_byId(user_id)
        if not user or user_pwd != user.pwd:
            return False
        return True

    #打印
    def pr_school(self):
        school_list = self.db.get_school_All()
        for index,school in enumerate(school_list):
            print(Tools.pr_color(str(index)),school)

    def pr_teachers_byschoolId(self,school_id):
        teacher_list = self.db.get_teachers_byschoolId(school_id)
        for index, teacher in enumerate(teacher_list):
            print(Tools.pr_color(str(index)), teacher)

    def pr_course_byschoolId(self,school_id):
        course_list = self.db.get_courses_byschoolId(school_id)
        for index, course in enumerate(course_list):
            print(Tools.pr_color(str(index)),course)

    def pr_grade_byschoolId(self,school_id):
        grade_list = self.db.get_grades_byschoolId(school_id)
        for index, grade in enumerate(grade_list):
            print(Tools.pr_color(str(index)),grade)

    def pr_grade_byteacherId(self,teacher_id):
        grade_list = self.db.get_grades_byteacherId(teacher_id)
        for index, grade in enumerate(grade_list):
            print(Tools.pr_color(str(index)),grade)

    def pr_grade_bystudentId(self,student_id):
        grade_id = self.db.get_grade_bystudentId(student_id)
        grade = self.db.get_grade_bygradeId(grade_id)
        print(Tools.pr_color(str(grade),color=34))

    def pr_student_bygradeId(self, grade_id):
        student_list = self.db.get_student_by_userId(grade_id)
        for index, student in enumerate(student_list):
            print(Tools.pr_color(str(index)), student_list)

    def pr_student_byteacherId(self,teacher_id):
        self.pr_grade_byteacherId(teacher_id)
        grade_id = self.db.get_gradeId_by_squenceid(int(input("请选择班级：>>")))
        self.pr_student_bygradeId(grade_id)

    # 打印所有信息（测试用）
    def pr_all(self):
        for item,item_list in self.db.data.items():
            print(Tools.pr_color(item,color=34),":")
            for obj in item_list:
                print(obj)
            print("="*50)
    #保存
    def save_data(self):
        self.db.save()
if __name__ == "__main__":
    w = Window.get_window()
    w.pr_all()


