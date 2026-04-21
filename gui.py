import tkinter as tk
from tkinter import messagebox
import json
from reportlab.pdfgen import canvas
import os

def load_users():
    with open("users.json") as f:
        return json.load(f)

def load_students():
    try:
        with open("data.json") as f:
            return json.load(f)
    except:
        return []

def save_students(data):
    with open("data.json", "w") as f:
        json.dump(data, f, indent=4)

def calc_gpa(marks):
    if marks >= 70:
        return "A"
    elif marks >= 60:
        return "B"
    elif marks >= 50:
        return "C"
    elif marks >= 40:
        return "D"
    else:
        return "F"

def generate_pdf(student):
    os.makedirs("reports", exist_ok=True)
    c = canvas.Canvas(f"reports/{student['name']}.pdf")
    c.drawString(100, 800, "THIKA MEDICAL SCHOOL RESULT SLIP")
    c.drawString(100, 750, f"Name: {student['name']}")
    c.drawString(100, 730, f"Course: {student['course']}")
    c.drawString(100, 710, f"Marks: {student['marks']}")
    c.drawString(100, 690, f"Grade: {calc_gpa(student['marks'])}")
    c.save()

def login_screen():
    root = tk.Tk()
    root.title("Login System")
    root.geometry("300x200")

    tk.Label(root, text="Username").pack()
    user = tk.Entry(root)
    user.pack()

    tk.Label(root, text="Password").pack()
    pwd = tk.Entry(root, show="*")
    pwd.pack()

    def login():
        users = load_users()
        for u in users:
            if u["username"] == user.get() and u["password"] == pwd.get():
                root.destroy()
                open_dashboard(u["role"])
                return
        messagebox.showerror("Error", "Invalid Login")

    tk.Button(root, text="Login", command=login).pack()
    root.mainloop()

def open_dashboard(role):
    win = tk.Tk()
    win.title(role.upper()+" DASHBOARD")
    win.geometry("400x400")

    students = load_students()

    def add_student():
        top = tk.Toplevel(win)
        tk.Label(top, text="Name").pack()
        name = tk.Entry(top); name.pack()
        tk.Label(top, text="Course").pack()
        course = tk.Entry(top); course.pack()
        tk.Label(top, text="Marks").pack()
        marks = tk.Entry(top); marks.pack()

        def save():
            students.append({
                "name": name.get(),
                "course": course.get(),
                "marks": int(marks.get())
            })
            save_students(students)
            messagebox.showinfo("Success", "Student Added")

        tk.Button(top, text="Save", command=save).pack()

    def view_students():
        top = tk.Toplevel(win)
        for s in students:
            tk.Label(top, text=f"{s['name']} | {s['course']} | {s['marks']} | {calc_gpa(s['marks'])}").pack()

    def export_pdf():
        for s in students:
            generate_pdf(s)
        messagebox.showinfo("Done", "PDF Generated")

    tk.Label(win, text=f"Logged in as {role}").pack()

    if role == "admin":
        tk.Button(win, text="Add Student", command=add_student).pack()

    tk.Button(win, text="View Students", command=view_students).pack()
    tk.Button(win, text="Generate PDF Reports", command=export_pdf).pack()

    win.mainloop()
