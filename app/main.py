class Cargo:
    def __init__(self, weight: int) -> None:
        self.weight = weight


class BaseRobot:

    def __init__(self,
                 name: str,
                 weight: int,
                 coords: list[int] = None
                 ) -> None:
        self.name = name
        self.weight = weight
        self.coords = coords or [0, 0]

    def go_forward(self, step: int = 1) -> None:
        self.coords[1] += step

    def go_right(self, step: int = 1) -> None:
        self.coords[0] += step

    def go_left(self, step: int = 1) -> None:
        self.coords[0] -= step

    def go_back(self, step: int = 1) -> None:
        self.coords[1] -= step

    def get_info(self) -> str:
        return f"Robot: {self.name}, Weight: {self.weight}"


class FlyingRobot(BaseRobot):

    def __init__(self,
                 name: str,
                 weight: int,
                 coords: list[int] = None
                 ) -> None:
        super().__init__(name,
                         weight,
                         coords=coords or [0, 0, 0])

    def go_up(self, up: int = 1) -> None:
        self.coords[2] += up

    def go_down(self, down: int = 1) -> None:
        self.coords[2] -= down


class DeliveryDrone(FlyingRobot):
    def __init__(self,
                 name: str,
                 weight: int,
                 coords: list[int] = None,
                 max_load_weight: int = 0,
                 current_load: Cargo = None
                 ) -> None:
        super().__init__(name, weight, coords)
        self.current_load = current_load
        self.max_load_weight = max_load_weight

    def hook_load(self, elem: Cargo) -> None:
        if self.current_load is None and elem.weight <= self.max_load_weight:
            self.current_load = elem

    def unhook_load(self) -> None:
        self.current_load = None
