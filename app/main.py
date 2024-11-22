class Cargo:
    def __init__(self, weight: int) -> None:
        self.weight = weight


class BaseRobot:
    def __init__(self, name: str, weight: int, coords: list = None):
        if coords is None:
            coords = [0, 0]

        self.name = name
        self.weight = weight
        self.coords = coords

    def go_forward(self, step=1):
        self.coords[1] += step

    def go_back(self, step=1):
        self.coords[1] -= step

    def go_right(self, step=1):
        self.coords[0] += step

    def go_left(self, step=1):
        self.coords[0] -= step

    def get_info(self):
        return f"Robot: {self.name}, Weight: {self.weight}"


class FlyingRobot(BaseRobot):
    def __init__(self, name: str, weight: int, coords: list = None):
        if coords is None:
            coords = [0, 0, 0]
        super(FlyingRobot, self).__init__(name, weight, coords)

    def go_up(self, step=1):
        self.coords[2] += step

    def go_down(self, step=1):
        self.coords[2] -= step


class DeliveryDrone(FlyingRobot):
    def __init__(
        self,
        name: str,
        weight: int,
        max_weight_load: int,
        current_load,
        coords: list = None,

    ):
        super(DeliveryDrone, self).__init__(name, weight, coords)
        self.max_weight_load = max_weight_load
        self.current_load = current_load

    def hook_load(self, cargo: Cargo):
        if self.current_load is None and cargo.weight <= self.max_weight_load:
            self.current_load = cargo

    def unhook_load(self):
        self.current_load = None
