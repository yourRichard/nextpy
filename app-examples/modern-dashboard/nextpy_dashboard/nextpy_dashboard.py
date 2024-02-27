"""Welcome to Nextpy! This file outlines the steps to create a basic app."""

import nextpy as xt
from .style import css,blink,dimensions
from .state import State
from .components import Box,Button

def index() -> xt.Component:
    return xt.vstack(
        xt.spacer(),
        xt.vstack(
            xt.hstack(xt.text(
                State.prompt,
                font_size = "32px",
                color = "rgba(255,255,255,0.81)",
            ),
            xt.divider(
                orientation="vertical",
                height = "4em",
                transform = "translateX(5px)",
                style=blink
            ),
        ),
            spacing="0",
            style = css["content"],
        ),
        xt.divider(height = "2em",opacity="0"),
        xt.hstack(
            xt.vstack(
                xt.hstack(
                    xt.vstack(
                        Box(dimensions["square"],"red","1.5","drag_handle",State.getMovies),
                        Box(dimensions["square"],"teal","1.5","at_sign",State.getQuates),
                        ),
                        
                    Box(
                        dimensions["rectangle"],
                        "orange",
                        "1.75",
                        "calendar",
                        State.getDate
                ),
                    ),
                Box(
                    dimensions["custom_1"],
                    "gray",
                    "4",
                    "time",
                    State.getTime
                ),
                transition = "all 550ms ease",
                spacing = State.leftSpacing,
            ),
            xt.vstack(
                xt.hstack(
                    xt.vstack(
                        Box(dimensions["square"],"teal","1.5","email"),
                        Box(dimensions["square"],"red","1.5","email"),
                        Box(dimensions["square"],"teal","1.5","email"),
                    ),
                    xt.vstack(
                        Box(dimensions["square"],"gray","1.5","email"),
                        Box(dimensions["rectangle"],"orange","1.75","lock",State.passwordGenerate),
                        ),
                ),
                Box(
                    dimensions["custom_2"],
                    "purple",
                    "1.75",
                    "email",
                ),
                spacing = State.oneBlockSpace,
                transition = "all 550ms ease",
            ),
            spacing = State.spacing
        ),
         xt.vstack(
                xt.text(
                    "Change your layout here",
                    _light = {"color":"rgba(255,255,255,0.81)"},
                    font_size = "14px"
                ),
                xt.hstack(
                    Button("1x",State.setFull),
                    Button("2x",State.setHalf),
                    Button("3x",State.setThree),
                    Button("4x",State.setFour),
                    spacing = "0"
                ),
                spacing = "0",
                padding_top ="30px"
            ),

        style = css["workSpace"],
        padding_bottom = "80px"
    )


# Add state and page to the app.
app = xt.App(style=css["app"])
app.add_page(index,on_load = State.greetOnLoad)
app.compile()
