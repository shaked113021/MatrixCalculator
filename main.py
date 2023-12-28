import sys
from view import MainWindow
from controller import MatrixController

def main(args):
    controller = MatrixController()
    window = MainWindow(controller)
    window.mainloop()


if __name__ == '__main__':
    main(sys.argv)
