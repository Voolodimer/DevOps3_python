#!/usr/bin/python3

# Создать сотрудника Mary, пользуясь классом
# Employee и перенести его в другую программу,
# используя модуль Pickle и файловую систему.
# Узнать про + и - модуля Pickle.


import pickle


class Employee:
    def __init__(self, name):
        self.name = name


Mary = Employee('Mary')
print(Mary)

with open('hw14.pickle', 'wb') as f:
    pickle.dump(Mary, f)

with open('hw14.pickle', 'rb') as f:
    data_emp = pickle.load(f)

print(data_emp.name)
