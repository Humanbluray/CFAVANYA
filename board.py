from style_sheet import *

normal_radius = 30
hover_radius = 40
normal_title_style = ft.TextStyle(size=16, color='white', font_family="Poppins Bold"),

hover_title_style = ft.TextStyle(
    size=22,
    color='white',
    font_family="Poppins Bold",
    shadow=ft.BoxShadow(blur_radius=2, color=ft.colors.BLACK54),
)


class TableaudeBord(ft.Container):
    def __init__(self, container_parent: object):
        super(TableaudeBord, self).__init__(
            padding=10,
        )
        self.container_parent = container_parent
        self.adherents_chart = ft.PieChart(
            sections=[
                ft.PieChartSection(
                    65,
                    title="40%",
                    title_style=normal_title_style,
                    color=ft.colors.TEAL,
                    radius=normal_radius,
                ),
                ft.PieChartSection(
                    35,
                    title="30%",
                    title_style=normal_title_style,
                    color=ft.colors.GREY,
                    radius=normal_radius,
                )
            ],sections_space=1,
            center_space_radius=40,
            on_chart_event=self.on_chart_event,
            expand=True,
        )

        self.content = ft.Column(
            # expand=True,
            controls=[

            ]
        )

    def on_chart_event(self, e: ft.PieChartEvent):
        for idx, section in enumerate(self.adherents_chart.sections):
            if idx == e.section_index:
                section.radius = hover_radius
                section.title_style = hover_title_style
            else:
                section.radius = normal_radius
                section.title_style = normal_title_style
        self.adherents_chart.update()
