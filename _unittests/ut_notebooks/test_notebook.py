"""
@brief      test log(time=1s)

You should indicate a time in seconds. The program ``run_unittests.py``
will sort all test files by increasing time and run them.
"""
import unittest
from pyquickhelper.loghelper import fLOG
from pyensae.notebookhelper.magic_notebook import MagicNotebook


class TestNotebook(unittest.TestCase):

    def test_head(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        mg = MagicNotebook()
        res = mg.nb_menu("")
        fLOG(res)
        assert res is not None


if __name__ == "__main__":
    unittest.main()
