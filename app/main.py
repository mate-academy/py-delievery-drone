class Cargo:
    def __init__(self, weight: int) -> None:
        self.weight = weight


class BaseRobot:
    def __init__(self, name: str, weight: int, coords: list = None) -> None:
        self.name = name
        self.weight = weight
        if coords:
            self.coords = coords
        else:
            self.coords = [0, 0]

    def go_somewhere_positive_direct(self, index: int, step: int = 1) -> None:
        self.coords[index] += step

    def go_somewhere_negative_direct(self, index: int, step: int = 1) -> None:
        self.coords[index] -= step

    def go_forward(self, step: int = 1) -> None:
        self.go_somewhere_positive_direct(index=1, step=step)

    def go_back(self, step: int = 1) -> None:
        self.go_somewhere_negative_direct(index=1, step=step)

    def go_right(self, step: int = 1) -> None:
        self.go_somewhere_positive_direct(index=0, step=step)

    def go_left(self, step: int = 1) -> None:
        self.go_somewhere_negative_direct(index=0, step=step)

    def get_info(self) -> str:
        return f"Robot: {self.name}, Weight: {self.weight}"


class FlyingRobot(BaseRobot):
    def __init__(self, name: str, weight: int, coords: list = None) -> None:
        if coords:
            super().__init__(name, weight, coords)
        else:
            super().__init__(name, weight, [0, 0, 0])

    def go_up(self, step: int = 1) -> None:
        self.go_somewhere_positive_direct(index=2, step=step)

    def go_down(self, step: int = 1) -> None:
        self.go_somewhere_negative_direct(index=2, step=step)


class DeliveryDrone(FlyingRobot):
    def __init__(self, name: str, weight: int, max_load_weight: int,
                 current_load: Cargo | None, coords: list = None) -> None:
        super().__init__(name, weight, coords)
        self.max_load_weight = max_load_weight
        self.current_load = current_load

    def hook_load(self, cargo: Cargo) -> None:
        if self.current_load is None and cargo.weight <= self.max_load_weight:
            self.current_load = cargo

    def unhook_load(self) -> None:
        if self.current_load is not None:
            self.current_load = None
