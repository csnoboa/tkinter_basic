import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.listWidgets = []
        self.listWidgetsButtons = []

        self.entrythingy = tk.Entry(self)
        self.entrythingy.pack(side="top")


        self.contents = tk.StringVar(self)
        self.contents.set("coloque a sua tarefa")
        self.entrythingy["textvariable"] = self.contents

        self.entrythingy.bind('<Key-Return>',
                             self.print_contents)

        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Nova Tarefa"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.delete_button = tk.Button(self)
        self.delete_button["text"] = "Deletar todas as tarefas"
        self.delete_button["command"] = self.delete_all
        self.delete_button.pack()



        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    def print_contents(self, event):
        print("Hi. The current entry content is:",
              self.contents.get())

    def say_hi(self):
        newDo = tk.Label(self, text=self.contents.get())
        newDo.pack(side="bottom")
        self.listWidgets.append(newDo)

    def delete_all(self):
        for i in self.listWidgets:
            i.destroy()



root = tk.Tk()
app = Application(master=root)
app.master.title("My To-Do")
app.master.minsize(400, 400)
app.mainloop()