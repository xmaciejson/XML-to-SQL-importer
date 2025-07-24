from parser.xml_parser import XMLProductParser
from db.db_manager import DBManager

def main():
    parser = XMLProductParser("data/products.xml")
    products = parser.parse()

    db = DBManager()
    for product in products:
        db.insert_product(product)
    db.close()

    print("Imported", len(products), "products.")

if __name__ == "__main__":
    main()
