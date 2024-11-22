class Cargo:
    def __init__(self, weight: int) -> None:
        self.weight = weight


class BaseRobot:
    """
    Represents a Base Robot with the ability to move on a 2D plane.

    Attributes:
    ----------
    name : str
        the name of the Robot
    weight : int
        the weight of the Robot
    coords : list
        the coordinates [x, y] of the Robot

    Methods:
    _______
    go_forward()
        move the Robot along the positive 'Y' coordinate by 'step'

    go_back()
        move the Robot along the negative 'Y' coordinate by 'step'

    go_right()
        move the Robot along the positive 'X' coordinate by 'step'

    go_left()
        move the Robot along the negative 'X' coordinate by 'step'

    get_info()
        returns a message about Robot
    """
    def __init__(
            self,
            name: str,
            weight: int,
            coords: list = None
    ) -> None:
        self.name = name
        self.weight = weight
        self.coords = coords or [0, 0]

    def go_forward(self, step: int = 1) -> None:
        """
        Move the Robot along the positive 'Y' coordinate by 'step'.
        :param step: int
        :return: None
        """
        self.coords[1] += step

    def go_back(self, step: int = 1) -> None:
        """
        Move the Robot along the negative 'Y' coordinate by 'step'.
        :param step: int
        :return: None
        """
        self.coords[1] -= step

    def go_right(self, step: int = 1) -> None:
        """
        Move the Robot along the positive 'X' coordinate by 'step'.
        :param step: int
        :return: None
        """
        self.coords[0] += step

    def go_left(self, step: int = 1) -> None:
        """
        Move the Robot along the negative 'Y' coordinate by 'step'.
        :param step: int
        :return: None
        """
        self.coords[0] -= step

    def get_info(self) -> str:
        """
        Returns a message about Robot.
        :return: str
        """
        return f"Robot: {self.name}, Weight: {self.weight}"


class FlyingRobot(BaseRobot):
    def __init__(
            self,
            name: str,
            weight: int,
            coords: list = None
    ) -> None:
        if not coords:
            super().__init__(name=name, weight=weight)
            self.coords.append(0)
        else:
            super().__init__(name=name, weight=weight, coords=coords)

    def go_up(self, step: int = 1) -> None:
        """
        Move the Flying Robot along the positive 'Z' coordinate by 'step'.
        :param step: int
        :return: None
        """
        self.coords[2] += step

    def go_down(self, step: int = 1) -> None:
        """
        Move the Flying Robot along the negative 'Z' coordinate by 'step'.
        :param step: int
        :return: None
        """
        self.coords[2] -= step


class DeliveryDrone(FlyingRobot):
    def __init__(
            self,
            name: str,
            weight: int,
            max_load_weight: int,
            current_load: int = None,
            coords: list = None
    ) -> None:
        super().__init__(name=name, weight=weight, coords=coords)
        self.max_load_weight = max_load_weight
        self.current_load = current_load

    def hook_load(self, cargo: Cargo) -> None:
        """
        Takes the Cargo object and keeps it.
        :param cargo: Cargo
        :return: None
        """
        if not self.current_load and cargo.weight <= self.max_load_weight:
            self.current_load = cargo

    def unhook_load(self) -> None:
        """
        Makes current load None.
        :return: None
        """
        self.current_load = None
