from tkinter import *
from tkinter import ttk

import Control.InsertData
from Control import Dropdown_Module , Search_Button , Export_Button , DateFormat , TimeFormat , TimerFormat ,Charts
from View import Frame_View

# ----------------------------------------------------Dropdown Frames --------------------------------------------------
Dropdowns_Frame = Frame(Frame_View.Window, width=150, height=100, relief='raised')

IO_Caller_Section_DD = Dropdown_Module.Dropdown(": مبدا تماس  ", "IO_Caller_Section", 0, 0)
Create_IO_Caller_Section_DD = IO_Caller_Section_DD.Create_Dropdown()

Caller_Channel_Code_DD = Dropdown_Module.Dropdown(": کد مبدا تماس", "Caller_Channel_Code", 1, 0)
Create_Caller_Channel_Code_DD = Caller_Channel_Code_DD.Create_Dropdown()

IO_Called_Section_DD = Dropdown_Module.Dropdown(": مقصد تماس", "IO_Called_Section", 2, 0)
Create_IO_Called_Section_DD = IO_Called_Section_DD.Create_Dropdown()

Called_Channel_Code_DD = Dropdown_Module.Dropdown(": کد مقصد تماس", "Called_Channel_Code", 3, 0)
Create_Called_Channel_Code_DD = Called_Channel_Code_DD.Create_Dropdown()

Status_DD = Dropdown_Module.Dropdown(": وضعيت تماس", "Status", 4, 0)
Create_Status_DD = Status_DD.Create_Dropdown()

Dropdowns_Frame.place(width=200, height=200, x=720, y=10)

# ----------------------------------------------Checkbox & Buttons Section ---------------------------------------------

Export_Data_Button = Dropdown_Module.Button(Frame_View.Window, text="خروجي اکسل", command=Export_Button.Export_Exel)
Export_Data_Button.configure(width=15)
Export_Data_Button.place(x=770, y=550)

Choose_File_Button = Button(Frame_View.Window, text='انتخاب فایل ...', command=Control.InsertData.Insert_Database)
Choose_File_Button.configure(width=15)
Choose_File_Button.place(x=90, y=550)

# --------------------------------------------# Period Frames ----------------------------------------------------------
# Period Frames
Periods_Frame = Frame(Frame_View.Window, relief='raised')
Periods_Frame.place(x=100, y=15)

Labels_Frame = Frame(Periods_Frame)
Textboxs_Frame = Frame(Periods_Frame)
Labels_Frame2 = Frame(Periods_Frame)
Button_Frame = Frame(Frame_View.Window)

Labels_Frame.grid(row=0, column=2)
Textboxs_Frame.grid(row=0, column=1)
Labels_Frame2.grid(row=0, column=0)
Button_Frame.place(x=165, y=180)

Get_Data_Button = Button(Button_Frame, text=" تهيه گزارش ", command=Search_Button.Click)
Get_Data_Button.configure(width=15, padx=5)
Get_Data_Button.grid(row=0, column=0)

Get_Details_Button = Button(Button_Frame, text="نمايش جزييات", command=Charts.Create)
Get_Details_Button.configure(width=15, padx=5, state='disabled')
Get_Details_Button.grid(row=1, column=0)

# Checkbox_Variable = IntVar()
# Checkbox = Checkbutton(Button_Frame, text=': حذف ايام تعطيل', variable=Checkbox_Variable)
# Checkbox.grid(row=0, column=1, padx=5)

Ring_Time_Label1 = Label(Labels_Frame, text=': زمان انتظار از')
Ring_Time_Label1.configure(pady=8)
Talk_Time_Label1 = Label(Labels_Frame, text=': زمان پاسخ از')
Talk_Time_Label1.configure(pady=8)
Date_Label1 = Label(Labels_Frame, text=': تاريخ از')
Date_Label1.configure(pady=8)
Time_Label1 = Label(Labels_Frame, text=': ساعت کاري از')
Time_Label1.configure(pady=8)

Ring_Time_Label1.grid(row=0, column=3)
Talk_Time_Label1.grid(row=1, column=3)
Date_Label1.grid(row=2, column=3)
Time_Label1.grid(row=3, column=3)

# Ring Time Frame
Ring_Time_Label2 = Label(Textboxs_Frame, text='تا')
Ring_Time_Label2.configure(pady=8)

Textbox1_Variable = StringVar()
Ring_Time_Textbox1 = Entry(Textboxs_Frame, width=25, textvariable=Textbox1_Variable)
Ring_Time_Textbox1.bind('<Key>', (lambda _: TimerFormat.Timer(Ring_Time_Textbox1)))

Textbox2_Variable = StringVar()
Ring_Time_Textbox2 = Entry(Textboxs_Frame, width=25, textvariable=Textbox2_Variable)
Ring_Time_Textbox2.bind('<Key>', (lambda _: TimerFormat.Timer(Ring_Time_Textbox2)))

