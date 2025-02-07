class Cars:
    def __init__ (self, name):
        self.name = name
class Russian(Cars):
     def __init__ (self, name):
        super().__init__(name)
class Tip(Russian):
     def __init__ (self, tip):
        super().__init__(tip)
class Colour(Tip):
    def __init__ (self, colour):
        super().__init__(colour)
tp = Tip("Vesta")
ru = Russian("Lada")
cl = Colour("Red")
print(ru.__dict__ , tp.__dict__, cl.__dict__)