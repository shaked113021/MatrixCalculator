import tkinter
from controller import MatrixController
from model import Mode


class MatrixFrame(tkinter.Frame):

    def __init__(self, parent, controller: MatrixController):
        super().__init__(parent)
        self.__parent = parent
        self.__controller = controller
        self.__cells = []
        self.__initialize_valid_chars()
        self.__validate_cell_command = self.register(self.__validate_cell)
        self.__controller.m_changed_observable().attach(self.__refresh_matrix)
        self.__controller.n_changed_observable().attach(self.__refresh_matrix)
        self.__controller.mode_changed_observable().attach(self.__clear_cells)
        self.__controller.modulus_changed_observable().attach(self.__clear_cells)

        for row in range(self.__controller.get_n()):
            row_list = []
            for col in range(self.__controller.get_m()):
                value = tkinter.StringVar()
                entry = tkinter.Entry(self, validate='all', validatecommand=(self.__validate_cell_command, '%P'),
                                      textvariable=value, width=5)
                value.trace('w', self.__build_callback_for_cell(row, col, value))
                row_list.append(entry)
                entry.grid(row=row, column=col)
            self.__cells.append(row_list)

    def __initialize_valid_chars(self):
        self.__real_valid = [str(num) for num in range(10)]
        self.__real_valid.append('(')
        self.__real_valid.append(')')
        self.__real_valid.append('/')
        self.__real_valid.append('+')
        self.__real_valid.append('-')
        self.__real_valid.append('*')
        self.__real_valid.append('^')
        self.__real_valid.append('.')
        self.__real_valid.append('-')

        self.__complex_valid = [*self.__real_valid]
        self.__complex_valid.append('i')

    def __build_callback_for_cell(self, row, col, value):
        return lambda *args: self.__controller.set_matrix_cell(row, col, value.get())

    def __validate_real(self, cell_str: str):
        if cell_str == '':
            return True
        else:
            for char in cell_str:
                if char not in self.__real_valid:
                    return False
            return True

    def __validate_complex(self, cell_str: str):
        if cell_str == '':
            return True
        else:
            for char in cell_str:
                if char not in self.__complex_valid:
                    return False
            return True

    def __validate_finite_field(self, cell_str: str):
        if cell_str == '':
            return True
        else:
            try:
                value = int(cell_str)
            except ValueError:
                return False
            if value < 0 or value >= self.__controller.get_modulus():
                return False
            return True

    def __validate_cell(self, cell_str: str):
        mode = self.__controller.get_mode().value
        if mode == Mode.REAL_NUMBERS:
            return self.__validate_real(cell_str)
        elif mode == Mode.COMPLEX_NUMBERS:
            return self.__validate_complex(cell_str)
        else:
            return self.__validate_finite_field(cell_str)

    def __clear_cells(self):
        for row in self.__cells:
            for cell in row:
                cell.delete(0, tkinter.END)

    def __destroy_cells(self):
        for row in self.__cells:
            for cell in row:
                cell.destroy()
        self.__cells = []

    def __refresh_matrix(self):
        self.__destroy_cells()
        for row in range(self.__controller.get_n()):
            row_list = []
            for col in range(self.__controller.get_m()):
                value = tkinter.StringVar()
                entry = tkinter.Entry(self, validate='all', validatecommand=(self.__validate_cell_command, '%P'),
                                      textvariable=value, width=5)
                value.trace('w', self.__build_callback_for_cell(row, col, value))
                row_list.append(entry)
                entry.grid(row=row, column=col)
            self.__cells.append(row_list)

