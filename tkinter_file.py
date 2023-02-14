import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title("Registration")

collegee = ["College of Arts and Creative Enterprises", ["College of Business"],
            ["College of Communication and Media Sciences"],
            ["College of Education"], ["College of Humanities and Social Sciences"],
            ["College of Natural and Health Sciences"], ["College of Technological Innovation"]]
maj = [["Animation Design"], ["Graphic Design"], ["Interior Design"], ["Visual Arts"], ["Multimedia Design"],
       ["Accounting"], ["Finance"], ["Human Resource Management"], ["Marketing and Entrepreneurship"],
       ["Media Production and Storytelling"], ["Integrated Strategic Communications"],
       ["Tourism and Cultural Communications"], ["Early Childhood Education"], ["International Relations"],
       ["Middle East/Gulf Studies"], ["Political Economy and Development"],
       ["Environmental Science and Sustainability"], ["Public Health and Nutrition"], ["Psychology"],
       ["Security and Network Technologies"], ["Web and Mobile Application Development"],
       ["Enterprise Systems"], ["Management of Information Systems"], ["Business Intelligence"]]

term = [["Fall"], ["Spring"], ["Summer"]]


class University:
    def __init__(self, master):
        self.master = master
        self.name = tk.Label(master, text="Welcome to Zayed University!")
        self.name.grid(row=1, column=2)

        self.add = tk.Label(master, text="Our university is located in Dubai!")
        self.add.grid(row=2, column=2)

        self.web1 = tk.Label(master, text="Please ensure you are write")
        self.web1.grid(row=3, column=2)

        self.web2 = tk.Label(master, text="Your details correctly! to register")
        self.web2.grid(row=4, column=2)

        self.name = tk.Label(master, text="Enter Your First Name")
        self.name.grid(row=5, column=1)

        self.fname = tk.Entry(width=40)
        self.fname.grid(row=5, column=2)

        self.surname = tk.Label(master, text="Enter Your Last Name")
        self.surname.grid(row=6, column=1)

        self.sname = tk.Entry(width=40)
        self.sname.grid(row=6, column=2)

        self.number = tk.Label(master, text="Enter Your Contact Number")
        self.number.grid(row=7, column=1)

        self.num = tk.Entry(width=40)
        self.num.grid(row=7, column=2)

        self.id = tk.Label(master, text="Enter Your ID Number")
        self.id.grid(row=8, column=1)

        self.idd = tk.Entry(width=40)
        self.idd.grid(row=8, column=2)

        self.gender = tk.Label(master, text="Gender")
        self.gender.grid(row=9, column=1, sticky="w")

        self.gender = tk.StringVar()
        r1 = tk.Radiobutton(text="Male", variable=self.gender, value="Male")
        r1.grid(row=9, column=2)

        r2 = tk.Radiobutton(text="Female", variable=self.gender, value="Female")
        r2.grid(row=9, column=3)

        self.college = tk.Label(master, text="Which college?")
        self.college.grid(row=10, column=1)

        self.col = tk.StringVar(master)
        self.col.set(collegee[0])
        self.coll = tk.OptionMenu(master, self.col, *collegee)
        self.coll.grid(row=10, column=2)

        self.major = tk.Label(master, text="What is your major?")
        self.major.grid(row=11, column=1)

        self.mjorr = tk.StringVar(master)
        self.mjorr.set(maj[0])
        self.mjor = tk.OptionMenu(master, self.mjorr, *maj)
        self.mjor.grid(row=11, column=2)

        self.advice = tk.Label(master, text="Type of advising?")
        self.advice.grid(row=12, column=1)

        self.advice = tk.StringVar()
        a1 = tk.Radiobutton(text="Current", variable=self.advice, value="Current")
        a1.grid(row=12, column=2)

        a2 = tk.Radiobutton(text="Future", variable=self.advice, value="Future")
        a2.grid(row=12, column=3)

        self.GPA = tk.Label(master, text="Enter Your GPA")
        self.GPA.grid(row=13, column=1)

        self.gp = tk.Entry(width=15)
        self.gp.grid(row=13, column=2)

        self.term = tk.Label(master, text="Which semester?")
        self.term.grid(row=14, column=1)

        self.trm = tk.StringVar()
        self.trm.set(term[0])
        self.terrm = tk.OptionMenu(master, self.trm, *term)
        self.terrm.grid(row=14, column=2)

        self.enter = tk.Button(master, text="Enter", command=self.register)
        self.enter.grid(row=15, column=2)

        self.exit = tk.Button(master, text="Exit", command=self.exit)
        self.exit.grid(row=15, column=3)

    def register(self):
        if self.fname.get() != '' != self.sname.get() != '' != self.num.get() != '' \
                != self.idd.get() != '' != self.gender.get() != '' != self.coll != '' != self.mjor != '' != \
                self.advice != '' != self.gp.get() != '' != self.terrm != '\n':
            print(self.fname.get(), " ", self.sname.get(), " ", self.num.get(), " ", self.idd.get(), " ",
                  self.gender.get(), " ", self.coll, " ", self.mjor, " ", self.advice, " ", self.gp.get(), " ",
                  self.terrm)
        else:
            tk.messagebox.showwarning(title="Warning", message="Kindly complete the missing information")


    def exit(self):
        window.destroy()

    def save(self):
        first_name = self.fname.get()
        last_name = self.sname.get()
        contact_info = self.num.get()
        email_add = self.idd.get()
        department = self.gender.get()
        credit = self.coll
        reg_date = self.mjor
        previous_stud = self.advice
        password = self.gp.get()
        reg_id = self.terrm

        data = '\n' + first_name + '\t' + last_name + '\t' + contact_info + \
               '\t' + email_add + '\t' + department + '\t' + credit + '\t' + reg_date + \
               '\t' + previous_stud + '\t' + password + '\t' + reg_id
        file = open('Registration.txt', 'a')
        file.write(data)
        file.close()


r = University(window)
window.mainloop()
