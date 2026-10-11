# **notes-storage**
Store notes with data (year, month, day, hour, minute, second) and contet in utf-8

## IMPORTANT
For some motivation, the sys and os modules works if you import them AFTER using.  
So please don't open an issue or a Pull Request for this **unless isn't working for you**.  

## details:
You can keep a detailed diary, and no one is gonna add stuff to your register without the password!  
The default password is `1999`, but you can easily change it at line 4.  

Basically, the code works with this:  
```python
def enternote():
    global notepath
    global addtx
    addtx = TextEntry.get()
    with open(str(notepath), "a", encoding="utf-8") as file:
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"[{current_time}]\n{addtx}\n")
        file.write("_" * 40 + "\n")
```
Utf-8 is a formatting option.  

It actually includes every character in the Unicode standard, which means it supports over 150,000 characters covering almost every modern and  
historical written language, as well as emojis, math symbols, and technical notation.  

Password and Log Path is defined at lines 3-4.  

The program is fully written in [Python](https://www.python.org/), a local-based language.  
You can dowload the interpreter on [the official python organiztion site.](https://www.python.org/downloads/)  

## Libraries
### Not-preinstalled modules:
**Keyboard**  
more details - [https://pypi.org/project/keyboard](https://pypi.org/project/keyboard/)  
Here, keyboard module is used for direct entering button-less.  

**Customtkinter**  
more details - [https://customtkinter.tomschimansky.com](https://customtkinter.tomschimansky.com/)  
The amazing plug-in for the basic pre-installed library called Tkiner.  

Used for the interface (text entries, labels...)  
### Basic python modules:
**Tkinter**  
Basic version of CustomTkinter, used for errors/infos windows.  
more details - [https://docs.python.org/3/library/tkinter](https://docs.python.org/3/library/tkinter.html)  

**Sys**  
Module for system reading and infos, useful.  
more details - [https://docs.python.org/3/library/sys](https://docs.python.org/3/library/sys.html)  

**Os**  
Module to communicate with the os.  
more details . [https://docs.python.org/3/library/os](https://docs.python.org/3/library/os.html)  

**DateTime**  
Module to take the actual timezone's date (Y, M, D, h, m, s).  
more details - [https://docs.python.org/3/library/datetime](https://docs.python.org/3/library/datetime.html)  

# Console log
The program prints on the console a very long actions log:  
```
actions log
defining target file path
deining pre-functions
importing modules
 | catching import errors
 | interface module importing
 | interface module imported
 | keyboard module importing
 | keyboard module imported
 | sys, os modules importing
 | sys, os modules imported
 | datetime moule importing
 | datetime module imported
no import errors found
loading source
source loaded
loading interface
 | interface root initialized
 | interface title created
 | interface root created
 | interface icon resetted
 | creating interface labels
defining functions
functions defined
loading labels 2nd block
labels 2nd block loaded
adding keyboard shortcuts
keyboards shortcuts added
packaging interface labels
interface labels packaged
interface loaded
opening root
program exit
```
*note: this is the log **IF THE PROGRAM DOESN'T ENCOUNTERS ERRORS***  
The console log is a debug feature, but is also useful to **know what the program really does.**  

* Debug: if at a certain point the program outputs an error in the terminal, you'll see what actions it completed before the error.  
* Other: what the program really does in background?? You'll see that in the log!!  

# Pull requests, issues and other
Feel free to make an issue if you find an error.  
But, if you can SOLVE THAT ERROR, **open a pull request instead!**  

The only thing i ask is:  
Please try to avoid spam or not useful pull requests.  
Open an issue if there's a bug, NOT IF YOU GUESS there's a bug.  

If you think a part of the code would fail, try it.  
If it does, open an issue or a pull request.  

You can also open an issue or a PR because:  
* You found a security flaw. Please report it in an issue.  
* You want to suggest an edit. Open a pull reuqest!  

Also, please, add in the pull request your Name or NickName, or some socials link,  
so i can add you in the credits section here.  

Thank you.  

# configuartion
## step 1 - target file path
Go to line 3. You'll see `notepath = "log.txt"`. Replace it with the path of txt file.  
**Attention: don't use \ or / for the path. Use \\\\.**  

## step 2 - modules installation
To use this program you'll have to install a few libraries:  
open your terminal and type  

`pip install keyboard`  
`pip install customtkinter`  

# credits
<details>
  <summary><b>topojinn</b></summary>
    main coder - topojinn (Erma)
    <br>
    <br>
    join topojinn's discord server - https://discord.gg/UK7TacmKRu  
    <br>
    see topojinn's newgrounds profile - https://topojinn.newgrounds.com  
    <br>
    check flowlab.io community profile - https://community.flowlab.io/u/topojinn.game/summary  
  </details>
 
