import flet as ft
from board import TableaudeBord
from adherants import Adherants


class ItemMenu(ft.Container):
    def __init__(self, title: str, icone: str):
        super(ItemMenu, self).__init__(
            bgcolor="white",
            # border_radius=14,
            on_hover=self.hover_ct,
            shape=ft.RoundedRectangleBorder(radius=16),
            padding=ft.padding.only(20, 12, 0, 12),
            # width=170,
            scale=ft.transform.Scale(1),
            animate_scale=ft.animation.Animation(300, ft.AnimationCurve.FAST_LINEAR_TO_SLOW_EASE_IN)
        )
        self.title = title
        self.icone = icone
        self.is_clicked = False

        self.visuel = ft.Icon(icone, size=18, color=ft.colors.BLACK38)
        self.name = ft.Text(title, size=11, font_family="Poppins Medium", color="black")

        self.content = ft.Row(controls=[self.visuel, self.name], alignment='start')

    def hover_ct(self, e):
        if e.data == "true":
            e.control.scale = 1.1
            e.control.bgcolor = None
            e.control.visuel.color = "grey"
            e.control.name.font_family = "Poppins Medium"
            e.control.name.color = "#7B39EB"
            e.control.visuel.update()
            e.control.name.update()
            e.control.update()
        else:
            if self.is_clicked:
                self.bgcolor = "white"
                self.visuel.color = ft.colors.BLACK45
                self.name.color = "black"
                self.name.font_family = "Poppins Bold"
                self.border = ft.border.only(left=ft.BorderSide(5, "#7B39EB"))
                self.visuel.update()
                self.name.update()
                self.update()
            else:
                self.bgcolor = "white"
                self.border = None
                self.visuel.color = ft.colors.BLACK38
                self.name.font_family = "Poppins Medium"
                self.name.color = "black"
                self.visuel.update()
                self.name.update()
                self.update()

            e.control.scale = 1
            e.control.update()

    def set_is_clicked_true(self):
        self.is_clicked = True
        self.bgcolor = "white"
        self.visuel.color = ft.colors.BLACK45
        self.name.font_family = "Poppins Bold"
        self.border = ft.border.only(left=ft.BorderSide(5, "#7B39EB"))
        self.visuel.update()
        self.name.update()
        self.update()

    def set_is_clicked_false(self):
        self.is_clicked = False
        self.bgcolor = "white"
        self.visuel.color = ft.colors.BLACK38
        self.name.font_family = "Poppins Medium"
        self.border = None
        self.name.color = "black"
        self.visuel.update()
        self.name.update()
        self.update()


class Menu(ft.Container):
    def __init__(self, container_parent: object):
        super(Menu, self).__init__(
            padding=ft.padding.only(20, 15, 20, 15),
            bgcolor="white",
            border_radius=8,
            expand=True,
        )
        self.container_parent = container_parent
        self.tableau = ItemMenu('BOARD'.upper(), ft.icons.DASHBOARD_OUTLINED)
        self.adherants = ItemMenu("Adhérants".upper(), ft.icons.PERSON_OUTLINED)
        self.prets = ItemMenu("Prêts".upper(), ft.icons.CURRENCY_EXCHANGE_OUTLINED)
        self.versements = ItemMenu("Versements".upper(), ft.icons.MONETIZATION_ON_OUTLINED)
        self.journaux = ItemMenu('Journaux'.upper(), ft.icons.AUTO_STORIES_OUTLINED)
        self.comptes = ItemMenu('Comptes'.upper(), ft.icons.ASSURED_WORKLOAD_OUTLINED)
        self.exit = ItemMenu("Quitter".upper(), ft.icons.EXIT_TO_APP_OUTLINED)
        self.childrens = [
            self.tableau, self.adherants, self.prets, self.versements, self.journaux, self.comptes,
            self.exit
        ]

        for item in self.childrens:
            item.on_click = self.cliquer_menu

        self.content = ft.Column(
            expand=True,
            controls=[
                ft.Column(
                    controls=[
                        ft.Row([ft.Text("M E N U", size=16, font_family="Poppins Regular")], alignment='center'),
                        ft.Divider(height=1, thickness=1),
                        ft.Divider(height=2, color="transparent"),
                        ft.Column(
                            controls=[
                                self.tableau, self.adherants, self.prets, self.versements, self.journaux, self.comptes,
                            ], spacing=20, horizontal_alignment='center'
                        ),
                    ]
                ),
                ft.Column(
                    controls=[
                        ft.Divider(height=1, thickness=1),
                        self.exit,
                        ft.Text("CFA VANYA 1.0 BY VAN TECH", size=9, color="grey")
                    ], spacing=30,  horizontal_alignment='center'
                )
            ],
            horizontal_alignment="center",
            alignment="spaceBetween"
        )

    def cliquer_menu(self, e):
        for item in self.childrens:
            item.set_is_clicked_false()

        e.control.set_is_clicked_true()
        e.control.update()

        for row in self.container_parent.contenu.content.controls[:]:
            self.container_parent.contenu.content.controls.remove(row)

        if e.control.name.value == "Board".upper():
            self.container_parent.contenu.content.controls.append(TableaudeBord(self.container_parent))
            self.container_parent.update()

        if e.control.name.value == "Adhérants".upper():
            self.container_parent.contenu.content.controls.append(Adherants(self.container_parent))
            self.container_parent.update()


