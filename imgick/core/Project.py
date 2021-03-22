import zipfile
import xml.etree.ElementTree as ET

from io import BytesIO
from typing import List, Tuple
from PIL import Image

from .Layer import Layer


class Project(object):
    def __init__(self, size: (int, int), layers: List[Tuple[str, Layer]] = None):
        self._size: (int, int) = size
        self._layers: List[Tuple[str, Layer]] = layers

    @classmethod
    def load(cls, filename):
        with zipfile.ZipFile(filename, 'r') as zf:
            root = ET.fromstring(zf.read('data.xml').decode("utf-8"))
            size = (int(root.attrib.get('width')), int(root.attrib.get('height')))

            layers = []
            root[:] = sorted(root, key=lambda child: child.get('z-index'))
            for child in root:
                location = (int(child.get('top')), int(child.get('left')))
                image_file = BytesIO(zf.read(child.get('path')))
                image = Image.open(image_file, formats=['BMP'])
                layers.append((child.get('name'), Layer(image, location)))

            return cls(size, layers)

    @property
    def size(self) -> (int, int):
        return self._size

    @property
    def layers(self) -> List[Tuple[str, Layer]]:
        return self._layers

    def xml(self) -> ET.ElementTree:
        root = ET.Element('project', {
            'width': str(self._size[0]),
            'height': str(self._size[1])
        })
        if self._layers:
            for index, (name, layer) in enumerate(self._layers):
                root.append(layer.xml(name, index))

        return ET.ElementTree(root)

    def _render_layer(self, layers: List[Layer], size: (int, int)) -> Image:
        if layers:
            base = self._render_layer(layers[1:], size)
            base.paste(layers[0].img, layers[0].loc)
            return base
        else:
            return Image.new('RGBA', size, (0, 0, 0, 0))

    def render(self) -> Image:
        return self._render_layer([layer for (_, layer) in self._layers], self._size)

    def save(self, filename):
        with zipfile.ZipFile(filename, 'w') as zf:
            zf.writestr('data.xml', ET.tostring(self.xml().getroot()))
            if self._layers:
                for (name, layer) in self._layers:
                    image_file = BytesIO()
                    exif_data = layer.img.info.get('exif')
                    layer.img.save(image_file, 'BMP', exif=exif_data)
                    zf.writestr('resources/%s.bmp' % name, image_file.getvalue())

    def add_layer(self, name, layer, index=0):
        self._layers.insert(index, (name, layer))
