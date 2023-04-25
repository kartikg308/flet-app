from flet import *
from controls import add_to_control_reference
from btn import return_form_button


class AppForm(UserControl):
    def __init__(self):
        super().__init__()

    def app_form_input_instance(self):
        add_to_control_reference("AppForm", self)

    def app_form_input_field(self, name: str, expand: int):
        return Container(
            expand=expand,
            height=45,
            bgcolor="#ebebeb",
            border_radius=6, 
            padding=8,
            content=Column(
                spacing=1,
                data = [
                    Text(value=name, size=9, color="black", weight=FontWeight.BOLD),
                    TextField(
                        border_color="transparent",
                        height=20,
                        text_size=13, 
                        content_padding=0, 
                        cursor_color="black",
                        cursor_width=1,
                        cursor_height=18,
                        color="black",
                    ),
                ]
            ),
        )

    def build(self):
        return Container(
            expand=True,
            height=190,
            bgcolor="white10",
            border=border.border.all(1, "#ebebeb"),
            border_radius=8,
            padding=15,
            content=Column(
                expand=True, 
                controls=[
                    Row(
                        data=[
                            self.app_form_input_field("Field *", True),
                        ],
                    ),
                    Row(
                        data=[
                            self.app_form_input_field("Field One *", 3),
                            self.app_form_input_field("Field Two *", 1),
                            self.app_form_input_field("Field Three *", 1),
                        ],
                    ),
                    Divider(height=2, color="transparent"),
                    Row(
                        alignment=MainAxisAlignment.END,
                        data=[
                            return_form_button()
                        ],
                    ),
                ],
            )
        )
