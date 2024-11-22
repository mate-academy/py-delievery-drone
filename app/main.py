class Cargo:
    def __init__(self, weight: int) -> None:
        self.weight = weight


class BaseRobot:
    def __init__(self, name: str, weight, coords: list = None):
        self.name = name
        self.weight = weight
        self.coords = [0, 0] if coords is None else coords

    def go_forward(self, y: int = 1):
        self.coords[1] += y

    def go_back(self, y: int = 1):
        self.coords[1] -= y

    def go_right(self, x: int = 1):
        self.coords[0] += x

    def go_left(self, x: int = 1):
        self.coords[0] -= x

    def get_info(self):
        return f"Robot: {self.name}, Weight: {self.weight}"


class FlyingRobot(BaseRobot):
    def __init__(self, name: str, weight, coords: list = None):
        super().__init__(name, weight, coords)
        self.coords = [0, 0, 0] if coords is None else coords

    def go_up(self, z: int = 1):
        self.coords[2] += z

    def go_down(self, z: int = 1):
        self.coords[2] -= z


class DeliveryDrone(FlyingRobot):
    def __init__(self, name: str,
                 weight: int,
                 coords: list = None,
                 max_load_weight: int = 0,
                 current_load: int = None):
        super().__init__(name, weight, coords)
        self.max_load_weight = max_load_weight
        self.current_load = current_load

    def hook_load(self, object):
        if self.current_load is None and object.weight <= self.max_load_weight:
            self.current_load = object

    def unhook_load(self):
        self.current_load = None
