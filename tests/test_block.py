"""
Bare-bones but we don't even import block in any tests yet
"""

from mcpi import block


class TestBlock:
    def test_instantiation(self):
        b = block.Block(0)
        assert b.id == 0

    def test_instantiation_with_data(self):
        data = 'foo'
        b = block.Block(1, data)
        assert b.id == 1
        assert b.data == data

    def test_comparison(self):
        data = 'minecraft'
        assert block.Block(3, data) == block.Block(3, data)

    def test_hash(self):
        assert hash(block.Block(9)) == hash((9 << 8) + 0)

    def test_with_data(self):
        data = 'bar'
        b = block.Block(4).withData(data)
        assert b.data == data

    def test_iteration(self):
        data = (7, 8)
        for i, x in enumerate(block.Block(7, 8)):
            assert x == data[i]

    def test_repr(self):
        assert repr(block.Block(5)) == 'Block(5, 0)'
        assert repr(block.Block(5, 6)) == 'Block(5, 6)'
