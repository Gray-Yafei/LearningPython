class User(object):
    def __init__(self, name, age, gender, id):
        self.name = name
        self.age = age
        self.gender = gender
        self.id = id
    def __str__(self):
        return f"姓名:{self.name}\n年龄:{self.age}\n性别:{self.gender}\n学(工)号:{self.id}\n"
class Student(User):
    # 属性：姓名，年龄，性别，学号
    def __init__(self, name, age, gender, id):
        super().__init__(name, age, gender, id)
        self.courses = []
        # print("*"*30)
        # print(f"学生姓名:{self.name}")
        # print(f"学生年龄:{self.age}")
        # print(f"学生性别:{self.gender}")
        # print(f"学生学号:{self.id}")
        # print("*" * 30)
    def __str__(self):
        print('该学生的选课信息：')
        if self.courses == []:
            print("未选课")
        else:
            for course in self.courses:
                print(course.name)
        return super().__str__()

    def addCourse(self, course):
        self.courses.append(course)

    def removeCourse(self, course):
        self.courses.remove(course)


class Teacher(User):
    # 属性：姓名、年龄、性别、工号、是否是导员
    def __init__(self, name, age, gender, id, isInstructor,cla):
        super().__init__(name, age, gender, id)
        self.isInstructor = isInstructor
        self.cla = cla

    def __str__(self):
        return super().__str__() + f"是否是导员:{['是','否'][self.isInstructor]}\n所带班级:{self.cla}\n"


class Class(object):
    # 属性：班级名称，班级号，辅导员，学生
    def __init__(self,name,id,teacher,students):
        self.name=name
        self.id=id
        self.teacher=teacher
        self.students=students
    def show_infos(self):
        print("*"*15 + "班级信息" + "*"*15)
        print(f"班级名称:{self.name}")
        print(f"班级班号:{self.id}")
        print(f"辅导员：:{self.teacher.name}")
        print("学生信息:")
        if not self.students:
            print("无")
        else:
            for student in self.students:
                print(student.name)
        print("*" * 15 + "班级信息" + "*" * 15)

    def add_student(self,student):  # 增加学生
        if student not in self.students:
            self.students.append(student)
            return True
        else:
            raise Exception("此学生已经在该班级里")

    def del_student(self,student):  # 减少学生
        if student in self.students:
            self.students.remove(student)
            return True
        else:
            raise Exception("此学生不在该班级里")

class Course(object):
    # 属性：课名，id，老师，学生，课程性质，课程容量
    # 类属性
    courses = []
    def __init__(self,name,id,teacher,students,type,number):
        self._name=name
        self.id=id
        self.teacher=teacher
        self.students=students
        self.type=type
        self.number=number
        self.studentNum=len(self.students)
        self.validNum=self.number-self.studentNum
        for student in self.students:
            student.addCourse(self)
        Course.courses.append(self.name)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,name):
        if name == '':
            raise Exception("出现错误")
        if not isinstance(name,str):
            raise Exception("请输入字符串")
        self._name=name

    def show_infos(self):
        print("*" * 15 + "课程信息" + "*" * 15)
        print(f"课程名称:{self.name}")
        print(f"课程号:{self.id}")
        print(f"授课老师：:{self.teacher.name}")
        print("课程类型：" + self.type)
        print(f"课程容量：:{self.number}")
        print(f"已选学生人数：:{self.studentNum}")
        print(f"剩余学生人数：:{self.validNum}")
        print("学生信息:")
        if not self.students:
            print("无")
        else:
            for student in self.students:
                print(student.name)
        print("*" * 15 + "课程信息" + "*" * 15)

    def add_student(self,student):  # 增加学生
        if student  in self.students:
            raise Exception("此学生已经在该课程里")
        if self.validNum <= 0:
            raise Exception("此课程已满，请选择其他课程")
        self.students.append(student)
        self.studentNum+=1
        self.validNum-=1
        student.addCourse(self)
        return True

    def del_student(self,student):  # 减少学生
        if student in self.students:
            self.students.remove(student)
            student.removeCourse(self)
            self.studentNum-=1
            self.validNum+=1
            return True
        else:
            raise Exception("此学生不在该课程里")

    @classmethod
    def showCoursesList(cls):
        return cls.courses




mia = Student('Mia', 24, '女', 1)
wei = Student('wei', 26, '男', 2)
yang = Student('yang', 25, '女', 3)
xin = Student('xin',24,'女',4)
# print(mia)

jack = Teacher("jack",50,'男',5,False,[])
# print(jack)

computer_2 = Class('计算机二班',10002,jack,[])
# computer_2.show_infos()

computer_1 = Class('计算机一班',10001,jack,[mia,wei])
# computer_1.show_infos()

# computer_1.add_student(yang)
# computer_1.show_infos()
# computer_1.del_student(mia)
# computer_1.show_infos()

python = Course('Python',1,jack,[mia,wei],'必修',3)
java = Course('java',2,jack,[xin,wei],'选修',2)
# python.show_infos()
# python.add_student(yang)
# python.del_student(wei)
# python.add_student(wei)
# python.show_infos()
print(Course.showCoursesList())
python.name = 'python精讲课程'
print(python.name)