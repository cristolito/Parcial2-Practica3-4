import flet as ft
from product_list import ProductList
from product import Product
class PageView:
    def __init__(self, page: ft.Page) -> None:
        self.page = page
        self.product_list = ProductList()
        self.product_list_recalled = ProductList()
        self.total = ft.Text(size=25, weight="bold", color=ft.colors.RED_100)
        self.msg_name = ft.Text("Es necesario llenar este campo", size=15, weight="bold", visible=False)
        self.msg_key = ft.Text("Es necesario llenar este campo", size=15, weight="bold", visible=False)
        self.msg_price = ft.Text(size=15, weight="bold", visible=False)
        self.msg_error = ft.Text("El producto ya existe", size=15, weight="bold", visible=False)
        self.msg_delete = ft.Text(size=15, weight="bold", visible=False)
        self.input_key = ft.TextField(label="Llave del producto", width=200)
        self.input_name = ft.TextField(label="Nombre del producto", width=200)
        self.input_price = ft.TextField(label="Precio del producto", width=200)
        self.container = ft.Container()
        self.matriz_text = []
        self.input_delete = ft.TextField(label="Llave del producto para eliminar", text_align="right", width=250)

    def reset_msg_visible(self):
        self.msg_name.visible = False
        self.msg_key.visible = False
        self.msg_price.visible = False
        self.msg_error.visible = False

    def reset(self):
        self.reset_msg_visible()
        self.input_delete.value = ""
        self.input_key.value = ""
        self.input_name.value = ""
        self.input_price.value = ""

    def home_page(self):
        self.container.content = self.print_available()
        container = ft.Container(ft.Column([
                    ft.Container(ft.Text("¡Bienvenido al Supermercado Mazorca!", size=35, weight="bold"), margin=ft.margin.only(bottom=20)),
                    ft.Row([
                        ft.Column([
                            self.input_key,
                            self.msg_key,
                            self.input_name,
                            self.msg_name,
                            self.input_price,
                            self.msg_price,
                            ft.ElevatedButton("Agregar producto", on_click=self.handle_add),
                            self.msg_error
                        ], width=200),
                        ft.Column([
                            self.input_delete,
                            self.msg_delete,
                            ft.ElevatedButton("Eliminar producto", on_click=self.handle_delete),
                        ], width=200),
                        ft.Column([self.total, self.container]),
                    ], expand=True),
                ], 
                horizontal_alignment=ft.CrossAxisAlignment.CENTER),
            padding=ft.padding.all(10),
            margin=ft.margin.all(0),
            border=ft.border.all(5, ft.colors.WHITE),
            border_radius=ft.border_radius.all(15),
            expand=True
        )

        return container
    
    def handle_add(self, e):
        self.reset_msg_visible()
        if self.input_key.value == "":
            self.msg_key.visible = True
        if self.input_name.value == "":
            self.msg_name.visible = True
        if self.input_price.value == "":
            self.msg_price.value = "Es necesario llenar este campo"
            self.msg_price.visible = True

        if self.input_key.value != "" and self.input_name.value != "" and self.input_price.value != "":
            if self.input_price.value.isdigit():
                product = Product(self.input_key.value, self.input_name.value , float(self.input_price.value))
                if self.product_list.insert(product):
                    self.reset()
                    self.container.content = self.print_available()
                else:
                    self.msg_error.visible = True
            else:
                self.msg_price.visible = True
                self.msg_price.value = "Ingresa un precio válido"
                
        self.page.update()
    
    def print_available(self):
        self.product_list = self.product_list.sort_by_name()
        matriz = self.product_list.display()
        if matriz:
            self.total.value = f"El total es ${self.product_list.calculate_total_cost()}"
            columna = ft.Column(spacing=7, scroll=ft.ScrollMode.ALWAYS, expand=True)
            for i in range(len(matriz)):
                columna.controls.append(ft.Text(f"{matriz[i]}", size=15))
            return columna
        else:
            self.total.value = ""
    
    def print_recalled(self):
        self.product_list_recalled = self.product_list_recalled.sort_by_name()
        matriz = self.product_list_recalled.display()
        if matriz:
            columna = ft.Column(spacing=7, scroll=ft.ScrollMode.ALWAYS, height=500, width=500)
            for i in range(len(matriz)):
                columna.controls.append(ft.Text(f"{matriz[i]}", size=15))
            return columna
        else: return ft.Text("No hay productos que mostrar", size=35, weight="bold")

    def recalled_product_page(self):
        container = ft.Container(
            self.print_recalled()
        )

        return container
    
    def handle_delete(self, e):
        self.msg_error.visible = False
        if self.input_delete.value == "":
            self.msg_delete.value = "Es necesario llenar este campo"
            self.msg_delete.visible = True
        else:
            deleted_product = self.product_list.delete_product(self.input_delete.value)
            if deleted_product:
                self.product_list_recalled.insert(deleted_product)  
                self.container.content = self.print_available()
            else:
                self.msg_delete.value = "La llave proporcionada no existe"
                self.msg_delete.visible = True
                
        self.page.update()