# pylint: disable=missing-module-docstring
import os
import random
import tkinter
from tkinter import messagebox
from MODULE11_ui.app2 import LoginWindow
from functools import partial
from MODULE16.connect import send_mail,read_mail
import re


# pylint: disable=missing-class-docstring
class MenuWindow():
    # pylint: disable=missing-function-docstring
    def __init__(self, login_info:tuple):
        self.open_file=None
        self.user,self.passw=login_info

        root_window = tkinter.Tk()
        root_window.title("Menu")
        self.root_window = root_window

        main_menu = tkinter.Menu(root_window)
        self.root_window.config(menu=main_menu)

        file_menu = tkinter.Menu(main_menu)
        main_menu.add_cascade(label='File', menu=file_menu)

        edit_menu = tkinter.Menu(main_menu)
        main_menu.add_cascade(label="Edit", menu=edit_menu)

        view_menu = tkinter.Menu(main_menu)
        main_menu.add_cascade(label="View", menu=view_menu)

        send_menu = tkinter.Menu(main_menu)
        main_menu.add_cascade(label="Send", menu=send_menu)

        file_menu.add_command(label='New', command=self.file_new_menu)
        file_menu.add_separator()
        file_menu.add_command(label='Edit', command=self.file_edit_menu)
        file_menu.add_separator()
        file_menu.add_command(label='Close', command=self.file_close_menu)
        self.frame1 = tkinter.Frame(self.root_window, width=100, height=300)
        self.frame1.pack(side=tkinter.LEFT)

        refresh_button = tkinter.Button(self.frame1, text="Show Folders", command=self.get_directory)
        refresh_button.pack(side=tkinter.TOP)

        self.frame2 = tkinter.Frame(self.root_window)
        self.frame2.pack(side=tkinter.RIGHT)

        self.text = tkinter.Text(self.frame2, height=25, width=80)
        self.dest_entry = tkinter.Entry(self.frame2)
        self.subj_entry = tkinter.Entry(self.frame2)
        self.search_box = tkinter.Entry(self.frame2)
        self.searched_text = self.search_box.get()
        self.result = self.text.search(self.searched_text, "0.0", tkinter.END)

        self.read_button=tkinter.Button(self.root_window,text="read mails",command=self.read)
        self.read_button.pack()

    def read(self):
        read_mail(self.user,self.passw)

    def load_message(self, dir):
        with open(dir, 'r') as file:
            self.open_file = dir
            content = file.read()

            for line in content.splitlines():
                from_ = re.match(r"^From: (.+)",line)
                if from_:
                    self.user=from_.group(1)
                destination = re.search(r'^TO: (.+)', line)
                if destination:
                    self.dest_entry.insert("0",destination.group(1))
                    continue
                subject = re.search(r'^Subject: (.+)', line)
                if subject:
                    self.subj_entry.insert("0",subject.group(1))
                    continue
                self.text.insert(tkinter.END, line+"\n")




    def get_directory(self):
        for dir in os.listdir():
            if os.path.isdir(dir):
                label = tkinter.Label(self.frame1, text=str(dir))
                label.pack()
            else:
                command = partial(self.load_message, dir)
                label = tkinter.Button(self.frame1, text=str(dir), command=command)
                label.pack()

    def run(self):
        self.root_window.mainloop()


    @staticmethod
    def file_new_menu():
        print("Creating new file...")
        # self.root_window.mainloop()
        new_main_window = tkinter.Tk()
        new_main_window.title("Copy of menu")
        new_menu = MenuWindow(new_main_window)
        new_menu.run()

    def file_edit_menu(self):
        print("Editing new file...")
        destination = tkinter.Label(self.frame2, text="TO: ")
        destination.grid(row=0, column=0, sticky=tkinter.E)
        subject = tkinter.Label(self.frame2, text="Subject: ")
        subject.grid(row=1, column=0, sticky=tkinter.E)

        self.dest_entry.grid(row=0, column=1, sticky=tkinter.W)
        self.subj_entry.grid(row=1, column=1, sticky=tkinter.W)
        send_button = tkinter.Button(self.frame2, text="Send", command=self.send_message)
        send_button.grid(row=0, rowspan=2, column=2)
        search_button = tkinter.Button(self.frame2, text='Search', command=self.search_message)
        search_button.grid(row=3, column=0)
        self.search_box.grid(row=3, column=1, columnspan=2, sticky=tkinter.NE + tkinter.SW)

        self.text.grid(row=2, columnspan=3)

    def save(self):
        to=self.dest_entry.get()
        subj=self.subj_entry.get()
        text = self.text.get("0.0", tkinter.END)
        header=f"TO: {to}\nSubject: {subj}\n"
        result=header+text
        with open(self.open_file,'w') as file:
            file.write(result)
        return text,to

    def search_message(self):
        # pylint: disable=use-maxsplit-arg
        var = str(int(self.result.split('.')[1]) + len(self.searched_text))
        self.text.tag_add('selection', self.result, self.result.split(".")[0] + '.' + var)
        self.text.tag_config("selection", background="yellow")

    def send_message(self):
        if not self.dest_entry.get():
            messagebox.showinfo("Warning", "Missing destination")
            return
        if not self.subj_entry.get():
            messagebox.showinfo("Warning", "Missing subject")
            return
        if not self.text.get("0.0", tkinter.END).strip():
            messagebox.showinfo("Warning", "Missing text")
            return

        answer = messagebox.askquestion("Confirmation", "Are you sure you want to send?")
        if answer == "yes":
            print("Running code...")
            msg,to=self.save()
            send_mail(self.user,self.passw,msg,to)
        else:
            print("Canceling...")

    def file_close_menu(self):
        self.root_window.quit()


login = LoginWindow()
login.run()

menu = MenuWindow(login.login_info)
menu.run()
