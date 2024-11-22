class Cargo:
    def __init__(self, weight: int) -> None:
        self.weight = weight


class BaseRobot:

    def __init__(self, name, weight, coords: list = None):
        self.name = name
        self.weight = weight
        self.coords = coords if coords else [0, 0]

    def get_info(self):
        return f"Robot: {self.name}, Weight: {self.weight}"

    def go_forward(self, step=1):
        self.coords[1] += step

    def go_back(self, step=1):
        self.coords[1] -= step

    def go_right(self, step=1):
        self.coords[0] += step

    def go_left(self, step=1):
        self.coords[0] -= step


class FlyingRobot(BaseRobot):
    def __init__(self, name, weight, coords: list = None):
        super(FlyingRobot, self).__init__(
            name=name,
            weight=weight,
            coords=coords if coords else [0, 0, 0]
        )

    def go_up(self, step=1):
        self.coords[2] += step

    def go_down(self, step=1):
        self.coords[2] -= step


class DeliveryDrone(FlyingRobot):
    def __init__(self, name, weight, max_load_weight,
                 current_load, coords: list = None):
        super(DeliveryDrone, self).__init__(
            name=name,
            weight=weight,
            coords=coords
        )
        self.max_load_weight = max_load_weight
        self.current_load = current_load

    def hook_load(self, cargo: Cargo):
        if not self.current_load and cargo.weight <= self.max_load_weight:
            self.current_load = cargo

    def unhook_load(self):
        self.current_load = None
