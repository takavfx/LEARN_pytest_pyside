import sys

import pytest

from PySide2 import QtCore
from PySide2 import QtWidgets
from PySide2 import QtTest


def test_add_count():
    from sample import gui

    app = QtWidgets.QApplication.instance()
    if app is None:
        app = QtWidgets.QApplication(sys.argv)
    gui = gui.SampleDialog()
    gui.show()

    QtTest.QTest.mouseClick(gui.button, QtCore.Qt.LeftButton)
    assert gui.label.text() == '1'

    QtTest.QTest.mouseClick(gui.button, QtCore.Qt.LeftButton)
    assert gui.label.text() == '2'

    app.exec_()