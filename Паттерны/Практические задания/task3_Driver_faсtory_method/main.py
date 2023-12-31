from abc import ABC, abstractmethod

from drivers import IStructureDriver, SimpleFileDriver


#  Реализовать абстрактный класс
class DriverFactoryMethod(ABC):
    @classmethod
    @abstractmethod
    def get_driver(cls):
        ...


class SimpleFileFactoryMethod(DriverFactoryMethod):
    DEFAULT_NAME = 'untitled.txt'

    @classmethod
    def get_driver(cls) -> IStructureDriver:
        filename = input('Введите название текстового файла: (.txt): ').strip()
        filename = filename or cls.DEFAULT_NAME
        if not filename.endswith('.txt'):
            filename = f'{filename}.txt'

        return SimpleFileDriver(filename)


if __name__ == '__main__':
    driver = SimpleFileFactoryMethod().get_driver()  # с помощью фабричного метода инциализировать драйвер
    print(driver)
