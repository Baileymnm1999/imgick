import argparse

from imgick.core.Project import *


def alter(argv):
    parser = argparse.ArgumentParser(description='Alter an existing layer on an imgick project')
    parser.add_argument('project', help='Imgick project to alter')
    parser.add_argument('layer', type=int, help='Layer to alter by index')
    parser.add_argument('-o', '--output', help='Output file name. If omitted will overwrite the existing project')
    parser.add_argument('-n', '--name', default=None, help='Layer name')
    parser.add_argument('-i', '--index', type=int, default=None, help='Index to insert the layer if different')
    parser.add_argument('-t', '--top', type=int, default=None, help='Layer top offset, 0 if omitted')
    parser.add_argument('-l', '--left', type=int, default=None, help='Layer left offset, 0 if omitted')
    parser.add_argument('-W', '--width', type=int, default=None, help='Layer width, same as project if omitted')
    parser.add_argument('-H', '--height', type=int, default=None, help='Layer height, same as project if omitted')
    parser.add_argument('--visible', dest='visible', action='store_true', help='If set the layer will appear visible')
    parser.add_argument('--hidden', dest='visible', action='store_false', help='If set the layer will not appear visible')
    parser.set_defaults(visible=None)
    args = parser.parse_args(argv)

    # Get layer info
    project = Project.load(args.project)
    name = project.layers[args.layer][0]
    layer = project.layers[args.layer][1]

    if args.name is not None:  # Update name
        name = args.name

    loc = layer.loc
    if args.top is not None and args.left is not None:  # Update location
        loc = (args.top, args.left)

    visible = layer.visible
    if args.visible is not None:  # Update visibility
        visible = args.visible

    img = layer.img
    if args.width is not None and args.height is not None:  # Resize
        img = layer.img.resize((args.width, args.height))

    index = args.layer
    if args.index is not None:
        index = args.index

    # Update layer
    project.remove_layer(args.layer)
    project.add_layer(name, Layer(img, loc, visible), index)

    # Save project
    if args.output:
        project.save(args.output)
    else:
        project.save(args.project)
