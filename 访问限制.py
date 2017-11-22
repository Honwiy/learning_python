# -*- coding: utf-8 -*-

class Student(object):
    def __init__(self,name,score):
        self.__name = name
        self.__score = score

    def get_name(self):
        return self.__name
    def get_score(self):
        return self.__score

    def set_score(self,score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')

    def get_grade(self):
        if self.__score >= 90:
            return 'A'
        elif self.__score >= 60:
            return 'B'
        else:
            return 'C'

bart = Student('bart',95)
print('bart.name =',bart.get_name())
print('bart.firstscore =',bart.get_score())
bart.set_score(60)
print('bart.get_score() =', bart.get_score())