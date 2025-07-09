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
print('Old Skill ::',SRK_skills)
SRK_skills.add('Python')
print('Added Skill ::',SRK_skills)

#Update Skills
updated_skills = ['Testing', 'Apache-Superset']
SRK_skills.update(updated_skills)
print('Updated Skill ::',SRK_skills)

#Removing unnecessary skills
SRK_skills.discard('Responsive Design')
print('Updated Skills after discarding unnecessary skills ::',SRK_skills)

try:
    SRK_skills.remove('Responsive Design')
    print('Updated Skills after removing unnecessary skills ::',SRK_skills)
except KeyError as e:
    print(f"Error: {e}")

poped_skill = SRK_skills.pop()
print('Skills you are best at ::',poped_skill)

#Joining Sets
# Skills required for Java Backend Developer
java_backend_skills = {
    'Java', 'Spring Boot', 'Hibernate', 'REST APIs', 'SQL', 'Maven', 'JUnit', 'Microservices',
    'Docker', 'Git', 'CI/CD', 'Security', 'Jenkins', 'Kafka'
}
print('Required Skills for Java Backend Developer::',java_backend_skills)

# Skills required for Angular Developer
angular_developer_skills = {
    'HTML', 'CSS', 'JavaScript', 'TypeScript', 'Angular', 'RxJS', 'NgRx', 'REST APIs',
    'Responsive Design', 'Git', 'Testing', 'Jasmine', 'Karma'
}

print('Required Skills for Angular Developer::',angular_developer_skills)

JAVA_full_stack_developer = angular_developer_skills.union(java_backend_skills)
print('Required Skills for Java-Angular Developer::',JAVA_full_stack_developer)

JAVA_full_stack_developer = angular_developer_skills | java_backend_skills
print('Required Skills for Java-Angular Developer::',JAVA_full_stack_developer)

most_important_skill_for_developer = angular_developer_skills.intersection(java_backend_skills)
print('Most Important Skills for Java-Angular Developer::',most_important_skill_for_developer)

# Skills of two Java Developer candidates
candidate1_skills = {'Java', 'Spring Boot', 'Hibernate', 'REST APIs', 'SQL', 'Git', 'Docker', 'JUnit'}
candidate2_skills = {'Java', 'Spring Boot', 'REST APIs', 'SQL', 'Maven', 'Git', 'Jenkins', 'Kafka'}

print('Candidate 1 Skills:', candidate1_skills)
print('Candidate 2 Skills:', candidate2_skills)
skill_difference = candidate1_skills.difference(candidate2_skills)
print("Skill differnce between 1st candidate from 2nd candidate::", skill_difference)