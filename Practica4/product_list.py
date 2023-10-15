from node import Node
class ProductList:
    def __init__(self):
        self.head = None

    def insert(self, product):
        current = self.head
        while current:
            product_list = current.data
            if product_list.key == product.key or product_list.name == product.name:
                return False #Existe un producto igual
            current = current.next_node

        new_node = Node(product)
        new_node.next_node = self.head
        self.head = new_node

        return True

    def display(self):
        current = self.head
        list = []
        while current:
            product = current.data
            list.append(f"Name: {product.name} Key: {product.key} Price: ${product.price}")
            current = current.next_node

        return list

    def delete_product(self, key):
        current = self.head
        previous = None

        while current:
            if current.data.key == key:
                deleted_product = current.data
                if previous:
                    previous.next_node = current.next_node
                else:
                    self.head = current.next_node
                return deleted_product  # Product deleted successfully

            previous = current
            current = current.next_node

        return False  # Product with the given key not found

    def sort_by_name(self):
        products = []
        current = self.head

        while current:
            products.append(current.data)
            current = current.next_node

        sorted_products = sorted(products, key=lambda x: x.name.lower())
        sorted_products.reverse()
        sorted_list = ProductList()

        for product in sorted_products:
            sorted_list.insert(product)

        return sorted_list

    def calculate_total_cost(self):
        total_cost = 0
        current = self.head

        while current:
            total_cost += current.data.price
            current = current.next_node

        return total_cost
