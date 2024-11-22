class Cargo:
    def __init__(self, weight: int) -> None:
        self.weight = weight


class BaseRobot:

    def __init__(self, name: str, weight: int, coords: None = None) -> None:
        self.name = name
        self.weight = weight
        self.coords = coords
        if self.coords is None:
            self.coords = [0, 0]

    def go_forward(self, step: int = 1) -> None:
        self.coords[1] += 1 * step

    def go_back(self, step: int = 1) -> None:
        self.coords[1] -= 1 * step

    def go_right(self, step: int = 1) -> None:
        self.coords[0] += 1 * step

    def go_left(self, step: int = 1) -> None:
        self.coords[0] -= 1 * step

    def get_info(self) -> str:
        return f"Robot: {self.name}, Weight: {self.weight}"


class FlyingRobot(BaseRobot):

    def __init__(self, name: str, weight: int, coords: None = None) -> None:
        super().__init__(name, weight)
        self.coords = coords
        if self.coords is None or self.coords == [0, 0]:
            self.coords = [0, 0, 0]

    def go_up(self, step: int = 1) -> None:
        self.coords[2] += (1 * step)

    def go_down(self, step: int = 1) -> None:
        self.coords[2] -= (1 * step)


class DeliveryDrone(FlyingRobot):
    def __init__(self, name: str,
                 weight: int,
                 max_load_weight: int,
                 current_load: int, coords: None = None) -> None:
        super().__init__(name, weight, coords)
        self.max_load_weight = max_load_weight
        self.current_load = current_load

    def hook_load(self, cargo_stat: Cargo) -> None:
        if self.current_load is None \
                and self.max_load_weight >= cargo_stat.weight:
            self.current_load = cargo_stat

    def unhook_load(self) -> None:
        self.current_load = None
