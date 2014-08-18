## Thumbnailer

A script that takes a directory of images, resizes them to their longest side and adds borders to fill the space if they don't fit.

### Installation

I like using [`virtualenv`](http://virtualenv.readthedocs.org/en/latest/), but you can also just use the system python.

```
pip install -r requirements.txt
```

### Configuration:

Edit `thumbnailer.py` and set the width, height, background color, source, and target directories.

### Usage:

```
$ python thumbnailer.py
```

### Why?

I took *a lot* of pictures at the [The Relay](http://www.therelay.com/) and wanted to make a [video](https://www.youtube.com/watch?v=aACiyeQ9dFM) of them, but I needed all the pictures to line up. It was also a pretty cool learning experience for image processing.

#### Example

##### Original

![Original Picture](sample/source/harvey_bear_ranch.jpg?raw=true "Original Picture")

##### Resized and Cropped

![Resized and Cropped](sample/source_300x250/harvey_bear_ranch.jpg?raw=true "Resized and Cropped")
