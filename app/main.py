from __future__ import annotations


class Cargo:
    def __init__(self, weight: int) -> None:
        self.weight = weight


class BaseRobot:
    def __init__(self, name: str, weight: int, coords: list = None) -> None:
        self.name = name
        self.weight = weight
        self.coords = coords or [0, 0]

    def get_info(self) -> str:
        return f"Robot: {self.name}, Weight: {self.weight}"

    def go_forward(self, step: int = 1) -> BaseRobot | FlyingRobot:
        self.coords[1] += step
        return self

    def go_back(self, step: int = 1) -> BaseRobot | FlyingRobot:
        self.coords[1] -= step
        return self

    def go_right(self, step: int = 1) -> BaseRobot | FlyingRobot:
        self.coords[0] += step
        return self

    def go_left(self, step: int = 1) -> BaseRobot | FlyingRobot:
        self.coords[0] -= step
        return self


class FlyingRobot(BaseRobot):
    def __init__(self, name: str, weight: int, coords: list = None) -> None:
        super().__init__(name, weight)
        self.coords = coords or [0, 0, 0]

    def go_up(self, step: int = 1) -> FlyingRobot | DeliveryDrone:
        self.coords[2] += step
        return self

    def go_down(self, step: int = 1) -> FlyingRobot | DeliveryDrone:
        self.coords[2] -= step
        return self


class DeliveryDrone(FlyingRobot):
    def __init__(
            self, name: str,
            weight: int,
            max_load_weight: int,
            coords: list = None,
            current_load: list = None
    ) -> None:
        super().__init__(name, weight, coords)
        self.max_load_weight = max_load_weight
        self.current_load = current_load

    def hook_load(self, cargo: Cargo) -> DeliveryDrone:
        if self.current_load is None and self.max_load_weight >= cargo.weight:
            self.current_load = cargo
        return self

    def unhook_load(self) -> DeliveryDrone:
        self.current_load = None
        return self
