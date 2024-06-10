class Products:
    def __init__(self, products, bonuses=0):
        self.bonuses = bonuses
        self.products = products

    def get_products_price(self):
        return sum(self.products.values()) - self.bonuses

    def __add__(self, other):
        if isinstance(other, int):
            return Products(self.products, self.bonuses + other)
        elif isinstance(other, Products):
            new_products = {}
            for product, price in self.products.items():
                if product not in new_products:
                    new_products[product] = price
            for product, price in other.products.items():
                if product not in new_products:
                    new_products[product] = price
            return Products(new_products)

    def __radd__(self, other):
        if isinstance(other, int):
            return Products(self.products, self.bonuses + other)

    def __sub__(self, other):
        if isinstance(other, int):
            return Products(self.products, self.bonuses - other)
        elif isinstance(other, Products):
            new_products = {}
            for product, price in self.products.items():
                if product not in other.products:
                    new_products[product] = price
            return Products(new_products)

    def __rsub__(self, other):
        if isinstance(other, int):
            return Products(self.products, self.bonuses - other)


products1 = Products({'Молоко': 3, 'Сыр': 5})
print(f'Цена: {products1.get_products_price()}. {products1.products}')
products2 = Products({'Кефир': 2})
products3 = products1 + products2
print(f'Цена: {products3.get_products_price()}. {products3.products}')
products4 = products3 + 2
products5 = 1 + products4
products5 += 1
print(f'Цена: {products5.get_products_price()}. {products5.products}')
print('-' * 40)
products5 -= 1
products6 = 1 - products5
products7 = products6 - products2
print(f'Цена: {products6.get_products_price()}. {products6.products}')
print(f'Цена: {products7.get_products_price()}. {products7.products}')

# ДЗ
# 1. Реализовать логику для удаления продуктов из корзины
# 2. Реализовать логику для списания(удаления) бонусов
# (i) __sub__ и __rsub__