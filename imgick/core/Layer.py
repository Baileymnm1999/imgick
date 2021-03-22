import xml.etree.ElementTree as ET

from PIL import Image


class Layer(object):
    def __init__(self, image: Image, location: (int, int)):
        self._img = image
        self._loc = location

    def xml(self, name: str, z_index: int) -> ET.Element:
        element = ET.Element('layer', {
            'name': name,
            'path': 'resources/%s.bmp' % name,
            'z-index': str(z_index),
            'top': str(self._loc[0]),
            'left': str(self._loc[1])
        })
        return element

    @property
    def img(self) -> Image:
        return self._img

    @property
    def loc(self):
        return self._loc
