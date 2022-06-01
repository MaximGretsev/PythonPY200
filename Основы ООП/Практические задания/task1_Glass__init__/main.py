from typing import Union


class Glass:
    def __init__(self, capacity_volume: Union[int, float], occupied_volume: Union[int, float]):
        #  TODO инициализировать объект "Стакан"
        if not isinstance(capacity_volume, (int, float)):
            raise TypeError("Not int or float")
        if capacity_volume <= 0:
            raise ValueError("Некорректное значение")

        if not isinstance(occupied_volume, (int, float)):
            raise TypeError("not int or float")
        if occupied_volume <= 0:
            raise ValueError("Некорректное значение")

        if occupied_volume > capacity_volume:
            raise ValueError("Перелить нельзя")
        self.capacity_volume = capacity_volume
        self.occupied_volume = occupied_volume

if __name__ == "__main__":
    ...  # TODO инициализировать два объекта типа Glass
    glass_1 = Glass(14, 2.9)
    print(glass_1)
    glass_2 = Glass(32, 3)
    # TODO попробовать инициализировать не корректные объекты
    glass_3 = Glass(3, 'test')
    print(glass_3.occupied_volume)