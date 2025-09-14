class Robot :
    def __init__(self, name, model, position=(0, 0)):
        self.name = name
        self.model = model
        self.battery_level = 100
        self.position = position

    def charge(self, amount):
        self.battery_level = min(100, self.battery_level + amount)
        print(f"{self.name} charged to {self.battery_level}%")

    def report_status(self):
        print(f"Robot Name: {self.name}")
        print(f"Model: {self.model}")
        print(f"Battery Level: {self.battery_level}%")
        print(f"Position: {self.position}")
    
    def move(self, new_position):
        self.position = new_position
        print(f"{self.name} moved to position {self.position}")

    def interact(self, other_robot):
        print(f"{self.name} is interacting with {other_robot.name}")

    def create_cleaning_robot(name, position=(0, 0)):
        return Robot(name, "Cleaning Robot", position)
    
    def create_delivery_robot(name, position=(0, 0)):
        return Robot(name, "Delivery Robot", position)
    
if __name__ == "__main__":

    robot1 = Robot.create_cleaning_robot("CleanerBot", (5, 5))
    robot2 = Robot.create_delivery_robot("DeliveryBot", (10, 10))

    robot1.report_status()
    robot2.report_status()

    robot1.move((6, 6))
    robot1.charge(20)

    robot1.interact(robot2)