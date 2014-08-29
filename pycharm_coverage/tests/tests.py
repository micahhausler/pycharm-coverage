from unittest import TestCase

from pycharm_coverage import Resource


class ResourceTests(TestCase):
    """
    A test class for Resource
    """
    def setUp(self):
        self.resource = Resource()

    def test_get_with_author(self):
        """
        Test .get() with an author arg
        """
        # Call the method
        response = self.resource.get(author='Micah Hausler')

        self.assertFalse(response)

    # This method is intentionally commented out
    #
    #
    # def test_without_author(self):
    #     """
    #     Test .get() without an author arg
    #     """
    #     response = self.resource.get()
    #
    #     self.assertFalse(response)
