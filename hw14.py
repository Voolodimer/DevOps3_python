import pickle


class Employee:
    def __init__(self, name):
        self.name = name
    pass


# Mary = Employee('Mary')
# print(Mary)
#
# with open('hw14.pickle', 'wb') as f:
#     pickle.dump(Mary, f)

with open('hw14.pickle', 'rb') as f:
    data_emp = pickle.load(f)
print(data_emp.name)
