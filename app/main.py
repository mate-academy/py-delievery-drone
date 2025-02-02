class Cargo:
    def __init__(self, weight: int) -> None:
        self.weight = weight

    def __str__(self):
        return f"Вантаж вагою {self.weight} кг"


class BaseRobot:
    def __init__(self, name: str, weight: float, coords = None):
        if coords is None:
            coords = [0, 0]
        self.name = name
        self.weight = weight
        self.coords = coords

    def go_forward(self, step=1):
        self.coords[1] +=step

    def go_back(self, step=1):
        self.coords[1] -= step

    def go_right(self, step=1):
        self.coords[0] += step

    def go_left(self, step=1):
        self.coords[0] -= step

    def get_info(self):
        return f"Robot: {self.name}, Weight: {self.weight}"

class FlyingRobot(BaseRobot):
    def __init__(self, name: str, weight: float, coords=None):
        if coords is None:
            coords = [0, 0]
        coords += [0]
        super().__init__(name, weight, coords)

    def go_up(self, step=1):
        self.coords[2] += step
        print(self.coords)

    def go_down(self, step=1):
        self.coords[2] -= step
        print(self.coords)
class DeliveryDrone(FlyingRobot):
    def __init__(
            self, name: str,
            weight: float,
            max_load_weight: int,
            coords=None,
            current_load: Cargo = None
    ):
        super().__init__(name, weight, coords)
        self.max_load_weight = max_load_weight
        self.current_load = None

    def hook_load(self, cargo: Cargo):
        if self.current_load is None and cargo.weight <= self.max_load_weight:
            self.current_load = cargo
        print(self.current_load)

    def unhook_load(self):
        self.current_load = None
        print(self.current_load)

cargo = Cargo(14)
drone = DeliveryDrone(
    name="Jim",
    weight=18,
    coords=[11, -4, 16],
    max_load_weight=20,
    current_load=None,
)
drone.hook_load(cargo)
# drone.current_load is cargo

cargo2 = Cargo(2)
drone.hook_load(cargo2)
# drone.current_load is cargo
# didn't hook cargo2, cargo already in current load


