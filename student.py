from tkinter import *
from tkinter.ttk import Combobox
from tkinter import ttk
import tkinter.messagebox
import sqlite3

window=Tk()
window.title('Student Details')
#window.geometry('800x500')

connection = sqlite3.connect('student.db')

TABLE_NAME = "student_table"
STUDENT_ID = "student_id"
STUDENT_NAME = "student_name"
STUDENT_SUB1 = "student_sub1"
STUDENT_SUB2 = "student_sub2"
STUDENT_SUB3 = "student_sub3"
STUDENT_SUB4 = "student_sub4"

connection.execute(" CREATE TABLE IF NOT EXISTS " + TABLE_NAME + " ( " + STUDENT_ID +
                   " INTEGER PRIMARY KEY, " +
                   STUDENT_NAME + " TEXT, " + STUDENT_SUB1 + " INTEGER, " +
                   STUDENT_SUB2 + " INTEGER, " + STUDENT_SUB3 + " INTEGER, " + STUDENT_SUB4 + " INTEGER);")
                   

class Student:
    studentID = 0
    studenName = ""
    sub_1 = 0
    sub_2 = 0
    sub_3 = 0
    sub_4 = 0
    
    
    def __init__(self, studentID, studentName, sub_1, sub_2, sub_3, sub_4):
        self.studentID = studentID
        self.studentName = studentName
        self.sub_1 = sub_1
        self.sub_2 = sub_2
        self.sub_3 = sub_3
        self.sub_4 = sub_4
    
def take_input():
    global student_ID_entry, student_name_entry, student_sub1_entry, student_sub2_entry, student_sub3_entry, student_sub4_entry
    # global studentname, sub1, sub2, sub3, sub4
    global list
    global TABLE_NAME, STUDENT_ID, STUDENT_NAME, STUDENT_SUB1, STUDENT_SUB2, STUDENT_SUB3, STUDENT_SUB4
    studentID = student_ID_entry.get()
    student_ID_entry.delete(0, END)
    studenName = student_name_entry.get()
    student_name_entry.delete(0, END)
    sub_1 = int(student_sub1_entry.get())
    student_sub1_entry.delete(0, END)
    sub_2 = int(student_sub2_entry.get())
    student_sub2_entry.delete(0, END)
    sub_3 = int(student_sub3_entry.get())
    student_sub3_entry.delete(0, END)
    sub_4 = int(student_sub4_entry.get())
    student_sub4_entry.delete(0, END)

    connection.execute("INSERT INTO " + TABLE_NAME + " ( " + STUDENT_ID + ", " + STUDENT_NAME + ", " +
                       STUDENT_SUB1 + ", " + STUDENT_SUB2 + ", " +
                       STUDENT_SUB3 + "," + STUDENT_SUB4 +" ) VALUES ( '" + studentID + "', '"
                       + studenName + "', '" + str(sub_1) + "', '" + str(sub_2) + "', '" + str(sub_3) + "', " 
                       + str(sub_4)+ " ); ")
    connection.commit()
    messagebox.showinfo("Success", "Data Saved Successfully.")

    
def displayWindow():
    display_Window = Tk()

    display_Window.title("Display results")

    appLabel = Label(display_Window, text="Student Details", fg="blue", width=40)
    appLabel.config(font=("Sylfaen", 30))
    appLabel.pack()

    tree = ttk.Treeview(display_Window)
    tree["columns"] = ("one", "two", "three", "four", "five", "six")

    tree.heading("one", text="Roll Number")
    tree.heading("two", text="Student Name")
    tree.heading("three", text="Subject1")
    tree.heading("four", text="Subject2")
    tree.heading("five", text="Subject3")
    tree.heading("six", text="Subject4")

    cursor = connection.execute("SELECT * FROM " + TABLE_NAME + " ;")
    i = 0

    for row in cursor:
        tree.insert('', i, values=(row[0], row[1], row[2], row[3], row[4], row[5]))
        i = i + 1

    tree.pack()
    display_Window.mainloop()

def conditional_del():
        
    condition_del = Tk()
    condition_del.title("Delete")
    condition_del.geometry("300x300")
       
    cond_lbl1=Label(condition_del, text='Roll Number')
    cond_lbl1.place(x=20,y=20)
    
    global cond_id_entry  
    cond_id_entry=Entry(condition_del, bd=2)
    cond_id_entry.place(x=140, y=20)
    
    
    cond_submit_btn= Button(condition_del, text="  Submit  ", fg='black', command = data_delete)
    cond_submit_btn. place(x=80, y=60)
    condition_del.mainloop()

def data_delete():
    stu_id = int(cond_id_entry .get())
    cond_id_entry .delete(0, END)
        
    connection.execute("DELETE  FROM " + TABLE_NAME + " WHERE " + STUDENT_ID + " = " + str(stu_id) + ";")
    connection.commit()
    messagebox.showinfo("Success", "Data deleted Successfully.")
    
    
def exitWindow():
    messagebox.showinfo("Exit","Closing Window.")
    window.destroy()

up_frame = Frame(window, cursor='hand1', height=100, width=800)
up_frame.grid_propagate(0)
up_frame.pack(side=TOP, expand=True, fill=BOTH)


welcomeText = Label(up_frame,text="Agent Details by Sathish",font=('Verdana', 16, 'roman italic'))
welcomeText.place(relx=.5, rely=.5, anchor='center')

down_frame = Frame(window, cursor='hand1', height=400,width=800)
down_frame.grid_propagate(0)
down_frame.pack(side=TOP, expand=True, fill=BOTH)


student_ID=Label(text='Roll Number')
student_name=Label(text='Name')
student_sub1=Label(text='Subject1')
student_sub2=Label(text='Subject2')
student_sub3=Label(text='Subject3')
student_sub4=Label(text='Subject4')

add_agent_btn= Button(down_frame, text="  Submit  ", fg='black',command=lambda :take_input())
displayButton = Button(down_frame, text=" Display result ", command=lambda :displayWindow())
condition_delete_btn= Button(down_frame, text=" Delete ", fg='black', command = conditional_del)
exitButton = Button(down_frame, text="    Exit    ", command=exitWindow)

student_ID_entry=Entry(bd=2)
student_name_entry=Entry(bd=2)
student_sub1_entry=Entry(bd=2)
student_sub2_entry=Entry(bd=2)
student_sub3_entry=Entry(bd=2)
student_sub4_entry=Entry(bd=2)

student_ID.place(x=40,y=140)
student_name.place(x=40,y=170)
student_sub1.place(x=40,y=200)
student_sub2.place(x=40,y=230)
student_sub3.place(x=40,y=260)
student_sub4.place(x=40,y=290)

student_ID_entry.place(x=140, y=140)
student_name_entry.place(x=140, y=170)
student_sub1_entry.place(x=140, y=200)
student_sub2_entry.place(x=140, y=230)
student_sub3_entry.place(x=140, y=260)
student_sub4_entry.place(x=140, y=290)

add_agent_btn.place(x=140,y=240)
displayButton.place(x=500, y=30)
condition_delete_btn.place(x=500, y=80)
exitButton.place(x=500, y=130)

window.mainloop()
