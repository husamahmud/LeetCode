class ParkingSystem:
    def __init__(self, big: int, medium: int, small: int):
        self.parking = [big, medium, small]
        self.res = []

    def addCar(self, carType: int) -> bool:
        if carType == 1 and self.parking[0]:
            self.parking[0] -= 1
            return True
        elif carType == 2 and self.parking[1]:
            self.parking[1] -= 1
            return True
        elif carType == 3 and self.parking[2]:
            self.parking[2] -= 1
            return True
        return False
