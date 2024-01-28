class Player:
  def __init__(self, x, y, symbol):
    self.x = x
    self.y = y
    self.symbol = symbol
  def move(self, dir, m):
    if dir == "n":
        self.y += 1
    elif dir == "s":
        self.y -= 1
    elif dir == "e":
        self.x += 1
    elif dir == "w":
        self.x -= 1