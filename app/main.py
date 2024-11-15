class Cargo:
    def __init__(self, weight: int) -> None:
        self.weight = weight


class BaseRobot:
    def __init__(self, name: str, weight: int,
                 coords: list = None) -> None:
        self.name = name
        self.weight = weight
        self.coords = coords
        if coords is None:
            self.coords = [0, 0]

    def go_forward(self, step: int = 1) -> None:
        self.coords[1] += step
    """Robot move by step(1 by default) forward"""

    def go_back(self, step: int = 1) -> None:
        self.coords[1] -= step
    """Robot move by step(1 by default) back"""

    def go_right(self, step: int = 1) -> None:
        self.coords[0] += step
    """Robot move by step(1 by default) right"""

    def go_left(self, step: int = 1) -> None:
        self.coords[0] -= step
    """Robot move by step(1 by default) left"""

    def get_info(self) -> str:
        return f"Robot: {self.name}, Weight: {self.weight}"
    """Write info above Robot"""


class FlyingRobot(BaseRobot):
    def __init__(self, name: str, weight: int,
                 coords: list = None) -> None:
        super().__init__(name, weight, coords)
        if coords is None:
            self.coords = [0, 0, 0]

    def go_up(self, step: int = 1) -> None:
        self.coords[2] += step

    def go_down(self, step: int = 1) -> None:
        self.coords[2] -= step


"""Method go_up move Robot by step(1 by default) up
Method go_down move Robot by step(1 by default) down"""


class DeliveryDrone(FlyingRobot):
    def __init__(self, name: str, weight: int,
                 max_load_weight: int,
                 coords: list = None,
                 current_load: Cargo = None) -> None:
        super().__init__(name, weight, coords)
        self.max_load_weight = max_load_weight
        self.current_load = current_load

    def hook_load(self, cargo: Cargo) -> None:
        if self.current_load is None and cargo.weight <= self.max_load_weight:
            self.current_load = cargo

    def unhook_load(self) -> None:
        self.current_load = None


"""
Method hook_load changes to object current_load by Drone,
if the weight of the object not greater
than max_load_weight of the drone
Method unhook_load changes to None current_load by Drone"""
