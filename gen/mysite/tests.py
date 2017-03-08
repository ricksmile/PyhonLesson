from django.test import TestCase
from views import mergepic

class mergepicCase(TestCase):

    def test_full_path(self):
        self.assertRegexpMatches(
            mergepic("/var/www/gen/media/Jva-IHrMRzGqurlRLcWIBg.jpg",
                     "Test Message", 
                     24, 
                     10, 10), 
            ".+\.jpg")

    def test_just_file(self):
        self.assertRegexpMatches(
            mergepic("Jva-IHrMRzGqurlRLcWIBg.jpg",
                     "Test Message", 
                     24, 
                     10, 10), 
            ".+\.jpg")
