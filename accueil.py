from components import *
import datetime

class Accueil(ft.View):
    def __init__(self, page):
        super(Accueil, self).__init__(
             horizontal_alignment="center", route="/", bgcolor="white"
        )
        self.page = page
        self.menu = Menu(self)
        self.barre = ft.Container(
            content=self.menu,
            width=180,
        )
        self.contenu = ft.Container(
            padding=10,
            border_radius=0,  border=ft.border.only(left=ft.BorderSide(1, "#ebebeb")),
            expand=True,
            content=ft.Column(
                expand=True,
                controls=[
                    ft.Row(
                        controls=[
                            ft.Text("...", size=16, font_family="Poppins Regular"),
                        ]
                    )
                ],
            )
        )
        # Dialog box
        self.box = ft.AlertDialog(
            surface_tint_color="white",
            title=ft.Text("", size=20, font_family="Poppins Light"),
            content=ft.Row(controls=[], alignment='center'),
            actions=[ft.TextButton("Quitter", on_click=self.close_box)]
        )
        self.dp_dob = ft.DatePicker(last_date=datetime.date.today())
        self.dp_cni = ft.DatePicker(last_date=datetime.date.today())
        self.dp_registration = ft.DatePicker(last_date=datetime.date.today())

        # Overlays _________________________________________________________

        for widget in (self.box, self.dp_dob, self.dp_registration, self.dp_cni):
            self.page.overlay.append(widget)

        self.controls = [
            ft.Container(
                expand=True,
                content=ft.Row(
                    expand=True,
                    controls=[
                        self.barre,
                        self.contenu
                    ],
                )
            )
        ]

    def close_box(self, e):
        self.box.open = False
        self.box.update()










