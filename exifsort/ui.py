#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Filename: ui.py
"""
ui
~~~~

- parse arguments

"""
__author__ = ["Andrew G. Dunn"]
__copyright__ = __author__
__license__ = "Check root folder LICENSE file"
__email__ = "andrew.g.dunn@gmail.com"

import argparse

def main():

    description = """Organize a folder of images into sub-folders based on the order of sorting parameters."""

    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('directory', help='The directory of images to be sorted recursively')
    parser.add_argument('-C', '--copy', help='Copy the images')
    parser.add_argument('-X', '--cut', help='Cut the images')
    #parser.add_argument('-V', '--video', help='Copy/Cut found Video')
    parser.add_argument('-o', '--output', help='The directory to output, otherwise output in place')
    parser.add_argument('-d', '--date', help='Sort by Date')
    parser.add_argument('-c', '--camera', help='Sort by Camera Model')
    parser.add_argument('-l', '--lens', help='Sort by Lens Model')
    parser.add_argument('-o', '--orient', help='Sort by Orientation')
    parser.add_argument('-f', '--flash', help='Sort by if Flash fired')

    args = parser.parse_args()
    input_path = args.directory
