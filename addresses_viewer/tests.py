import unittest
from django.db.utils import IntegrityError

from .models import Address

class TestAddress(unittest.TestCase):
    def setUp(self):
        Address.objects.all().delete()

    def test_address_only_lat(self):
        address = Address(lat=50)
        with self.assertRaises(IntegrityError):
            address.save()

    def test_address_only_lng(self):
        address = Address(lng=-80.999)
        with self.assertRaises(IntegrityError):
            address.save()

    def test_address_only_address_name(self):
        address = Address(address_name="Live Avenue")
        with self.assertRaises(IntegrityError):
            address.save()

    def test_valid_address(self):
        address = Address(address_name="Complete Live Avenue", lat=50, lng=-80.999, place_id="place_id_test")
        address.save()
        self.assertEqual(Address.objects.count(), 1)


    def test_duplicate_place_id(self):
        address = Address(address_name="Complete Live Avenue", lat=50, lng=-80.999, place_id="place_id_test")
        address.save()

        duplicated_address = Address(address_name="Complete Live Avenue", lat=50, lng=-80.999, place_id="place_id_test")
        with self.assertRaises(IntegrityError):
            duplicated_address.save()

        self.assertEqual(Address.objects.count(), 1)
