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

student_id = input("Enter a student id: ")
query_results = get_student_schedule(student_id)

for result in query_results:
    period = str(result[1])
    course = result[2]
    room = result[3]
    teacher_first_name = result[4]
    teacher_last_name = result[5]
    print("Period: " + period)
    print("Course: " + course)
    print("Room: " + room)
    print("Teacher: " + teacher_first_name + " " + teacher_last_name)
    print()
