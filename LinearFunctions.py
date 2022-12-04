import tkinter as tk

class Program:
    def __init__(self):
        # Creating window
        self.window = tk.Tk()
        self.window.title('Linear Functions')

        # Creating left panel    
        self.LeftPanel = tk.Frame(self.window)
        self.LeftPanel.grid(row=0,column=0)
        tk.Label(self.LeftPanel, text="y = ").grid(row=0, column=0)
        e1 = tk.Entry(self.LeftPanel); e1.grid(row=0,column=1)
        tk.Button(self.LeftPanel,text='Draw Function',command=self.__DrawFunction()).grid(row=1,column=0,columnspan=2)

        # Creating right panel
        self.canvas_width = 600
        self.canvas_height = 600
        self.canvas = tk.Canvas(self.window,width=self.canvas_width,height=self.canvas_height, background="white")
        self.canvas.grid(row=0,column=1)
    def __DrawAxes(self):
        # todo
    def __DrawFunction(self):
        # todo
    def Run(self):
        self.window.mainloop()

program = Program()
program.Run()