import select
import socket

try:
    from unittest import mock
except ImportError:
    import mock

import pytest
import six

from mcpi.connection import Connection


@pytest.fixture
def conn():
    with mock.patch('socket.socket', spec=socket.socket):
        return Connection('localhost', 8000)



def test__send(conn):
    conn.socket = mock.MagicMock(spec=socket.socket)
    data = six.text_type('foo')

    with mock.patch('select.select', spec=select.select) as sel:
        sel.side_effect = [(True, 0, 0), (False, 0, 0)]
        conn._send(data)  # send some data

    # check we got it
    assert conn.socket.sendall.called
    conn.socket.sendall.assert_called_with(data)
