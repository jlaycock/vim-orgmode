#!/usr/bin/env python
# -*- coding: utf-8 -*-

import test_vimbuffer
import test_edit_structure
import test_misc
import test_navigator
import test_show_hide
import test_tags_properties
import test_todo
import test_date

import unittest

if __name__ == '__main__':
	tests = unittest.TestSuite([
		test_vimbuffer.suite(),
		#test_edit_structure.suite(),
		#test_misc.suite(),
		#test_navigator.suite(),
		#test_show_hide.suite(),
		#test_tags_properties.suite(),
		#test_date.suite(),
		#test_todo.suite()
		])
	runner = unittest.TextTestRunner()
	runner.run(tests)
