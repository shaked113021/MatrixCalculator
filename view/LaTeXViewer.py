import tkinter
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
matplotlib.use('TkAgg')
matplotlib.rcParams['font.size'] = 20
matplotlib.rcParams['text.usetex'] = True
matplotlib.rcParams['text.latex.preamble'] = r'\usepackage{{amsmath}}'
import pyperclip


class LaTeXViewer(tkinter.Toplevel):

    def __init__(self, parent, latex_string):
        super().__init__(parent)
        self.title('LaTex Viewer')

        self.__top_frame = tkinter.Frame(self)
        self.__top_frame.pack()
        self.__label = tkinter.Label(self.__top_frame)
        self.__label.pack()
        self.__figure = matplotlib.figure.Figure(figsize=(5, 5), dpi=100, layout='tight')
        self.__subplot = self.__figure.add_subplot(111)
        self.__canvas = FigureCanvasTkAgg(self.__figure, master=self.__label)
        self.__canvas.get_tk_widget().pack(fill=tkinter.BOTH, expand=True)

        self.__subplot.get_xaxis().set_visible(False)
        self.__subplot.get_yaxis().set_visible(False)
        self.__subplot.spines['top'].set_visible(False)
        self.__subplot.spines['right'].set_visible(False)
        self.__subplot.spines['bottom'].set_visible(False)
        self.__subplot.spines['left'].set_visible(False)

        self.__subplot.clear()
        self.__subplot.text(0.2, 0.6, f'${latex_string}$', fontsize=20)
        self.__canvas.draw()
        self.__bottom_frame = tkinter.Frame(self)
        self.__bottom_frame.pack()
        self.__copy_button = tkinter.Button(self.__bottom_frame, text='Copy LaTeX',
                                            command=lambda: pyperclip.copy(latex_string))
        self.__copy_button.pack(side=tkinter.LEFT)
        self.__close_button = tkinter.Button(self.__bottom_frame, text='Close',
                                             command= lambda: self.destroy())
        self.__close_button.pack(side=tkinter.LEFT)