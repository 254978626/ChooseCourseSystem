#!/usr/bin/python3
# -*-encoding:utf-8-*-
# Author: wuxiaobo
# @Time: 2019/1/24
import hashlib
import random
import time

# 创建 对象id
def create_id():
    # 1.md5 工厂
    h_md5 = hashlib.md5()
    h_md5.update(str(time.time()).encode("utf-8"))
    h_md5.update(str(random.random()).encode("utf-8"))
    id = h_md5.hexdigest()
    return id


#创建打印颜色
def pr_color(s,color=31):
    return "\033[7;"+str(color)+"m" + s + "\033[0m"

if __name__ == '__main__':
    print(pr_color("pppp",color=34))

