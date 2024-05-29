import smtplib
import webbrowser

from tkinter.ttk import *
from tkinter import *


def sendmail():
    senders = from_.get()
    receivers = to_.get()
    password = pass_.get()
    subject = sub_.get()
    message = msg_text.get('1.0', 'end')
    main_message = """
    From: %s
    To: %s
    Subject: %s """ % (senders, receivers, subject, message)
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(senders, password)
    try:
        server.sendmail(senders, receivers, main_message)
        sent = Message(window,
                       text="Mail sent successfully").grid(row=6, columnspan=2)

    except:
        error = Label(window, text="Error please try again")

    server.close()


window = Tk()

window.title("Mailer")

global msg_text


def destry():
    window.quit()
    window.destroy()


def instruct():
    webbrowser.open_new(
        r"https://www.google.com/settings/security/lesssecureapps")


menub = Menu(window)
help_mail = Menu(menub, tearoff=0)
help_mail.add_command(label="Help", command=instruct)
menub.add_cascade(label="Instructions", menu=help_mail)

window.config(menu=menub)


def fclear(event):
    if from_entry.get() == "Enter your email id..":
        from_entry.delete(0, "end")
        from_entry.insert(0, "")
        from_entry.config(fg="black")


def tclear(event):
    if to_entry.get() == "Enter receivers email id..":
        to_entry.delete(0, "end")
        to_entry.insert(0, "")
        to_entry.config(fg="black")


def pclear(event):
    if pass_entry.get() == "Enter your accounts password..":
        pass_entry.delete(0, 'end')
        pass_entry.insert(0, "")
        pass_entry.config(fg="black")
    else:
        pass_entry.config(show="*")


def sclear(event):
    if sub_entry.get() == "Enter subject and start typing your mail below..":
        sub_entry.delete(0, 'end')
        sub_entry.insert(0, "")
        sub_entry.config(fg="black")


def fvisible(event):
    if from_entry.get() == "":
        from_entry.insert(0, "Enter your email id..")
        from_entry.config(fg="grey")


def tvisible(event):
    if to_entry.get() == "":
        to_entry.insert(0, "Enter receivers email id..")
        to_entry.config(fg="grey")


def pvisible(event):
    if pass_entry.get() == "":
        pass_entry.insert(0, "Enter your accounts password..")
        pass_entry.config(fg="grey")
    else:
        pass_entry.config(show="*")


def svisible(event):
    if sub_entry.get() == "":
        sub_entry.insert(0, "Enter subject and start typing your mail below..")
        sub_entry.config(fg="grey")


def numbs(c1, c2):
    return c1.isdigit()
    return c2.isdigit()


window.columnconfigure(0, pad=1, weight=1)
window.columnconfigure(1, pad=1, weight=1)
window.columnconfigure(2, pad=1, weight=1)
window.rowconfigure(0, pad=1, weight=1)
window.rowconfigure(1, pad=1, weight=1)
window.rowconfigure(2, pad=1, weight=1)
window.rowconfigure(3, pad=1, weight=1)
window.rowconfigure(4, pad=1, weight=1)
window.rowconfigure(5, pad=1, weight=1)
window.rowconfigure(6, pad=1, weight=1)
window.rowconfigure(7, pad=1, weight=1)
window.rowconfigure(8, pad=1, weight=1)
window.rowconfigure(9, pad=1, weight=1)
window.rowconfigure(10, pad=1, weight=1)
window.rowconfigure(11, pad=1, weight=1)
window.rowconfigure(12, pad=1, weight=1)

validation = window.register(numbs)

to_ = StringVar()
from_ = StringVar()
pass_ = StringVar()
sub_ = StringVar()
msg_text = StringVar()

note = Label(window,
             font="Ariel 13",
             fg="red",
             text="You have to turn ON 'Less Secure Apps'\
 in your google account \
             \n To do so click on Instructions")
note.grid(sticky="nsew", row=0, columnspan=3)

from_label = Label(window, text="From", relief=FLAT, font="Ariel 13")
from_label.grid(sticky="nsew", row=1, column=0, padx=5, pady=3)

se1 = Separator(window, orient=VERTICAL).grid(sticky="ns", row=1, column=1)

from_entry = Entry(window,
                   textvariable=from_,
                   relief=FLAT,
                   font="Ariel 13",
                   validate='key',
                   validatecommand=(validation, '%d', '%i'))
