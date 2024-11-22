class Cargo:
    def __init__(self, weight: int) -> None:
        self.weight = weight


class BaseRobot:

    def __init__(
            self,
            name: str,
            weight: int,
            coords: list[int] = None
    ) -> None:

        self.name = name
        self.weight = weight
        self.coords = coords
        self.coords = coords or [0, 0]

    def go_forward(self, steps: int = 1) -> None:
        self.coords[1] += steps

    def go_back(self, steps: int = 1) -> None:
        self.go_forward(-steps)

    def go_right(self, steps: int = 1) -> None:
        self.coords[0] += steps

    def go_left(self, steps: int = 1) -> None:
        self.go_right(-steps)

    def get_info(self) -> str:
        return f"Robot: {self.name}, Weight: {self.weight}"


class FlyingRobot(BaseRobot):

    def __init__(
            self, name: str, weight: int, coords: list[int] = None
    ) -> None:

        super().__init__(name, weight, coords or [0, 0, 0])

    def go_up(self, levels: int = 1) -> None:
        self.coords[-1] += levels

    def go_down(self, levels: int = 1) -> None:
        self.go_up(-levels)


class DeliveryDrone(FlyingRobot):

    def __init__(
            self,
            max_load_weight: int,
            name: str,
            weight: int,
            coords: list[int] = None,
            current_load: int = None
    ) -> None:

        super().__init__(name, weight, coords)
        self.max_load_weight = max_load_weight
        self.current_load = current_load

    def hook_load(self, cargo: Cargo) -> None:
        if cargo.weight <= self.max_load_weight and self.current_load is None:
            self.current_load = cargo

    def unhook_load(self) -> None:
        self.current_load = None
