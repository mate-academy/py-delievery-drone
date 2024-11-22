from typing import Union


class Cargo:
    def __init__(self, weight: int) -> None:
        self.weight = weight


class BaseRobot:
    def __init__(
        self,
        name: str,
        weight: int,
        coords: list[int] | None = None
    ) -> None:
        self.name = name
        self.weight = weight
        self.coords = coords if coords else [0, 0]

    def go_forward(self, point: int = 1) -> None:
        self.coords[1] += point

    def go_back(self, point: int = 1) -> None:
        self.coords[1] -= point

    def go_right(self, point: int = 1) -> None:
        self.coords[0] += point

    def go_left(self, point: int = 1) -> None:
        self.coords[0] -= point

    def get_info(self) -> str:
        return f"Robot: {self.name}, Weight: {self.weight}"


class FlyingRobot(BaseRobot):
    def __init__(
        self,
        name: str,
        weight: int,
        coords: list[int] | None = None
    ) -> None:
        if coords is None:
            coords = [0, 0, 0]
        super().__init__(
            name,
            weight,
            coords
        )

    def go_up(self, point: int = 1) -> None:
        self.coords[2] += point

    def go_down(self, point: int = 1) -> None:
        self.coords[2] -= point


class DeliveryDrone(FlyingRobot):
    def __init__(
        self,
        max_load_weight: int,
        name: str,
        weight: int,
        coords: list[int] | None = None,
        current_load: Union[None, "Cargo"] = None
    ) -> None:
        if coords is None:
            coords = [0, 0, 0]
        super().__init__(
            name,
            weight,
            coords
        )
        self.max_load_weight = max_load_weight
        self.current_load = current_load

    def hook_load(self, other: "Cargo") -> None:
        if self.current_load is None and other.weight <= self.max_load_weight:
            self.current_load = other

    def unhook_load(self) -> None:
        self.current_load = None
