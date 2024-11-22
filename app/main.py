from __future__ import annotations


class BaseRobot:
    def __init__(
            self,
            name: str,
            weight: float,
            coords: list[float] = None
    ) -> None:
        self.name = name
        self.weight = weight
        self.coords = coords if coords else [0, 0]

    def go_forward(self, step: float = 1) -> None:
        self.coords[1] += step

    def go_back(self, step: float = 1) -> None:
        self.coords[1] -= step

    def go_right(self, step: float = 1) -> None:
        self.coords[0] += step

    def go_left(self, step: float = 1) -> None:
        self.coords[0] -= step

    def get_info(self) -> str:
        return f"Robot: {self.name}, Weight: {self.weight}"


class FlyingRobot(BaseRobot):
    def __init__(
            self,
            name: str,
            weight: float,
            coords: list[float] = None
    ) -> None:
        coords = coords if coords else [0, 0, 0]
        super().__init__(name, weight, coords)

    def go_up(self, step: float = 1) -> None:
        self.coords[2] += step

    def go_down(self, step: float = 1) -> None:
        self.coords[2] -= step


class Cargo:
    def __init__(self, weight: float) -> None:
        self.weight = weight


class DeliveryDrone(FlyingRobot):
    def __init__(
        self,
        name: str,
        weight: float,
        max_load_weight: float,
        current_load: Cargo | None = None,
        coords: list[float] = None,
    ) -> None:
        super().__init__(name, weight, coords)
        self.max_load_weight = max_load_weight
        self.current_load = current_load

    def hook_load(self, cargo: Cargo) -> None:
        if self.current_load is None and cargo.weight <= self.max_load_weight:
            self.current_load = cargo

    def unhook_load(self) -> None:
        self.current_load = None
