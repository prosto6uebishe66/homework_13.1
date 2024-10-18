class Category:
    def __init__(self, name, description='', products=None):
        self.name = name
        self.description = description
        self.total_categories = 0
        self.unique_products = set()
        if products is None:
            self.products = []
        else:
            self.products = products

    def add_product(self, product):
        self.products.append(product)
        self.unique_products.add(product)
        self.total_categories += 1

    def get_all_products(self):
        return self.products

    @property
    def total_unique_products(self):
        return len(self.unique_products)

    def clear_data(self):
        self.products = []
        self.unique_products = set()
        self.total_categories = 0


# Добавление категорий и продуктов
electronics_category = Category('Электроника')
furniture_category = Category('Мебель')


class Product:
    def __init__(self, name, description='', price=0, quantity=0):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

# Примеры использования
tv = Product('Телевизор Samsung QLED', 'Телевизор с разрешением 4K', 69999, 10)
sofa = Product('Диван', 'Комфортный диван для гостиной', 39999, 2)
chair = Product('Кресло', 'Кресло для отдыха', 19999, 3)

# Добавление продуктов в категории
electronics_category = Category('Электроника')
furniture_category = Category('Мебель')

electronics_category.add_product(tv)
electronics_category.add_product(sofa)
furniture_category.add_product(chair)

print("Total categories:", electronics_category.total_categories + furniture_category.total_categories)
print("Unique products:", electronics_category.total_unique_products + furniture_category.total_unique_products)


tv = Product('Телевизор Samsung QLED', 'Телевизор с разрешением 4K', 69999, 10)
sofa = Product('Диван', 'Комфортный диван для гостиной', 39999, 2)
chair = Product('Кресло', 'Кресло для отдыха', 19999, 3)

electronics_category.add_product(tv)
electronics_category.add_product(sofa)
furniture_category.add_product(chair)

print("Total categories:", electronics_category.total_categories + furniture_category.total_categories)
print("Unique products:", electronics_category.total_unique_products + furniture_category.total_unique_products)
