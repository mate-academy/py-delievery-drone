from __future__ import annotations


class Cargo:
    def __init__(self, weight: int) -> None:
        self.weight = weight


class BaseRobot:
    def __init__(self, name: str, weight: int, coords: list = None) -> None:
        self.name = name
        self.weight = weight
        self.coords = coords if coords else [0, 0]

    def go_forward(self, coord_y: int = 1) -> None:
        self.coords[1] += coord_y

    def go_back(self, coord_y: int = 1) -> None:
        self.coords[1] -= coord_y

    def go_right(self, coord_x: int = 1) -> None:
        self.coords[0] += coord_x

    def go_left(self, coord_x: int = 1) -> None:
        self.coords[0] -= coord_x

    def get_info(self) -> str:
        return f"Robot: {self.name}, Weight: {self.weight}"


class FlyingRobot(BaseRobot):
    def __init__(self, name: str, weight: int, coords: list = None) -> None:
        super().__init__(name, weight)
        self.coords = coords if coords else [0, 0, 0]

    def go_up(self, coord_z: int = 1) -> None:
        self.coords[2] += coord_z

    def go_down(self, coord_z: int = 1) -> None:
        self.coords[2] -= coord_z


class DeliveryDrone(FlyingRobot):
    def __init__(self,
                 name: str,
                 weight: int,
                 max_load_weight: int,
                 current_load: (None, Cargo),
                 coords: list = None) -> None:
        super().__init__(name, weight, coords)
        self.max_load_weight = max_load_weight
        self.current_load = current_load

    def hook_load(self, item: Cargo) -> None:
        if not self.current_load and item.weight <= self.max_load_weight:
            self.current_load = item

    def unhook_load(self) -> None:
        self.current_load = None
