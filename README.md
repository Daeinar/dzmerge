### DZMerge

DZMerge is a simple Python script to produce standalone versions of [DZSlides](http://paulrouget.com/dzslides/) presentations for simpler distribution. This is done by replacing all images and fonts (TODO) with the corresponding base64 encoded variants and by including external stylesheets.

####Requirements
The [LXML](http://lxml.de/) Python package is used for parsing and modifying HTML files.

####Usage
Simply execute the following command to convert the source presentation `in.html` to the corresponding standalone variant `out.html`.
```
./dzmerge.py in.html out.html
```

####License
This software package is released under the BSD (3-Clause) license. See the file `LICENSE` for more details.
