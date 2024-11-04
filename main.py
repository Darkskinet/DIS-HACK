import gspread
import pandas as pd
import random
from flask import Flask, jsonify
from threading import Timer

# gc = gspread.service_account(filename='credentials.json')
# sh = gc.open_by_key('1-NDPq_BWp2IUNGkJ1he8jfnrbYMDNS_XzY10UTOpkU0')
# worksheet = sh.sheet1

# res = worksheet.get_all_records()
# df = pd.DataFrame(res)

# total_entries = df.shape[0]
# teams_needed = total_entries // 3



# TYPE - 1

# skills = []
# grouped = df.groupby('Programming Skill')
# for skill, group in grouped:
#     student_list = group[['Student Name', 'School Name']].values.tolist()
#     random.shuffle(student_list)  
#     skills.append((skill, student_list))


# teams = []
# for _ in range(teams_needed):
#     team = []
#     used_schools = set()


#     for skill, students in skills:
#         available_students = [s for s in students if s[1] not in used_schools]
#         if available_students:
#             selected_student = available_students.pop(0)  
#             team.append((skill, selected_student[0], selected_student[1]))
#             used_schools.add(selected_student[1])  
#             students.remove(selected_student)  
    
#     teams.append(team)


# remaining_students = []
# for skill, students in skills:
#     for student in students:
#         remaining_students.append(student)
# if remaining_students:
#     for student in remaining_students:
#         for team in teams:
#             if len(team) < 3:
#                 team.append(("Remaining", student[0], student[1]))
#                 break


# for i, team in enumerate(teams, start=1):
#     print(f"\nTeam {i}")
#     for skill, name, school in team:
#         print(f"  Skill: {skill}, Name: {name}, School: {school}")



# TYPE - 2

# skills = []
# grouped = df.groupby('Programming Skill')
# for skill, group in grouped:
#     student_list = group[['Student Name', 'School Name']].values.tolist()
#     random.shuffle(student_list)  
#     skills.append((skill, student_list))


# teams = [[] for _ in range(teams_needed)]


# for skill, students in skills:
#     team_index = 0  

#     while students:
#         team = teams[team_index]
#         used_schools = {s[2] for s in team}  


#         available_students = [s for s in students if s[1] not in used_schools]

#         if available_students:
#             selected_student = available_students.pop(0)
#             team.append((skill, selected_student[0], selected_student[1]))
#             students.remove(selected_student)  


#         team_index = (team_index + 1) % teams_needed


# remaining_students = [student for skill, students in skills for student in students]
# random.shuffle(remaining_students) 

# for student in remaining_students:
#     for team in teams:
#         if len(team) < 3:
#             team.append(("Remaining", student[0], student[1]))
#             break


# for i, team in enumerate(teams, start=1):
#     print(f"\nTeam {i}")
#     for skill, name, school in team:
#         print(f"  Skill: {skill}, Name: {name}, School: {school}")

# teams_json = json.dumps(teams)


# with open("teams.json", "w") as file:
#     file.write(teams_json)




# # Initialize Flask app
# app = Flask(__name__)

# # Authenticate with Google Sheets
# gc = gspread.service_account(filename='credentials.json')
# sh = gc.open_by_key('1-NDPq_BWp2IUNGkJ1he8jfnrbYMDNS_XzY10UTOpkU0')
# worksheet = sh.sheet1

# # Function to create teams with largest multiple of 3
# def fetch_and_create_teams():
#     res = worksheet.get_all_records()
#     df = pd.DataFrame(res)
    
#     total_entries = df.shape[0]
#     max_entries = (total_entries // 3) * 3  # Largest multiple of 3
#     df = df.head(max_entries)

#     # Group by skill and shuffle each group
#     skills = []
#     grouped = df.groupby('Programming Skill')
#     for skill, group in grouped:
#         student_list = group[['Student Name', 'School Name']].values.tolist()
#         random.shuffle(student_list)
#         skills.append((skill, student_list))

#     # Form teams
#     teams = [[] for _ in range(max_entries // 3)]
#     team_index = 0
#     for skill, students in skills:
#         while students:
#             if len(teams[team_index]) < 3:
#                 teams[team_index].append(students.pop())
#             team_index = (team_index + 1) % len(teams)

#     return teams

# # API endpoint to get the current teams
# @app.route('/teams', methods=['GET'])
# def get_teams():
#     teams = fetch_and_create_teams()
#     return jsonify(teams)

# if __name__ == '__main__':
#     app.run(debug=True)

import gspread
import pandas as pd
import random
from flask import Flask, jsonify
from flask_cors import CORS

# Initialize Flask app
app = Flask(__name__)
CORS(app) 


gc = gspread.service_account(filename='credentials.json')
sh = gc.open_by_key('1-NDPq_BWp2IUNGkJ1he8jfnrbYMDNS_XzY10UTOpkU0')
worksheet = sh.sheet1


def fetch_and_create_teams():
    res = worksheet.get_all_records()
    df = pd.DataFrame(res)
    

    total_entries = df.shape[0]
    max_entries = (total_entries // 3) * 3
    df = df.head(max_entries)


    skills = []
    grouped = df.groupby('Programming Skill')
    for skill, group in grouped:
        student_list = group[['Student Name', 'School Name']].values.tolist()
        random.shuffle(student_list)
        skills.append((skill, student_list))


    teams = [[] for _ in range(max_entries // 3)]
    team_index = 0
    for skill, students in skills:
        while students:
            if len(teams[team_index]) < 3:
                teams[team_index].append(students.pop())
            team_index = (team_index + 1) % len(teams)

    return teams


@app.route('/teams', methods=['GET'])
def get_teams():
    teams = fetch_and_create_teams()
    return jsonify(teams)

if __name__ == '__main__':
    app.run(debug=True)



# flask --app main.py --debug run