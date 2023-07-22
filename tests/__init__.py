import hashlib
import os
import unittest

from ctmd5 import change_the_md5, get_md5


class TestCliTool(unittest.TestCase):
    def setUp(self):
        self.file = "test.txt"
        with open(self.file, "w") as f:
            f.write("test")

    def tearDown(self):
        os.remove(self.file)

    def test_get_md5(self):
        md5 = get_md5(self.file)
        self.assertEqual(md5, hashlib.md5(b"test").hexdigest())

    def test_change_the_md5(self):
        md5_before = get_md5(self.file)
        change_the_md5(self.file)
        md5_after = get_md5(self.file)
        self.assertNotEqual(md5_before, md5_after)


if __name__ == "__main__":
    unittest.main()
