# -*- coding: utf-8 -*-
# @Time    : 2020/5/1 21:45
# @Author  : 小疯
# @File    : pywin.py
# @Software: PyCharm


from pywinauto.application import Application
app = Application(backend="uia").start('notepad.exe')
app.UntitledNotepad.draw_outline()
app.UntitledNotepad.menu_select("Edit -> Replace")
app.Replace.print_control_identifiers()