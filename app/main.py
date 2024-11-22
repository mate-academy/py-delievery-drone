class Cargo:
    def __init__(self, weight: int) -> None:
        self.weight = weight


class BaseRobot:
    def __init__(
            self,
            name: str,
            weight: int,
            coords: list | None = None
    ) -> None:
        self.name = name
        self.weight = weight
        self.coords = coords if coords else [0, 0]

    def get_info(self) -> str:
        return f"Robot: {self.name}, Weight: {self.weight}"

    def go_forward(self, step: int = 1) -> list:
        self.coords[1] += step
        return self.coords

    def go_back(self, step: int = 1) -> list:
        self.coords[1] -= step
        return self.coords

    def go_right(self, step: int = 1) -> list:
        self.coords[0] += step
        return self.coords

    def go_left(self, step: int = 1) -> list:
        self.coords[0] -= step
        return self.coords


class FlyingRobot(BaseRobot):
    def __init__(
            self,
            name: str,
            weight: int,
            coords: list | None = None
    ) -> None:
        self.coords = coords if coords else [0, 0, 0]
        super().__init__(name, weight, self.coords)

    def go_up(self, step: int = 1) -> list:
        self.coords[2] += step
        return self.coords

    def go_down(self, step: int = 1) -> list:
        self.coords[2] -= step
        return self.coords


class DeliveryDrone(FlyingRobot):
    def __init__(
            self,
            name: str,
            weight: int,
            max_load_weight: int,
            current_load: Cargo | None,
            coords: list | None = None,
    ) -> None:
        self.max_load_weight = max_load_weight
        self.current_load = current_load
        super().__init__(name, weight, coords)

    def hook_load(self, cargo: Cargo) -> None:
        if not self.current_load and cargo.weight <= self.max_load_weight:
            self.current_load = cargo

    def unhook_load(self) -> None:
        self.current_load = None
