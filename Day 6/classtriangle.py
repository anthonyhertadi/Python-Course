class Shape:
    def __init__(self, alas, tinggi):
        self.alas = alas
        self.tinggi = tinggi
    def calc(self):
        return f'{self.alas} x {self.tinggi} / 2'
    def itung(self):
        triangle = Shape(20,30)
        print('Luas adalah: ' f'{self.alas}'*f'{self.tinggi}'/2)
