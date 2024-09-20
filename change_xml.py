import os
import xml.etree.ElementTree as ET

xml_folder = '/Users/mac/Desktop/Datasets CAR /Red Car.v1i.voc/train'  # or "valid"/"test" directory

for filename in os.listdir(xml_folder):
    if filename.endswith('.xml'):
        file_path = os.path.join(xml_folder, filename)

        # Парсимо XML файл
        tree = ET.parse(file_path)
        root = tree.getroot()

        for obj in root.findall('object'):
            name = obj.find('name')
            if name is not None:
                name.text = 'car'

        tree.write(file_path)

print("Зміни виконано успішно!")