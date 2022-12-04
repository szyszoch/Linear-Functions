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

        # Creating canvas
        self.canvas_width = 600
        self.canvas_height = 600
        self.canvas = tk.Canvas(self.window,width=self.canvas_width,height=self.canvas_height, background="white")
        self.canvas.grid(row=0,column=1)

        self.__DrawAxes()

    def __DrawAxes(self):

        axes_spacing = 25
        axes_count = int(self.canvas_width/axes_spacing)
        main_axes_width = 3

        # X axes
        for i in range(axes_count):
            self.canvas.create_line(0,axes_spacing*i,self.canvas_width,axes_spacing*i)
        # Y axes
        for i in range(axes_count):
            self.canvas.create_line(axes_spacing*i,0,axes_spacing*i,self.canvas_height)

        # Main x axis
        self.canvas.create_line(0,axes_spacing*axes_count/2,self.canvas_width,axes_spacing*axes_count/2,width=main_axes_width)

        # Main y axis
        self.canvas.create_line(axes_spacing*axes_count/2,0,axes_spacing*axes_count/2,self.canvas_height,width=main_axes_width)


    def __DrawFunction(self):
        d= 0
    def Run(self):
        self.window.mainloop()

program = Program()
program.Run()