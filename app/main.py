class Cargo:
    def __init__(self, weight: int) -> None:
        self.weight = weight


class BaseRobot:
    def __init__(self, name: str, weight: int,
                 coords: list[int] = None) -> None:
        self.name = name
        self.weight = weight
        self.coords = coords or [0, 0] or [0, 0, 0]

    def go_forward(self, step: int = 1) -> list[int]:
        self.coords[1] += step
        return self.coords

    def go_back(self, step: int = 1) -> list[int]:
        self.coords[1] -= step
        return self.coords

    def go_right(self, step: int = 1) -> list[int]:
        self.coords[0] += step
        return self.coords

    def go_left(self, step: int = 1) -> list[int]:
        self.coords[0] -= step
        return self.coords

    def get_info(self) -> str:
        return f"Robot: {self.name}, Weight: {self.weight}"


class FlyingRobot(BaseRobot):
    def __init__(self, name: str, weight: int,
                 coords: list[int] = None) -> None:
        self.coords = coords or [0, 0, 0]
        super().__init__(name=name, weight=weight, coords=self.coords)

    def go_up(self, step: int = 1) -> list[int]:
        if len(self.coords) < 3:
            self.coords.append(step)
        self.coords[2] += step
        return self.coords

    def go_down(self, step: int = 1) -> list[int]:
        if len(self.coords) < 3:
            self.coords.append(step)
        self.coords[2] -= step
        return self.coords


class DeliveryDrone(FlyingRobot):
    def __init__(self, name: str, weight: int, max_load_weight: int,
                 current_load: Cargo, coords: list[int] = None) -> None:
        self.coords = coords or [0, 0, 0]
        super().__init__(name=name, weight=weight, coords=self.coords)
        self.max_load_weight = max_load_weight
        self.current_load = current_load

    def hook_load(self, cargo_object: Cargo) -> None:
        if self.current_load is None\
                and cargo_object.weight <= self.max_load_weight:
            self.current_load = cargo_object

    def unhook_load(self) -> None:
        self.current_load = None
