class Cargo:
    def __init__(self, weight: int) -> None:
        self.weight = weight


class BaseRobot(Cargo):
    def __init__(self, name, weight, coords: list = None):
        super().__init__(weight)
        self.name = name
        self.coords = coords or [0, 0]

    def go_forward(self, step: int = 1):
        self.coords[1] += step
        return self.coords

    def go_back(self, step: int = 1):
        self.coords[1] -= step
        return self.coords

    def go_right(self, step: int = 1):
        self.coords[0] += step
        return self.coords

    def go_left(self, step: int = 1):
        self.coords[0] -= step
        return self.coords

    def get_info(self):
        return f'Robot: {self.name}, Weight: {self.weight}'


class FlyingRobot(BaseRobot):
    def __init__(self, name, weight, coords: list = None):
        super().__init__(name, weight)
        self.coords = coords or [0, 0, 0]

    def go_up(self, air_step: int = 1):
        self.coords[2] += air_step
        return self.coords

    def go_down(self, air_step: int = 1):
        self.coords[2] -= air_step
        return self.coords


class DeliveryDrone(FlyingRobot):

    def __init__(self, name, weight, max_load_weight, current_load):
        super().__init__(name, weight)
        self.max_load_weight = max_load_weight
        self.current_load = current_load

    def hook_load(self, package):
        if self.current_load is None \
                and package.weight <= self.max_load_weight:
            self.current_load = package

    def unhook_load(self):
        self.current_load = None
