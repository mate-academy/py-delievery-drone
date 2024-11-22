class Cargo:
    def __init__(self, weight: int) -> None:
        self.weight = weight


class BaseRobot:
    def __init__(self, name: str, weight: int, coords: list = None):
        self.name = name
        self.weight = weight
        if coords is not None:
            self.coords = coords
        else:
            self.coords = [0, 0]

    def go_back(self, steep: int = 1):
        self.coords[1] -= steep

    def go_left(self, steep: int = 1):
        self.coords[0] -= steep

    def go_right(self, steep: int = 1):
        self.coords[0] += steep

    def go_forward(self, steep: int = 1):
        self.coords[1] += steep

    def get_info(self):
        return f"Robot: {self.name}, Weight: {self.weight}"


class FlyingRobot(BaseRobot):
    def __init__(self, name: str, weight: int, coords: list = None):
        super().__init__(name, weight)
        if coords is not None:
            self.coords = coords
        else:
            self.coords = [0, 0, 0]

    def go_up(self, steep: int = 1):
        self.coords[2] += steep

    def go_down(self, steep: int = 1):
        self.coords[2] -= steep


class DeliveryDrone(FlyingRobot):
    def __init__(self, name: str, weight: int, max_weight_load: int = 0,
                 current_load: Cargo = None, coords: list = None):
        super().__init__(name, weight, coords)
        self.max_weight_load = max_weight_load
        self.current_load = current_load

    def hook_load(self, cargo: Cargo):
        if self.current_load is None and self.max_weight_load >= cargo.weight:
            self.current_load = cargo

    def unhook_load(self):
        self.current_load = None
