from .MatrixCalculator import MatrixCalculator
from controller import MatrixController
from sympy import parse_expr, Matrix, mod_inverse


class FiniteMatrixCalculator(MatrixCalculator):

    def __init__(self, controller: MatrixController):
        self.__controller = controller
        self.__modulus = self.__controller.get_modulus()
        self.__controller.modulus_changed_observable().attach(self.__update_modulus)

    def __update_modulus(self):
        self.__modulus = self.__controller.get_modulus()

    def calculate(self):
        matrix = self.__create_matrix()
        matrix_rref = matrix.rref(iszerofunc=lambda num: num % self.__modulus == 0, pivots=False)
        return matrix_rref.applyfunc(self.__frac_mod)

    def __frac_mod(self, num):
        numerator, denominator = num.as_numer_denom()
        return numerator * mod_inverse(denominator, self.__modulus) % self.__modulus

    def __create_matrix(self):
        old_mat = self.__controller.get_matrix()
        new_mat = []

        for row in old_mat:
            new_row = []
            for cell in row:
                new_row.append(parse_expr(cell))
            new_mat.append(new_row)

        return Matrix(new_mat)