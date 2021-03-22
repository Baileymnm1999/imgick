import argparse

from imgick.core.Project import *


def create(argv):
    parser = argparse.ArgumentParser(description='Create an imgick project')
    parser.add_argument('width', type=int, help='Height of project in pixels')
    parser.add_argument('height', type=int, help='Height of project in pixels')
    parser.add_argument('output', help='Output file name')
    parser.add_argument('-b', '--bg', help='Background layer to compose, specify an RGBA color in hex or image file')
    parser.add_argument('-n', '--bg-name', default="Background", help='Background layer name')
    parser.add_argument('-t', '--bg-top', type=int, default=0, help='Background layer top offset, 0 if omitted')
    parser.add_argument('-l', '--bg-left', type=int, default=0, help='Background layer left offset, 0 if omitted')
    parser.add_argument('-W', '--bg-width', type=int, default=0, help='Background layer width, same as project if omitted')
    parser.add_argument('-H', '--bg-height', type=int, default=0, help='Background layer height, same as project if omitted')
    args = parser.parse_args(argv)

    # Establish sizes, bg defaults to project size if height or width isn't specified
    project_size = (args.width, args.height)
    bg_size = (args.bg_width, args.bg_height)

    # Create background layer, image or color
    layers = None
    if args.bg:
        location = (args.bg_top, args.bg_left)
        try:  # image bg
            image = Image.open(args.bg)
            if not bg_size.count(0):  # a resize has been specified
                image = image.resize(bg_size)
            layers = [(args.bg_name, Layer(image, location))]

        except FileNotFoundError:  # solid color bg
            if bg_size.count(0):  # set to project size if no size specified
                bg_size = project_size
            layers = [(args.bg_name, Layer(Image.new('RGBA', bg_size, hex2rgba(args.bg)), location))]

    # Create project
    project = Project(project_size, layers)
    project.save(args.output)


def hex2rgba(h):
    h = h[1:]
    return int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16), int(h[6:8], 16)
