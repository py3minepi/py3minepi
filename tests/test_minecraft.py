from mcpi.minecraft import intFloor


def test_int_floor_id():
    intlist = [1, 2, 3]

    assert intFloor(intlist) == intlist


def test_int_floor_floats():

    assert type(intFloor([1.0])[0]) == int
