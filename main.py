import mysql.connector


def get_database_connection():
    connection = mysql.connector.connect(user='shakiba4',
                                         password='233255090',
                                         host='10.8.37.226',
                                         database='shakiba4_db')
    return connection


def execute_statement(connection, statement):
    cursor = connection.cursor()
    cursor.execute(statement)
    query_results = []

    for row in cursor:
        query_results.append(row)

    cursor.close()
    connection.close()

    return query_results


def get_student_schedule(student_id):
    statement = "CALL getStudentSchedule(" + student_id + ");"
    return execute_statement(get_database_connection(), statement)

def get_specific_class_grades(student_id, class_id):
    statement = "CALL getClassGrade(" + student_id + ", " + class_id + ");"
    return execute_statement(get_database_connection(), statement)

def get_teacher_schedule(teacher_id):
    statement = "CALL getTeacherSchedule(" + teacher_id + ");"
    return execute_statement(get_database_connection(), statement)


person_type = input("Choose your login type [student/teacher/administrator]: ")
person_type = person_type.lower()

person_id = input("Enter your id: ")

query_results = ""

if person_type == "student":
    action = input("Type in a number from the list below to choose an action:\n1. View schedule\n2. View grades for a specific class\n3.View overall grade")
    if action == "1":
        query_results = get_student_schedule(person_id)
    elif action == "2":
        query_results = get_specific_class_grades(person_id)
    elif action == "3":

elif person_type == "teacher":
    action = input("Type in a number from the list below to choose an action:\n1. View schedule\n2. View grades for a specific class\n3.View overall grade")
    if action == "1":
        query_results = get_teacher_schedule(person_id)
elif person_type == "administrator":
    print("yes")  # do nothing for now
else:
    print("ERROR WITH PERSON TYPE")

for result in query_results:
    if action == "1":
        class_id = str(result[0])
        period = str(result[2])
        course = result[3]
        room = result[4]
        teacher_first_name = result[5]
        teacher_last_name = result[6]
        print("Class ID: " + class_id)
        print("Period: " + period)
        print("Course: " + course)
        print("Room: " + room)
        print("Teacher: " + teacher_first_name + " " + teacher_last_name)
        print()
