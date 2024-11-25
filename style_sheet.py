import flet as ft

filter_style: dict = dict(
    dense=True, height=40,
    border_color="#f2f2f2", bgcolor="#f2f2f2",
    content_padding=12, cursor_height=20,
    label_style=ft.TextStyle(size=11, font_family="Poppins Medium"),
    hint_style=ft.TextStyle(size=11, font_family="Poppins Medium"),
    text_style=ft.TextStyle(size=12, font_family="Poppins Medium"),
    border_radius=6,
    focused_border_color="#f4f0f7", focused_bgcolor="#f4f0f7",
    capitalization=ft.TextCapitalization.CHARACTERS,
    cursor_color="#47358c"
)
underline_style: dict = dict(
    dense=True, height=40,
    content_padding=12, cursor_height=20,
    label_style=ft.TextStyle(size=11, font_family="Poppins Medium"),
    hint_style=ft.TextStyle(size=11, font_family="Poppins Medium"),
    text_style=ft.TextStyle(size=12, font_family="Poppins Medium"),
    border="underline",
    capitalization=ft.TextCapitalization.CHARACTERS,
    cursor_color="#47358c"
)
inactive_style: dict = dict(
    dense=True, height=40,
    disabled=True,
    content_padding=12, cursor_height=20,
    label_style=ft.TextStyle(size=12, font_family="Poppins Medium"),
    hint_style=ft.TextStyle(size=12, font_family="Poppins Medium"),
    text_style=ft.TextStyle(size=12, font_family="Poppins Medium"),
    border_radius=6,
    capitalization=ft.TextCapitalization.CHARACTERS,
)
sweet_style: dict = dict(
    dense=True, height=40,
    content_padding=12, cursor_height=20,
    label_style=ft.TextStyle(size=12, font_family="Poppins Medium"),
    hint_style=ft.TextStyle(size=12, font_family="Poppins Medium"),
    text_style=ft.TextStyle(size=12, font_family="Poppins Medium"),
    border_radius=6,
    capitalization=ft.TextCapitalization.CHARACTERS,
)
drop_style: dict = dict(
    dense=True, height=40, border_radius=6, bgcolor="#f0f0f6", border_color="#f0f0f6",
    focused_border_color="#f4f0f7", focused_bgcolor="#f4f0f7",
    content_padding=12, label_style=ft.TextStyle(size=11, font_family="Poppins Medium", color="black"),
    text_style=ft.TextStyle(size=12, font_family="Poppins Medium", color="black")
)

italic_style: dict = dict(
    size=11, font_family="Poppins Italic", color='grey'
)