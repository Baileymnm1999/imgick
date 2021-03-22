import argparse

from imgick.core.Project import *


def render(argv):
    parser = argparse.ArgumentParser(description='Render an imgick project')
    parser.add_argument('project', help='Imgick project to render')
    parser.add_argument('-o', '--output', help='Output file name. If omitted will open with image viewer')
    parser.add_argument('-f', '--format', default='PNG', help='Image format to use')
    args = parser.parse_args(argv)

    project = Project.load(args.project)
    image = project.render()
    if args.output:
        image.save('%s.%s' % (args.output, args.format.lower()), format=args.format)
    else:
        image.show(args.project)
