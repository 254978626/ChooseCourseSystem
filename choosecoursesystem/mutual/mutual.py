#!/usr/bin/python3
# -*-encoding:utf-8-*-
# Author: wuxiaobo
# @Time: 2019/1/24 
from choosecoursesystem.mutual.window import Window
import choosecoursesystem.tools.tools as Tools

class Mutual:
    '''
    管理用户交互
    '''
    def __init__(self):
        self.w = Window.get_window()

    def student_view(self,user_info):
        '''
         学生模块：注册
        '''
        menu = '''
        选择操作内容<按q退出系统>:
        1. 注册<重复>
        2. 交学费
        3. 换班
        '''
        while True:
            print("欢迎：", Tools.pr_color(user_info["name"]),"学员")
            print(menu)
            choice = input(">> ")
            if choice == '1':
               print("开始后注册了")
            elif choice == '2':
                print("交学费?不肯能，这辈子都不可能交学费!")
            elif choice == '3':
                print("报了名还想换班？不可能的")
                self.w.pr_grade_bystudentId(user_info["id"])
            elif choice == 'q':
                self.w.save_data()
                print("byebye!!!")
                exit(0)
            else:
                print("您的输入有误！")

    def teacher_view(self,user_info):
        '''
            1.查看班级信息
            2.查看学生信息（先班级后学生）
        '''
        menu = '''
           选择操作内容<按q退出系统>:
           1. 查看班级信息
           2. 查看学生信息

           '''
        print("欢迎：", Tools.pr_color(user_info["name"]),"老师")
        while True:
            print(menu)
            choice = input(">> ")
            if choice == '1':
                self.w.pr_grade_byteacherId(user_info["id"])
            elif choice == '2':
                self.w.pr_student_byteacherId(user_info["id"])

    def manager_view(self,user_info):
        '''
         创建学校，讲师，课程，班级
        '''
        menu = '''
        选择操作内容<按q退出系统>:
        1. 创建学校
        2. 创建课程
        3. 创建老师
        4. 创建班级
        '''
        print("欢迎：", Tools.pr_color(user_info["name"]))
        while True:
            print(menu)
            choice = input(">> ")
            if choice == '1':
                print("开始创建学校=========")
                name = input("请输入学校>>")
                addr = input("请输入地址>>")
                self.w.create_school(name,addr)
            elif choice == '2':
                print("开始创建课程=========")
                self.w.pr_school()
                school_seqid = int(input("请选择学校(输入序列号)>>"))
                school_id = self.w.get_schoolId_by_squenceid(school_seqid)
                name = input("请输入课程名>>")
                price = input("请输入课程价格>>")
                period = input("请输入课程学时>>")

                self.w.create_course(name,price,period,school_id)
            elif choice == '3':
                print("开始创建老师=========")
                self.w.pr_school()
                school_seqid = int(input("请选择学校(输入序列号)>>"))
                school_id = self.w.get_schoolId_by_squenceid(school_seqid)
                user_id = input("用户名>")
                user_pwd = input("密码>")
                name = input("老师名称>>")
                age = input("老师年龄>>")
                salary = input("薪资>>")
                self.w.create_teacher(user_id,user_pwd,school_id,name,age,salary)
            elif choice == '4':
                print("开始创建班级=========")
                self.w.pr_school()
                school_seqid = int(input("请选择学校(输入序列号)>>"))
                school_id = self.w.get_schoolId_by_squenceid(school_seqid)
                self.w.pr_teachers_byschoolId(school_id)
                teacher_seqid = int(input("请选择代课老师>>"))
                teacher_id = self.w.get_teacherId_by_squenceid(teacher_seqid)
                self.w.pr_course_byschoolId(school_id)
                course_seqid = int(input("请选择课程：>>"))
                course_id = self.w.get_courseId_by_squenceid(course_seqid)
                name = input("班级名称>>")
                start_time = input("开班日期>>")
                self.w.create_grade(name,start_time,teacher_id,course_id,school_id)
            elif choice == 'q':
                self.w.save_data()
                self.w.pr_all()
                print("byebye!!!")
                exit(0)
            else:
                print("您的输入有误！")

    def register(self):
        print("欢饮来到注册页面！")
        print("注册中=========")
        user_id = input("请输入用户名>")
        user_pwd = input("请输入密码>")
        self.w.pr_school()
        school_seqid = int(input("请选择学校名>>"))
        school_id = self.w.get_schoolId_by_squenceid(school_seqid)
        self.w.pr_grade_byschoolId(school_id)
        grade_seqid = int(input("请选择班级：>>"))
        grade_id = self.w.get_gradeId_by_squenceid(grade_seqid)
        name = input("你叫啥？>>")
        age = input("多大了？>>")
        self.w.register_student(user_id,user_pwd,school_id,grade_id,name,age)

    def login(self):
        print("欢饮来到登录页面！")
        user_id = input("请输入用户名>")
        user_pwd = input("请输入密码>")
        if self.w.login(user_id, user_pwd):
            #user_info(学生|老师 id ,名字，角色）
            user_info = self.w.get_user_info(user_id)
            if user_info["role"] == "student":
                self.student_view(user_info)
            elif user_info["role"] == "teacher":
                self.teacher_view(user_info)
            else:
                self.manager_view(user_info)
        else:
            print("用户名，密码错误")

    def main(self):
        main_page = '''
            欢迎来到选课系统
        '''
        print(main_page)
        menu = '''
选择操作内容<按q退出系统>:
1.登陆
2.注册
            '''
        while True:
            print(menu)
            choice = input(">>")
            if choice == '1':
                self.login()
            elif choice == '2':
                self.register()
            elif  choice == 'q':
                exit(0)
            else:
                print("输入有误")
