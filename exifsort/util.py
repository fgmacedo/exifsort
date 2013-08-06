#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Filename: util.py
"""
util.py
~~~~

Miscellaneous utility functions.
"""
__author__ = ["Andrew G. Dunn"]
__copyright__ = __author__
__license__ = "Check root folder LICENSE file"
__email__ = "andrew.g.dunn@gmail.com"


import os
import datetime


def du_path(path):
    """ Recursively calcualtes the total size of a given path
    and all of its contents
    """
    total_size = os.path.getsize(path)
    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        if os.path.isfile(item_path):
            total_size += os.path.getsize(item_path)
        elif os.path.isdir(item_path):
            total_size += du_path(item_path)
    return total_size


def du_list(item_list):
    """ Iterates through list and tallies the size of the files
    in the list. I do check, but mainly assume that you're going
    to pass me a list of actual paths that exist
    """
    total_size = 0
    for item in item_list:
        if(os.path.exists(item)):
            total_size += os.path.getsize(item)
    return total_size


def search_path_by_extension(path, recurse, *extensions):
    """    Return a list of file paths found in dirPath.
    If recurse is true, then move into the sub directories
    if there are no extensions, all files will be returned.
    """
    file_list = []
    for file in os.listdir(path):
        file_path = os.path.join(path, file)
        if os.path.isfile(file_path):
            if not extensions:
                file_list.append(file_path)
            else:
                if os.path.splitext(file_path)[1][1:] in extensions: # Caps check?
                    file_list.append(file_path)
        elif os.path.isdir(file_path) and recurse:
            file_list.extend(search_path_by_extension(file_path, recurse, *extensions))
    return sorted(file_list)


def parse_date(exif_datetime):
    """
    """
    parse_format = '%Y:%m:%d %H:%M:%S'
    return datetime.datetime.strptime(exif_datetime, parse_format)


def copy_image(image_path, destination_path):
    pass


def move_image(image_path, destination_path):
    pass

