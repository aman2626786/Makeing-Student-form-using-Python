# Importing module using import function
from tkinter import *

# define a variable getvalue to input user info
def getvalue():
    print(f"STUDENT NAME:{namevalue.get()}")
    print(f"STUDENT COLLEGE:{collegevalue.get()}")
    print(f"STUDENT STATE:{statevalue.get()}")
    print(f"STUDENT COURSE:{coursevalue.get()}")
    print(f"STUDENT PHONE NO:{phonenovalue.get()}")
    print(f"STUDENT FATHER NAME:{fathervalue.get()}")
    print(f"STUDENT MOTHER NAME:{mothervalue.get()}")
    print(f"PARENT MOBILE NO:{parentsmobilenovalue.get()}")
    print(f"STUDENT WORKING SKILLS:{workvalue.get()}")
    print(f"STUDENT HOBBY:{hobbyvalue.get()}")
    with open("StudentInformation.txt","a") as f:
        f.write(f"\nSTUDENT INFO:\nSTUDENT NAME:{namevalue.get()},\nSTUDENT COLLEGE:{collegevalue.get()},\nSTUDENT STATE:{statevalue.get()},"
              f"STUDENT COURSE:{coursevalue.get()},\nSTUDENT PHONE NO:{phonenovalue.get()},\nSTUDENT FATHER NAME:{fathervalue.get()},\n"
              f"STUDENT MOTHER NAME:{mothervalue.get()},\nPARENT MOBILE NO:{parentsmobilenovalue.get()},\nSTUDENT WORKING SKILLS:{workvalue.get()},"
              f"STUDENT HOBBY:{hobbyvalue.get()}")


root = Tk()
# Geometry of our GUI interface (hint:root.geometry(X_axis x Y_axis)
root.geometry('600x400')
# Title of GUI
root.title('Student Login Form')
# Title of form ex:Student login form, Eximination form, official form etc.
title = Label(root, text='Student Login Form:', fg='black', font='Helvetica 15 bold')
title.grid(row=1, column=2, padx=5)
# Give option for taking info.
# Personal information
personal = Label(root, text='PERSONAL INFO:', fg='black', font='Helvetica 10 bold')
personal.grid(row=2, column=2, pady=5)
name = Label(root, text='STUDENT NAME', font='Helvetica 10')
name.grid(row=3, column=2)
college = Label(root, text='STUDENT COLLEGE', font='Helvetica 10')
college.grid(row=4, column=2)
state = Label(root, text='STUDENT STATE', font='Helvetica 10')
state.grid(row=5, column=2)
course = Label(root, text='STUDENT COURSE', font='Helvetica 10')
course.grid(row=6, column=2)
phone_no = Label(root, text='STUDENT PHONE NO', font='Helvetica 10')
phone_no.grid(row=7, column=2)
# Family information
family_info = Label(root, text='STUDENT FAMILY INFO:', font='Helvetica 10 bold ')
family_info.grid(row=8, column=2, pady=5)
father = Label(root, text='STUDENT FATHER NAME', font='Helvetica 10')
father.grid(row=9, column=2)
mother = Label(root, text='STUDENT MOTHER NAME', font='Helvetica 10')
mother.grid(row=10, column=2)
parents_mobile_no = Label(root, text='PARENTS MOBILE NO', font='Helvetica 10')
parents_mobile_no.grid(row=11, column=2)
# Working Skills or Hobby
work_info = Label(root, text='STUDENT WORK INFO', font='Helvetica 10 bold')
work_info.grid(row=12, column=2, pady=5)
work = Label(root, text='STUDENT WORKING SKILL', font='Helvetica 10')
work.grid(row=13, column=2)
hobby = Label(root, text='STUDENT HOBBY', font='Helvetica 10')
hobby.grid(row=14, column=2)

# Give entry box
namevalue = StringVar()
collegevalue = StringVar()
statevalue = StringVar()
coursevalue = StringVar()
phonenovalue = IntVar()
fathervalue = StringVar()
mothervalue = StringVar()
parentsmobilenovalue = IntVar()
workvalue = StringVar()
hobbyvalue = StringVar()
nameentry = Entry(root, textvariable=namevalue)
collegeentry = Entry(root, textvariable=collegevalue)
stateentry = Entry(root, textvariable=statevalue)
courseentry = Entry(root, textvariable=coursevalue)
phonenoentry = Entry(root, textvariable=phonenovalue)
fatherentry = Entry(root, textvariable=fathervalue)
motherentry = Entry(root, textvariable=mothervalue)
parentsmobilenoentry = Entry(root, textvariable=parentsmobilenovalue)
workentry = Entry(root, textvariable=workvalue)
hobbyentry = Entry(root, textvariable=hobbyvalue)
nameentry.grid(row=3, column=3, padx=5)
collegeentry.grid(row=4, column=3, padx=5)
stateentry.grid(row=5, column=3, padx=5)
courseentry.grid(row=6, column=3, padx=5)
phonenoentry.grid(row=7, column=3, padx=5)
fatherentry.grid(row=9, column=3, padx=5)
motherentry.grid(row=10, column=3, padx=5)
parentsmobilenoentry.grid(row=11, column=3, padx=5)
workentry.grid(row=13, column=3, padx=5)
hobbyentry.grid(row=14, column=3, padx=5)

# Give Button command to show submit button and save user info
Button(text='SUBMIT', command=getvalue, font='Helvetica 10 bold', fg='red').grid(row=15, column=3, pady=5)

root.mainloop()