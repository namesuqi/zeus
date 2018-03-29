# coding=utf-8
"""
TODO: Add description for file

__author__ = 'zengyuetian'

"""

# from distutils.core import setup
# import py2exe
#
# options = {"py2exe":{"bundle_files": 1}}
#
# setup(windows=['test_helper.py'], options=options)

from distutils.core import setup
import py2exe
import sys
sys.argv.append("py2exe")
options = {"py2exe":   { "bundle_files": 1 }
                }
setup(options = options,
      zipfile=None,
      windows = [{"script":'test_helper.py'}])