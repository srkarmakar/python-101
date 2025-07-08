# Skills required for the job
required_skills = {
    'HTML', 'CSS', 'JavaScript', 'React', 'TypeScript', 'Redux', 'Responsive Design', 'Git',
    'Node.js', 'Express', 'MongoDB', 'SQL', 'REST APIs', 'GraphQL', 'Docker', 'Testing', 'CI/CD', 'Python'
}
#Showing all skills in required_skills
print('Required Skill for Fullstack Developer')
for skill in required_skills:
    print(skill)

#Skill Present or Not
SRK_skills ={'HTML', 'CSS', 'JavaScript','TypeScript','Responsive Design', 'Git', 'Angular'}
if list(SRK_skills)[0] in required_skills:
    print(list(SRK_skills)[0],"Skill Present!")
else:
    print(list(SRK_skills)[0],"Skill not Present!")

#Adding Skills
print('Old Skill',SRK_skills)
SRK_skills.add('Python')
print('Added Skill',SRK_skills)

#Update Skills
updated_skills = ['Testing', 'Apache-Superset']
SRK_skills.update(updated_skills)
print('Updated Skill',SRK_skills)