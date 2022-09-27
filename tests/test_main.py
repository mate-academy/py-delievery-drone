import pytest
import ast
import inspect
import typing
from typing import Callable

from app.main import BaseRobot, FlyingRobot, DeliveryDrone, Cargo


@pytest.mark.parametrize(
    "args,result",
    [
        (("John", 50), ("John", 50, [0, 0])),
        (("Michael", 30, [10, 1]), ("Michael", 30, [10, 1]))
    ]
)
def test_base_robot_has_attrs(args, result):
    robot = BaseRobot(*args)
    assert all([hasattr(robot, attr) for attr in ["name", "weight", "coords"]])
    assert (robot.name, robot.weight, robot.coords) == result


def test_base_robot_go():
    robot = BaseRobot("Michael", 40)
    robot.go_forward(4)
    assert robot.coords == [0, 4]
    robot.go_forward()
    assert robot.coords == [0, 5]
    robot.go_back(5)
    assert robot.coords == [0, 0]
    robot.go_back()
    assert robot.coords == [0, -1]
    robot.go_right(3)
    assert robot.coords == [3, -1]
    robot.go_right()
    assert robot.coords == [4, -1]
    robot.go_left(7)
    assert robot.coords == [-3, -1]
    robot.go_left()
    assert robot.coords == [-4, -1]


def test_base_robot_do_not_use_mutable_as_default():
    robot_1 = BaseRobot("", 1)
    robot_2 = BaseRobot("", 1)
    robot_1.go_forward(1)
    assert robot_2.coords == [0, 0]


def test_base_robot_get_info_method():
    robot = BaseRobot("Michael", 40)
    assert robot.get_info() == "Robot: Michael, Weight: 40"


def test_flying_robot_go():
    robot = FlyingRobot("Michael", 40)
    robot.go_forward(4)
    assert robot.coords == [0, 4, 0]
    robot.go_forward()
    assert robot.coords == [0, 5, 0]
    robot.go_back(5)
    assert robot.coords == [0, 0, 0]
    robot.go_back()
    assert robot.coords == [0, -1, 0]
    robot.go_right(3)
    assert robot.coords == [3, -1, 0]
    robot.go_right()
    assert robot.coords == [4, -1, 0]
    robot.go_left(7)
    assert robot.coords == [-3, -1, 0]
    robot.go_left()
    assert robot.coords == [-4, -1, 0]
    robot.go_up(3)
    assert robot.coords == [-4, -1, 3]
    robot.go_up()
    assert robot.coords == [-4, -1, 4]
    robot.go_down(4)
    assert robot.coords == [-4, -1, 0]
    robot.go_down()
    assert robot.coords == [-4, -1, -1]


@pytest.mark.parametrize(
    "args,result",
    [
        (("John", 50), ("John", 50, [0, 0, 0])),
        (("Michael", 30, [10, 1, 100]), ("Michael", 30, [10, 1, 100]))
    ]
)
def test_flying_robot_has_attrs(args, result):
    robot = FlyingRobot(*args)
    assert all([hasattr(robot, attr) for attr in ["name", "weight", "coords"]])
    assert (robot.name, robot.weight, robot.coords) == result


def test_flying_robot_do_not_use_mutable_as_default():
    robot_1 = FlyingRobot("", 1)
    robot_2 = FlyingRobot("", 1)
    robot_1.go_up(1)
    assert robot_2.coords == [0, 0, 0]


@pytest.mark.parametrize(
    "kwargs,result",
    [
        (
            {
                "name": "John", "weight": 50,
                "max_load_weight": 30, "current_load": None
            },
            ("John", 50, 30, None, [0, 0, 0])
        ),
        (
            {
                "name": "Michael", "weight": 30, "max_load_weight": 20,
                "current_load": None, "coords": [10, 1, 100]
            },
            ("Michael", 30, 20, None, [10, 1, 100])
        )
    ]
)
def test_deliver_robot_has_attrs(kwargs, result):
    robot = DeliveryDrone(**kwargs)
    assert all(
        hasattr(robot, attr)
        for attr in [
            "name", "weight", "max_load_weight", "current_load", "coords"
        ]
    )
    assert (
               robot.name, robot.weight, robot.max_load_weight,
               robot.current_load, robot.coords
           ) == result


def test_deliver_robot_hook_load_cargo_is_not_heavy():
    cargo = Cargo(20)
    drone = DeliveryDrone(
        name="Mike",
        weight=12,
        max_load_weight=30,
        current_load=None,
    )
    drone.hook_load(cargo)
    assert isinstance(drone.current_load, Cargo)


