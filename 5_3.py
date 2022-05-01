tutors = [
        'Иван', 'Анастасия', 'Петр', 'Сергей',
        'Дмитрий', 'Борис', 'Елена', 'Дмитрий', 'Борис', 'Елена'
    ]
klasses = [
        '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
    ]
def gen_of_people():

    for num in range(len(tutors)):
        if len(klasses) <= num:
            yield (tutors[num], None)
        else:
            yield (tutors[num], klasses[num])


print(gen_of_people()) # доказательство что генератор
print(next(gen_of_people()))
print(next(gen_of_people()))# не понял почему next возвращает одно и то же значение?
for gen in gen_of_people():
    print(gen)







