
#10/10, would test again!

class Band:
    def __init__(self, name, hometown):
        self._name = None
        self._hometown = None
        self.name = name
        self.hometown = hometown
        self._concerts = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError('Name must be a string')
        if len(value) == 0:
            raise ValueError('Name must contain at least one character')
        self._name = value
    @property
    def hometown(self):
        return self._hometown

    @hometown.setter
    def hometown(self, value):
        if not isinstance(value, str):
            raise ValueError('Hometown must be a string')
        if len(value) == 0:
            raise ValueError('Hometown must contain at least one character')
        self._hometown = value

    @property
    def concerts(self):
        return self._concerts
    def play_in_venue(self, venue, date):
        from classes.concert import Concert 
        concert = Concert(date, self, venue)
        venue.add_concert(concert)
        self._concerts.append(concert)
    def all_introductions(self):
        return [
            f'Hello {concert.venue.city}!!!!!, we are {self.name} and we\'re from {self.hometown}'
            for concert in self._concerts
            if isinstance(concert.band, Band)
        ]