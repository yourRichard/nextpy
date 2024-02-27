"""Welcome to Nextpy! This file outlines the steps to create a basic app."""
from xtconfig import config

import nextpy as xt


class State(xt.State):
    """The app state."""

    pass


def index():
    _main =xt.container(
        xt.box(
            xt.box(
                xt.image(src="./icon.svg",width="200px",height="200px",margin_top="160px",margin_left="30px"),
                xt.text("Nextpy",fontSize="80px",color="black",font_weight="bold",margin_top="175px",),
                display="flex",
            ),
            xt.box(
                xt.box(
                    xt.box(
                        xt.text(
                            "Login to your account",
                            fontSize="35px",
                            color="#eaeaea",
                            font_weight="bold",
                            letter_spacing="1.3px",
                        ),
                        xt.text(
                            "The Pure Python Framework for Web Apps, Meticulously Optimized for AI agents. World's first AMS.",
                            fontSize="14px",
                            font_weight="bold",
                            width="350px",
                            margin_left="175px",
                            margin_top="12px",
                            color = "#8c8c8c"
                        ),
                        xt.image(src="./gradient_underline.svg",position="absolute",margin_top="60px",margin_left="-318px",height="14px"),
                        text_align="center",
                        padding_top = "60px"
                    ),
                    xt.box(
                        xt.form(
                        xt.vstack(
                            xt.image(src="./draw.png",position="absolute",width="100px",height="100px",margin_left="245px",margin_top = "40px"),
                            xt.input(
                                placeholder="Email / Phone number",
                                name="first_name",
                                width = "240px",
                                border="none",
                                bg = "#222222",
                                color ="#373737"
                            ),
                            xt.input(
                                placeholder="Password",
                                name="password",
                                width = "240px",
                                border="none",
                                bg = "#222222",
                                color = "#373737"
                            ),
                            xt.button(
                                "Login to your account",
                                 width = "240px",
                                 background_image= "linear-gradient(to top, #fbc2eb 0%, #a6c1ee 100%)",
                                 text_align ="left",
                                 font_weight = "bold"
                            ),
                            xt.text(
                                "Don't have an account? Regiester",
                                fontSize="14px",
                                color="#373737",
                                cursor="pointer"
                            ), 
                            align_items = "left",
                            margin_left="60px",
                            margin_top="60px"
                        ),
                    ),
                        xt.form(
                        xt.vstack(
                            xt.box(
                                xt.image(src="./google.svg",width="25px",height="25px",                                margin_left = "8px",),
                                xt.text("Sign in with Google",fontSize ="15px",font_weight="bold",color="white",margin_left="15px"),
                                height = "42px",
                                width = "240px",
                                border="1px solid #ff3d00",
                                bg = "#222222",
                                border_radius = "5px",
                                display="flex",
                                align_items = "center",
                                text_align = "center",
                                cursor="pointer"
                            ),
                            xt.box(
                                xt.image(src="./github.svg",width="25px",height="25px",                                margin_left = "8px",),
                                xt.text("Sign in with Github",fontSize ="15px",font_weight="bold",color="white",margin_left="15px"),
                                height = "42px",
                                width = "240px",
                                border="1px solid #494369",
                                bg = "#222222",
                                border_radius = "5px",
                                display="flex",
                                align_items = "center",
                                text_align = "center",
                                cursor="pointer"
                            ),
                            xt.box(
                                xt.image(src="./facebook.svg",width="26px",height="26px",                                margin_left = "8px",),
                                xt.text("Sign in with Facebook",fontSize ="15px",font_weight="bold",color="white",margin_left="15px"),
                                height = "42px",
                                width = "240px",
                                border="1px solid #039be5",
                                bg = "#222222",
                                border_radius = "5px",
                                display="flex",
                                align_items = "center",
                                text_align = "center",
                                cursor="pointer"
                            ),
                            xt.text(
                                "Fogot Password?",
                                fontSize = "14px",
                                color="#373737",
                            ),
                            align_items = "right",
                            margin_left="90px",
                            margin_top="66px"
                        ),
                    ),
                    display = "flex"
                    ),
                    
                    width="700px",
                    height="500px",
                    bg="#1d1d1d",
                    margin_left="50px",
                    border_radius = "10px",
                    margin_top="40px"
                ),

            ),
            display="flex",
        ),
        
        maxWidth ="auto",
        height = "100vh",
        bg="#d8cafc",
    )
    return _main


# Add state and page to the app.
app = xt.App()
app.add_page(index)
app.compile()
