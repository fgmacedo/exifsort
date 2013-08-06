#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Filename: ui.py
"""
ui
~~~~

- parse arguments
- test input_path
- get input_path size (recursively)
- parse sort order (from input order (sys.argv))
- recursively enumerate files
- for each file
    - Read exif
    - create proper directory path
    - move or copy file
- fax glitter

"""
__author__ = ["Andrew G. Dunn"]
__copyright__ = __author__
__license__ = "Check root folder LICENSE file"
__email__ = "andrew.g.dunn@gmail.com"

import sys # For argument order
import os.path
import argparse

from exifsort.util import search_path_by_extension, du_path, du_list

def main():

    description = """Organize a folder of images into sub-folders based on the order of sorting parameters."""

    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('input_path', help='The path of images to be sorted recursively')
    parser.add_argument('output_path', help='The path to make a \'sorted\' directory structure')
    parser.add_argument('-C', '--copy', dest='copy', action='store_true', help='Copy the images')
    parser.add_argument('-X', '--cut', dest='cut', action='store_true', help='Cut the images')
    #parser.add_argument('-V', '--video', help='Copy/Cut found Video')
    parser.add_argument('-d', '--date', dest='date', action='store_true', help='Sort by Date')
    parser.add_argument('-c', '--camera', dest='camera', action='store_true', help='Sort by Camera Model')
    parser.add_argument('-l', '--lens', dest='lens', action='store_true', help='Sort by Lens Model')
    parser.add_argument('-o', '--orient', dest='orient', action='store_true', help='Sort by Orientation')
    parser.add_argument('-f', '--flash', dest='flash', action='store_true', help='Sort by if Flash fired')

    args = parser.parse_args()
    
    print args #dis is for debug
    print sys.argv #dis is for order

    if os.path.exists(args.input_path):
        du_path_size = du_path(args.input_path)
        images = search_path_by_extension(args.input_path, True, "JPG", "CR2")
        du_list_size = du_list(images)
        print du_path_size / 1024 / 1024
        print du_list_size / 1024 / 1024

    else:
        print 'input path does not exist'
