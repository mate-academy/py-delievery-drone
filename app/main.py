from app.base_robot import BaseRobot
from app.constants import FLYING_STEP, Z_INDEX


class Cargo:
    def __init__(self, weight: int) -> None:
        self.weight = weight


class FlyingRobot(BaseRobot):

    def __init__(self, name: str, weight: int,
                 coords: list[int] | None = None) -> None:
        super().__init__(name, weight, coords)
        self.coords = coords if coords else [0, 0, 0]

    def go_up(self, step: int = FLYING_STEP) -> None:
        self.move(step, "+", Z_INDEX)

    def go_down(self, step: int = FLYING_STEP) -> None:
        self.move(step, "-", Z_INDEX)


class DeliveryDrone(FlyingRobot):
    def __init__(self, name: str,
                 weight: int,
                 max_load_weight: int,
                 current_load: None | Cargo = None,
                 coords: list[int] | None = None
                 ) -> None:
        super().__init__(name=name, weight=weight,
                         coords=coords)
        self.max_load_weight = max_load_weight
        self.current_load = current_load

    def hook_load(self, cargo: Cargo) -> None:
        if (cargo.weight <= self.max_load_weight
                and self.current_load is None):
            self.current_load = cargo

    def unhook_load(self) -> None:
        if self.current_load is not None:
            self.current_load = None
