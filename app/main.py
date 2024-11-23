class BaseRobot:
    def __init__(self,
                 name: str,
                 weight: int,
                 coords: list[int] = None) -> None:
        self.name = name
        self.weight = weight
        self.coords = coords if coords is not None else [0, 0]

    def go_forward(self, steps: int = 1) -> None:
        self.coords[1] += steps

    def go_back(self, steps: int = 1) -> None:
        self.coords[1] -= steps

    def go_left(self, steps: int = 1) -> None:
        self.coords[0] -= steps

    def go_right(self, steps: int = 1) -> None:
        self.coords[0] += steps

    def get_info(self) -> str:
        return f"Robot: {self.name}, Weight: {self.weight}"


class FlyingRobot(BaseRobot):
    def __init__(self,
                 name: str,
                 weight: int,
                 coords: list[int] = None,
                 ) -> None:
        if coords is None:
            coords = [0, 0, 0]
        elif len(coords) <= 2:
            coords.append(0)
        elif len(coords) >= 3:
            coords = coords[:3]
        super().__init__(name, weight, coords[:2])
        self.coords = coords

    def go_up(self, steps: int = 1) -> None:
        self.coords[2] += steps

    def go_down(self, steps: int = 1) -> None:
        self.coords[2] -= steps


class DeliveryDrone(FlyingRobot):
    def __init__(self,
                 name: str,
                 weight: int,
                 max_load_weight: int,
                 coords: list[int] = None,
                 current_load: "Cargo" = None,
                 ) -> None:
        super().__init__(name, weight, coords)
        self.max_load_weight = max_load_weight
        self.current_load = current_load

    def hook_load(self, cargo: "Cargo") -> None:
        if self.current_load is None and cargo.weight <= self.max_load_weight:
            self.current_load = cargo

    def unhook_load(self) -> None:
        self.current_load = None


class Cargo:
    def __init__(self, weight: int) -> None:
        self.weight = weight
