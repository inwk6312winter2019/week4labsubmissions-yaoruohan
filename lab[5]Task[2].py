import copy
class rectangle(object):
class Point(object):
box = Rectangle()
box.width = 100.0
box.height = 200.0
box.corner = Point()
box.corner.x = 0.0
box.corner.y = 0.0

def __init_(self):
    self.width = 0
    self.height = 0
    self.corner = 0
def find_center(box):
     p = Point()
     p.x = box.corner.x + box.width/2.0
     p.y = box.corner.y + box.height/2.0

def move_rectangle(box, dx, dy):
         box.corner.x += dx
         box.corner.y += dy
def modified_moverectangle(box, dx, dy):
         res = copy.deepcopy(box)
         move_rectangle(res, dx, dy)
         return res

     rect = Rectangle()
     rect.width = 50.0
     rect.height = 70.0
     rect.corner = Point()
     rect.corner.x = 0.0
     rect.corner.y = 0.0

     print('Center')
     p = find_center(rect)
     print('(%g, %g)' % (p.x, p.y))
     print('')

     print('(%g, %g)' % (rect.corner.x, rect.corner.y))
     print('move')
     move_rectangle(rect, 100, 50)
     print('(%g, %g)' % (rect.corner.x, rect.corner.y))
     print('')

     print('New move')
     n_rect = modified_moverectangle(rect, 50, 100)
     print('(%g, %g)' % (n_rect.corner.x, n_rect.corner.y))


