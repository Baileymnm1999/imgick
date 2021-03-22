# Imgick
A simple framework for image composition and editing based off [Pillow](https://pypi.org/project/Pillow/)

## Table of Contents:

- [Imgick](#imgick)
- [Status](#status)
- [Getting Started](#getting-started)
    - [Quickstart Dev Guide](#see-quickstart-dev-guidedocquickstartdevguidemd)
- [Documentation](#documentation)
    - [Commands](#commands)
    - [Api](#Api)
- [Dependencies](#dependencies)
    - [Pillow](#pillow)
- [Licenses](#licenses)

## Status
TODO

## Getting Started
```
git pull https://github.com/Baileymnm1999/imgick
cd imgick
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
pip install -e .
```


## Documentation

### Commands
imgick can be used from the commandline or programmatically through the python api.
If you would like to contribute and help develop either of these, please open a pr.

- **create**
```
usage: imgick [-h] [-b BG] [-n BG_NAME] [-t BG_TOP] [-l BG_LEFT] [-W BG_WIDTH] [-H BG_HEIGHT] width height output

Create an imgick project

positional arguments:
  width                 Height of project in pixels
  height                Height of project in pixels
  output                Output file name

optional arguments:
  -h, --help            show this help message and exit
  -b BG, --bg BG        Background layer to compose, specify an RGBA color in hex or image file
  -n BG_NAME, --bg-name BG_NAME
                        Background layer name
  -t BG_TOP, --bg-top BG_TOP
                        Background layer top offset, 0 if omitted
  -l BG_LEFT, --bg-left BG_LEFT
                        Background layer left offset, 0 if omitted
  -W BG_WIDTH, --bg-width BG_WIDTH
                        Background layer width, same as project if omitted
  -H BG_HEIGHT, --bg-height BG_HEIGHT
                        Background layer height, same as project if omitted
```

- **render**
```
usage: imgick [-h] [-o OUTPUT] [-f FORMAT] project

Render an imgick project

positional arguments:
  project               Imgick project to render

optional arguments:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        Output file name. If omitted will open with image viewer
  -f FORMAT, --format FORMAT
                        Image format to use
```
    

- **list**
```
usage: imgick [-h] project

List project details

positional arguments:
  project     Imgick project to list

optional arguments:
  -h, --help  show this help message and exit
```


- **compose**
```
usage: imgick [-h] [-o OUTPUT] [-n NAME] [-i INDEX] [-t TOP] [-l LEFT] [-W WIDTH] [-H HEIGHT] project layer

Compose a new layer onto an imgick project

positional arguments:
  project               Imgick project to render
  layer                 Background layer to compose, specify an RGBA color in hex or image file

optional arguments:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        Output file name. If omitted will overwrite the existing project
  -n NAME, --name NAME  Layer name
  -i INDEX, --index INDEX
                        Index to insert the layer, 0 if omitted
  -t TOP, --top TOP     Background layer top offset, 0 if omitted
  -l LEFT, --left LEFT  Background layer left offset, 0 if omitted
  -W WIDTH, --width WIDTH
                        Background layer width, same as project if omitted
  -H HEIGHT, --height HEIGHT
                        Background layer height, same as project if omitted
```

### Api
TODO

## Dependencies

- **Pillow** - [Pillow](https://pypi.org/project/Pillow/) is an image manipulation library written in python

### License
This software is licensed under the MIT license
