import tkinter as tk
from tkinter import *
import os
import os.path
from tkinter import messagebox
import webbrowser
import socket as s
import time
import platform
import sys

while True:
    try:
        # Main info
        version = 'V 0.1 2021'
        bg_color = 'gray5'
        text_color = 'green3'
        home_dir = os.path.expanduser("~")
        font = "NSimSun 14"
        hostname = s.gethostname()
        local_ip = s.gethostbyname(hostname)
        local_time = time.asctime()

        # GUI
        win = tk.Tk()
        win.title('Alex Terminal 0.1')
        win.geometry("950x450")
        win.resizable(0, 0)

        win.configure(bg=bg_color)

        intro_text = f"""---------------------------------------------
ALEX IT Version[{version}]
(c) ALEX IT - 825. All rights reserved.
---------------------------------------------
        
{home_dir}>
        """
        commands_list = """
================== Commands List ===============
> custom      -- Terminal Appearance [Not ready]
> info        -- Terminal information
> open <url>  -- Open Web page
> ip          -- IP info
> clear / cls -- Clear 
> platform    -- Platform information
> time        -- Current time
> config      -- [Not ready]
> help / h    -- Commands list
> exit        -- Close terminal
=================================================
        """

        intro_lbl = tk.Label(text=intro_text, fg=text_color, bg=bg_color, justify='left', font=font)
        intro_lbl.grid(row=1, column=1)

        entry = tk.Entry(width=69, borderwidth=0, fg=text_color, font=font, insertbackground=text_color, bg=bg_color)
        entry.place(x=155, y=97)

        main = tk.Text(width=85,
                       borderwidth=0,
                       fg=text_color,
                       font=font,
                       insertbackground=text_color,
                       height=15,
                       bg=bg_color,
                       selectbackground='white',
                       selectforeground='green')
        main.place(x=0, y=125)

        # Commands
        def about():
            tk.messagebox.showinfo('INFO', "Version: 0.1\nCreating date: 21.03.21\nAuthor: AlexIT-825")

        def github():
            os.system('start https://github.com/AlexIT-825')

        def submit():
            global bg_color, text_color
            if entry.get() != '':
                if entry.get() == 'info':
                    tk.messagebox.showinfo('INFO', "Version: 0.1\nCreating date: 21.03.21\nAuthor: AlexIT-825")
                if 'open' in entry.get():
                    url = entry.get().split()
                    webbrowser.open(f'https://{url[1]}')
                if entry.get() == 'ip':
                    main.configure(state=NORMAL)
                    main.delete(1.0, END)
                    text = f'IP: {local_ip}\nHostname: {hostname}'

                    main.insert('end', text)
                    main.configure(state=DISABLED)
                if entry.get() == 'clear' or entry.get() == 'cls':
                    main.configure(state=NORMAL)
                    main.delete(1.0, END)
                    main.configure(state=DISABLED)
                    clear()
                if entry.get() == 'platform':
                    main.configure(state=NORMAL)
                    main.delete(1.0, END)
                    uname = platform.uname()
                    tech_info = f"""
                                \n========== System Information ==========
                                \nOS: {platform.system()}
                                \nRelease: {platform.release()}
                                \nVersion: {platform.version()}
                                \nMachine: {uname.machine}
                                \nProcessor: {uname.processor}
                                \nHostname: {hostname}
                        """
                    main.configure(state=NORMAL)
                    main.delete(1.0, END)
                    main.insert('end', tech_info)
                    main.configure(state=DISABLED)

                if entry.get() == 'time':
                    text = f'\nCurrent time: {time.asctime()}'
                    main.configure(state=NORMAL)
                    main.delete(1.0, END)
                    main.insert('end', text)
                    main.configure(state=DISABLED)
                if entry.get() == 'config':
                    main.configure(state=NORMAL)
                    main.delete(1.0, END)
                    main.configure(state=DISABLED)
                    pass
                if entry.get() == 'help' or entry.get() == 'h':
                    main.configure(state=NORMAL)
                    main.delete(1.0, END)
                    main.insert('end', commands_list)
                    main.configure(state=DISABLED)
                if entry.get() == 'custom':
                    main.configure(state=NORMAL)
                    main.delete(1.0, END)
                    text = """
        =============== Appearance ===============
        > custom 1 -- green text, black background
        > custom 2 -- white text, black background
                    """
                    main.insert('end', text)
                    main.configure(state=DISABLED)
                if entry.get() == 'custom 1':
                    main.configure(state=NORMAL)
                    main.delete(1.0, END)
                    bg_color = 'gray5'
                    text_color = 'green3'
                    text = 'COMPLETE'
                    main.insert('end', text)
                    main.configure(state=DISABLED)
                if entry.get() == 'custom 3':
                    main.configure(state=NORMAL)
                    main.delete(1.0, END)
                    bg_color = 'gray5'
                    text_color = 'white'
                    text = 'COMPLETE'
                    main.insert('end', text)
                    main.configure(state=DISABLED)
                if entry.get() == 'exit':
                    main.configure(state=NORMAL)
                    main.delete(1.0, END)
                    Exit()

        def clear():
            if entry.get() != '':
                entry.delete(0, END)

        def Exit():
            sys.exit()

        submit_btn = tk.Button(text='>>>', borderwidth=0, fg=text_color, width=10, bg='gray10', command=submit)
        submit_btn.place(x=860, y=97)

        clear_btn = tk.Button(text='<', borderwidth=0, fg=text_color, width=5, bg='gray15', command=clear)
        clear_btn.place(x=830, y=97)

        # Title bar
        menu = Menu()
        win.config(menu=menu)

        aboutMenu = Menu(menu, tearoff=0)
        aboutMenu.add_command(label="Info...", command=about)

        githubMenu = Menu(menu, tearoff=0)
        githubMenu.add_command(label="GitHub ->", command=github)

        exitMenu = Menu(menu, tearoff=0)
        exitMenu.add_command(label="Exit >", command=Exit)

        menu.add_cascade(label='About', menu=aboutMenu)
        menu.add_cascade(label='GitHub', menu=githubMenu)
        menu.add_cascade(label='Exit', menu=exitMenu)

        win.mainloop()
    except Exception:
        pass