class Cargo:
    def __init__(self, weight: int) -> None:
        self.weight = weight


class BaseRobot:
    def __init__(self, name, weight, coords=None):
        self.name = name
        self.weight = weight
        self.coords = coords
        if self.coords is None:
            self.coords = [0, 0]

    def go_forward(self, step=1):
        self.coords[1] += step
        return self.coords

    def go_back(self, step=1):
        self.coords[1] -= step
        return self.coords

    def go_right(self, step=1):
        self.coords[0] += step
        return self.coords

    def go_left(self, step=1):
        self.coords[0] -= step
        return self.coords

    def get_info(self):
        return f"Robot: {self.name}, Weight: {self.weight}"


class FlyingRobot(BaseRobot):
    def __init__(self, name, weight, coords=None):
        super().__init__(name, weight)
        self.coords = coords
        if self.coords is None:
            self.coords = [0, 0, 0]

    def go_up(self, step=1):
        self.coords[2] += step
        return self.coords

    def go_down(self, step=1):
        self.coords[2] -= step
        return self.coords


class DeliveryDrone(FlyingRobot):
    def __init__(self, name, weight, max_load_weight, current_load,
                 coords=None):
        super().__init__(name, weight, coords)
        self.max_load_weight = max_load_weight
        self.current_load = current_load

    def hook_load(self, cargo):
        if self.current_load is None and cargo.weight <= self.max_load_weight:
            self.current_load = cargo
        return self.current_load

    def unhook_load(self):
        self.current_load = None
        return self.current_load
