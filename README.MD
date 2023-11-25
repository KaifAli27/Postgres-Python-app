syed kaif ali - student no 101180909

This is the README file for as4Students.py . A python application that creates and operates CRUD operations on a postgres Database.

The file is structured in a OOP python class called StudentsDB which is initialized with an init method in which we pass in the connection parameters to the postgres database. I used the psycopg2 library which
is a Postgres adapter for python application.
My connection parameters at stored in a variable called db.

With the help of python cursor object, we can execute sql commands from within the python script, which is what is used in this application.

the method create_table passes in the sql query that sets up the students table in the database with the fields and constraints provided in the assignment. Which is set up when first running the application with init,
The table is also initialized with the three starting rows with the method populate_initial_data which passes in an sql INSERT INTO query with the help of cursor and cursor.execute/cursor.commit

To implement auto-incrementing of the student_id for the students, the SERIAL data type is used in sql which allows sql to handling the id and automatically add and incremenete it.

The user then has the option to apply four CRUD operations to this table called students with 3 entries. All functions are run in a similar way, the passing a sql query stored in a variable and executing and committing changes using the python cursor. Print statements are used to display errors, output results and display successful messages.

CRUD Functions

All functions are placed inside a try/exception block to help error handling and rpevent the function from failing. There are dedicated error messages printed out to the user to help the user recorrect the problem. There is also a confirmation message to re assure the user that the operation was successfull and the changes have been applied.

getAllStudents - This function fetches and retrieves all existing entries in the students table from the database and prints them out in the terminal in a sequential format. It prints out the total number of students along with the information of each student. It does this passing in a sql query stored in the variable query, which is executed and commited using cursor. the fetchAll is a pre defined function in the cursor libary that does the same.

addStudent - this function takes in four parameters when called (self, first_name, last_name, email, enrollment_date) and updates the database with the new student. Same as the above function, the query is passed and executed. Since the email of each student is unique, the function throws and error when trying to add a student which an email that already exists in the database. An example for running this function is - addStudent('ben','franklin','benjakn3@gmail.com','2000-12-12')

updateStudentEmail - this function takes in the student_id to locate the entry being altered as well as an email that will be updated to that student in the database. the fucntion is run in the terminal eg. updateStudentEmail(3,'speedokaif@gmail.com). This overwrites the existing email in the database to the new one.

deleteStudent - this function takes in a student_id and deletes the entry in the database for the corresponding student. it prints out that the student with the given id has been deleted. If there is no entry in the database with that student_id, the function outputs an error message stating 'no student found with that id'

if the user tries to use other functions not mentioned in the application or doesnt pass in a function, the application outputs an error message stating 'Invalid action. Use 'init', 'get_all_students', 'add_student', 'update_student_email', or 'delete_student'.'

Under the name == main , there is a set of if/elif functions that catch the keyword for the action being performed and execute the corresponding method in the class. action is default set to argv(1) which initalizing the table for the other crud operations to be performed. With the help of the python sys module, we can manipulate the functions required to run during the python runtime envirnonment

VIDEO LINK : https://youtu.be/dwbeuaUhAJQ
