from django.test import TestCase
from apps.accounts.models import CustomerUser, Address

class CustumUserTests(TestCase):
    def setUp(self) -> None:
        self.user = CustomerUser.objects.create(
            email = 'mahsan_gillani@yahoo.com',
            phone_number = '09011777265',
            birthday = '1376-09-04',
            user_role = CustomerUser.UserRole.CUSTOMERUSER_CUSTOMER,
            is_deleted = False,
            username = 'mahsangilani',
            password = '123@qweASD'
        )
        
        self.address = Address.objects.create(
            user = self.user,
            country ='Iran',
            province = 'Tehran',
            city = 'Tehran',
            main_street = 'Tehran Street',
            address_detail = 'highway, square',
            postal_code = '123456789',
            house_number = '21',
        )
        
        
    def test_delete_method_sets_is_deleted_to_true(self):
        self.user.delete()
        self.assertTrue(self.user.is_deleted)
        
    def test_undelete_method_sets_is_deleted_to_false(self):
        self.user.is_deleted = True
        self.user.save()
        self.user.undelete()
        self.assertFalse(self.user.is_deleted)
        
    def test_deleted_manager_only_returns_deleted_objects(self):
        self.user.is_deleted = True
        self.user.save()
        deleted_users = CustomerUser.objects.deleted()
        self.assertIn(self.user, deleted_users)
        
    def test_archive_manager_returns_all_objects(self):
        all_users = CustomerUser.objects.archive()
        self.assertIn(self.user, all_users)
        
    def test_get_queryset_only_returns_non_deleted_objects(self):
        non_delete_users = CustomerUser.objects.get_queryset()
        self.assertIn(self.user, non_delete_users)
        self.user.is_deleted = True
        self.user.save()
        self.assertIn(self.user, non_delete_users)
        
    def test_str_method(self):
        test_str = f'{self.address.city}-{self.address.main_street}-->{self.address.address_detail}'
        self.assertEqual(str(self.address), test_str)