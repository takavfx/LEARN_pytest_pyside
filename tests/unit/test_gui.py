import sys

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
    n1 = gui.number

    QtTest.QTest.mouseClick(gui.button, QtCore.Qt.LeftButton)
    n2 = gui.number
    assert n2 - n1 == 1