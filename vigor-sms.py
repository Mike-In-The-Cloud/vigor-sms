import tkinter as tk
from telnetConn import telnetConnection


fields = 'Host Address', 'UserName', 'Password', 'Message To', 'Text'

def fetch(entries):
    input_list = []
    for entry in entries:
        field = entry[0]
        text  = entry[1].get()
        input_list.append(text)
        # print('%s: "%s"' % (field, text)) 
    telnetConnection(input_list[0],input_list[1],input_list[2],input_list[3],input_list[4])
    


def makeform(root, fields):
    entries = []
    for field in fields:
        row = tk.Frame(root)
        lab = tk.Label(row, width=15, text=field, anchor='w')
        ent = tk.Entry(row)
        row.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
        lab.pack(side=tk.LEFT)
        ent.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.X)
        entries.append((field, ent))
    return entries





if __name__ == '__main__':
    root = tk.Tk()
    ents = makeform(root, fields)
    root.bind('<Return>', (lambda event, e=ents: fetch(e)))   

    btnSend = tk.Button(root, text='Send',
                  command=(lambda e=ents: fetch(e)))                  
    btnSend.pack(side=tk.LEFT, padx=5, pady=5)

    btnQuit = tk.Button(root, text='Quit', command=root.quit)
    btnQuit.pack(side=tk.LEFT, padx=5, pady=5)

    root.mainloop()