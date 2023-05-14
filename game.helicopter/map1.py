class Map:

    def print_map(self): #функция которая выводит карту
        for row in self.cells:
            for cell in row:
                if cell == 0:
                    print("🟩", end="")
                elif cell == 1:
                    print("🌲", end="")
                elif cell == 2:
                    print("🌊", end="")
            print()

   # def generate_rivers(): #генератор рек

   # def generator_forest(): #генератор лесов

    def __init__(self, w, h): #функция отвечает за координаты на карте
        self.cells = [[0 for i in range(w)] for j in range(h)]

tmp = Map(10, 10)
tmp.cells[1][1] = 1 
tmp.cells[1][3] = 2
tmp.print_map()