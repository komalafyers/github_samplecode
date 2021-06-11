import unittest
from unittest.mock import patch
from ..app.employee import Employee


class TestEmployee(unittest.TestCase):
    """
    """
    @classmethod
    def setUpClass(cls) -> None:
        print('setup class')

    @classmethod
    def tearDownClass(cls) -> None:
        print('teardown class')

    def setUp(self) -> None:
        print('setup')
        self.emp_1 = Employee('komala', 'peddannagari', 15000)
        self.emp_2 = Employee('peddannagari', 'rohitha', 25000)

    def tearDown(self) -> None:
        print('teardown')

    def test_email(self):
        print('test_mail')
        self.assertEqual(self.emp_1.email, 'komalap@gmail.com')
        self.assertEqual(self.emp_2.email, 'rohithap@email.com')

        self.emp_1.first = 'komaa'
        self.emp_2.first = 'rohi'

        self.assertEqual(self.emp_1.email, 'komala@email.com')
        self.assertEqual(self.emp_2.email, 'rohitha@email.com')

    def test_fullname(self):
        print('test_fullname')
        self.assertEqual(self.emp_1.fullname, 'komala peddannagari')
        self.assertEqual(self.emp_2.fullname, 'rohitha peddannagari')

        self.emp_1.first = 'komaa'
        self.emp_2.first = 'rohit'

        self.assertEqual(self.emp_1.fullname, 'komaa peddannagari')
        self.assertEqual(self.emp_2.fullname, 'rupa peddannagari')

    def test_apply_raise(self):
        print('test_apply_raise')
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.pay, 15200)
        self.assertEqual(self.emp_2.pay, 25500)

    def test_monthly_schedule(self):
        with patch('app.employee.requests.get') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = 'success'

            schedule = self.emp_1.monthly_schedule('June')
            mocked_get.assert_called_with('company.com/komalap@email.com/June')
            self.assertEqual(schedule, 'success')

            mocked_get.return_value.ok = False
            schedule = self.emp_2.monthly_schedule('June')
            mocked_get.assert_called_with('company.com/rohithap@email.com/June')
            self.assertEqual(schedule, 'Bad Response')


if __name__ == '__main__':
    unittest.main()
