import argparse

from imgick.core.Project import *


def compose(argv):
    parser = argparse.ArgumentParser(description='Compose a new layer onto an imgick project')
    parser.add_argument('project', help='Imgick project to compose onto')
    parser.add_argument('layer', help='Background layer to compose, specify an RGBA color in hex or image file')
    parser.add_argument('-o', '--output', help='Output file name. If omitted will overwrite the existing project')
    parser.add_argument('-n', '--name', default="New Layer", help='Layer name')
    parser.add_argument('-i', '--index', type=int, default=0, help='Index to insert the layer, 0 if omitted')
    parser.add_argument('-t', '--top', type=int, default=0, help='Background layer top offset, 0 if omitted')
    parser.add_argument('-l', '--left', type=int, default=0, help='Background layer left offset, 0 if omitted')
    parser.add_argument('-W', '--width', type=int, default=0, help='Background layer width, same as project if omitted')
    parser.add_argument('-H', '--height', type=int, default=0, help='Background layer height, same as project if omitted')
    args = parser.parse_args(argv)

    project = Project.load(args.project)

    # Establish sizes, bg defaults to project size if height or width isn't specified
    size = (args.width, args.height)

    # Create background layer, image or color
    location = (args.top, args.left)
    try:  # image bg
        image = Image.open(args.layer)
        if not size.count(0):  # a resize has been specified
            image = image.resize(size)
        layer = Layer(image, location)

    except FileNotFoundError:  # solid color bg
        if size.count(0):  # set to project size if no size specified
            bg_size = project.size
        layer = Layer(Image.new('RGBA', size, hex2rgba(args.layer)), location)

    # Add layer to project
    project.add_layer(args.name, layer, args.index)

    # Save project
    if args.output:
        project.save(args.output)
    else:
        project.save(args.project)


def hex2rgba(h):
    h = h[1:]
    return int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16), int(h[6:8], 16)
