class Cargo:
    def __init__(self, weight: int) -> None:
        self.weight = weight


class BaseRobot:
    def __init__(
        self,
        name: str,
        weight: int,
        coords : list | None = None
    ) -> None:
        self.name = name
        self.weight = weight
        self.coords = self.init_coords(coords)

    def init_coords(self, coords: list | None) -> list:
        return coords if coords else [0, 0]

    def move(self, index: int, step: int) -> None:
        self.coords[index] += step

    def go_forward(self, step: int = 1) -> None:
        self.move(1, step)

    def go_back(self, step: int = 1) -> None:
        self.move(1, -step)

    def go_right(self, step: int = 1) -> None:
        self.move(0, step)

    def go_left(self, step: int = 1) -> None:
        self.move(0, -step)

    def get_info(self) -> str:
        return f"Robot: {self.name}, Weight: {self.weight}"


class FlyingRobot(BaseRobot):
    def __init__(
        self,
        name: str,
        weight: int,
        coords : list | None = None
    ) -> None:
        super().__init__(
            name, weight, coords if coords is not None else [0, 0, 0]
        )

    def go_up(self, step: int = 1) -> None:
        self.move(2, step)

    def go_down(self, step: int = 1) -> None:
        self.move(2, -step)


class DeliveryDrone(FlyingRobot):
    def __init__(
        self,
        name: str,
        weight: int,
        coords: list | None = None,
        max_load_weight: int = 0,
        current_load: Cargo | None = None
    ) -> None:
        super().__init__(name, weight, coords)
        self.max_load_weight = max_load_weight
        self.current_load = current_load

    def hook_load(self, cargo: Cargo) -> None:
        if not self.current_load and cargo.weight <= self.max_load_weight:
            self.current_load = cargo

    def unhook_load(self) -> None:
        self.current_load = None
