class Cargo:
    def __init__(self, weight: int) -> None:
        self.weight = weight


class BaseRobot:
    def __init__(self, name, weight, coords=None):
        self.name = name
        self.weight = weight
        self.coords = [0, 0] if coords is None else coords

    def go_forward(self, y=1):
        self.coords[1] += y

    def go_back(self, y=1):
        self.coords[1] -= y

    def go_right(self, x=1):
        self.coords[0] += x

    def go_left(self, x=1):
        self.coords[0] -= x

    def get_info(self):
        return f"Robot: {self.name}, Weight: {self.weight}"


class FlyingRobot(BaseRobot):
    def __init__(self, name, weight, coords=None):
        coords = [0, 0, 0] if coords is None else coords
        super().__init__(name, weight, coords)

    def go_up(self, z=1):
        self.coords[2] += z

    def go_down(self, z=1):
        self.coords[2] -= z


class DeliveryDrone(FlyingRobot):
    def __init__(self, name, weight, coords=None,
                 max_load_weight=0,
                 current_load=0):
        super().__init__(name, weight, coords)
        self.max_load_weight = max_load_weight
        self.current_load = current_load

    def hook_load(self, cargo):
        if self.current_load is None and cargo.weight <= self.max_load_weight:
            self.current_load = cargo

    def unhook_load(self):
        self.current_load = None
