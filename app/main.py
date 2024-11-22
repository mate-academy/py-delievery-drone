class Cargo:
    def __init__(self, weight: int) -> None:
        self.weight = weight


class BaseRobot:
    def __init__(self, name: str, weight: int, coords: list = None):
        self.weight = weight
        self.name = name
        self.coords = coords if coords is not None else [0, 0]

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
        super().__init__(name, weight, coords)
        self.coords = [0, 0, 0] if self.coords == [0, 0] else coords

    def go_up(self, step: int = 1):
        self.coords[2] += step

    def go_down(self, step: int = 1):
        self.coords[2] -= step


class DeliveryDrone(FlyingRobot):
    def __init__(self, name: str, weight: int,
                 max_load_weight: int, current_load: Cargo,
                 coords: list = None):
        super().__init__(name, weight, coords)

        self.max_load_weight = max_load_weight
        self.current_load = current_load

    def hook_load(self, cargo):
        if cargo.weight <= self.max_load_weight and self.current_load is None:
            self.current_load = cargo

    def unhook_load(self):
        self.current_load = None
