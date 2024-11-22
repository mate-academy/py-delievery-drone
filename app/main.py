class Cargo:
    def __init__(self, weight: int) -> None:
        self.weight = weight


class BaseRobot:

    def __init__(self, name, weight, coords=None):
        self.name = name
        self.weight = weight
        if coords:
            self.coords = coords
        else:
            self.coords = [0, 0]

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
    def __init__(self, name, weight, coords=None):
        super().__init__(name, weight, coords)
        if not coords:
            self.coords = [0, 0, 0]

    def go_up(self, step=1):
        self.coords[2] += step

    def go_down(self, step=1):
        self.coords[2] -= step


class DeliveryDrone(FlyingRobot):
    def __init__(self, name, weight, max_load_weight,
                 current_load, coords=None):
        super().__init__(name, weight, coords)
        self.max_load_weight = max_load_weight
        self.current_load = current_load

    def hook_load(self, cargo):
        if not self.current_load and cargo.weight <= self.max_load_weight:
            self.current_load = cargo

    def unhook_load(self):
        self.current_load = None
