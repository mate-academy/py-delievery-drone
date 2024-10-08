class Cargo:
    def __init__(self, weight: int) -> None:
        self.weight = weight


class BaseRobot:
    def __init__(self, name: str, weight: int, coords: [int] = None) -> None:
        self.name = name
        self.weight = weight
        if coords is None:
            self.coords = [0, 0]
        else:
            self.coords = coords

    def go_forward(self, num: int = 1) -> None:
        self.coords[1] += num

    def go_back(self, num: int = 1) -> None:
        self.coords[1] -= num

    def go_right(self, num: int = 1) -> None:
        self.coords[0] += num

    def go_left(self, num: int = 1) -> None:
        self.coords[0] -= num

    def get_info(self) -> str:
        return f"Robot: {self.name}, Weight: {self.weight}"


class FlyingRobot(BaseRobot):
    def __init__(self, name: str, weight: int, coords: [int] = None) -> None:
        if coords is None:
            coords = [0, 0, 0]
        super().__init__(name, weight, coords)

    def go_up(self, num: int = 1) -> None:
        self.coords[2] += num

    def go_down(self, num: int = 1) -> None:
        self.coords[2] -= num


class DeliveryDrone(FlyingRobot):
    def __init__(self, name: str, weight: int,
                 max_load_weight: int,
                 current_load: Cargo,
                 coords: int = None) -> None:
        if coords is None:
            coords = [0, 0, 0]
        super().__init__(name, weight, coords)
        self.max_load_weight = max_load_weight
        self.current_load = current_load

    def hook_load(self, cargo: Cargo) -> None:
        if self.current_load is None and cargo.weight <= self.max_load_weight:
            self.current_load = cargo

    def unhook_load(self,) -> None:
        if self.current_load is not None:
            self.current_load = None
