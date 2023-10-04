class Cargo:
    def __init__(self, weight: int) -> None:
        self.weight = weight


class BaseRobot:
    def __init__(self, name: str, weight: int, coords: tuple[int] = (0, 0)) -> None:
        self.name = name
        self.weight = weight
        self.coords = list(coords)

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
        coords: tuple[int] = (0, 0, 0)
    ) -> None:
        super().__init__(name, weight, coords)

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
        coords: tuple[int] = (0, 0, 0),
        current_load: None = None | int
    ) -> None:
        super().__init__(name, weight, coords)
        self.max_load_weight = max_load_weight
        self.current_load = current_load

    def hook_load(self, other: "Cargo") -> None:
        if self.current_load is None and other.weight <= self.max_load_weight:
            self.current_load = other

    def unhook_load(self) -> None:
        self.current_load = None
