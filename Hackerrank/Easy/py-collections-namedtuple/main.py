from collections import namedtuple

if __name__ == '__main__':
    n = int(raw_input())
    fields = raw_input()
    Student = namedtuple('Student', fields)
    sum_ = 0
    for i in range(n):
        id_, mark, name, class_ = raw_input().split()
        student = Student(id_, mark, name, class_)
        sum_ += float(student.MARKS)
    print ("{0:.2f}".format(sum_ / float(n)))
