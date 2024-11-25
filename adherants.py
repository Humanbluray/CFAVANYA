import time
import datetime
from style_sheet import *
import backend as be


class Adherants(ft.Container):
    def __init__(self, ctpr: object):
        super(Adherants, self).__init__(
            expand=True
        )
        self.ctpr = ctpr
        self.filter = ft.TextField(
            **filter_style, prefix_icon=ft.icons.SAVED_SEARCH, hint_text="Rechercher", width=300
        )
        self.check_all = ft.Switch(
            active_color="blue700", scale=0.5, on_change=self.check_datas
        )
        self.table_adherants = ft.DataTable(
            show_checkbox_column=True,
            data_text_style=ft.TextStyle(font_family="Poppins Medium", size=11, color='black87'),
            heading_text_style=ft.TextStyle(font_family="Poppins Medium", size=11, color="grey"),
            columns=[
                ft.DataColumn(self.check_all),
                ft.DataColumn(ft.Text("Numero")),
                ft.DataColumn(ft.Text("Nom")),
                ft.DataColumn(ft.Text("Fond")),
                ft.DataColumn(ft.Text("")),
                ft.DataColumn(ft.Text("Banque")),
                ft.DataColumn(ft.Text("Tontine")),
                ft.DataColumn(ft.Text("")),

            ]
        )

        # Widgets du formulaire de nouveau adhérant
        self.name = ft.TextField(
            **filter_style, width=400, prefix_icon="person", label="Nom".upper(),
            on_change=self.count_champs_infos
        )
        self.matricule = ft.TextField(
            **inactive_style, prefix_icon="credit_card", width=180, label="Matricule".upper(),
            on_change=self.count_champs_infos
        )
        self.bt_date = ft.IconButton(
            ft.icons.CALENDAR_MONTH, icon_size=18, icon_color="black87", bgcolor="#f0f0f6",
            on_click=lambda _: self.ctpr.dp_dob.pick_date(),
        )
        self.sel_date = ft.TextField(
            **inactive_style, label='Né le', width=120, on_change=self.count_champs_infos,
        )
        self.lieu = ft.TextField(
            **filter_style, width=170, label="à".upper(), on_change=self.count_champs_infos
        )
        self.bt_date_cni = ft.IconButton(
            ft.icons.CALENDAR_MONTH, icon_size=18, icon_color="black87", bgcolor="#f0f0f6",
            on_click=lambda _: self.ctpr.dp_cni.pick_date(),
        )
        self.cni = ft.TextField(
            **filter_style, width=250, prefix_icon=ft.icons.CREDIT_CARD, label="CNI", on_change=self.count_champs_infos
        )
        self.date_cni = ft.TextField(
            **inactive_style, width=120, label="Fait le".upper(),
        )
        self.lieu_cni = ft.TextField(
            **filter_style, width=90, label="Fait à".upper(),
        )
        self.adresse = ft.TextField(
            **filter_style, width=500, label="Adresse".upper(), prefix_icon=ft.icons.LOCATION_ON, on_change=self.count_champs_infos
        )
        self.ville = ft.TextField(
            **filter_style, width=200, label="Ville".upper(), prefix_icon=ft.icons.LOCATION_CITY, on_change=self.count_champs_infos
        )
        self.tel_1 = ft.TextField(
            **filter_style, width=200, label="Contact 1".upper(), prefix_icon=ft.icons.PHONE_ANDROID,
            input_filter=ft.NumbersOnlyInputFilter(), on_change=self.count_champs_infos
        )
        self.tel_2 = ft.TextField(
            **filter_style, width=200, label="Contact 2".upper(), prefix_icon=ft.icons.PHONE_ANDROID,
            input_filter=ft.NumbersOnlyInputFilter(), on_change=self.count_champs_infos
        )
        self.email = ft.TextField(
            **filter_style, width=300, label="Email".upper(), prefix_icon=ft.icons.MAIL, on_change=self.count_champs_infos
        )
        self.ref_person = ft.TextField(
            **filter_style, width=400, prefix_icon="person", label="Nom".upper(), on_change=self.count_champs_infos
        )
        self.ref_contact = ft.TextField(
            **filter_style, width=200, label="Contact".upper(), prefix_icon=ft.icons.PHONE_ANDROID,
            input_filter=ft.NumbersOnlyInputFilter(), on_change=self.count_champs_infos
        )
        self.bt_reg_date = ft.IconButton(
            ft.icons.EDIT_CALENDAR, icon_size=18, icon_color="black87", bgcolor="#f0f0f6",
            on_click=lambda _: self.ctpr.dp_registration.pick_date(),
        )
        self.sel_reg_date = ft.TextField(**inactive_style, label='date', width=120, on_change=self.count_champs_infos)
        self.counter = ft.ProgressBar(value=0, color="red", bgcolor="grey", height=6, width=100, border_radius=12)
        self.verif = ft.Icon(
            ft.icons.CHECK_CIRCLE, size=18, color="lightgreen",
            scale=ft.transform.Scale(0),
            animate_scale=ft.animation.Animation(300, ft.AnimationCurve.ELASTIC_IN_OUT)
        )
        self.tta = ft.Text(**italic_style, value="Masquer section")
        self.ttv = ft.Text(**italic_style, value="Masquer section")

        self.section_adherant = ft.Container(
            padding=0,  border=ft.border.all(1, "#ebebeb"),
            border_radius=4,
            content=ft.Column(
                controls=[
                    ft.Container(
                        padding=ft.padding.only(30, 2, 10, 2), bgcolor="#ebebeb", border=ft.border.all(1, "#ebebeb"),
                        border_radius=4,
                        content=ft.Row(
                            controls=[
                                ft.Text("1- Section infos adhérant".upper(), size=11, color="black", font_family="Poppins Bold"),
                                ft.Row(
                                    controls=[
                                        self.tta,
                                        ft.IconButton(
                                            ft.icons.KEYBOARD_ARROW_UP_OUTLINED, scale=0.8, icon_color="black",
                                            on_click=self.masquer_afficher_section_adherant
                                        )
                                    ], spacing=2
                                )
                            ], alignment="spaceBetween"
                        )
                    ),
                    ft.Divider(height=2, color="transparent"),
                    ft.Container(
                        padding=ft.padding.only(40, 10, 40, 10),
                        content=ft.Column(
                            controls=[
                                ft.Column(
                                    controls=[
                                        ft.Text(**italic_style, value="Noms et prénoms".upper()),
                                        ft.Divider(height=1, thickness=1),
                                        ft.Divider(height=1, color="transparent"),
                                        self.matricule, self.name,
                                        ft.Row(
                                            controls=[
                                                self.cni,
                                                ft.Row(
                                                    controls=[self.bt_date_cni, self.date_cni]
                                                ), self.lieu_cni
                                            ], spacing=20
                                        ),
                                        ft.Row(
                                            controls=[
                                                ft.Row(
                                                    controls=[
                                                        self.bt_date, self.sel_date
                                                    ]
                                                ), self.lieu
                                            ]
                                        ),
                                    ], spacing=12
                                ),
                                ft.Divider(height=2, color="transparent"),
                                ft.Text(**italic_style, value="Adressse et contacts".upper()),
                                ft.Divider(height=1, thickness=1),
                                ft.Divider(height=1, color="transparent"),
                                ft.Column(
                                    controls=[
                                        self.adresse, self.ville,
                                        self.email,
                                        ft.Row(
                                            controls=[
                                                self.tel_1, self.tel_2,
                                            ]
                                        ),
                                    ], spacing=12
                                ),
                                ft.Divider(height=2, color="transparent"),
                                ft.Text(**italic_style, value="Personne à contacter".upper()),
                                ft.Divider(height=1, thickness=1),
                                ft.Divider(height=1, color="transparent"),
                                ft.Column(
                                    controls=[
                                        self.ref_person, self.ref_contact,
                                        ft.Row(
                                            controls=[self.bt_reg_date, self.sel_reg_date]
                                        ),
                                    ], spacing=12
                                )
                            ]
                        )
                    )
                ]
            )
        )
        self.montant = ft.TextField(
            **filter_style, width=160, prefix_icon=ft.icons.MONETIZATION_ON_OUTLINED, label="montant".upper(),
            input_filter=ft.NumbersOnlyInputFilter(), text_align="right", on_change=self.count_champs_infos
        )
        self.methode = ft.Dropdown(
            **drop_style, label="Moyen paiement".upper(), width=180, prefix_icon=ft.icons.CREDIT_CARD_OUTLINED,
            on_change=self.count_champs_infos
        )
        self.type = ft.Dropdown(
            **drop_style, label="Type versement".upper(), width=180, prefix_icon=ft.icons.ACCOUNT_BALANCE,
            on_change=self.count_champs_infos
        )
        self.piece = ft.TextField(
            **filter_style, label="N° Reçu".upper(), width=180, prefix_icon=ft.icons.EDIT_DOCUMENT,
            on_change=self.count_champs_infos
        )
        self.section_versement = ft.Container(
            padding=0,  border_radius=4, border=ft.border.all(1, "#ebebeb"),
            content=ft.Column(
                controls=[
                    ft.Container(
                        padding=ft.padding.only(30, 2, 10, 2), bgcolor="#ebebeb", border_radius=4, border=ft.border.all(1, "#ebebeb"),
                        content=ft.Row(
                            controls=[
                                ft.Text("2- Section Versement".upper(), size=11, color="black", font_family="Poppins Bold"),
                                ft.Row(
                                    controls=[
                                        self.ttv,
                                        ft.IconButton(
                                            ft.icons.KEYBOARD_ARROW_UP_OUTLINED, scale=0.8, icon_color="black",
                                            on_click=self.masquer_afficher_section_versement
                                        )
                                    ]
                                )
                            ], alignment="spaceBetween"
                        )
                    ),
                    ft.Divider(height=2, color="transparent"),
                    ft.Container(
                        padding=ft.padding.only(40, 10, 40, 10),
                        content=ft.Column(
                            controls=[
                                ft.Row(
                                    controls=[
                                        self.montant, self.type, self.methode
                                    ], spacing=20
                                ),
                                self.piece
                            ], spacing=12
                        )
                    ),
                    ft.Divider(height=2, color="transparent"),
                ]
            )
        )

        self.formulaire_adherant = ft.Card(
            clip_behavior=ft.ClipBehavior.HARD_EDGE, elevation=50, surface_tint_color="white",
            scale=ft.transform.Scale(0), expand=True, show_border_on_foreground=True, width=750,
            animate_scale=ft.animation.Animation(300, ft.AnimationCurve.FAST_LINEAR_TO_SLOW_EASE_IN),
            content=ft.Container(
                padding=ft.padding.only(20, 10, 20, 10), expand=True, bgcolor="white",
                content=ft.Column(
                    expand=True,
                    controls=[
                        ft.Row(
                            controls=[
                                ft.Text("  Formulaire d'adhésion".upper(), size=16, font_family="Poppins Bold"),
                                ft.Row(
                                    controls=[
                                        ft.Text(**italic_style, value="Jauge Remplissage".upper()),
                                        self.counter, self.verif
                                    ]
                                ),
                                ft.IconButton(
                                    ft.icons.CLOSE, scale=0.7, icon_color="black", tooltip="Fermer",
                                    on_click=self.close_formulaire_new_adherent
                                )
                            ], alignment="SpaceBetween"
                        ),
                        ft.Divider(height=1, color="transparent"),
                        ft.Column(
                            expand=True, scroll="auto",
                            controls=[
                                self.section_adherant,
                                self.section_versement,
                                ft.Container(
                                    padding=ft.padding.only(10, 10, 10, 10),
                                    content=ft.Row(
                                        controls=[
                                            ft.ElevatedButton(
                                                on_click=self.add_new_adherant,
                                                bgcolor="#47358c", width=130,
                                                style=ft.ButtonStyle(
                                                    shape=ft.ContinuousRectangleBorder(radius=16)
                                                ),
                                                content=ft.Row(
                                                    controls=[
                                                        ft.Icon(ft.icons.CHECK, color="white", size=16),
                                                        ft.Text("Valider", size=12, color="white")
                                                    ]
                                                )
                                            ),
                                            ft.ElevatedButton(
                                                on_click=self.close_formulaire_new_adherent,
                                                bgcolor="#47358c", width=130,
                                                style=ft.ButtonStyle(
                                                    shape=ft.ContinuousRectangleBorder(radius=16)
                                                ),
                                                content=ft.Row(
                                                    controls=[
                                                        ft.Icon(ft.icons.CLOSE, color="white", size=16),
                                                        ft.Text("Annuler", size=12, color="white")
                                                    ]
                                                )
                                            )
                                        ]
                                    )
                                )
                            ]
                        ),
                    ]
                )
            )
        )
        # Dialog box
        self.box_icon = ft.Icon(
            ft.icons.DANGEROUS_OUTLINED, color="lightgreen",
            scale=ft.transform.Scale(0),
            animate_scale=ft.animation.Animation(300, ft.AnimationCurve.EASE_IN_QUAD)
        )
        self.box_content = ft.Text("", size=12, font_family="Poppins Light")
        self.box_title = ft.Text("", size=20, font_family="Poppins Light")
        self.box = ft.Card(
            clip_behavior=ft.ClipBehavior.HARD_EDGE, elevation=50, surface_tint_color="white",
            scale=ft.transform.Scale(0), show_border_on_foreground=True,
            animate_scale=ft.animation.Animation(300, ft.AnimationCurve.FAST_LINEAR_TO_SLOW_EASE_IN),
            height=300,
            content=ft.Container(
                padding=20, bgcolor="white", border_radius=8, on_click=self.close_box,
                content=ft.Column(
                    controls=[
                        self.box_title,
                        self.box_icon,
                        self.box_content
                    ], spacing=50, horizontal_alignment="center", alignment="center"

                )
            )
        )

        self.content = ft.Stack(
            controls=[
                ft.Container(
                    content=ft.Column(
                        expand=True,
                        controls=[
                            ft.Container(
                                padding=10, border_radius=8,  # border=ft.border.all(1, "#ebebeb"),
                                content=ft.Row(
                                    controls=[
                                        self.filter,
                                        ft.Row(
                                            controls=[
                                                ft.IconButton(
                                                    ft.icons.PERSON_ADD, icon_size=18, icon_color="black87",
                                                    on_click=self.open_formulaire_new_adherent
                                                ),
                                                ft.IconButton('print', icon_size=18, icon_color="black87")
                                            ]
                                        )
                                    ], alignment="spaceBetween"
                                )
                            ),
                            ft.Container(
                                expand=True,
                                border_radius=8,  # border=ft.border.all(1, "#ebebeb"), padding=10,
                                content=ft.Column(
                                    expand=True, scroll="auto",
                                    controls=[self.table_adherants]
                                )
                            )
                        ]
                    ),
                ),
                self.formulaire_adherant,
                self.box

            ],
            alignment=ft.alignment.center
        )
        self.load_datas()
        self.load_lists()

        # overlays
        self.ctpr.dp_dob.on_change = self.change_date_dob
        self.ctpr.dp_registration.on_change = self.change_date_registration
        self.ctpr.dp_cni.on_change = self.change_date_cni

    def check_datas(self, e):
        if self.check_all.value is True:
            for widget in self.table_adherants.rows:
                widget.cells[0].content.value = True
                widget.cells[0].content.update()

            self.table_adherants.update()

        else:
            for widget in self.table_adherants.rows:
                widget.cells[0].content.value = False
                widget.cells[0].content.update()

            self.table_adherants.update()

    def load_lists(self):
        # liste des methodes de paiement
        for row in self.methode.options:
            self.methode.options.remove(row)

        methodes = be.all_methodes()
        for methode in methodes:
            self.methode.options.append(ft.dropdown.Option(methode))

        for row in self.type.options:
            self.methode.options.remove(row)

        types = be.all_types()
        for typp in types:
            self.type.options.append(ft.dropdown.Option(typp))

    def load_datas(self):
        for row in self.table_adherants.rows[:]:
            self.table_adherants.rows.remove(row)

    @staticmethod
    def hover_ct(e):
        if e.control.data == 'true':
            e.control.opacity = 1
            e.control.update()
        else:
            e.control.opacity = 0
            e.control.update()

    def masquer_afficher_section_adherant(self, e):
        if e.control.icon == ft.icons.KEYBOARD_ARROW_UP_OUTLINED:
            self.section_adherant.height = 47
            self.section_adherant.update()
            e.control.icon = ft.icons.KEYBOARD_ARROW_DOWN_OUTLINED
            self.tta.value = "Afficher la section"
            self.tta.update()
            e.control.update()

        elif e.control.icon == ft.icons.KEYBOARD_ARROW_DOWN_OUTLINED:
            self.section_adherant.height = None
            self.section_adherant.update()
            e.control.icon = ft.icons.KEYBOARD_ARROW_UP_OUTLINED
            self.tta.value = "Masquer la section"
            self.tta.update()

    def masquer_afficher_section_versement(self, e):
        if e.control.icon == ft.icons.KEYBOARD_ARROW_UP_OUTLINED:
            self.section_versement.height = 47
            self.section_versement.update()
            e.control.icon = ft.icons.KEYBOARD_ARROW_DOWN_OUTLINED
            self.ttv.value = "Afficher la section"
            self.ttv.update()
            e.control.update()

        elif e.control.icon == ft.icons.KEYBOARD_ARROW_DOWN_OUTLINED:
            self.section_versement.height = None
            self.section_versement.update()
            e.control.icon = ft.icons.KEYBOARD_ARROW_UP_OUTLINED
            self.ttv.value = "Masquer la section"
            self.ttv.update()
            e.control.update()

    def count_champs_infos(self, e):
        count_none = 0
        # widgets = [
        #     self.name, self.cni, self.lieu, self.adresse, self.ville, self.lieu_cni,
        #     self.tel_2, self.tel_1, self.email, self.ref_contact, self.ref_person,
        #     self.montant, self.methode, self.type, self.piece,
        # ]
        widgets = [
            self.name,
            self.montant, self.methode, self.type, self.piece,
        ]

        for widget in widgets:
            if widget.value is None:
                count_none += 1
            elif widget.value == "":
                count_none += 1

        taux = (len(widgets) - count_none) / len(widgets)

        if 0 <= taux < 0.3:
            self.counter.color = "red"

        elif 0.3 <= taux < 0.6:
            self.counter.color = "amber"

        elif 0.6 <= taux < 1:
            self.counter.color = "lightgreen"

        else:
            date_count = 0
            for widget in (self.date_cni, self.sel_date, self.sel_reg_date):
                if widget.value is None or widget.value == "":
                    date_count += 1

            if date_count == 0:
                self.counter.color = "green"
                self.verif.scale = 1
                self.verif.update()

            else:
                self.counter.color = "green"
                self.verif.scale = 0
                self.verif.update()

        self.counter.value = taux
        self.counter.update()

    def change_date_dob(self, e):
        self.sel_date.value = str(self.ctpr.dp_dob.value)[0:10]
        self.sel_date.update()

    def change_date_registration(self, e):
        self.sel_reg_date.value = str(self.ctpr.dp_registration.value)[0:10]
        self.sel_reg_date.update()

    def change_date_cni(self, e):
        self.date_cni.value = str(self.ctpr.dp_cni.value)[0:10]
        self.date_cni.update()

    def close_box(self, e):
        self.box.scale = 0
        self.box.update()

    def open_formulaire_new_adherent(self, e):
        self.matricule.value = be.numero_matricule_nouveau()
        self.matricule.update()
        self.formulaire_adherant.scale = 1
        self.formulaire_adherant.update()

    def close_formulaire_new_adherent(self, e):
        widgets = [
            self.name, self.cni, self.lieu, self.adresse, self.ville, self.lieu_cni,
            self.tel_2, self.tel_1, self.email, self.ref_contact, self.ref_person,
            self.montant, self.methode, self.type, self.piece, self.date_cni,
            self.sel_date, self.sel_reg_date
        ]
        for widget in widgets:
            widget.value = None
            widget.update()

        self.counter.value = 0
        self.counter.update()

        self.formulaire_adherant.scale = 0
        self.formulaire_adherant.update()
        self.verif.scale = 0
        self.verif.update()

    def add_new_adherant(self, e):
        tel1 = 1 if self.tel_1.value is None or "" else self.tel_1.value
        tel2 = 1 if self.tel_2.value is None or "" else self.tel_2.value
        montant = int(self.montant.value)
        date_n = "0000-00-00" if self.sel_date.value is None or "" else self.sel_date.value
        lieu_n = "xxx" if self.lieu.value is None or "" else self.lieu.value
        cni = "xxx" if self.cni.value is None or "" else self.cni.value
        date_cni = "0000-00-00" if self.date_cni.value is None or "" else self.date_cni.value
        lieu_cni = "xxx" if self.lieu_cni.value is None or "" else self.lieu_cni.value
        adresse = "xxx" if self.adresse.value is None or "" else self.adresse.value
        ville = "xxx" if self.ville.value is None or "" else self.ville.value
        email = "xxx" if self.email.value is None or "" else self.email.value
        ref_person = "xxx" if self.ref_person.value is None or "" else self.ref_person.value
        ref_contact = 1 if self.ref_contact.value is None or "" else self.ref_contact.value
        sel_reg_date = "0000-00-00" if self.sel_reg_date.value is None or "" else self.sel_reg_date.value

        # Ajoput nouvel adhérant
        be.ajouter_adherant(
            self.matricule.value, self.name.value, date_n, lieu_n,
            cni, date_cni, lieu_cni, adresse,
            ville, tel1, tel2, email,
            ref_person, ref_contact, sel_reg_date
        )

        # Ajout du versement
        be.ajouter_versement(
            be.numero_du_versement(), self.sel_reg_date.value, self.matricule.value, montant,
            self.methode.value, self.type.value, self.piece.value
        )

        self.box_title.value = "Validé"
        self.box_title.update()
        self.box_content.value = "Nouvel adhérant enregistré"
        self.box_content.update()
        self.box.scale = 1
        self.box.update()
        time.sleep(0.5)
        self.box_icon.scale = 4.5
        self.box_icon.name = ft.icons.CHECK_CIRCLE_OUTLINE
        self.box_icon.color = "green"
        self.box_icon.update()
        self.load_datas()
        self.table_adherants.update()

        self.matricule.value = be.numero_matricule_nouveau()
        self.matricule.update()

        widgets = [
            self.name, self.cni, self.lieu, self.adresse, self.ville, self.lieu_cni,
            self.tel_2, self.tel_1, self.email, self.ref_contact, self.ref_person,
            self.montant, self.methode, self.type, self.piece, self.date_cni,
            self.sel_date, self.sel_reg_date
        ]
        for widget in widgets:
            widget.value = None
            widget.update()

        self.counter.value = 0
        self.counter.update()

        self.verif.scale = 0
        self.verif.update()




