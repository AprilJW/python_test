from xml.etree import ElementTree
from lxml import etree
from pathlib import Path
import uuid

XML_EXT = '.xml'

class PascalVocReader:
    def __init__(self, filepath):
        self.filepath = Path(filepath)
        self.shapes = []
        self.parseXML()


    def addShapeWithVertex(self, name, lineWidth, vertex, guid, parentGuid, width=None, height=None):
        self.shapes.append((name, lineWidth, vertex, guid, parentGuid, width, height))

    def parseXML(self):
        assert self.filepath.suffix == XML_EXT
        parser = etree.XMLParser(encoding='utf-8')
        root = ElementTree.parse(self.filepath, parser=parser).getroot()

        self.width = (root.find('size').find('width').tag, root.find('size').find('width').text)
        self.height = (root.find('size').find('height').tag, root.find('size').find('height').text)

        for obj in root.findall('object'):
            self.parseShapeVertex(obj)

    def parseShapeVertex(self, obj):
        vertex = []
        name = obj.find('name').text
        lineWidth = obj.find('lineWidth').text
        guid = uuid.uuid4()
        parentGuid = guid
        for v in obj.findall('vertex'):
            vertex.append((v.find('x').text, v.find('y').text))
        self.addShapeWithVertex(name, lineWidth, vertex, guid, parentGuid, self.width, self.height)


if __name__ == '__main__':
    pascalvocreader = PascalVocReader('/Users/jw/Projects/0920test_2D/data/2007_000048.xml')
    print(pascalvocreader.shapes)
    pascalvocreader.parseXML()
    print(pascalvocreader.shapes)