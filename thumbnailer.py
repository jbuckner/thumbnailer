#!/usr/bin/env python
import glob
import os

from PIL import Image
from progressbar import ProgressBar

width, height = 300, 250  # in px
r, g, b = 0, 0, 0  # background color, 0-255
source_dir = 'sample/source'
destination_dir = '%s_%sx%s' % (source_dir, width, height)

try:
    os.makedirs(destination_dir)
except:
    pass

filelist = glob.glob('%s/*' % source_dir)
number_of_files = len(filelist)

count = 0
progress = ProgressBar(maxval=number_of_files).start()
for filename in filelist:
    if filename[-3:].lower() not in ('png', 'jpg', 'gif'):
        continue
    image = Image.open('%s' % filename)

    exif = image._getexif()
    orientation_key = 274  # cf ExifTags
    if orientation_key in exif:
        orientation = exif[orientation_key]

        rotate_values = {
            3: 180,
            6: 270,
            8: 90
        }

        if orientation in rotate_values:
            # Rotate and save the picture
            image = image.rotate(rotate_values[orientation])

    image.thumbnail((width, height), Image.ANTIALIAS)
    background = Image.new('RGB', (width, height), (r, g, b))
    background.paste(
        image,
        ((width - image.size[0]) / 2, (height - image.size[1]) / 2))
    background.save('%s/%s' % (
        destination_dir, os.path.basename(filename)), 'JPEG')
    count = count + 1
    progress.update(count)
