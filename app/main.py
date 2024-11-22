class Cargo:
    def __init__(self, weight: int) -> None:
        self.weight = weight


class BaseRobot:
    def __init__(self, name: str, weight: int, coords=None):
        self.name = name
        self.weight = weight
        self.coords = coords
        self.set_coordinats()

    def go_forward(self, step=1):
        self.coords[1] += step
        return self

    def go_back(self, step=1):
        self.coords[1] -= step

    def go_right(self, step=1):
        self.coords[0] += step

    def go_left(self, step=1):
        self.coords[0] -= step

    def get_info(self):
        return f"Robot: {self.name}, Weight: {self.weight}"

    def set_coordinats(self):
        if self.coords is None:
            if isinstance(self, (FlyingRobot, DeliveryDrone)):
                self.coords = [0, 0, 0]
            else:
                self.coords = [0, 0]


class FlyingRobot(BaseRobot):
    def __init__(self, name: str, weight: int, coords=None):
        super(FlyingRobot, self).__init__(name, weight, coords)

    def go_up(self, step=1):
        self.coords[2] += step
        return self

    def go_down(self, step=1):
        self.coords[2] -= step


class DeliveryDrone(FlyingRobot):
    def __init__(self, name: str, weight: int, max_load_weight: int,
                 coords=None, current_load=None):
        super(DeliveryDrone, self).__init__(name, weight, coords)
        self.max_load_weight = max_load_weight
        self.current_load = current_load

    def hook_load(self, load: Cargo):
        if self.max_load_weight >= load.weight and self.current_load is None:
            self.current_load = load

    def unhook_load(self):
        self.current_load = None
