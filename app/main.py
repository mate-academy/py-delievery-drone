class Cargo:
    def __init__(self, weight: int) -> None:
        self.weight = weight


class BaseRobot:
    def __init__(self, name: str, weight: int, coords: list = None) -> None:
        self.coords = coords if coords is not None else [0, 0]
        self.weight = weight
        self.name = name

    def go_forward(self, rew: int = 1) -> None:
        self.coords[1] += rew

    def go_back(self, rew: int = 1) -> None:
        self.coords[1] -= rew

    def go_right(self, rew: int = 1) -> None:
        self.coords[0] += rew

    def go_left(self, rew: int = 1) -> None:
        self.coords[0] -= rew

    def get_info(self) -> str:
        if self.coords != [0, 0]:
            return (f"Robot: {self.name}, "
                    f"Weight: {self.weight}, Coordinates: {self.coords}")
        else:
            return f"Robot: {self.name}, Weight: {self.weight}"


class FlyingRobot(BaseRobot):
    def __init__(self, name: str, weight: int, coords: list = None) -> None:
        super().__init__(name, weight,
                         coords if coords is not None else [0, 0, 0])

    def go_up(self, rew: int = 1) -> None:
        self.coords[2] += rew

    def go_down(self, rew: int = 1) -> None:
        self.coords[2] -= rew


class DeliveryDrone(FlyingRobot):
    def __init__(self, name: str,
                 weight: int, max_load_weight: int,
                 current_load: Cargo = None, coords: list = None) -> None:
        super().__init__(name,
                         weight, coords if coords is not None else [0, 0, 0])
        self.max_load_weight = max_load_weight
        self.current_load = current_load

    def hook_load(self, cargo: Cargo) -> None:
        if self.current_load is None:
            if self.max_load_weight >= cargo.weight:
                self.current_load = cargo
            else:
                print(
                    f"Cannot hook load: Cargo weight"
                    f" {cargo.weight}"
                    f" exceeds maximum "
                    f"load weight {self.max_load_weight}.")
        else:
            print("Cannot hook load: A load is already hooked.")

    def unhook_load(self) -> None:
        self.current_load = None
