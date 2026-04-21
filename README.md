# Thika Medical System

## Features
- Multi-user login
- Admin dashboard
- Student management
- GPA grading
- PDF report generation

## Default logins
admin/admin123
lecturer/lect123
student/stud123

## How to run
1. Install requirements:
   pip install reportlab

2. Run:
   python main.py


##simple explanation of the project



# Thika School of Medical and Health Sciences Student Management System

This project is a **desktop application built using Python** that helps manage student records in a school.
The system allows administrators and lecturers to **store, manage, and generate student academic records**.

The system uses:

* Python
* Tkinter
* JSON file storage instead of a database
* ReportLab for generating result slips.

---

# 1. Login System

The system starts with a **login window** where users enter a username and password.

There are three types of users:

* **Admin**
* **Lecturer**
* **Student**

The system checks the credentials from the **users.json** file and grants access depending on the user's role.

This is called **role-based access control**.

---

# 2. Dashboard

After login, the user sees a **dashboard window** created using Tkinter.

The dashboard provides options such as:

* Add student
* View students
* Generate student reports

Different users have different permissions.

For example:

* **Admin** can add students
* **Lecturers** can view student records
* **Students** can view their academic information

---

# 3. Student Management

The system allows the admin to **add student details**, including:

* Student name
* Course
* Marks

These records are stored in a **JSON file called data.json**, which acts like a simple database.

This demonstrates **file handling and data storage in Python**.

---

# 4. GPA / Grade Calculation

The system automatically calculates a **grade** based on marks.

Example grading:

* 70 and above → A
* 60–69 → B
* 50–59 → C
* 40–49 → D
* Below 40 → F

This feature demonstrates **basic algorithm logic in Python**.

---

# 5. PDF Result Slip Generation

The system can generate **student result slips in PDF format** using the library ReportLab.

Each report contains:

* Student name
* Course
* Marks
* Grade

The generated reports are saved in the **reports folder**.

This feature demonstrates **automation and document generation**.

---

# 6. Graphical User Interface

The entire system uses **Tkinter**, which is a built-in GUI library in Python.

The interface includes:

* Login window
* Dashboard
* Forms for adding students
* Display windows for student records

