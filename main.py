print("actions log")
print("defining target file path")
notepath = "log.txt"
print("deining pre-functions")
def wrong():
    sys.exit(1)
    os._exit(1)
print("importing modules")
print(" | catching import errors")
try:
    print(" | interface module importing")
    import customtkinter as ctk
    from tkinter import messagebox
    print(" | interface module imported")
    print(" | keyboard module importing")
    import keyboard as key
    print(" | keyboard module imported")
    print(" | sys, os modules importing")
    import sys, os
    print(" | sys, os modules imported")
    print(" | datetime moule importing")
    from datetime import datetime
    print(" | datetime module imported")
    print("no import errors found")
except ModuleNotFoundError:
    print("module not found")
    print("error exit")
    wrong()
except ImportError:
    print("module import fail")
    print("error exit")
    wrong()
print("loading source")
print("source loaded")
print("loading interface")
root = ctk.CTk()
print(" | interface root initialized")
root.title("data notes")
print(" | interface title created")
root.geometry("800x600")
print(" | interface root created")
root.iconbitmap()
print(" | interface icon resetted")
print(" | creating interface labels")
SplitEntry = ctk.CTkLabel(root, text="") 
PassEntry = ctk.CTkEntry(
    root, 
    placeholder_text="insert passcode to continue", 
    width=250,
    height=35)
print("defining functions")
def note():
    global PassEntry
    global passStr
    global TextEntry
    global TextEntryBtn
    global enternote
    global NoteEntrySplit
    passStr = str(PassEntry.get())
    if passStr == "1999":
        NoteEntrySplit = ctk.CTkLabel(root, text="")
        NoteEntrySplit.pack()
        TextEntry = ctk.CTkEntry(
            root, 
            placeholder_text="insert note",
            width=250,
            height=35)
        TextEntry.pack()
        def enternote():
            print(" | defining note entering sub-function")
            global notepath
            global addtx
            addtx = TextEntry.get()
            with open(str(notepath), "a", encoding="utf-8") as file:
                current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                file.write(f"[{current_time}]\n{addtx}\n")
                file.write("_" * 40 + "\n")
                messagebox.showinfo("Note saved", "the note was saved in the file called log.txt\n" \
                "you can see that file at the path 'C:\\dev\\haxe\\log.txt'.")
        TextEntryBtn = ctk.CTkButton(root, text="save note", command=enternote)
        TextEntryBtn.pack()
    else:
        ErrorLabel = ctk.CTkLabel(root, text="The password is wrong. Aturomatic exit in 3 seconds.")
        ErrorLabel.pack() 
        print(" | password match fail")
        print(" | exit 3000 msec")
        print(" | exitcode 1")
        root.after(3000, wrong)
def exit():
    try:
        sys.exit(0)
    finally:
        print(" | exitcode 0")
        os._exit(0)
print("functions defined")
print("loading labels 2nd block")
SplitLabel = ctk.CTkLabel(root, text="") 
EnterBtn = ctk.CTkButton(root, text="proceed", command=note)
print("labels 2nd block loaded")
print("adding keyboard shortcuts")
key.add_hotkey('enter', note)
key.add_hotkey('esc', exit)
print("keyboards shortcuts added")
print("packaging interface labels")
SplitEntry.pack()
PassEntry.pack()
SplitLabel.pack()
EnterBtn.pack()
print("interface labels packaged")
print("interface loaded")
print("opening root")
root.mainloop()
print("program exit")
