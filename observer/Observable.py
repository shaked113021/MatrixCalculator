
class Observable:

    def __init__(self):
        self.__observers = []

    def attach(self, observer_callback):
        self.__observers.append(observer_callback)

    def notify(self):
        if len(self.__observers) > 0:
            for observer in self.__observers:
                observer()

