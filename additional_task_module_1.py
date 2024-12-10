grades = [[5, 3 , 3 , 5, 4], [2, 2 , 2 , 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
print(grades)
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

#преобразовуем множество students в список students
students = list(students)

#упорядочиваем в алфавитном порядке с помощью поиска перовго символа с минимальным ASCII-кодом
fisrt_student = min(students)   #поиск элемента по алфавиту первого студента в старом списке
new_list = [fisrt_student]      #создаем новый список студентов new_list и добавляем в список найденный элемент
students.remove(fisrt_student)  #удаляем найденный элемент из старого списка студентов

second_student = min(students)  #поиск элемента по алфавиту второго студента в старом списке
new_list.append(second_student) #добавляем в новый список найденный элемент
students.remove(second_student) #удаляем найденный элемент из старого списка студентов


third_student = min(students)   #поиск элемента по алфавиту третьего студента в старом списке
new_list.append(third_student)  #добавляем в новый список найденный элемент
students.remove(third_student)  #удаляем найденный элемент из старого списка студентов

fourth_student = min(students)  #поиск элемента по алфавиту четвертого студента в старом списке
new_list.append(fourth_student) #добавляем в новый список найденный элемент
students.remove(fourth_student) #удаляем найденный элемент из старого списка студентов

fifth_student = students[0]     #сохраняем имя оставшегося пятого студента
new_list.append(students[0])    #добавляем в новый список последний элемент из старого списка под индексом [0]
del students                    #удаляем старый список за ненадобностью

print(new_list)                 #выводим новый список для проверки алфавитного порядка на экран

#далее вычисляем средний балл студентов:
fisrt_student_average_grade =  sum(grades[0])/(len(grades[0]))
second_student_average_grade = sum(grades[1])/(len(grades[1]))
third_student_average_grade =  sum(grades[2])/(len(grades[2]))
fourth_student_average_grade = sum(grades[3])/(len(grades[3]))
fifth_student_average_grade =  sum(grades[4])/(len(grades[4]))

final_result = {fisrt_student:   sum(grades[0])/(len(grades[0])),
                second_student:  sum(grades[1])/(len(grades[1])),
                third_student:   sum(grades[2])/(len(grades[2])),
                fourth_student:  sum(grades[3])/(len(grades[3])),
                fifth_student:   sum(grades[4])/(len(grades[4]))
                }
print(final_result) #выводим итоговый результат поставленной задачи


#Ниже сократил немного текст, но менее понятно
'''grades = [[5, 3 , 3 , 5, 4], [2, 2 , 2 , 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
print(grades)
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

#преобразовывам множество students в список students
students = list(students)

#упорядочиваем в алфавитном порядке с помощью поиска перовго символа с минимальным ASCII-кодом
student = min(students)   #поиск элемента по алфавиту первого студента в старом списке
new_list = [student]      #создаем новый список студентов new_list и добавляем в список найденный элемент
students.remove(student)  #удаляем найденный элемент из старого списка студентов

student = min(students)  #поиск элемента по алфавиту второго студента в старом списке
new_list.append(student) #добавляем в новый список найденный элемент
students.remove(student) #удаляем найденный элемент из старого списка студентов


student = min(students)  #поиск элемента по алфавиту второго студента в старом списке
new_list.append(student) #добавляем в новый список найденный элемент
students.remove(student)  #удаляем найденный элемент из старого списка студентов

student = min(students)  #поиск элемента по алфавиту второго студента в старом списке
new_list.append(student) #добавляем в новый список найденный элемент
students.remove(student) #удаляем найденный элемент из старого списка студентов

new_list.append(students[0])    #добавляем в новый список последний элемент из старого списка под индексом [0]
del students                    #удаляем старый список за ненадобностью

print(new_list)                 #выводим новый список для проверки алфавитного порядка на экран


final_result = {new_list[0]:  sum(grades[0])/(len(grades[0])),
                new_list[1]:  sum(grades[1])/(len(grades[1])),
                new_list[2]:  sum(grades[2])/(len(grades[2])),
                new_list[3]:  sum(grades[3])/(len(grades[3])),
                new_list[4]:  sum(grades[4])/(len(grades[4]))
                }
print(final_result) #выводим итоговый результат поставленной задачи'''