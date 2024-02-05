import tkinter
import tkinter.messagebox as messagebox
from calculator import RealMatrixCalculator, MatrixCalculator, ComplexMatrixCalculator, FiniteMatrixCalculator
from controller import MatrixController
from .MatrixFrame import MatrixFrame
from .LaTeXViewer import LaTeXViewer
from model import Mode
from sympy import latex


class MainWindow(tkinter.Tk):

    def __init__(self, controller: MatrixController):
        super().__init__()
        self.__controller = controller
        self.__real_matrix_calculator = RealMatrixCalculator(controller)
        self.__complex_matrix_calculator = ComplexMatrixCalculator(controller)
        self.__finite_matrix_calculator = FiniteMatrixCalculator(controller)
        self.__matrix_calculator: MatrixCalculator = self.__real_matrix_calculator
        self.resizable(False, False)
        self.title('Matrix Calculator')
        validate_mat_size_range = self.register(self.__validate_mat_size_range)
        validate_modulus_range = self.register(self.__validate_modulus_range)
        self.__top_frame = tkinter.Frame(self)
        self.__n_value = tkinter.StringVar()
        self.__n_label = tkinter.Label(self.__top_frame, text='n: ')
        self.__n_spinbox = tkinter.Spinbox(self.__top_frame, from_=1, to=30, textvariable=self.__n_value, width=3,
                                           validate='all', validatecommand=(validate_mat_size_range, '%P'))

        def set_n(*args):
            if self.__n_value.get() != '':
                self.__controller.set_n(int(self.__n_value.get()))

        self.__n_value.trace('w', set_n)
        self.__m_value = tkinter.StringVar()
        self.__m_label = tkinter.Label(self.__top_frame, text='m: ')
        self.__m_spinbox = tkinter.Spinbox(self.__top_frame, from_=1, to=30, textvariable=self.__m_value, width=3,
                                           validate='all', validatecommand=(validate_mat_size_range, '%P'))

        def set_m(*args):
            if self.__m_value.get() != '':
                self.__controller.set_m(int(self.__m_value.get()))

        self.__m_value.trace('w', set_m)
        self.__mode_value = tkinter.StringVar()
        self.__mode_option_list = tkinter.OptionMenu(self.__top_frame, self.__mode_value, 'Real Numbers',
                                                     'Complex Numbers', 'Finite Integer Field')
        self.__mode_value.set('Real Numbers')
        self.__mode_value.trace('w', self.__on_mode_changed)
        self.__modulus_label = tkinter.Label(self.__top_frame, text='mod: ')
        self.__modulus_value = tkinter.StringVar()
        self.__modulus_spinbox = tkinter.Spinbox(self.__top_frame, from_=1, to=100, textvariable=self.__modulus_value,
                                                 width=4, state=tkinter.DISABLED,
                                                 validate='all', validatecommand=(validate_modulus_range, '%P'))

        def set_modulus(*args):
            if self.__modulus_value.get() != '':
                self.__controller.set_modulus(int(self.__modulus_value.get()))

        self.__modulus_value.trace('w', set_modulus)

        self.__top_frame.pack()
        self.__n_label.grid(row=0, column=0)
        self.__n_spinbox.grid(row=0, column=1)
        self.__m_label.grid(row=0, column=2)
        self.__m_spinbox.grid(row=0, column=3)
        self.__mode_option_list.grid(row=1, column=0)
        self.__modulus_label.grid(row=1, column=1)
        self.__modulus_spinbox.grid(row=1, column=2)
        self.__matrix_frame = MatrixFrame(self, self.__controller)
        self.__matrix_frame.pack()
        self.__calculate_button = tkinter.Button(self, text='Calculate', command=self.__on_calculate_clicked)
        self.__calculate_button.pack()

        self.__error_not_full = messagebox.Message(title='Matrix is not full', parent=self,
                                                   icon=messagebox.ERROR, type=messagebox.OK,
                                                   message='Please fill all cells')

    @classmethod
    def __validate_mat_size_range(cls, str_in):
        if str_in == '':
            return True
        else:
            try:
                value = int(str_in)
            except ValueError:
                return False
            if value < 1 or value > 30:
                return False
            return True

    @classmethod
    def __validate_modulus_range(cls, str_in):
        if str_in == '':
            return True
        else:
            try:
                value = int(str_in)
            except ValueError:
                return False
            if value < 1 or value > 100:
                return False
            return True

    def __on_mode_changed(self, *args):
        mode_str = self.__mode_value.get()
        current_mode = self.__controller.get_mode()
        if mode_str == 'Real Numbers' and current_mode.value != Mode.REAL_NUMBERS:
            self.__controller.set_mode(Mode(Mode.REAL_NUMBERS))
            self.__modulus_spinbox.config(state=tkinter.DISABLED)
            self.__matrix_calculator = self.__real_matrix_calculator
        elif mode_str == 'Complex Numbers' and current_mode.value != Mode.COMPLEX_NUMBERS:
            self.__controller.set_mode(Mode(Mode.COMPLEX_NUMBERS))
            self.__modulus_spinbox.config(state=tkinter.DISABLED)
            self.__matrix_calculator = self.__complex_matrix_calculator
        elif mode_str == 'Finite Integer Field' and current_mode.value != Mode.FINITE_FIELD:
            self.__modulus_spinbox.config(state=tkinter.NORMAL)
            self.__controller.set_mode(Mode(Mode.FINITE_FIELD))
            self.__matrix_calculator = self.__finite_matrix_calculator

    def __on_calculate_clicked(self):
        if self.__controller.is_full():
            matrix = self.__matrix_calculator.calculate()
            LaTeXViewer(self, latex(matrix))
        else:
            self.__error_not_full.show()



