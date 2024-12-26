class Product:
    def __init__(self, name:str, weight:float, category:str):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}"

class Shop:
    __file_name = 'products.txt'
    def get_products(self):
        file = open(self.__file_name, 'r')
        product = file.read()
        file.close()
        return product

    def add(self, *products):
        file_content = self.get_products()
        lines = file_content.split('\n') if file_content else []
        product_dict = {}
        for line in lines:
            if line.strip():
                name, weight, category = line.split(', ')
                product_dict[(name, category)] = float(weight)
        with open(self.__file_name, 'w') as file:
            for product in products:
                key = (product.name, product.category)
                if key in product_dict:
                    product_dict[key] += product.weight
                    print(
                        f'Продукт {product.name} уже есть в магазине, его общий вес теперь равен {product_dict[key]}'
                    )
                else:
                    product_dict[key] = product.weight
            for (name, category), weight in product_dict.items():
                file.write(f'{name}, {weight}, {category}\n')

s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

s1.add(p1, p2, p3)

print(s1.get_products())
