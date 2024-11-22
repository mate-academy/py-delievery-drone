class Cargo:
    def __init__(self, weight: int) -> None:
        self.weight = weight


class BaseRobot:
    def __init__(self, name: str, weight: int, coords: list = None):
        self.name = name
        self.weight = weight
        self.coords = [0, 0] if coords is None else coords

    def go_forward(self, step: int = 1):
        self.coords[1] += step

    def go_back(self, step: int = 1):
        self.coords[1] -= step

    def go_right(self, step: int = 1):
        self.coords[0] += step

    def go_left(self, step: int = 1):
        self.coords[0] -= step

    def get_info(self):
        return f"Robot: {self.name}, Weight: {self.weight}"


class FlyingRobot(BaseRobot):
    def __init__(self, name: str, weight: int, coords: list = None):
        coord = [0, 0, 0] if coords is None else coords
        super().__init__(name, weight, coord)

    def go_up(self, step: int = 1):
        self.coords[2] += step

    def go_down(self, step: int = 1):
        self.coords[2] -= step


class DeliveryDrone(FlyingRobot):
    def __init__(
            self,
            name: str,
            weight: int,
            max_weight_load: int,
            current_load: None,
            coords: list = None,
    ):
        super().__init__(name, weight, coords)
        self.max_weight_load = max_weight_load
        self.current_load = current_load

    def hook_load(self, other: Cargo):
        if self.current_load is None and other.weight <= self.max_weight_load:
            self.current_load = other

    def unhook_load(self):
        self.current_load = None
