class Cargo:
    def __init__(self, weight: int) -> None:
        self.weight = weight


class BaseRobot(Cargo):

    def __init__(self, name: str, weight: int, coords: list = None) -> None:
        super().__init__(weight=weight)
        coords = [0, 0] if coords is None else coords

        self.name = name
        self.coords = coords

    def go_forward(self, step: int = 1) -> None:
        self.coords[1] = self.coords[1] + step

    def go_back(self, step: int = 1) -> None:
        self.coords[1] = self.coords[1] - step

    def go_right(self, step: int = 1) -> None:
        self.coords[0] = self.coords[0] + step

    def go_left(self, step: int = 1) -> None:
        self.coords[0] = self.coords[0] - step

    def get_info(self) -> str:
        return f"Robot: {self.name}, Weight: {self.weight}"


class FlyingRobot(BaseRobot):
    def __init__(self, name: str, weight: int, coords: list = None) -> None:
        coords = [0, 0, 0] if coords is None else coords

        super().__init__(name=name, weight=weight, coords=coords)

    def go_up(self, step: int = 1) -> None:
        self.coords[2] = self.coords[2] + step

    def go_down(self, step: int = 1) -> None:
        self.coords[2] = self.coords[2] - step


class DeliveryDrone(FlyingRobot):
    def __init__(self,
                 max_load_weight: int,
                 current_load: int,
                 name: str,
                 weight: int,
                 coords: list = None) -> None:

        super().__init__(name=name, weight=weight, coords=coords)
        self.max_load_weight = max_load_weight
        self.current_load = current_load

    def hook_load(self, cargo_load: Cargo) -> None:
        if (self.current_load is None
                and cargo_load.weight <= self.max_load_weight):
            self.current_load = cargo_load

    def unhook_load(self) -> None:
        self.current_load = None
