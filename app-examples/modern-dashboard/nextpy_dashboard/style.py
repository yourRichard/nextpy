# style class for components

#main css dict
css: dict = {
    "app" : {
        "_dark" : {"bg":"#1f2128"},
        "_light" : {"bg":"#312e2a"},
        "font_family":"Gill Sans",
    },
    "header":{
        "width":"100%",
        "height":"7vh",
        "box_shadow":"0px 8px 16px 0px rgba(0,0,0,0.35)",
        "justify_content":"center",
        "padding":["0 1rem","0 1rem","0 1rem","0 4rem","0 10rem"],
        "transition":"all 400ms ease",
        
        "_dark": {
            "bg":"#141518",
        },
        
        "_light": {
            "bg":"#292824",
        },
    },
    "content": {
        "width":"100%",
        "display":"flex",
        "justify_content":"center",
        "align_items":"center",
    },
    "workSpace": {
        "width":"100%",
        "display":"flex",
        "justify_content":"center",
        "align_items":"center",
        "height":"100vh"
    },
    "main": {
        "width":"100%",
        "display":"flex",
        "justify_content":"center",
        "align_items":"center",
        "height":"100vh"
    }
}

def create_box_dimensions(width,height) -> dict[str,any]:
    return {
        "width":width,
        "height":height,
        "box_shadow":"0px 10px 20px 0px rgba(0,0,0,0.5)",
        "_hover":{"box_shadow":"none"},
        "transition":"all 450ms ease",
        "display":"flex",
        "justify_content":"center",
        "align_items":"center",
    }
    
dimensions = {
    "square": create_box_dimensions("5em","5em"),
    "rectangle":create_box_dimensions("5em","10.5em"),
    "custom_1":create_box_dimensions("10.5em","10.5em"),
    "custom_2":create_box_dimensions("10.5em","5em")
}
blink = {
    "@keyframes blink": {
        "0%":{"opacity":"0"},
        "50%":{"opacity":"1"},
        "100%":{"opacity":"0"},
    },
    "animation":"blink 0.9s infinite",
}