students = ("Harry", "Hermione", "Ron", "Draco")

print(list(enumerate(students))) # => [(0, 'Harry'), (1, 'Hermione'), (2, 'Ron'), (3, 'Draco')]
print(list(enumerate(students, start = 1))) # => [(1, 'Harry'), (2, 'Hermione'), (3, 'Ron'), (4, 'Draco')]

#print does not show str if the work list is omitted