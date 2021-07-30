# Напишите программу, которая читает данные из файлов
# /etc/passwd и /etc/group на вашей системе и выводит
# следующую информацию в файл output.txt:
# 1. Количество пользователей, использующих все имеющиеся
# интерпретаторы-оболочки.
# ( /bin/bash - 8 ; /bin/false - 11 ; ... )
# 2. Для всех групп в системе - UIDы пользователей
# состоящих в этих группах.
# ( root:1, sudo:1001,1002,1003, ...)

def read_file(file_name):
    res_buff = []
    with open(file_name) as file:
        res_buff += file.readlines()
        i = 0
        while i < len(res_buff):
            res_buff[i] = res_buff[i].rstrip('\n')
            i += 1
        return res_buff


def write_file(datas):
    with open('output.txt', 'a') as file_to_w:
        for el in datas:
            file_to_w.write(el + '-' + str(datas[el]) + ' ; ')
        file_to_w.write('\n')


etc_passwd = read_file('/etc/passwd')
i = 0
res_dict_pswd = {}
# считаем количество пользователей каждой оболочки
while i < len(etc_passwd):
    if etc_passwd[i].split(':')[6] not in res_dict_pswd:
        res_dict_pswd[etc_passwd[i].split(':')[6]] = 1
    else:
        res_dict_pswd[etc_passwd[i].split(':')[6]] += 1
    i += 1

write_file(res_dict_pswd)

etc_group = read_file('/etc/group')
del etc_group[len(etc_group) - 1]

name_set = {}
res_str_grp = ''
i = 0
# получаем все имена пользователей
while i < len(etc_group):
    if etc_group[i].split(':')[3] != '':
        names = etc_group[i].split(':')[3].split(',')
        for name in names:
            if name in name_set:
                continue
            x = 0
            while x < len(etc_passwd):
                if etc_passwd[x].split(':')[0] == name:
                    name_set[name] = etc_passwd[x].split(':')[2]
                x += 1
        i += 1
        continue
    i += 1

i = 0
while i < len(etc_group):
    res_str_grp += etc_group[i].split(':')[0] + ':' + etc_group[i].split(':')[2] + ','
    if len(etc_group[i].split(':')[3]) > 1:
        for name in etc_group[i].split(':')[3].split(','):
            res_str_grp += name_set[name] + ','
        res_str_grp += ' '
    else:
        res_str_grp += ' '
        i += 1
        continue
    i += 1
with open('output.txt', 'a') as file:
    file.write(res_str_grp)