Ring_Time_Textbox1.grid(row=0, column=2, pady=8)
Ring_Time_Label2.grid(row=0, column=1)
Ring_Time_Textbox2.grid(row=0, column=0, pady=8)

# Talk Time Frame
Talk_Time_Label2 = Label(Textboxs_Frame, text='تا')
Talk_Time_Label2.configure(pady=8)

Talk_Time_Variable1 = StringVar()
Talk_Time_Textbox1 = Entry(Textboxs_Frame, width=25, textvariable=Talk_Time_Variable1)
Talk_Time_Textbox1.bind('<Key>', (lambda _: TimerFormat.Timer(Talk_Time_Textbox1)))

Talk_Time_Variable2 = StringVar()
Talk_Time_Textbox2 = Entry(Textboxs_Frame, width=25, textvariable=Talk_Time_Variable2)
Talk_Time_Textbox2.bind('<Key>', (lambda _: TimerFormat.Timer(Talk_Time_Textbox2)))

Talk_Time_Textbox1.grid(row=1, column=2, pady=8)
Talk_Time_Label2.grid(row=1, column=1)
Talk_Time_Textbox2.grid(row=1, column=0, pady=8)

# Date Frame
Date_Label2 = Label(Textboxs_Frame, text='تا')
Date_Label2.configure(pady=8)

Date_Variable1 = StringVar()
Date_Textbox1 = Entry(Textboxs_Frame, width=25, textvariable=Date_Variable1)
Date_Textbox1.bind('<Key>', (lambda _: DateFormat.Date(Date_Textbox1)))

Date_Variable2 = StringVar()
Date_Textbox2 = Entry(Textboxs_Frame, width=25, textvariable=Date_Variable2)
Date_Textbox2.bind('<Key>', (lambda _: DateFormat.Date(Date_Textbox2)))

Date_Textbox1.grid(row=2, column=2, pady=8)
Date_Label2.grid(row=2, column=1)
Date_Textbox2.grid(row=2, column=0, pady=8)

# Time Frame
Time_Label2 = Label(Textboxs_Frame, text='تا')
Time_Label2.configure(pady=8)

Time_Variable1 = StringVar()
Time_Textbox1 = Entry(Textboxs_Frame, width=25, textvariable=Time_Variable1)
Time_Textbox1.bind('<Key>', (lambda _: TimeFormat.Time(Time_Textbox1)))

Time_Variable2 = StringVar()
Time_Textbox2 = Entry(Textboxs_Frame, width=25, textvariable=Time_Variable2)
Time_Textbox2.bind('<Key>', (lambda _: TimeFormat.Time(Time_Textbox2)))

Time_Textbox1.grid(row=3, column=2, pady=8)
Time_Label2.grid(row=3, column=1)
Time_Textbox2.grid(row=3, column=0, pady=8)

Ring_Time_Label3 = Label(Labels_Frame2, text='0:00', fg='snow4')
Ring_Time_Label3.configure(pady=8)

Talk_Time_Label3 = Label(Labels_Frame2, text='0:00', fg='snow4')
Talk_Time_Label3.configure(pady=8)

Date_Time_Label3 = Label(Labels_Frame2, text='1399/01/01', fg='snow4')
Date_Time_Label3.configure(pady=8)

Time_Label3 = Label(Labels_Frame2, text='08:00:00', fg='snow4')
Time_Label3.configure(pady=8)

Ring_Time_Label3.grid(row=0, column=0)
Talk_Time_Label3.grid(row=1, column=0)
Date_Time_Label3.grid(row=2, column=0)
Time_Label3.grid(row=3, column=0)

# -----------------------------------------------------Treeview --------------------------------------------------------

# Create Treeview In Frame
Table_Frame = Frame(Frame_View.Window, relief='raised', borderwidth=5)
Tree_View = ttk.Treeview(Table_Frame)
Y_ScrollBar = ttk.Scrollbar(Table_Frame, orient="vertical", command=Tree_View.yview)
X_ScrollBar = ttk.Scrollbar(Table_Frame, orient="horizontal", command=Tree_View.xview)

Tree_View.configure(yscrollcommand=Y_ScrollBar.set, xscrollcommand=X_ScrollBar.set)
Tree_View["columns"] = (
    "Date", "Year", "Month", "Day", "Time", "IO_Caller_Number", "IO_Caller_Number_Section", "Caller_Number",
    "Caller_Channel_Code", "Caller_Channel", "IO_Called_Number", "IO_Called_Number_Section", "Called_Number",
    "Called_Channel_Code", "Called_Channel", "Ring_Time", "Talk_Time", "Status", "Details")

Table_Frame.place(width=1000, y=250)
Y_ScrollBar.pack(side='left', fill='y')
Tree_View.pack()
X_ScrollBar.pack(side='bottom', fill='x')
Frame_View.Window.mainloop()

