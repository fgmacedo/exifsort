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

import sys
import argparse
import os

from exifsort.util import config_read_extensions
from exifsort.util import search_path_by_extension

#import exifread


def main():
    """
     * Parse arguments
     * Gather the sort order
     * Test the path
     * Get the size of the images (du_list_size)
     * Get the size of the path (du_path_size)
     * Warn user if different sizes
     * Move through list (copy/move) images into folders
    """

    description = """Organize a folder of images into sub-folders based on the order of sorting parameters."""

    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('input_path', help='The path of images to be sorted recursively')
    parser.add_argument('output_path', help='The path to make a \'sorted\' directory structure')
    # Optional sort parameters
    parser.add_argument('-d', '--date', dest='sort_date', action='store_true', help='Sort by Date')
    parser.add_argument('-c', '--camera', dest='sort_camera', action='store_true', help='Sort by Camera Model')
    parser.add_argument('-l', '--lens', dest='sort_lens', action='store_true', help='Sort by Lens Model')
    parser.add_argument('-o', '--orient', dest='sort_orient', action='store_true', help='Sort by Orientation')
    parser.add_argument('-f', '--flash', dest='sort_flash', action='store_true', help='Sort by if Flash fired')

    args = parser.parse_args()
    
    if os.path.exists(args.input_path):
        image_extensions = config_read_extensions('image')
        image_list = search_path_by_extension(args.input_path, True, image_extensions)
        ordered_path = ordered_path(sys.argv)

        for image in image_list:
            tags = exifread.process_file(open(os.path.join(args.input_path, image)), details=False, stop_tag='JPEGThumbnail')
            new_path = args.output_path
            
            for sort in ordered_path.keys():

            # pull exif


        pass
    else:
        print 'Path does not exist'
        return


# FOR VIDEO MOVEMENT            
# video_extensions = config_read_extensions('video')
# video_list = search_path_by_extension(args.input_path, True, video_extensions)
    

# if not args.video and args.cut and video_list:
#     print 'The Following Videos will be left behind:\n'
#     for video in video_list:
#         print video

# if args.video and video_list:
#     for video in video_list:
#         # move to base destination directo
#         pass