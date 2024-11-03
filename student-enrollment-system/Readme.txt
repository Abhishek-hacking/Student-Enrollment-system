Student Enrollment System

Overview:
The Student Enrollment System is a web application built with Flask that allows students to register for courses and administrators to manage student records. This application features student registration, admin login, and a dashboard for managing student data.

Features:
- Student enrollment form to collect student information.
- Admin login for managing student records.
- View, edit, and delete student records from an admin dashboard.
- Responsive design for an optimal user experience on various devices.
- Environment variables for secure database configuration.

Technologies Used:
- Backend: Flask
- Database: MySQL
- Frontend: HTML, CSS, JavaScript
- Environment Management: dotenv for handling environment variables

Installation:

Prerequisites:
- Python 3.x
- MySQL server
- pip

Clone the Repository:
1. Open your terminal/command prompt.
2. Clone the repository:
   git clone https://github.com/Abhishek-hacking/student-enrollment-system.git
3. Change to the project directory:
   cd student-enrollment-system

Setup the Environment:
1. Create a virtual environment:
   python -m venv venv
2. Activate the virtual environment:
   - On Windows:
     venv\Scripts\activate
   - On macOS/Linux:
     source venv/bin/activate

3. Install the required packages:
   pip install -r requirements.txt

Create a .env File:
1. Create a .env file in the root directory and add the following environment variables:
   SECRET_KEY=your_secret_key
   DB_USER=your_db_username
   DB_PASSWORD=your_db_password
   ADMIN_USERNAME=your_admin_username
   ADMIN_PASSWORD=your_admin_password

Database Setup:
1. Create a MySQL database named student_enrollment.
2. Create a table for students with the following SQL command:
   CREATE TABLE students (
       create database student_enrollment;
 	id INT AUTO_INCREMENT PRIMARY KEY,
 	student_name VARCHAR(255) NOT NULL,
 	father_name VARCHAR(255),
 	email VARCHAR(255) NOT NULL,
 	phone VARCHAR(15),
 	address TEXT,
 	city VARCHAR(100),
 	state VARCHAR(100),
 	pin_code VARCHAR(10),
 	department VARCHAR(100),
 	course VARCHAR(100),
 	comments TEXT
	);


Running the Application:
To run the application, use the following command:
flask run
You can access the application at http://127.0.0.1:5000/.

Usage:
1. Student Registration: Navigate to the home page and click on "Register" to fill out the enrollment form.
2. Admin Login: Access the admin dashboard by navigating to /admin/login and enter the admin credentials.
3. Manage Records: After logging in, you can view, edit, or delete student records in the admin dashboard.

Contributing:
Contributions are welcome! If you have suggestions for improvements or want to report issues, feel free to open an issue or submit a pull request.


Acknowledgements:
- Flask documentation: Flask (https://flask.palletsprojects.com/)
- MySQL Connector for Python: mysql-connector-python (https://pypi.org/project/mysql-connector-python/)
