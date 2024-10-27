class Cargo:
    def __init__(self, weight: int) -> None:
        self.weight = weight


class BaseRobot:
    def __init__(self, name: str, weight: int, coords: list = None) -> None:
        if coords is None:
            coords = [0, 0]
        self.name = name
        self.weight = weight
        self.coords = coords

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

    def get_info(self) -> str:
        return f"Robot: {self.name}, Weight: {self.weight}"


class FlyingRobot(BaseRobot):
    def __init__(self, name: str, weight: int, coords: list = None) -> None:
        if coords is None:
            coords = [0, 0, 0]
        super().__init__(name, weight)
        self.coords = coords

    def go_up(self, step: int = 1) -> list:
        self.coords[2] += step
        return self.coords

    def go_down(self, step: int = 1) -> list:
        self.coords[2] -= step
        return self.coords


class DeliveryDrone(FlyingRobot):
    def __init__(self, name: str, weight: int, max_load_weight: int,
                 current_load: Cargo = None, coords: list = None) -> None:
        if coords is None:
            coords = [0, 0, 0]
        super().__init__(name, weight, coords)
        self.max_load_weight = max_load_weight
        self.current_load = current_load

    def hook_load(self, cargo: Cargo) -> bool:
        if self.current_load is None and cargo.weight <= self.max_load_weight:
            self.current_load = cargo
            return True
        return False

    def unhook_load(self) -> Cargo:
        cargo = self.current_load
        self.current_load = None
        return cargo