def test_deliver_robot_hook_load_cargo_equals_max_load_weight():
    cargo = Cargo(20)
    drone = DeliveryDrone(
        name="Mike",
        weight=12,
        max_load_weight=20,
        current_load=None,
    )
    drone.hook_load(cargo)
    assert isinstance(drone.current_load, Cargo)


def test_deliver_robot_hook_load_cargo_is_too_heavy():
    cargo = Cargo(50)
    drone = DeliveryDrone(
        name="Mike",
        weight=12,
        max_load_weight=30,
        current_load=None,
    )
    drone.hook_load(cargo)
    assert drone.current_load is None


def test_deliver_robot_hook_load_cargo_current_load_isnt_none():
    cargo = Cargo(20)
    cargo2 = Cargo(12)
    drone = DeliveryDrone(
        name="Mike",
        weight=12,
        max_load_weight=30,
        current_load=cargo2,
    )
    drone.hook_load(cargo)
    assert drone.current_load is cargo2


def test_deliver_robot_unhook_load():
    drone = DeliveryDrone(
        name="Mike",
        weight=12,
        max_load_weight=30,
        current_load=Cargo(12),
    )
    drone.unhook_load()
    assert drone.current_load is None


@pytest.mark.parametrize(
    "class_,parent",
    [
        (FlyingRobot, "BaseRobot"),
        (DeliveryDrone, "FlyingRobot"),
    ],
)
def test_inheritance_of_flying_and_delivery(
    class_, parent
):
    class_source = inspect.getsource(class_)
    parsed_class = ast.parse(class_source)
    assert [name.id for name in parsed_class.body[0].bases] == [
        parent
    ], f"'{class_.__name__}' should be inherited from {parent.__name__}'"


@pytest.mark.parametrize(
    "class_,methods,length",
    [
        (FlyingRobot, ["__init__", "go_up", "go_down"], 3),
        (DeliveryDrone, ["__init__", "hook_load", "unhook_load"], 3)
    ]
)
def test_methods_declared_in_inherited_classes(class_, methods, length):
    class_source = inspect.getsource(class_)
    parsed_class = ast.parse(class_source)
    assert (
            len(parsed_class.body[0].body) == length
    ), f"Only {length} methods should be defined inside class '{class_.__name__}'"
    assert (
            [parsed_class.body[0].body[it].name for it in range(length)] == methods
    ), f"Only {methods} should be defined inside class '{class_.__name__}'"


def test_removed_comment():
    import app
    with open(app.main.__file__, "r") as file:
        file_content = file.read()
        assert "# write your code here" not in file_content, ("You have to"
               " remove the unnecessary comment '# write your code here'")


@pytest.mark.parametrize(
    "function,result",
    [
        (
                BaseRobot.__init__,
                {"coords": typing.Optional[list[int]],
                 "name": str,
                 "weight": int,
                 "return": type(None)}
        ),
        (
                BaseRobot.go_forward,
                {"step": int, "return": type(None)}
        ),
        (
                BaseRobot.go_back,
                {"step": int, "return": type(None)}
        ),
        (
                BaseRobot.go_left,
                {"step": int, "return": type(None)}
        ),
        (
                BaseRobot.go_right,
                {"step": int, "return": type(None)}
        ),
        (
                BaseRobot.get_info,
                {} | {"return": str}
        ),
        (
                FlyingRobot.__init__,
                {"coords": typing.Optional[list[int]],
                 "name": str,
                 "weight": int,
                 "return": type(None)}
        ),
        (
                FlyingRobot.go_down,
                {"step": int, "return": type(None)}
        ),
        (
                FlyingRobot.go_up,
                {"step": int, "return": type(None)}
        ),
        (
                DeliveryDrone.__init__,
                {"coords": typing.Optional[list[int]],
                 "name": str,
                 "weight": int,
                 "max_load_weight": int,
                 "current_load": Cargo,
                 "return": type(None)}
        ),
        (
                DeliveryDrone.hook_load,
                {"cargo": Cargo, "return": type(None)}
        ),
        (
                DeliveryDrone.unhook_load,
                {} | {"return": type(None)}
        ),
    ]
)
def test_added_type_annotation(function: Callable, result: dict) -> None:
    hints = typing.get_type_hints(function)
    assert dict(hints) == result, "Add or fix type annotation for methods"

