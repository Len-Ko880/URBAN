class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        floor = 0
        if new_floor > self.number_of_floors or new_floor < 1:
            print('Такого этажа не существует')
        else:
            for floor in range(new_floor):
                print(floor + 1)

h1 = House('Олимпийский парк', 6)
h2 = House('ЖК Раменское', 24)
h1.go_to(15)
h2.go_to(20)