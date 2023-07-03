```
██▓▒░░░░░░░░░░░░░░░░░░░░▒▓██
█████▓▒░░░░░░░░░░░░░░▒▓█████ ██╗███╗   ███╗ █████╗  ██████╗ ███████╗
████████▓▒░░░░░░░░▒▓████████ ██║████╗ ████║██╔══██╗██╔════╝ ██╔════╝
███████████▓░░░░▓███████████ ██║██╔████╔██║███████║██║  ███╗█████╗
████████▓▒░░░░░░░░▒▓████████ ██║██║╚██╔╝██║██╔══██║██║   ██║██╔══╝
█████▓▒░░░░░░░░░░░░░░▒▓█████ ██║██║ ╚═╝ ██║██║  ██║╚██████╔╝███████╗
██▓▒░░░░░░░░░░░░░░░░░░░░▒▓██ ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝

 ██████╗ ██████╗ ███╗   ███╗██████╗ ██████╗ ███████╗███████╗███████╗
██╔════╝██╔═══██╗████╗ ████║██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
██║     ██║   ██║██╔████╔██║██████╔╝██████╔╝█████╗  ███████╗███████╗
██║     ██║   ██║██║╚██╔╝██║██╔═══╝ ██╔══██╗██╔══╝  ╚════██║╚════██║
╚██████╗╚██████╔╝██║ ╚═╝ ██║██║     ██║  ██║███████╗███████║███████║
 ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝
```

# Image Compress

This script allow you to compress images without having to upload your images to a 3rd party where your images can be stored and used or even cause you to leak sensitive data.

Compression is the act of encoding information using lesser bytes count than what was used for the original file. Depending on where you get your images files or how they are generated, the files can be dozens to hundreds of megabytes and may be too large for different needs, especially using them on websites.

This script depends on the Python Imaging Library [Pillow](https://github.com/python-pillow/Pillow), it adds support for opening, manipulating, and saving many different image file formats. This script in particular works with files that end with `.jpg`, `.jpeg` or `.png`.

## Installing Pillow

You will first need to ensure you have Python installed, if not, install it. There are great guides to get that done so hit the web for instructions.

- Install pillow:
```
pip install pillow
```
- download the repo to a place on your computer you want to run it
- drop your images into the dir directory
- run the script:
```
./imgCompress.py
```
- when completed, it will show you a message like:
```
Compressed filename.png
```
- Example of a file compression:
```
94K Jun  8 20:20 filename.png   before
80K Jun 15 19:49 filename.png   after (edited)
```

## Image Quality

Pillow allows you to set the resulting image quality on a scale from 1 (worst) to 95 (best), with a default of 75. Going over 95 is not recommended as it can cause your resulting files to become very large.
