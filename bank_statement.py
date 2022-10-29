import csv
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkmacosx import Button
from tkinterdnd2 import DND_FILES, TkinterDnD
from tkinter.font import Font

def read_csv():
    global my_csv_file
    my_csv_file = file_input.get('1.0', END)
    my_csv_file = my_csv_file.removesuffix('\n')

    with open(my_csv_file, mode = 'r') as file:
        bank_statement = csv.reader(file)
        if my_csv_file != '':      
            for rows in bank_statement:
                # 0 - transaction date
                # 1 - post date
                # 2 - description
                # 3 - category
                # 4 - type
                # 5 - amount
                # 6 - memo
                transaction_date.append(rows[0])
                description.append(rows[2])
                category.append(rows[3])
                amount.append(rows[5])
                csv_rows.append(rows)
        else:
            messagebox.showinfo(title=None, message='Please input a file first')
        sort_list()

def sort_list():
    # all values in list amount are in type:str
    resize_window()
    amount[0] = '0'
    int_amount = [eval(a) for a in amount] # changing all string amounts to int amounts

    # sort by category
    for index, i in enumerate(category): # looping through the category list and grabbing the index of each item in list
        trans_date = transaction_date[index]
        desc = description[index]
        amou = amount[index].removeprefix('-')
        if i == 'Food & Drink' or i == 'Shopping': # grabbing all transactions from Food & Drink cateogry  
            amount[index].removeprefix('-') # removing the negative sign coming from a charge on the account
            output.insert(INSERT, trans_date + "    " + desc + " " + amou + '\n\n')
        
        # grabbing all transactions from Shopping category and outputing to new Text called shopping_output

def resize_window():
    w = 1400
    h = 1000
    root.geometry(f"{w}x{h}")

def input_button():
    try:
        read_csv()
    except:
        if my_csv_file == '':
            messagebox.showinfo(title=None, message='No file inputed')
        else:
            messagebox.showinfo(title=None, message='File does not exist')
        pass

def reset_button():
    w = 500
    h = 1000
    root.geometry(f"{w}x{h}")
    file_input.delete("1.0", END)
    output.delete("1.0", END)

def quit_button():
    root.destroy()

if __name__ == '__main__':
    # root = Tk()
    root = TkinterDnD.Tk()
    root.title('은행 명세서 분석이') # title of gui window
    root.geometry("500x1000") # size of entire gui

    # Buttons for bank
    bank_label = Label(root, text='은행을 선택 하세요:', font=(root, 20))
    bank_label.grid(row=0, column=0)
    amex = Button(root, text='AMEX')
    amex.grid(row=0, column=1)
    boa = Button(root, text='BOA')
    boa.grid(row=0, column=2)
    citi = Button(root, text='CITI')
    citi.grid(row=0, column=3)

    # area for file input
    file_label = Label(root, text='파일: ', font=(root, 20))
    file_label.grid(row=1, column=0, columnspan=4, sticky=W, padx=5)
    file_input = Text(root, height=1, width=30, font=(root, 20))
    file_input.grid(row=1, column=0, columnspan=4, sticky=W, padx=50)
    file_input.config(highlightthickness=2, highlightbackground='black')
    # registering file_input as area for drop target
    file_input.drop_target_register(DND_FILES)
    file_input.dnd_bind('<<Drop>>', lambda e: file_input.insert(END, e.data))

    # submit button
    submit_button = Button(root, text='입력', command=input_button, font=(root, 20))
    submit_button.grid(row=2, column=0, columnspan=2)
    submit_button.config(height=50, width=100, bg='green', fg='white')

    # reset button
    submit_button = Button(root, text='재설정', command=reset_button, font=(root, 20))
    submit_button.grid(row=2, column=2, columnspan=1)
    submit_button.config(height=50, width=100, bg='red', fg='white')

    # quit button
    quit_button = Button(root, text='그만두다', command=quit_button,font=(root, 20))
    quit_button.grid(row=3, column=0, columnspan=4)

    # labels above output boxes
    date_label = Label(root, text='날짜', font=(root, 30))
    date_label.grid(column=4, row=0, padx=(40,0), pady=(20,0), sticky=W)
    date_label = Label(root, text='아이템', font=(root, 30))
    date_label.grid(column=4, row=0, padx=(220,0), pady=(20,0), sticky=W)
    date_label = Label(root, text='금액', font=(root, 30))
    date_label.grid(column=4, row=0, padx=(500,0), pady=(20,0), sticky=W)

    # output data box
    output = Text(root, height=30, width=50, font=(root, 25))
    output.grid(row=1, column=4, rowspan=3, padx=(40,0))
    output.config(highlightthickness=2, highlightbackground='black')

    # padding for bottom of gui
    #hidden_label = Label(root, text='')
    #hidden_label.grid(row=4, column=0, columnspan=4, pady=10)

    csv_rows = [] # entire csv file

    # columns of csv file
    category = []
    transaction_date = []
    description = []
    amount = []

    root.mainloop()