class Point:
  color = 'red'
  circle = 2

  def set_coords(self, x, y):
    print('Вызов метода set_coord')
    self.x = x
    self.y = y
pt = Point()
pt.set_coords(1, 2)
print(pt.__dict__)
print(pt.color, pt.circle)
pt_2 = Point()
pt_2.set_coords(10, 20)
print(pt.__dict__)
print(pt_2.__dict__)