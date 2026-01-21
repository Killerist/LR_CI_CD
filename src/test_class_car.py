import unittest
import pytest

from .car import Car


class TestCase(unittest.TestCase):
    def setUp(self):
        self.car = Car(model="BMW X5", fuel_capacity=80)

    def tearDown(self):
        pass

    def test_drive(self):
        # Обработка исключения для случая с недостатком топлива (tank=0)
        with pytest.raises(Exception):
            self.car.drive(20)
        # Для unittest-стиля: self.assertRaises(Exception, lambda: self.car.drive(20))
        # Но поскольку Pytest запускает тесты, with pytest.raises работает
        # Теперь тест не упадёт здесь, и дойдёт до следующей проверки
        self.assertRaises(Exception, lambda: self.car.drive(80000))

    def test_refuel(self):
        # Заправим 20 литров
        self.car.refuel_car(20)
        assert self.car.get_current_fuel_level() == 20
        # Проверим, что будет исключение, если перельем
        self.assertRaises(Exception, lambda: self.car.refuel_car(80))
