from tkinter import *
import datetime
import json

#initialize tkinter
root = Tk()
root.geometry("700x500")
root.title(" SYS-AUDIT: Active Telemetry Shell")
root.configure(bg = "#1E1E1E")

#list with all alert Keywords
alerts = ["rm -rf", "sudo", "net user", "password", "nmap", "chmod 777", "shutdown", "id_rsa"]

#function that commits every line to a file and checks for suspiciios activity
def saveTextandCheck(event):
    #locates and gets current line
    current_line = inputtxt.index("insert").split('.')[0]
    INPUT = inputtxt.get(f"{current_line}.0", f"{current_line}.end")
    #removes prompt prefix 
    logtxt = INPUT.removeprefix("[ root@security-audit:~ ]# ")
    #console check
    print(logtxt)

    #traverses inputted line and checks for suspicious activity
    for trigger in alerts:
        if trigger in logtxt.lower():
            print("ALERT DETECTED")
            inputtxt.insert("insert", "\n[ALERT]: SUSPICIOUS ACTIVITY DETECTED\n")
            break

    #convert text into json format
    log_entry = {
        "timestamp":datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "identity": "root@security-audit",
        "raw_input": logtxt
    }
    #Insert log text into json file
    with open("activity_log.json", "a") as log_file:
        log_file.write(json.dumps(log_entry) + "\n")

    #new prompt line
    inputtxt.after(15, lambda: inputtxt.insert("insert", "\n[ root@security-audit:~ ]# "))

    # Overrides the default "Enter" key behavior so it doesn't create double blank lines
    return "break"


#to prevent prompt statement deletion
def prevent_prompt_delete(event):
    #gets cursor position in line
    cursor_column = int(inputtxt.index("insert").split('.')[1])
    
    if cursor_column <= 27:
        #return statement overrides backspace
        return "break"
    
# Terminal heading   
title = Label(text = "SYSTEM AUDIT TELEMETRY MONITOR",  fg = "#00FF00", bg = "#000000",font=("Consolas", 10, "bold"))
#Create input text box
inputtxt = Text(root,fg = "#00FF00",width=100,height=20, bg = "#000000",font=("Consolas",12))
#first prompt
inputtxt.insert("1.0", "[ root@security-audit:~ ]# ")


#binds enter and backspace to events
inputtxt.bind("<Return>",saveTextandCheck)
inputtxt.bind("<BackSpace>", prevent_prompt_delete)


title.pack()
inputtxt.pack()

mainloop()