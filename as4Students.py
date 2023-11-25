import psycopg2
from psycopg2 import sql
from psycopg2 import errors 
from datetime import date
import pandas as pd                                                                                                                                                                                                                                                                             
import sys
#kaif ali - student number 101180909
class StudentsDb:
    def __init__(self,hostname, dbname, username, password, port):
        self.con = psycopg2.connect(
            host=hostname, dbname=dbname, user=username, password=password, port=port
        )
        self.curr = self.con.cursor()
    
    def create_table(self):
        # Creating the students table
        create_table_query = '''
            CREATE TABLE IF NOT EXISTS students (
                student_id SERIAL PRIMARY KEY,
                first_name TEXT NOT NULL,
                last_name TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE,
                enrollment_date DATE
            );
        '''
        self.curr.execute(create_table_query)
        self.con.commit()

    def populate_initial_data(self):
        # Populating the students table with initial data
       
        initial_data_query = '''INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES
        ('John', 'Doe', 'john.doe@example.com', '2023-09-01'),
        ('Jane', 'Smith', 'jane.smith@example.com', '2023-09-01'),
        ('Jim', 'Beam', 'jim.beam@example.com', '2023-09-02')
        ON CONFLICT (email) DO NOTHING;'''
        self.curr.execute(initial_data_query)
        self.con.commit()
    
    def getAllStudents(self):

        try:
           # Retrieve and display all records from the students table
           query = 'SELECT * FROM students;'
           self.curr.execute(query)
           self.con.commit()
           students = self.curr.fetchall()
           print(f"Number of students: {len(students)}")
           print("All Students:")
           print("--------------")
           for student in students:
               print(f"Student ID: {student[0]}, First Name: {student[1]}, Last Name: {student[2]}, Email: {student[3]}, Enrollment Date: {student[4]}")

        except Exception as e:
           print(f"Error: {e}")
  
    def addStudent(self, first_name, last_name, email, enrollment_date):
        # Insert a new student record into the table
        query = '''
            INSERT INTO students (first_name, last_name, email, enrollment_date) 
            VALUES (%s, %s, %s, %s) RETURNING student_id;
        '''
        try:
            self.curr.execute(query, (first_name, last_name, email, enrollment_date))
            student_id = self.curr.fetchone()[0]
            self.con.commit()
            print(f"Student added successfully with ID: {student_id}")
        except psycopg2.IntegrityError as e:
            print(f"Error: {e}")
            self.con.rollback()
    
    def updateStudentEmail(self, student_id, new_email):
        # Update the email address for a student with the specified student_id
        query = 'UPDATE students SET email = %s WHERE student_id = %s;'
        try:
            self.curr.execute(query, (new_email, student_id))
            self.con.commit()
            print(f"Email updated successfully for student ID: {student_id}")
        except psycopg2.Error as e:
            print(f"Error: {e}")
            self.con.rollback()

    def deleteStudent(self, student_id):
        # Delete the record of the student with the specified student_id
        query = 'DELETE FROM students WHERE student_id = %s RETURNING *;'
        try:
            self.curr.execute(query, (student_id,))
            deleted_student = self.curr.fetchone()
            self.con.commit()
            if deleted_student:
                print(f"Student deleted successfully: {deleted_student}")
            else:
                print(f"No student found with ID: {student_id}")
        except psycopg2.Error as e:
            print(f"Error: {e}")
            self.con.rollback()

    


    def close_connection(self):
        if self.con:
            self.con.close()
            



if __name__ == "__main__":
    
    #used to set a default if the argv value is less than 2, hence setting the init.
    if len(sys.argv) < 2:
        #print("Usage: python script_name.py <action>")
        sys.exit(1)
        
    
    action = sys.argv[1]
    

    db = StudentsDb(
        hostname="localhost", dbname="students", username="postgres", password="Hewson27", port=5432
    )
    
    if action == "init":
        
        db.create_table()
        db.populate_initial_data()

    elif action == "getAllStudents":
       db.getAllStudents()
    
    elif action == "addStudent":
        first_name = sys.argv[2]
        last_name = sys.argv[3]
        email = sys.argv[4]
        enrollment_date = sys.argv[5]
        db.addStudent(first_name, last_name, email, enrollment_date)

    elif action == "updateStudentEmail":
        student_id = sys.argv[2]
        new_email = sys.argv[3]
        db.updateStudentEmail(student_id, new_email)
    elif action == "deleteStudent":
        student_id = sys.argv[2]
        db.deleteStudent(student_id)
    else:
        print("Invalid action. Use 'init', 'get_all_students', 'add_student', 'update_student_email', or 'delete_student'.")