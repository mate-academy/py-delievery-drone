from typing import Optional, List


class Cargo:
    def __init__(self, weight: int) -> None:
        self.weight = weight


class BaseRobot:
    def __init__(
        self,
        name: str,
        weight: int,
        coords: Optional[List[int]] = None
    ) -> None:
        self.name = name
        self.weight = weight
        self.coords = [0, 0] if coords is None else coords

    def get_info(self) -> str:
        return f"Robot: {self.name}, Weight: {self.weight}"

    def go_forward(self, step_y: int = 1) -> None:
        self.coords[1] += step_y

    def go_back(self, step_y: int = 1) -> None:
        self.coords[1] -= step_y

    def go_right(self, step_x: int = 1) -> None:
        self.coords[0] += step_x

    def go_left(self, step_x: int = 1) -> None:
        self.coords[0] -= step_x


class FlyingRobot(BaseRobot):
    def __init__(
        self,
        name: str,
        weight: int,
        coords: Optional[List[int]] = None
    ) -> None:
        super().__init__(
            name,
            weight,
            coords=[0, 0, 0] if coords is None else coords
        )

    def go_up(self, step_z: int = 1) -> None:
        self.coords[2] += step_z

    def go_down(self, step_z: int = 1) -> None:
        self.coords[2] -= step_z


class DeliveryDrone(FlyingRobot):
    def __init__(
        self,
        name: str,
        weight: int,
        coords: Optional[List[int]] = None,
        max_load_weight: int = None,
        current_load: Optional[Cargo] = None
    ) -> None:
        super().__init__(name, weight, coords)
        self.max_load_weight = max_load_weight
        self.current_load = current_load

    def hook_load(self, cargo: Cargo) -> None:
        self.current_load = (
            cargo
            if self.current_load
            is None and cargo.weight <= self.max_load_weight
            else self.current_load
        )

    def unhook_load(self) -> None:
        self.current_load = None