from_entry.grid(sticky="nsew",
                row=1,
                column=2,
                ipadx=130,
                ipady=5,
                padx=5,
                pady=3)
from_entry.insert(0, "Enter your email id..")
from_entry.insert(1, '')
from_entry.config(fg="black")
from_entry.bind("<FocusIn>", fclear)
from_entry.bind("<FocusOut>", fvisible)

sep1 = Separator(window, orient=HORIZONTAL).grid(sticky="we",
                                                 row=2,
                                                 columnspan=3)

to_label = Label(window, text="To", relief=FLAT, font="Ariel 13")
to_label.grid(sticky="nsew", row=3, column=0, padx=5, pady=3)

se2 = Separator(window, orient=VERTICAL).grid(sticky="ns", row=3, column=1)

to_entry = Entry(window,
                 textvariable=to_,
                 relief=FLAT,
                 font="Ariel 13",
                 validate='key',
                 validatecommand=(validation, '%d', '%i'))
to_entry.grid(sticky="nsew",
              row=3,
              column=2,
              ipadx=130,
              ipady=5,
              padx=5,
              pady=3)
to_entry.insert(0, "Enter receivers email id..")
to_entry.config(fg="black")
to_entry.bind("<FocusIn>", tclear)
to_entry.bind("<FocusOut>", tvisible)

sep2 = Separator(window, orient=HORIZONTAL).grid(sticky="we",
                                                 row=4,
                                                 columnspan=3)

pass_label = Label(window, text="Password", relief=FLAT, font="Ariel 13")
pass_label.grid(sticky="nsew", row=5, column=0, padx=5, pady=3)

se3 = Separator(window, orient=VERTICAL).grid(sticky="ns", row=5, column=1)

pass_entry = Entry(window,
                   textvariable=pass_,
                   relief=FLAT,
                   font="Ariel 13",
                   validate='key',
                   validatecommand=(validation, '%d', '%i'))
pass_entry.grid(sticky="nsew",
                row=5,
                column=2,
                ipadx=80,
                ipady=5,
                padx=5,
                pady=3)
pass_entry.insert(0, "Enter your accounts password..")
pass_entry.bind("<FocusIn>", pclear)
pass_entry.bind("<FocusOut>", pvisible)

sep3 = Separator(window, orient=HORIZONTAL).grid(sticky="we",
                                                 row=7,
                                                 columnspan=3)

sub_label = Label(window, text="Subject", relief=FLAT, font="Ariel 13")
sub_label.grid(sticky="nsew", row=8, column=0, padx=5, pady=3)

se4 = Separator(window, orient=VERTICAL).grid(sticky="ns", row=8, column=1)

sub_entry = Entry(window,
                  textvariable=sub_,
                  relief=FLAT,
                  font="Ariel 13",
                  validate='key',
                  validatecommand=(validation, '%d', '%i'))
sub_entry.grid(sticky="nsew",
               row=8,
               column=2,
               ipadx=80,
               ipady=4,
               padx=5,
               pady=3)
sub_entry.insert(0, "Enter subject and start typing your mail below..")
sub_entry.bind("<FocusIn>", sclear)
sub_entry.bind("<FocusOut>", svisible)

msg_label = Label(window, text="Message", relief=FLAT, font="Ariel 13")
msg_label.grid(sticky="nsew", row=9, column=0, padx=5, pady=3)

se5 = Separator(window, orient=VERTICAL).grid(sticky="ns", row=9, column=1)

msg_text = Text(window, relief=FLAT, font="Ariel 13", height=15, width=50)
msg_text.grid(sticky="nsew", row=9, column=2, padx=5, pady=3)
scrollbar = Scrollbar(window)
scrollbar.grid(row=9, column=3, sticky='ns')
msg_text.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=msg_text.yview)

sep3 = Separator(window, orient=HORIZONTAL).grid(sticky="we",
                                                 row=10,
                                                 columnspan=3)

send = Button(window,
              command=sendmail,
              text="Send",
              font="Ariel 13",
              relief="raised",
              borderwidth=3).grid(row=11, column=2, ipadx=10, padx=5, pady=3)
cancel = Button(window,
                command=destry,
                text="Cancel",
                font="Ariel 13",
                relief="raised",
                borderwidth=3).grid(row=12, column=2, ipadx=10, padx=5, pady=3)

window.mainloop()
