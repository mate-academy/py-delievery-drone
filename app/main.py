from typing import Optional


class Cargo:
    def __init__(self, weight: int) -> None:
        self.weight = weight


class BaseRobot():
    def __init__(
            self,
            name: str,
            weight: int,
            coords: Optional[list[int]] = None
    ) -> None:

        self.name = name
        self.weight = weight
        self.coords = coords
        if coords is None and isinstance(self, FlyingRobot):
            self.coords = [0, 0, 0]
        elif coords is None and isinstance(self, BaseRobot):
            self.coords = [0, 0]

    def go_forward(self, step: int = 1) -> None:
        self.coords[1] += step

    def go_back(self, step: int = 1) -> None:
        self.coords[1] -= step

    def go_right(self, step: int = 1) -> None:
        self.coords[0] += step

    def go_left(self, step: int = 1) -> None:
        self.coords[0] -= step

    def get_info(self) -> str:
        return f"Robot: {self.name}, Weight: {self.weight}"


class FlyingRobot(BaseRobot):
    def __init__(
            self,
            name: str,
            weight: int,
            coords: Optional[list[int]] = None
    ) -> None:

        super().__init__(name, weight, coords)

    def go_up(self, fly_on_coordinates: int = 1) -> None:
        self.coords[2] += fly_on_coordinates

    def go_down(self, fall_down_coordinates: int = 1) -> None:
        self.coords[2] -= fall_down_coordinates


class DeliveryDrone(FlyingRobot):
    def __init__(
            self,
            name: str,
            weight: int,
            max_load_weight: int,
            current_load: Cargo | None,
            coords: Optional[list[int]] = None
    ) -> None:

        super().__init__(name, weight, coords)
        self.max_load_weight = max_load_weight
        self.current_load = current_load

    def hook_load(self, cargo: Cargo) -> None:
        if self.current_load is None and cargo.weight <= self.max_load_weight:
            self.current_load = cargo

    def unhook_load(self) -> None:
        self.current_load = None
