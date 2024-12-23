class Cargo:
    def __init__(self, weight: int) -> None:
        self.weight = weight

# write your code here
class BaseRobot:
    def __init__(self, name: str, weight: float, coords) -> None:
        self.name = name
        self.weight = weight
        self.coords = coords
    
    
    def define_coords(self):
        if self.coords == None:
            self.coords = [0, 0]
    
    def go_forward(self, step) -> None:
        self.coords[1] += step
    
    def go_back(self, step) -> None:
        self.coords[1] -= step
    
    def go_right(self, step) -> None:
        self.coords[0] += step
    
    def go_left(self, step) -> None:
        self.coords[0] -= step
    
    def get_info(self):
        return f"Robot: {self.name}, Weight: {self.weight}"

class FlyingRobot(BaseRobot):
    def __init__(self, name: str, weight: float, coords) -> None:
        super().__init__(name, weight, coords)
    
    def define_coords(self):
        if self.coords == None:
            self.coords = [0, 0, 0]
    
    def go_up(self, step) -> None:
        self.coords[2] += step
    
    def go_down(self, step) -> None:
        self.coords[2] -= step


class DeliveryDrone(FlyingRobot):
    def __init__(self, name: str, weight: float, max_load_weight, coords, current_load=None) -> None:
        super().__init__(name, weight, coords)
        self.max_load_weight = max_load_weight
        self.current_load = current_load
    
    def hook_load(self, cargo: Cargo):
        if (self.current_load == None and cargo.weight <= self.max_load_weight):
            self.current_load = cargo
    
    def unhook_load(self):
        self.current_load = None