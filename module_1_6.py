#1.Работа со словарями:
my_dict={'Александр':1799,'Михаил':1814,'Николай':1821}
print(my_dict)
print(my_dict['Михаил'])
print(my_dict.get('Владимир','Такого ключа нет'))
my_dict.update({'Сергей':1895,'Николай Г.':1886})
a=my_dict.pop('Николай')
print(a)
print(my_dict)
#2.Работа с множествами:
my_set={1,2,1,2,3,2,3,2,'Множество',(1,2,3),(1,2,3)}
print(my_set)
my_set.add(4)
my_set.add('Другое множество')
my_set.remove((1,2,3))
print(my_set)