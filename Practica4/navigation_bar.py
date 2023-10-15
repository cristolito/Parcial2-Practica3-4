import flet as ft

class NavigationBar:
    def __init__(self, page: ft.Page) -> None:
        self.page = page
        self.routes = ["/","/delete_products"]
        self.top_nav_items = [
            ft.NavigationRailDestination(
                label_content=ft.Text("Compra", size=13),
                label="Boards",
                icon=ft.icons.MONEY,
                selected_icon=ft.icons.MONEY
            ),
            ft.NavigationRailDestination(
                label_content=ft.Text("Eliminados", size=13),
                label="Boards",
                icon=ft.icons.REMOVE_SHOPPING_CART,
                selected_icon=ft.icons.REMOVE_SHOPPING_CART
            )
        ]
    
        self.top_nav_rail = ft.NavigationRail(
                                    selected_index=None,
                                    label_type="all",
                                    on_change=self.top_nav_change,
                                    destinations=self.top_nav_items,
                                    bgcolor=ft.colors.BLUE_GREY_700,
                                    extended=True,
                                    expand=True,)
        
    def build_navigation_bar(self):
        navigation_bar = ft.Container(
            content=ft.Column([
                ft.Row([
                    ft.Text("Secciones", size=20),
                ]),
                # divider
                ft.Container(
                    bgcolor=ft.colors.BLACK26,
                    border_radius=ft.border_radius.all(30),
                    height=1,
                    alignment=ft.alignment.center_right,
                    width=220
                ),
                ft.Container(
                    content=self.top_nav_rail,
                    bgcolor=ft.colors.BLACK26,
                    border_radius=ft.border_radius.all(30),
                    alignment=ft.alignment.center_right,
                    width=220,
                    height=320
                ),
                # divider
                ft.Container(
                    bgcolor=ft.colors.BLACK26,
                    border_radius=ft.border_radius.all(30),
                    height=1,
                    alignment=ft.alignment.center_right,
                    width=220
                ),
            ], tight=True),
            padding=ft.padding.all(15),
            margin=ft.margin.all(0),
            width=275,
            height=600,
            bgcolor=ft.colors.BLUE_GREY_700,
            border_radius=ft.border_radius.all(15)
        )
        return navigation_bar
                    

    def top_nav_change(self,e):
        self.top_nav_rail.selected_index = e.control.selected_index
        self.page.go(self.routes[e.control.selected_index])
        self.page.update()
        
    