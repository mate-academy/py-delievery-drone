from __future__ import annotations


class Cargo:
    def __init__(self, weight: int) -> None:
        self.weight = weight


class BaseRobot:
    def __init__(self, name: str, weight: int, coords: list = None) -> None:
        if coords is None:
            coords = [0, 0]
        self.name = name
        self.weight = weight
        self.coords = coords

    def go_forward(self, y_move: int = 1) -> None:
        self.coords[1] += y_move

    def go_right(self, x_move: int = 1) -> None:
        self.coords[0] += x_move

    def go_back(self, y_move: int = 1) -> None:
        self.coords[1] -= y_move

    def go_left(self, x_move: int = 1) -> None:
        self.coords[0] -= x_move

    def get_info(self) -> str:
        return f"Robot: {self.name}, Weight: {self.weight}"


class FlyingRobot(BaseRobot):
    def __init__(self, name: str,
                 weight: int,
                 coords: list = None) -> None:
        super().__init__(name, weight, coords)
        if coords is None:
            self.coords = [0, 0, 0]

    def go_up(self, z_move: int = 1) -> None:
        self.coords[2] += z_move

    def go_down(self, z_move: int = 1) -> None:
        self.coords[2] -= z_move


class DeliveryDrone(FlyingRobot):
    def __init__(self, max_load_weight: int, current_load: None | Cargo,
                 name: str, weight: int, coords: list = None) -> None:
        super().__init__(name, weight, coords)
        self.max_load_weight = max_load_weight
        self.current_load = current_load

    def hook_load(self, carg: Cargo) -> None:
        if not self.current_load and carg.weight <= self.max_load_weight:
            self.current_load = carg

    def unhook_load(self) -> None:
        self.current_load = None
