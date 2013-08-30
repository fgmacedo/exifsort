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
import json

def config_read_extensions(extension):
    config_file = json.load(open(os.path.join(os.path.dirname(__file__), '../config.json')))
    config_image_extensions = config_file['extensions'][extension].split()

    image_extensions = []

    for extension in config_image_extensions:
        image_extensions.append(str(extension))
        image_extensions.append(str(extension.upper()))

    return image_extensions


def ordered_path(sysarg):
    

    pass


def search_path_by_extension(path, recurse, extension_list):
    """
    Return a list of file paths found in dirPath.
    If recurse is true, then move into the sub directories
    if there are no extensions, all files will be returned.
    """
    file_list = []
    
    for file in os.listdir(path):
        file_path = os.path.join(path, file)
    
        if os.path.isfile(file_path):
            if not extension_list:
                file_list.append(file_path)
            else:
    
                if os.path.splitext(file_path)[1][1:] in extension_list:
                    file_list.append(file_path)
        elif os.path.isdir(file_path) and recurse:
            file_list.extend(search_path_by_extension(file_path, recurse, extension_list))
    
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


def check_path_create(path):
    """Check the path, if it doesn't exist then
    create it and return true
    """
    

