import flet as ft
from page_view import PageView
from navigation_bar import NavigationBar

def main(page: ft.Page):

    def route_change(e):
        page.views.clear()
        if page.route == "/":
            page.views.append(
                ft.View(
                    "/",
                    [
                        ft.AppBar(
                            leading_width=40,
                            title=ft.Text("Supermercado"),
                            center_title=False,
                            bgcolor=ft.colors.RED_900,
                        ),
                        ft.Row([
                            navigation_bar.build_navigation_bar(),
                            page_view.home_page()
                        ], expand=True)
                    ],
                )
            )
        if page.route == "/delete_products":
            page.views.append(
                ft.View(
                    "/delete_products",
                    [
                        ft.AppBar(
                            leading_width=40,
                            title=ft.Text("Supermercado"),
                            center_title=False,
                            bgcolor=ft.colors.RED_900,
                        ),
                        ft.Row([
                            navigation_bar.build_navigation_bar(),
                            ft.Column([
                                page_view.recalled_product_page(),
                            ], height=600)
                        ])
                    ],
                )
            )
        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page_view = PageView(page)
    navigation_bar = NavigationBar(page)
    page.on_view_pop = view_pop

    page.go(page.route)

ft.app(main)