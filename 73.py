class vechial:

    def __init__(self,brand,speed):
        self.brand=brand
        self.speed=speed   

class car(vechial):
    def __init__(self, brand,speed, fuel_type):
        super().__init__(brand, speed)
        self.fuel_type=fuel_type
    
    def show_details(self):
        print(f"brand :{self.brand}\n speed:{self.speed}\n fuel_type:{self.fuel_type}")

cars=car("BMW",200,"petrol")
cars.show_details()

