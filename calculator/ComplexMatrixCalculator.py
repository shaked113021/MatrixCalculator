from .MatrixCalculator import MatrixCalculator
from controller import MatrixController
from sympy import parse_expr, Matrix


class ComplexMatrixCalculator(MatrixCalculator):

    def __init__(self, controller: MatrixController):
        self.__controller = controller

    def calculate(self):
        matrix = self.__create_matrix()
        return matrix.rref(pivots=False)

    def __create_matrix(self):
        old_mat = self.__controller.get_matrix()
        formatted_mat = []

        for row in old_mat:
            new_row = []
            for cell in row:
                new_cell = parse_expr(cell.replace('^', '**').replace('i', 'I'))
                new_row.append(new_cell)
            formatted_mat.append(new_row)
        return Matrix(formatted_mat)



