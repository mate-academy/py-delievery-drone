class Cargo:
    def __init__(self, weight: int) -> None:
        self.weight = weight

# write your code here
class BaseRobot:
    def __init__(self, name: str, weight: float, coords: list[int] = None) -> None:
        self.name = name
        self.weight = weight
        self.coords = coords or [0, 0]

    def go_forward(self, step: int = 1) -> None:
        self.coords[1] += step

    def go_back(self, step: int = 1) -> None:
        self.coords[1] -= step

    def go_right(self, step: int = 1) -> None:
        self.coords[0] += step

    def go_left(self, step: int = 1) -> None:
        self.coords[0] -= step

    def get_info(self) -> None:
        print(f"Robot: {self.name}, Weight: {self.weight}")
