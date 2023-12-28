from .ModeEnum import Mode


class MatrixModel:

    def __init__(self):
        self.__n = 1
        self.__m = 1
        self.__create_matrix()
        self.__mode = Mode(Mode.REAL_NUMBERS)
        self.__modulus = 1

    def __create_matrix(self):
        self.__matrix = []

        for row in range(self.__n):
            row_list = [''] * self.__m
            self.__matrix.append(row_list)

    def get_n(self) -> int:
        return self.__n

    def set_n(self, n: int) -> None:
        if n < 1:
            raise ValueError('Value must be one or larger')
        else:
            self.__n = n
            self.__create_matrix()

    def get_m(self) -> int:
        return self.__m

    def set_m(self, m: int) -> None:
        if m < 1:
            raise ValueError('Value must be one or larger')
        else:
            self.__m = m
            self.__create_matrix()

    def get_matrix(self) -> list[list[str]]:
        return self.__matrix

    def set_matrix_cell(self, row: int, col: int, value: str) -> None:
        if row > self.__n:
            raise ValueError('Row is larger than rows in matrix')
        if col > self.__m:
            raise ValueError('Col is larger than columns in matrix')

        self.__matrix[row][col] = value

    def get_matrix_cell(self, row: int, col: int) -> str:
        if row > self.__n:
            raise ValueError('Row is larger than rows in matrix')
        if col > self.__m:
            raise ValueError('Col is larger than columns in matrix')

        return self.__matrix[row][col]

    def set_mode(self, mode: Mode) -> None:
        self.__mode = mode

    def get_mode(self) -> Mode:
        return self.__mode

    def set_modulus(self, modulus: int) -> None:
        if modulus < 1:
            raise ValueError('Value of modulus must be positive')
        self.__modulus = modulus

    def get_modulus(self) -> int:
        return self.__modulus
