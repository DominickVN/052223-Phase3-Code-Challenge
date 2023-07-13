from classes.concert import Concert

class Venue:
    all_venues = []
    def __init__(self, title, city):
        self._title = None
        self._city = None
        self.title = title
        self.city = city
        self._concerts = []
        self.__class__.all_venues.append(self)

    @property
    def title(self):
        return self._title
    @title.setter
    def title(self, value):
        if not isinstance(value, str):
            raise ValueError('Title must be a string')
        if len(value) == 0:
            raise ValueError("Title must contain at least one charcter")
        self._title = value

    @property
    def city(self):
        return self._city
    @city.setter
    def city(self, value):
        if not isinstance(value, str):
            raise ValueError("City must be a string")
        if len(value) == 0:
            raise ValueError("City must contain at least one character")
        self._city = value
    def add_concert(self, concert):
        self._concerts.append(concert)

    @property
    def concerts(self):
        return self._concerts
    def concert_on(self, date):
        for concert in self._concerts:
            if concert.date == date:
                return concert
        return None