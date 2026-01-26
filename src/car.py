class FuelError(Exception):
    """Custom exception for fuel-related errors."""

class Car:
    def __init__(self, model: str, fuel_capacity: float) -> None:
        self._model = model
        self._max_fuel_capacity: float = fuel_capacity
        self._fuel_in_tank: float = 0

    def get_current_fuel_level(self) -> float:
        return self._fuel_in_tank

    def refuel_car(self, fuel_quantity: float):
        if self._max_fuel_capacity - self._fuel_in_tank < fuel_quantity:
            msg = "Вы пытаетесь залить слишком много бензина!"
            raise FuelError(msg)
        self._fuel_in_tank += fuel_quantity

    def drive(self, distance_km: float):
        # Считаем, что расход 8 литров на 100 км
        fuel_burned: float = 8 * (distance_km / 100)  # Изменено на float для точности
        if self._fuel_in_tank < fuel_burned:
            msg = "Не доедем жеж..."
            raise FuelError(msg)
        self._fuel_in_tank -= fuel_burned  # Расскомментировано TODO
        return self.get_current_fuel_level()
