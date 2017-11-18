#学生管理系统 -- 添加、删除、查询、修改、退出
import time;

#1、先把整体框架考虑清楚，即搭框架
#1.1 展示选项
def showInfo():
	print("-"*30);
	print("  学生管理系统  ");
	print("1、添加学生信息");
	print("2、删除学生信息");
	print("3、查询学生信息");
	print("4、修改学生信息");
	print("5、列出所有学生信息");
	print("6、退出系统");
	print("-"*30);


#1.2 提示用户输入选项,并获取用户的输入


#1.3 根据用户输入的选项，执行相应行为

#学生信息的存储方式：字典{姓名：name，年龄：age，学号：id}
#学生列表：列表【{学生1}，{学生2}，。。。】
students = [];	
stuInfo = {};
def addStu(students):#添加学生信息
	stuInfo['name'] = input("请输入学生的姓名：");
	stuInfo['age'] = input("请输入学生的年龄：");
	stuInfo['stuId'] = input("请输入学生的学号：");
	students.append(stuInfo);
	
def delStu(students):#删除学生信息
	delNum = int(input("请输入您要删除的学生序号："));
	del students[delNum];
	
def lookupStu(students):
	num = int(input("请输入您要查询的学生序号："));
	print("查询中。。。");
	time.sleep(1);
	print("姓名：%s"%students[num]['name']);
	print("年龄：%s"%students[num]['age']);
	print("学号：%s"%students[num]['stuId']);
def editStu(students):
	num = int(input("请输入您要修改的学生序号："));
	info = int(input("请选择要修改的信息（1=姓名，2=年龄，3=学号）："));
	if(info==1):
		students[num]['name'] = input("请输入姓名：");
	elif(info==2):
		students[num]['age'] = input("请输入年龄：");
	elif(info==3):
		students[num]['stuId'] = input("请输入学号：");
	else:
		print("该选项不存在！")
	
	
	
	
def allStu(students):
	print("----学生列表----");
	print("序号\t姓名")
	for x,s in enumerate(students):
		
		print('%d\t%s'%(x,s['name']));
		
		
	
while(True):
	showInfo();	
	selected = int(input("请选择你要进行的操作（序号）："));
	if(selected==1):
		addStu(students);
	elif(selected==2):
		delStu(students);
	elif(selected==3):
		lookupStu(students);
	elif(selected==4):
		editStu(students);
	elif(selected==5):
		allStu(students);
	elif(selected==6):
		print("已退出系统");
		break
	else:
		print("您输入有误");
		break