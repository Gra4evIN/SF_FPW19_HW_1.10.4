class Guests:
    def __init__(self, name, city, position):
        self.name = name
        self.city = city
        self.position = position


    def __str__(self):
        return (f'"{self.name}, {self.city}, статус "{self.position}"')
