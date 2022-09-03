from flask import Flask, request, render_template, redirect, url_for

from models.Student import Student
from dal.Student_DAL import *

app = Flask(__name__)


@app.route('/student/create', methods=['GET', 'POST'])
def create_student():
    if request.method == 'GET':
        return render_template('create_student.html')
    if request.method == 'POST':
        name = request.form['student_name']
        date_of_birth = request.form['student_date_of_birth']
        address = request.form['student_address']
        student = Student(name=name, dateOfBirth=date_of_birth, address=address)
        insert_student(student)
        return redirect('/student')


@app.route('/student/update/<int:id_hs>', methods=['GET', 'POST'])
def update_student(id_hs):
    if not id_hs or id_hs != 0:
        student = get_student_by_id(id_hs)
        if student:
            if request.method == 'GET':
                return render_template('update_student.html', student=student)
            if request.method == 'POST':
                student.name = request.form['student_name']
                student.dateOfBirth = request.form['student_date_of_birth']
                student.address = request.form['student_address']
                update(student)
                return redirect('/student')
    return 'Failed'


@app.route('/student/index')
@app.route('/student', methods=['GET'])
def main_student():
    students = get_all_student()
    return render_template('student.html', list_student=students)


if __name__ == '__main__':
    app.run()
