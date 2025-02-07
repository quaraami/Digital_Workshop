class Cars:
    mark = 'Lada'
    tip = 'Cedan'
    country = 'Russia'
    def name_country(self, country):
        print("1")
cr = Cars()
cr.name_country("Japan")
print(cr.__dict__)
printe)