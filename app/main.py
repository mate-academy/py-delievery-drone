class Cargo:
    def __init__(self, weight: int) -> None:
        self.weight = weight


class BaseRobot:
    def __init__(
        self, name: str, weight: int, coords: list[int] | None = None
    ) -> None:
        self.name: str = name
        self.weight: int = weight
        self.coords: list[int] = [0, 0] if coords is None else coords

    def go_forward(self, step: int = 1) -> None:
        self.coords[1] += step

    def go_right(self, step: int = 1) -> None:
        self.coords[0] += step

    def go_back(self, step: int = 1) -> None:
        self.coords[1] -= step

    def go_left(self, step: int = 1) -> None:
        self.coords[0] -= step

    def get_info(self) -> str:
        return f"Robot: {self.name}, Weight: {self.weight}"


class FlyingRobot(BaseRobot):
    def __init__(
        self, name: str, weight: int, coords: list[int] | None = None
    ) -> None:
        super().__init__(name, weight, [0, 0, 0] if coords is None else coords)

    def go_up(self, step: int = 1) -> None:
        self.coords[2] += step

    def go_down(self, step: int = 1) -> None:
        self.coords[2] -= step


class DeliveryDrone(FlyingRobot):
    def __init__(
        self,
        name: str,
        weight: int,
        max_load_weight: int,
        current_load: Cargo | None,
        coords: list[int] | None = None,
    ) -> None:
        super().__init__(name, weight, coords)
        self.max_load_weight: int = max_load_weight
        self.current_load: Cargo | None = current_load

    def hook_load(self, cargo: Cargo) -> None:
        if not self.current_load and self.max_load_weight >= cargo.weight:
            self.current_load = cargo

    def unhook_load(self) -> None:
        self.current_load = None
