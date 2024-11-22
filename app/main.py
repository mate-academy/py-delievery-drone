class Cargo:
    def __init__(self, weight: int) -> None:
        self.weight = weight

# write your code here


class BaseRobot:
    def __init__(self,
                 name: str,
                 weight: int,
                 coords: list[int] | None = None) -> None:
        self.name = name
        self.weight = weight
        self.coords = [0, 0] if not coords else coords

    def go_forward(self, coordinate: int = 1) -> None:
        self.coords[1] += coordinate

    def go_back(self, coordinate: int = 1) -> None:
        self.coords[1] -= coordinate

    def go_left(self, coordinate: int = 1) -> None:
        self.coords[0] -= coordinate

    def go_right(self, coordinate: int = 1) -> None:
        self.coords[0] += coordinate

    def get_info(self) -> str:
        return f"Robot: {self.name}, Weight: {self.weight}"


class FlyingRobot(BaseRobot):
    def __init__(self,
                 name: str,
                 weight: int,
                 coords: list[int] = None) -> None:
        if not coords:
            coords = [0, 0, 0]
        super().__init__(name=name,
                         weight=weight,
                         coords=coords)

    def go_up(self, coordinate: int = 1) -> None:
        self.coords[2] += coordinate

    def go_down(self, coordinate: int = 1) -> None:
        self.coords[2] -= coordinate


class DeliveryDrone(FlyingRobot):
    def __init__(self,
                 max_load_weight: int,
                 name: str,
                 weight: int,
                 coords: list[int] = None,
                 current_load: Cargo = None) -> None:
        if not coords:
            coords = [0, 0, 0]
        super().__init__(name=name,
                         weight=weight,
                         coords=coords)
        self.max_load_weight = max_load_weight
        self.current_load = current_load

    def hook_load(self, cargo: Cargo) -> None:
        if cargo.weight <= self.max_load_weight and not self.current_load:
            self.current_load = cargo

    def unhook_load(self) -> None:
        self.current_load = None
