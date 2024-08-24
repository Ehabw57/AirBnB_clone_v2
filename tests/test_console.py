from unittest import TestCase
import io
from contextlib import redirect_stdout
from console import HBNBCommand
from models import storage


class TestConsle(TestCase):
    """Tests for the console"""

    def test_create(self):
        """tests create command"""
        with io.StringIO() as buf, redirect_stdout(buf):
            HBNBCommand().onecmd('create Place name="Manshea" max_guest=2 \
                    logitude=23.2 user_id="Ehab\\"me"')
            id = buf.getvalue().strip()
            place = storage._FileStorage__objects['Place.{}'.format(id)]
            self.assertEqual(place.id, id)
            self.assertEqual(place.name, "Manshea")
            self.assertEqual(place.max_guest, 2)
            self.assertEqual(place.user_id, 'Ehab"me')





