import unittest
from simplify_path import Solution


class TestSimplifyPath(unittest.TestCase):
    def setUp(self):
        pass

    def test_example_cwd_cd(self):
        s = Solution()
        cwd = "/a/b/c"
        cd = "/d/./e"
        expected = "/d/e"
        actual = s.simplify_path(cwd, cd)
        self.assertEqual(expected, actual)

    def test_example_cwd_empty(self):
        s = Solution()
        cwd = ""
        cd = "/d/./e"
        expected = "/d/e"
        actual = s.simplify_path(cwd, cd)
        self.assertEqual(expected, actual)

    def test_example_cd_empty(self):
        s = Solution()
        cwd = "/a/b/c"
        cd = ""
        expected = "/a/b/c"
        actual = s.simplify_path(cwd, cd)
        self.assertEqual(expected, actual)

    def test_example_cwd_cd_complicated(self):
        s = Solution()
        cwd = "a/b"
        cd = ".//c/../../d/f"
        expected = "/a/d/f"
        actual = s.simplify_path(cwd, cd)
        self.assertEqual(expected, actual)


unittest.main()
