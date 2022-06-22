class Date:
    def __init__(self, date, month, year):
        self.date = None
        self.set_date(date)
        self.month = None
        self.set_month(month)
        self.year = None
        self.set_year(year)
        pass

    def is_valid(self, data):
        if not isinstance(data, int):
            raise TypeError(f"Введдный вами {data} в неверном формате")

    def set_date(self, date: int):
        self.is_valid(date)
        self.date = date

    def set_month(self, month: int):
        self.is_valid(month)
        self.month = month

    def set_year(self, year):
        self.is_valid(year)
        self.year = year

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}'

    def __str__(self) -> str:
        return f'{str(self.date)}/{self.month}/{self.year}'


if __name__ == '__main__':
    date = Date(12, 12, 1993)
    print(date)