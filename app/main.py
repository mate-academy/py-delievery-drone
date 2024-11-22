from __future__ import annotations


class Cargo:
    def __init__(self, weight: int) -> None:
        self.weight = weight


class BaseRobot:
    def __init__(self,
                 name: str,
                 weight: int | float,
                 coords: list[int] | None = None) -> None:

        self.name = name
        self.weight = weight
        self.coords = coords if coords else [0, 0]

    def go_forward(self, y_step: int | float = 1) -> None:
        self.coords[1] += y_step

    def go_back(self, y_step: int | float = 1) -> None:
        self.coords[1] -= y_step

    def go_right(self, x_step: int | float = 1) -> None:
        self.coords[0] += x_step

    def go_left(self, x_step: int | float = 1) -> None:
        self.coords[0] -= x_step

    def get_info(self) -> str:
        return f"Robot: {self.name}, Weight: {self.weight}"


class FlyingRobot(BaseRobot):
    def __init__(self,
                 name: str,
                 weight: int | float,
                 coords: list[int] | None = None) -> None:
        super().__init__(name, weight, coords=coords if coords else [0, 0, 0])

    def go_up(self, z_step: int | float = 1) -> None:
        self.coords[-1] += z_step

    def go_down(self, z_step: int | float = 1) -> None:
        self.coords[-1] -= z_step


class DeliveryDrone(FlyingRobot):
    def __init__(self,
                 name: str,
                 weight: int | float,
                 max_load_weight: int | float,
                 current_load: int | float,
                 coords: list[int] | None = None) -> None:

        super().__init__(name, weight, coords)
        self.max_load_weight = max_load_weight
        self.current_load = current_load

    def hook_load(self, cargo: Cargo) -> None:
        if self.current_load is None:
            if cargo.weight <= self.max_load_weight:
                self.current_load = cargo

    def unhook_load(self) -> None:
        self.current_load = None
