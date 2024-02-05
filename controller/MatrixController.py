from model import MatrixModel, ModeEnum
from observer import Observable


class MatrixController:

    def __init__(self):

        self.__model = MatrixModel()
        self.__n_changed = Observable()
        self.__m_changed = Observable()
        self.__matrix_changed = Observable()
        self.__mode_changed = Observable()
        self.__modulus_changed = Observable()

    def get_n(self) -> int:
        return self.__model.get_n()

    def set_n(self, n: int) -> None:
        self.__model.set_n(n)
        self.__n_changed.notify()

    def get_m(self) -> int:
        return self.__model.get_m()

    def set_m(self, m: int) -> None:
        self.__model.set_m(m)
        self.__m_changed.notify()

    def get_matrix(self) -> list[list[str]]:
        return self.__model.get_matrix()

    def set_matrix_cell(self, row: int, col: int, value: str) -> None:
        self.__model.set_matrix_cell(row, col, value)
        self.__matrix_changed.notify()

    def get_matrix_cell(self, row: int, col: int) -> str:
        return self.__model.get_matrix_cell(row, col)

    def set_mode(self, mode: ModeEnum.Mode) -> None:
        self.__model.set_mode(mode)
        self.__mode_changed.notify()

    def get_mode(self) -> ModeEnum.Mode:
        return self.__model.get_mode()

    def set_modulus(self, modulus: int) -> None:
        self.__model.set_modulus(modulus)
        self.__modulus_changed.notify()

    def get_modulus(self) -> int:
        return self.__model.get_modulus()

    def n_changed_observable(self) -> Observable:
        return self.__n_changed

    def m_changed_observable(self) -> Observable:
        return self.__m_changed

    def matrix_changed_observable(self) -> Observable:
        return self.__matrix_changed

    def mode_changed_observable(self) -> Observable:
        return self.__mode_changed

    def modulus_changed_observable(self) -> Observable:
        return self.__modulus_changed

    def is_full(self) -> bool:
        return self.__model.is_full()

