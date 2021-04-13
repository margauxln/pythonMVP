from __future__ import (absolute_import, division, print_function)

import sys
import presenter
import view

import unittest
from mantid.py3compat import mock

class PresenterTest(unittest.TestCase):
    def setUp(self):
        self.view = mock.create_autospec(view.View)

        # mock view
        self.view.doSomethingSignal = mock.Mock()
        self.view.btn_click = mock.Mock()
        self.view.getValue = mock.Mock(return_value=3.14)

        self.presenter = presenter.Presenter(self.view)

    def test_doSomething(self):
        self.presenter.handleButton()
        assert(self.view.getValue.call_count == 1)

if __name__ == "__main__":
    unittest.main()
