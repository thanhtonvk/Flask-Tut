from flask import Flask, request, render_template, redirect, url_for
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


@app.route('/student/delete/<int:id_hs>')
def deletion_student(id_hs):
    if not id_hs or id_hs != 0:
        student = get_student_by_id(id_hs)
        if student:
            delete(id_hs)
            return redirect('/student')
    return 'Failed'


@app.route('/student', methods=['GET', 'POST'])
def main_student():
    students = get_all_student()
    if request.method == 'POST':
        timkiem = request.form['timkiem']
        if timkiem:
            students = [student for student in students if timkiem in student.name]
    return render_template('student.html', list_student=students)


upload_folder = './upload_file/'


@app.route('/upload', methods=['GET', 'POST'])
def uploader_file():
    if request.method == 'POST':
        f = request.files['file']
        file_path = upload_folder + f.filename
        f.save(file_path)
        students = read_student_from_excel(file_path)
        for student in students:
            insert_student(student)
        return redirect('/student')
    return render_template('upload.html')


if __name__ == '__main__':
    app.run()
