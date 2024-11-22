from app.constants import X_INDEX, Y_INDEX, BASE_ROBOT_STEP


class BaseRobot:

    def __init__(self, name: str, weight: int,
                 coords: list[int] | None = None) -> None:
        self.name = name
        self.weight = weight
        self.coords = coords if coords else [0, 0]

    def move(self, step: int,
             simbl: str, coord_index: int) -> None:
        value = eval(f"self.coords[{coord_index}] {simbl} {step}")
        self.coords[coord_index] = value

    def go_forward(self, step: int = BASE_ROBOT_STEP) -> None:
        self.move(step, "+", Y_INDEX)

    def go_back(self, step: int = BASE_ROBOT_STEP) -> None:
        self.move(step, "-", Y_INDEX)

    def go_right(self, step: int = BASE_ROBOT_STEP) -> None:
        self.move(step, "+", X_INDEX)

    def go_left(self, step: int = BASE_ROBOT_STEP) -> None:
        self.move(step, "-", X_INDEX)

    def get_info(self) -> str:
        return f"Robot: {self.name}, Weight: {self.weight}"
