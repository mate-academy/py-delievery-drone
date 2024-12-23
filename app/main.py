class Cargo:
    def __init__(self, weight: int) -> None:
        self.weight = weight

# write your code here
class Base_Robot:
    def __init__(self, name: str, weight: float, coords=[0, 0]) -> None:
        self.name = name
        self.weight = weight
        self.coords = coords
    
    def go_forward(self, step) -> None:
        self.coords[1] += step
    
    def go_back(self, step) -> None:
        self.coords[1] -= step
    
    def go_right(self, step) -> None:
        self.coords[0] += step
    
    def go_left(self, step) -> None:
        self.coords[0] -= step
    
    def get_info(name, weight):
        print(f"Robot: {name}, Weight: {weight}")

def FlyingRobot(BaseRobot):
    def __init__(self, name: str, weight: float, coords=[0, 0]) -> None:
        super().__init__(name, weight, coords)
    
    def go_up(self, step) -> None:
        self.coords[2] += step
    
    def go_down(self, step) -> None:
        self.coords[2] -= step


def DeliveryDrone(FlyingRobot):
    def __init__(self, name: str, weight: float, max_load_weight, current_load=None, coords=[0, 0]) -> None:
        super().__init__(name, weight, coords)
        self.max_load_weight = max_load_weight
        self.current_load = current_load
    
    def hook_load(self, cargo: Cargo):
        if (self.current_load == None and cargo.weight <= self.max_load_weight):
            self.current_load = cargo
    
    def unhook_load(self):
        self.current_load = None