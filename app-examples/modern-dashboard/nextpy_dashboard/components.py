import nextpy as xt
from .style import css
from .state import State

# Box class
class Box(xt.Container):
    def __init__(
        self,
        shape, # can be square or rectangle
        border_color,
        size,
        icon = "bell",
        function = State.emptyFunction
    ):
        super().__init__(
            style = shape,
            border =f"5px double {border_color}",
            cursor = "pointer",
            border_radius = "10px",
            children=[
                xt.icon(
                  tag=icon,
                  transform=f"Scale({size})",
                  _light= {"color":"rgba(255,255,255)"},
                )
            ],   
            on_click = function,
            
        )
class Button(xt.Button):
    def __init__(self,number,function = State.emptyFunction):
        super().__init__(
            color_scheme = xt.Var.create("none"),
            color = "rgba(255,255,255,0.81)",
            on_click = function,
            children = [xt.text(number,font_size = "10px")] 
        )
    