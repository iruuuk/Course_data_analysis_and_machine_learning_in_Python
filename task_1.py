my_list = [1, 'two', 'a', 4] 
my_list.reverse() 
print(my_list) 
print(my_list[2]) 
 
x = [15, 11, 13, 12, 14, 10] 
x.reverse() 
print(x) 
 
lst1 = [0, 1, 2, 3, 4, 5] 
lst2 = lst1 #copy 
lst1.pop(2) #удаление 3 элемента 
print(lst1) 
print(lst2) 
 
my_tuple = (1, 2, 3, 4, 5) 
another_tuple = (6, 7) 
print(my_tuple) 
print(my_tuple[1]) 
 
print(my_tuple[:3]) 
print(my_tuple.index(3)) 
print(my_tuple + another_tuple) 
print(my_tuple * 8) 
 
correct_answers = (1, 2, 3, 2, 1, 2, 1, 3, 1, 2, 1, 2, 3, 3, 2, 1, 2, 1, 2, 1) 
my_answers = [1, 3, 2, 3, 1, 2, 3, 2, 1, 2, 3, 2, 3, 2, 1, 2, 3, 1, 2, 1] 
i = (1, 2, 3) 
j = [1, 2, 3] 
print(list(i) == j) 
print (list(correct_answers) == my_answers) 
 
def checking(): 
    if list(correct_answers) == my_answers: 
        print('Экзамен сдан') 
    else: 
        print('Экзамен провален') 
 
checking() 
 
list_number = [1, 2, 3] 
print(tuple(list_number))

