from typing import Optional, List


class Cargo:
    def __init__(self, weight: int) -> None:
        self.weight = weight


class BaseRobot:
    def __init__(self, name: str,
                 weight: int,
                 coords: Optional[List[int]] = None) -> None:
        self.name = name
        self.weight = weight
        self.coords = coords or [0, 0]

    def get_info(self) -> str:
        return f"Robot: {self.name}, Weight: {self.weight}"

    def go_forward(self, step: int = 1) -> None:
        self.coords[1] += step

    def go_back(self, step: int = 1) -> None:
        self.coords[1] -= step

    def go_right(self, step: int = 1) -> None:
        self.coords[0] += step

    def go_left(self, step: int = 1) -> None:
        self.coords[0] -= step


class FlyingRobot(BaseRobot):
    def __init__(self, name: str,
                 weight: int,
                 coords: Optional[List[int]] = None) -> None:
        coords = [0, 0, 0] if not coords else coords
        super().__init__(name, weight, coords)

    def go_up(self, step: int = 1) -> None:
        self.coords[2] += step

    def go_down(self, step: int = 1) -> None:
        self.coords[2] -= step


class DeliveryDrone(FlyingRobot):
    def __init__(self, name: str,
                 weight: int,
                 coords: Optional[List[int]] = None,
                 max_load_weight: Optional[int] = None,
                 current_load: Optional[int] = None) -> None:
        super().__init__(name, weight, coords)
        self.max_load_weight = max_load_weight
        self.current_load = current_load

    def hook_load(self, cargo_obj: Cargo) -> None:
        if (
                self.max_load_weight >= cargo_obj.weight
                and self.current_load is None
        ):
            self.current_load = cargo_obj

    def unhook_load(self) -> None:
        self.current_load = None
