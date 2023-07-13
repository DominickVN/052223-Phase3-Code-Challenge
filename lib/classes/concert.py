class Concert:
    def __init__(self, date, band, venue):
        self._date = None
        self._band = None
        self._venue = None
        self.date = date
        self.band = band
        self.venue = venue
    @property
    def date(self):
        return self._date
    @date.setter
    def date(self, value):
        if not isinstance(value, str):
            raise ValueError('Date must be a string')
        if len(value) == 0:
            raise ValueError("Date must contain at least one character")
        self._date = value
    @property
    def band(self):
        return self._band

    @band.setter
    def band(self, value):
        from classes.band import Band
        if not isinstance(value, Band):
            raise ValueError('Band must be an instance of Band class')
        self._band = value
    @property
    def venue(self):
        return self._venue

    @venue.setter
    def venue(self, value):
        from classes.venue import Venue
        if not isinstance(value, Venue):
            raise ValueError('Venue must be an instance of Venue class')
        self._venue = value
    def hometown_show(self):
        return self.band.hometown == self.venue.city
    def introduction(self):
        return f'Hello {self.venue.city}!!!!!, we are {self.band.name} and we\'re from {self.band.hometown}'
