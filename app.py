from flask import Flask, render_template

app = Flask(__name__)

@app.route('/students')
def students():
    students_data = [
        {'name': 'Alice', 'age': 20},
        {'name': 'Bob', 'age': 21},
        {'name': 'Charlie', 'age': 22},
        {'name': 'David', 'age': 56}
    ]
    return render_template('index.html', students=students_data)


@app.route('/student/<name>/<int:age>')
def student(name, age):

    return render_template('students.html', name=name, age=age)


@app.errorhandler(404)
def not_found(error):
    return 'Page Not Found'


if __name__ == '__main__':
    app.run(debug=True, port=5100)
