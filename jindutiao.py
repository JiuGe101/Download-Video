import tkinter as tk
 
root = tk.Tk()
 
text = tk.Text(root)
text.pack()
 
# "insert" ������ʾ�����굱ǰ��λ��
text.insert("insert", "I love ")
text.insert("end", "Python.com!")
 
root.mainloop()