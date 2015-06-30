"""
API compatibility tests based on http://www.raspberrypi.org/documentation/usage/minecraft/

We do not want to break this API - we do not want to be responsible for sad children
(and adults) whose awesome Minecraft code no longer works.

Ergo this suite is a translation of that usage guide

Currently it doesn't actually test the __success__ of any of these commands, but it at
least verifies that the commands still exist, which is the most likely cause of breakage
"""

import pytest
import six

from mcpi import minecraft
from mcpi import block
from mcpi.vec3 import Vec3
from time import sleep


@pytest.fixture(autouse=True)
def mc(monkeypatch):
    def dummy_sendall(self, b):
        """
        https://docs.python.org/3/library/socket.html#socket.socket.sendall

        `sendall` takes _`bytes`_ explicitly in Python 3, _not_ `str`
        """

        assert isinstance(b, six.binary_type), "socket.socket.sendall was given non-bytes (%s)" % str(type(b))

    monkeypatch.setattr("socket.socket.connect", lambda x, y: None)
    monkeypatch.setattr("socket.socket.sendall", dummy_sendall)

    monkeypatch.setattr("mcpi.connection.Connection.drain", lambda x: None)
    monkeypatch.setattr("mcpi.minecraft.CmdPositioner.getPos", lambda x, y: Vec3(0.1, 0.1, 0.1))
    return minecraft.Minecraft.create()


def test_hello_world(mc):
    mc.postToChat("Hello world")

    assert mc.conn.lastSent == b"chat.post(Hello world)\n"


def test_get_pos(mc):
    x, y, z = mc.player.getPos()


def test_teleport(mc):
    x, y, z = mc.player.getPos()
    mc.player.setPos(x, y + 100, z)


def test_set_block(mc):
    x, y, z = mc.player.getPos()
    mc.setBlock(x + 1, y, z, 1)

    assert mc.conn.lastSent == ("world.setBlock(%d,%d,%d,%d)\n" % (x + 1, y, z, 1)).encode("cp437")


def test_blocks_as_variables(mc):
    x, y, z = mc.player.getPos()

    dirt = block.DIRT.id
    mc.setBlock(x, y, z, dirt)


def test_special_blocks(mc):
    x, y, z = mc.player.getPos()

    wool = 35
    mc.setBlock(x, y, z, wool, 1)


def test_set_blocks(mc):
    stone = 1
    x, y, z = mc.player.getPos()
    mc.setBlocks(x + 1, y + 1, z + 1, x + 11, y + 11, z + 11, stone)


def test_dropping_blocks_as_you_walk(mc):
    """
    'The following code will drop a flower behind you wherever you walk'

    We're not walking, and we don't want the infinite loop from the example, but this should do

    Note that the actual example uses xrange which is not in Python 3, so lets test with range
    """

    flower = 38

    for i in range(10):
        x, y, z = mc.player.getPos()
        mc.setBlock(x, y, z, flower)
        sleep(0.1)
