class Cargo:
    def __init__(self, weight: int) -> None:
        self.weight = weight


class BaseRobot(Cargo):
    def __init__(self, name: str, weight: int, coords: list = None) -> None:
        if coords is None:
            coords = [0, 0]
        super().__init__(weight)
        self.name = name
        self.coords = coords
        self.coords = coords if coords else [0, 0]

    def move(self, direction: str, step: int = 1) -> None:
        directions = {
            "forward": (0, step),
            "back": (0, -step),
            "right": (step, 0),
            "left": (-step, 0)
        }
        if direction in directions:
            self.coords[0] += directions[direction][0]
            self.coords[1] += directions[direction][1]

    def get_info(self) -> str:
        return f"Robot: {self.name}, Weight: {self.weight}"


class FlyingRobot(BaseRobot):
    def __init__(self, name: str, weight: int, coords: list = None) -> None:
        super().__init__(name, weight, coords if coords else [0, 0, 0])

    def move(self, direction: str, step: int = 1) -> None:
        super().move(direction, step)
        if direction == "up":
            self.coords[2] += step
        elif direction == "down":
            self.coords[2] -= step


class DeliveryDrone(FlyingRobot):
    def __init__(
            self,
            name: str,
            weight: int,
            coords: list = None,
            max_load_weight: int = 0,
            current_load: Cargo = None,
    ) -> None:
        super().__init__(name, weight, coords)
        self.max_load_weight = max_load_weight
        self.current_load = current_load

    def hook_load(self, cargo: Cargo) -> None:
        if self.current_load is None and cargo.weight <= self.max_load_weight:
            self.current_load = cargo
    # намагався використати тернарний оператор для присвоєння,
    # але виглядало жахливо

    def unhook_load(self) -> None:
        self.current_load = None
