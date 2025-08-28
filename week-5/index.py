# Base class
class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def info(self):
        return f"{self.brand} {self.model}"


# Child class (Smartphone inherits from Device)
class Smartphone(Device):
    def __init__(self, brand, model, storage, battery):
        super().__init__(brand, model)
        self.__storage = storage
        self.__battery = battery

    # Method to show smartphone details
    def show_specs(self):
        return f"{self.info()} | Storage: {self.__storage}GB | Battery: {self.__battery}mAh"

    # Method to simulate using battery
    def use(self, hours):
        self.__battery -= hours * 100
        return f"Used for {hours}h. Battery left: {self.__battery}mAh"

    # Getter for storage
    def get_storage(self):
        return self.__storage

    # Setter for storage (simulate adding memory card)
    def set_storage(self, extra):
        self.__storage += extra
        return f"Upgraded storage! Now: {self.__storage}GB"


# Create Smartphone objects
phone1 = Smartphone("Samsung", "Galaxy S23", 128, 5000)
phone2 = Smartphone("Apple", "iPhone 14", 256, 4200)

print(phone1.show_specs())
print(phone2.show_specs())

print(phone1.use(3))
print(phone1.set_storage(64))
