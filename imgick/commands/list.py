import argparse

from imgick.core.Project import *


def list(argv):
    parser = argparse.ArgumentParser(description='List project details')
    parser.add_argument('project', help='Imgick project to list')
    args = parser.parse_args(argv)

    # Create project
    project = Project.load(args.project)

    print()
    # List project details
    print('-'*10 + ' Project Details ' + '-'*10)
    print('width: %s' % project.size[0])
    print('height: %s' % project.size[1])

    # List project layes
    print('-'*10 + '     Layers      ' + '-'*10)
    for index, (name, layer) in enumerate(project.layers):
        print('%d:' % index)
        print('\tname: %s' % name)
        print('\tsize: %dx%d' % layer.img.size)
        print('\ttop: %d' % layer.loc[0])
        print('\tleft: %d' % layer.loc[1])

    print()
