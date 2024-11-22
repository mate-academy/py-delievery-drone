class Cargo:

    def __init__(
            self,
            weight: int
    ) -> None:
        self.weight = weight


class BaseRobot:
    def __init__(
            self,
            name: str,
            weight: int,
            coords: list = None
    ) -> None:
        self.name = name
        self.weight = weight
        self.coords = [0, 0] if coords is None else coords

    def go_forward(self, forward: int = 1) -> None:
        self.coords[1] += forward

    def go_back(self, back: int = 1) -> None:
        self.coords[1] -= back

    def go_right(self, right: int = 1) -> None:
        self.coords[0] += right

    def go_left(self, left: int = 1) -> None:
        self.coords[0] -= left

    def get_info(self) -> str:
        return f"Robot: {self.name}, Weight: {self.weight}"


class FlyingRobot(BaseRobot):
    def __init__(
            self,
            name: str,
            weight: int,
            coords: list = None
    ) -> None:
        super().__init__(
            name,
            weight,
            [0, 0, 0] if coords is None else coords
        )

    def go_up(self, up: int = 1) -> None:
        self.coords[2] += up

    def go_down(self, down: int = 1) -> None:
        self.coords[2] -= down


class DeliveryDrone(FlyingRobot):
    def __init__(
            self,
            name: str,
            weight: int,
            coords: list = None,
            max_load_weight: int = None,
            current_load: Cargo = None
    ) -> None:
        super().__init__(
            name,
            weight,
            coords
        )
        self.max_load_weight = max_load_weight
        self.current_load = current_load

    def hook_load(self, cargo: Cargo) -> None:
        if self.current_load is None and cargo.weight <= self.max_load_weight:
            self.current_load = cargo

    def unhook_load(self) -> None:
        self.current_load = None
