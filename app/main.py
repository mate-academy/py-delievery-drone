# Class to represent Cargo
class Cargo:
    def __init__(self, weight: int) -> None:
        self.weight = weight


class BaseRobot:
    def __init__(self, name: str, weight: int, coords: list = None) -> None:
        self.name = name
        self.weight = weight
        if coords is None:
            coords = [0, 0]
        self.coords = coords

    def go_forward(self, step: int = 1) -> None:
        self.coords[1] += step

    def go_back(self, step: int = 1) -> None:
        self.coords[1] -= step

    def go_right(self, step: int = 1) -> None:
        self.coords[0] += step

    def go_left(self, step: int = 1) -> None:
        self.coords[0] -= step

    def get_info(self) -> str:
        return f"Robot: {self.name}, Weight: {self.weight}"


class FlyingRobot(BaseRobot):
    def __init__(self, name: str, weight: float, coords: list = None) -> None:
        if coords is None:
            coords = [0, 0, 0]
        super().__init__(name=name, weight=weight, coords=coords)

    def go_up(self, step: int = 1) -> None:
        self.coords[2] += step

    def go_down(self, step: int = 1) -> None:
        self.coords[2] -= step


class DeliveryDrone(FlyingRobot):
    def __init__(self, name: str, weight: float,
                 max_load_weight: float,
                 current_load: object = None,
                 coords: list = None) -> None:
        super().__init__(name=name, weight=weight, coords=coords)
        self.max_load_weight = max_load_weight
        self.current_load = current_load

        # Hook load if current_load is not None
        if self.current_load is not None:
            self.hook_load(self.current_load)

    def hook_load(self, cargo: Cargo) -> None:
        if self.current_load is None and cargo.weight <= self.max_load_weight:
            self.current_load = cargo
            print(f"Cargo {cargo} hooked successfully.")
        else:
            print(f"Cannot hook cargo {cargo}.")

    def unhook_load(self) -> None:
        if self.current_load is not None:
            print(f"Unhooked cargo {self.current_load}.")
            self.current_load = None
        else:
            print("No cargo to unhook.")
