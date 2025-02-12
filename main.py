import flet as ft
from accueil import Accueil


def main(page: ft.Page):
    page.fonts = {
        "Poppins Regular": "fonts/Poppins-Regular.ttf",
        "Poppins Bold": "fonts/Poppins-Bold.ttf",
        "Poppins Black": "fonts/Poppins-Black.ttf",
        "Poppins Italic": "fonts/Poppins-Italic.ttf",
        "Poppins Medium": "fonts/Poppins-Medium.ttf",
        "Poppins ExtraBold": "fonts/Poppins-ExtraBold.ttf"
    }
    page.theme = ft.Theme(
        font_family="Poppins Medium"
    )

    def change_route(route):

        # initial route ...
        page.views.clear()
        page.views.append(Accueil(page))
        page.update()

        if page.route == "/accueil":
            pass

    def view_pop(view):
        page.views.pop()
        top_view = page.view[-1]
        page.go(top_view.route)

    page.on_route_change = change_route
    page.on_view_pop = view_pop
    page.go(page.route)


if __name__ == '__main__':
    ft.app(target=main, assets_dir='assets')
