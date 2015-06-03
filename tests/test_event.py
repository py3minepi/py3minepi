from mcpi.event import BlockEvent


class TestEvent():

    def test_instantiation(self):
        event_type = 0
        pos = [14, 15, 16]
        face = 2
        entity = 1
        event = BlockEvent(event_type, pos[0], pos[1], pos[2], face, entity)
        assert event.type == event_type
        assert event.pos.x == pos[0]
        assert event.pos.y == pos[1]
        assert event.pos.z == pos[2]
        assert event.face == face
        assert event.entityId == entity

    def test_representation(self):
        data = [0, 14, 15, 16, 1, 1]
        event = BlockEvent(data[0], data[1], data[2],
                           data[3], data[4], data[5])
        # block hit event has integer number converted in rep to text
        expected = "BlockEvent(BlockEvent.HIT, 14, 15, 16, 1, 1)"
        rep = repr(event)
        assert rep == expected

    def test_static_hit(self):
        x = 89
        y = -34
        z = 30
        event_type = 0
        face = 3
        entity = 1
        # test the variable HIT
        event = BlockEvent(BlockEvent.HIT, x, y, z, face, entity)
        assert event.type == event_type
        assert event.pos.x == x
        assert event.pos.y == y
        assert event.pos.z == z
        assert event.face == face
        assert event.entityId == entity

        # test the static function
        event_from_static = BlockEvent.Hit(x, y, z, face, entity)
        assert event_from_static.type == event.type
        assert event_from_static.pos.x == event.pos.x
        assert event_from_static.pos.y == event.pos.y
        assert event_from_static.pos.z == event.pos.z
        assert event_from_static.face == event.face
        assert event_from_static.entityId == event.entityId
