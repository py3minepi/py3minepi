from mcpi.vec3 import Vec3


class TestVec3():
    """ Test the functions of the Vec3 class """

    def test_instantiation(self):
        expect_x = -1.0
        expect_y = 4.0
        expect_z = 6.0
        v = Vec3(expect_x, expect_y, expect_z)
        assert v.x == expect_x
        assert v.y == expect_y
        assert v.z == expect_z

        vector3 = Vec3(1, -2, 3)
        assert vector3.x == 1
        assert vector3.y == -2
        assert vector3.z == 3

        assert vector3.x != -1
        assert vector3.y != +2
        assert vector3.z != -3

    def test_representation(self):
        # Test repr
        v1 = Vec3(2, -3, 8)
        expected_string = "Vec3({},{},{})".format(v1.x, v1.y, v1.z)
        rep = repr(v1)
        assert rep == expected_string
        e = eval(repr(v1))
        assert e == v1

    def test_iteration(self):
        coords = [1, 9, 6]
        v = Vec3(coords[0], coords[1], coords[2])
        for index, pos in enumerate(v):
            assert pos == coords[index]

    def test_equality(self):
        v1 = Vec3(2, -3, 8)
        v_same = Vec3(2, -3, 8)
        v_diff = Vec3(22, 63, 88)
        v_x_larger = Vec3(5, -3, 8)
        v_x_smaller = Vec3(0, -3, 8)
        v_y_larger = Vec3(2, 9, 8)
        v_y_smaller = Vec3(2, -10, 8)
        v_z_larger = Vec3(2, -3, 12)
        v_z_smaller = Vec3(2, -3, 4)

        assert v1 == v_same
        assert not v1 == v_diff
        assert v1 != v_diff

        otherVectors = [v_x_larger, v_y_larger, v_z_larger,
                        v_x_smaller, v_y_smaller, v_z_smaller]

        for other in otherVectors:
            assert v1 != other

        for other in otherVectors:
            assert not v1 == other

    def test_cloning(self):
        v = Vec3(2, -3, 8)
        v_clone = v.clone()
        assert v == v_clone
        v.x += 1
        assert v != v_clone

    def test_negation(self):
        v1 = Vec3(2, -3, 8)
        v_inverse = -v1
        assert v1.x == -v_inverse.x
        assert v1.y == -v_inverse.y
        assert v1.z == -v_inverse.z

    def test_addition(self):
        a = Vec3(10, -3, 4)
        b = Vec3(-7, 1, 2)
        c = a + b
        totV = Vec3(3, -2, 6)
        assert c == totV
        assert c - a == b
        assert c - b == a

    def test_subtraction(self):
        a = Vec3(10, -3, 4)
        b = Vec3(5, 3, 5)
        assert (a - a) == Vec3(0, 0, 0)
        assert (a + (-a)) == Vec3(0, 0, 0)
        assert (a - b) == Vec3(5, -6, -1)

    def test_multiplication(self):
        a = Vec3(2, -3, 8)
        assert (a + a) == (a * 2)
        k = 4
        a *= k
        assert a == Vec3(2 * k, -3 * k, 8 * k)

    def test_length(self):
        v = Vec3(2.0, -3.0, 8.0)
        length = v.length()
        expect_length = (((2 * 2) + (-3 * -3) + (8 * 8)) ** 0.5)
        assert length == expect_length

    def test_length_sqr(self):
        v = Vec3(2, -3, 8)
        ls = v.lengthSqr()
        assert ls == ((2 * 2) + (-3 * -3) + (8 * 8))

    def test_iround(self):
        v = Vec3(2.3, -3.7, 8.8)
        v.iround()
        expect_vec = Vec3(2, -3, 9)
        assert v == expect_vec

    def test_ifloor(self):
        v = Vec3(2.3, -3.7, 8.8)
        v.ifloor()
        expect_vec = Vec3(2, -3, 8)
        assert v == expect_vec

    def test_rotate_left(self):
        v = Vec3(2, -3, 8)
        v.rotateLeft()
        expect_vec = Vec3(8, -3, -2)
        assert v == expect_vec

    def test_rotate_right(self):
        v = Vec3(2, -3, 8)
        v.rotateRight()
        expect_vec = Vec3(-8, -3, 2)
        assert v == expect_vec
