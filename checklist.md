# Check Your Code Against the Following Points

1. If the function definition line is too long, place each parameter on a new line.

**Good example:**
```python
def long_function_name(
        var_one,
        var_two,
        var_three,
        var_four
) -> None:
```

**Bad example:**
```python
def long_function_name(var_one, var_two,
                       var_three,var_four) -> None:
```

2. If a variable can be `None`, specify it in the annotation.

3. Make sure you're not repeating yourself. If something can be done in the parent class, delegate it there.

4. To check if a variable is set to `None` and assign a default value, use the ternary operator:
`variable = other if other else 0`. Or even simpler: `variable = other or 0`.
Remember, a simple way is better than a complex one.

5. It is not a good practice to use mutable object as a default parameter of function,
set it to `None` by default. But in constructor itself you can use condition, and if `coords` equal to None,
assign [0, 0] to the `coords`.

**Good example:**
```python
def __init__(
        default_var: list | None = None
) -> None:
    self.default_var = default_var or [0, 0]
```

**Bad example:**
```python
def __init__(
        default_var: list = [0, 0]
) -> None:
    self.default_var = default_var
```
