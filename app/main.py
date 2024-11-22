class Cargo:
    def __init__(self, weight: int) -> None:
        self.weight = weight


class BaseRobot:
    def __init__(
            self, name: str, weight: int, coords: list[int] | None = None
    ) -> None:
        if coords is None:
            coords = [0, 0]
        self.name = name
        self.weight = weight
        self.coords = coords

    def go_forward(self, step: int = 1) -> None:
        for _ in range(step):
            self.coords[1] += 1

    def go_back(self, step: int = 1) -> None:
        for _ in range(step):
            self.coords[1] -= 1

    def go_right(self, step: int = 1) -> None:
        for _ in range(step):
            self.coords[0] += 1

    def go_left(self, step: int = 1) -> None:
        for _ in range(step):
            self.coords[0] -= 1

    def get_info(self) -> str:
        return f"Robot: {self.name}, Weight: {self.weight}"


class FlyingRobot(BaseRobot):
    def __init__(
            self, name: str, weight: int, coords: list[int] | None = None
    ) -> None:
        super().__init__(name, weight)
        if coords is None:
            coords = [0, 0, 0]
        self.coords = coords

    def go_up(self, step: int = 1) -> None:
        for _ in range(step):
            self.coords[2] += 1

    def go_down(self, step: int = 1) -> None:
        for _ in range(step):
            self.coords[2] -= 1


class DeliveryDrone(FlyingRobot):
    def __init__(
            self, name: str,
            weight: int, coords: list[int] | None = None,
            max_load_weight: int = 0, current_load: int = 0
    ) -> None:
        super().__init__(name, weight, coords)
        self.max_load_weight = max_load_weight
        self.current_load = current_load

    def hook_load(self, cargo: "Cargo") -> str:
        if self.current_load is None and cargo.weight <= self.max_load_weight:
            self.current_load = cargo
            return f"{self.current_load} is {cargo}"
        return f"didn't hook {cargo}"

    def unhook_load(self) -> str:
        self.current_load = None
        return f"{self.current_load} is None"
