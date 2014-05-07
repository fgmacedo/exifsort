#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Filename: ui.py
"""
ui
~~~~

"""
__author__ = ["Andrew G. Dunn"]
__copyright__ = __author__
__license__ = "Check root folder LICENSE file"
__email__ = "andrew.g.dunn@gmail.com"

import argparse
import os
import pathlib

from exifsort.util import config_read_meta
from exifsort.util import config_read_extensions
from exifsort.util import search_path_by_extension
from exifsort.util import sort_path
from exifsort.util import copy_image, move_image
from exifsort.util import unique_path

import exifread


def main():
    """
    - parse arguments
    - parse sort order (from input order (sys.argv))    - test input_path
    - load meta-dictionary for search
    - recursively enumerate files
    - for each file
        - Read exif
        - exif contains entries in meta-dictionary
        - create proper directory path
        - move or copy file
    """
    description = """Organize a folder of images into sub-folders based on the order of sorting parameters."""

    parser = argparse.ArgumentParser(description=description)
    
    # From Jeff Terrace <jterrace@gmail.com>
    class OrderedAction(argparse.Action):
        def __call__(self, parser, namespace, values, option_string=None):
            if not 'ordered_args' in namespace:
                setattr(namespace, 'ordered_args', [])
            previous = namespace.ordered_args
            previous.append((self.dest, values))
            setattr(namespace, 'ordered_args', previous)

    parser.add_argument('input_path', help='The path of images to be sorted recursively')
    parser.add_argument('output_path', help='The path to make a \'sorted\' directory structure')
    # sort actions
    parser.add_argument('--move', action='store_true', help='Move Files, default action is to copy')
    args = parser.parse_args()
    meta_dictionary = config_read_meta(['date'])
    image_extensions = config_read_extensions('image')


    if os.path.exists(args.input_path):
        image_list = search_path_by_extension(args.input_path, True, image_extensions)

        for image in image_list:
            image_path = pathlib.Path(os.path.join(args.input_path, image))
            extension = image_path.suffix
            try:
                exif = exifread.process_file(open(unicode(image_path)), details=False, stop_tag='JPEGThumbnail')
            except:
                exif = {}

            dest_path = sort_path(image_path, args.output_path, meta_dictionary, exif) + extension
            unique_dest_path = unique_path(image_path, pathlib.Path(dest_path))
            dest_dir = os.path.dirname(unicode(unique_dest_path))
            if not os.path.exists(dest_dir):
                os.makedirs(dest_dir)
            print "writting: ", unique_dest_path

            if args.move:
                move_image(unicode(image_path), unicode(unique_dest_path))
            else:
                copy_image(unicode(image_path), unicode(unique_dest_path))
    else:
        print 'Path does not exist'
        return
