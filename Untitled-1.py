from random import choice


details = []


a = int(input('Enter the number of teams: '))
for i in range(a):
    school = input('Enter the name of the School: ')
    details.append([]) 
    for j in range(3):
        name = input(f'Enter the Name of Student {j+1}: ')
        skill = input(f'Enter the Proficiency of Student {j+1}: ')
        details[-1].append([name, skill, school])

mix = []
for team in details:
    for student in team:
        mix.append(student)


new = [[] for _ in details]  

length = list(range(len(mix)))


for group in new:
    while len(group) < 3: 
        index = choice(length)
        student = mix[index]
        
        if student not in group and all(student[1] != elem[1] for elem in group) and all(student[2] != elem[2] for elem in group):
            group.append(student)


print(new)