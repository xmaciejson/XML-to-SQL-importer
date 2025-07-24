import xml.etree.ElementTree as ET

class Product:
    def __init__(self, product_id, name, price, category):
        self.id = int(product_id)
        self.name = name
        self.price = float(price)
        self.category = category

class XMLProductParser:
    def __init__(self, xml_path):
        self.xml_path = xml_path

    def parse(self):
        tree = ET.parse(self.xml_path)
        root = tree.getroot()
        products = []

        for product in root.findall('product'):
            pid = product.find('id').text
            name = product.find('name').text
            price = product.find('price').text
            category = product.find('category').text
            products.append(Product(pid, name, price, category))

        return products
