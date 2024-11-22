from __future__ import annotations


class Cargo:
    def __init__(self, weight: int) -> None:
        self.weight = weight


class BaseRobot:
    def __init__(self, name: str, weight: int, coords: list = None) -> None:
        self.name = name
        self.weight = weight
        if coords is None:
            self.coords = [0, 0]
        else:
            self.coords = coords

    def get_info(self) -> str:
        return f"Robot: {self.name}, Weight: {self.weight}"

    def go_forward(self, step: int = 1) -> list:
        self.coords[1] += step
        return self.coords

    def go_right(self, step: int = 1) -> list:
        self.coords[0] += step
        return self.coords

    def go_back(self, step: int = 1) -> list:
        self.coords[1] -= step
        return self.coords

    def go_left(self, step: int = 1) -> list:
        self.coords[0] -= step
        return self.coords


class FlyingRobot(BaseRobot):
    def __init__(self, name: str, weight: int, coords: list = None) -> None:
        if coords is None:
            super().__init__(name, weight, [0, 0, 0])
        else:
            super().__init__(name, weight, coords)

    def go_up(self, step: int = 1) -> list:
        self.coords[2] += step
        return self.coords

    def go_down(self, step: int = 1) -> list:
        self.coords[2] -= step
        return self.coords


class DeliveryDrone(FlyingRobot):
    def __init__(
            self,
            name: str,
            weight: int,
            coords: list = None,
            max_load_weight: int = 1,
            current_load: object = None) -> None:
        super().__init__(name, weight, coords)
        self.max_load_weight = max_load_weight
        self.current_load = current_load

    def hook_load(self, current_load: Cargo) -> None:
        if self.current_load is None and \
                current_load.weight <= self.max_load_weight:
            self.current_load = current_load

    def unhook_load(self) -> None:
        self.current_load = None
