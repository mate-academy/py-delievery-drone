from __future__ import annotations


class Cargo:
    def __init__(self, weight: int) -> None:
        self.weight = weight


class BaseRobot():
    def __init__(self, name: str, weight: int, coords: list = None) -> None:
        if coords is None:
            self.coords = [0, 0]
        else:
            self.coords = coords
        self.name = name
        self.weight = weight

    def go_forward(self, step: int = 1) -> list:
        self.coords[1] = self.coords[1] + step

    def go_back(self, step: int = 1) -> list:
        self.coords[1] = self.coords[1] - step

    def go_right(self, step: int = 1) -> list:
        self.coords[0] = self.coords[0] + step

    def go_left(self, step: int = 1) -> list:
        self.coords[0] = self.coords[0] - step

    def get_info(self) -> str:
        return f"Robot: {self.name}, Weight: {self.weight}"


class FlyingRobot(BaseRobot):
    def __init__(self, name: str, weight: int, coords: list = None) -> None:
        super().__init__(name, weight)
        if coords is None:
            self.coords = [0, 0, 0]
        else:
            self.coords = coords

    def go_up(self, step: int = 1) -> list:
        self.coords[2] = self.coords[2] + step

    def go_down(self, step: int = 1) -> list:
        self.coords[2] = self.coords[2] - step


class DeliveryDrone(FlyingRobot):
    def __init__(
            self, name: str, weight: int,
            coords: list = None, max_load_weight: int = None,
            current_load: int = None) -> None:
        super().__init__(name, weight, coords)
        self.max_load_weight = max_load_weight
        self.current_load = current_load

    def hook_load(self, other: Cargo) -> None:
            if self.current_load is None and other.weight <= self.max_load_weight:
                self.current_load = other

    def unhook_load(self) -> None:
        self.current_load = None
