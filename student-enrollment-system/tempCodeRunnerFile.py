
@app.route('/')
def enrollment_form():
    return render_template('index.html')

# Route to handle form submission
@app.route('/enroll', methods=['POST'])
def enroll_student():
    student_name = request.form['student_name']
    father_name = request.form['father_name']
    email = request.form['email']
    phone = request.form['phone']
    address = request.form['address']
    city = request.form['city']
    state = request.form['state']
    pin_code = request.form['pin_code']
    department = request.form['department']
    course = request.form['course']
    comments = request.form['comments']

    # Connecting to the MySQL database
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    # SQL query to insert data into the students table
    sql = '''INSERT INTO students 
             (student_name, father_name, email, phone, address, city, state, pin_code, department, course, comments)
             VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'''

    values = (student_name, father_name, email, phone, address, city, state, pin_code, department, course, comments)

    try:
        cursor.execute(sql, values)
        conn.commit()
        return redirect(url_for('enrollment_form'))  # Redirect to the form or a success page
    except Exception as e:
        print(f"Error: {e}")
        conn.rollback()
        return "There was an error enrolling the student."

    finally:
        cursor.close()
        conn.close()

if __name__ == '__main__':
    app.run(debug=True)
