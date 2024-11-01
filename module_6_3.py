class Horse:

    def __init__(self):
        self.x_distance = 0
        self.__sound = 'Frrr'

    def run(self, dx):
        self.x_distance += dx
        return self.x_distance


class Eagle:

    def __init__(self):
        self.y_distance = 0
        self.sound = 'I train, eat, sleep, and repeat'

    def fly(self, dy):
        self.y_distance += dy
        return self.y_distance

    def voice(self):
        return self.sound


class Pegasus(Horse, Eagle):

    def __init__(self):
        super().__init__()
        Eagle.__init__(self)

    def move(self, dx, dy):
        return super().run(dx), Eagle.fly(self, dy)

    def get_pos(self):
        return (self.x_distance, self.y_distance)

    def voice(self):
        print(Eagle.voice(self))


p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()
