"""Welcome to Nextpy! This file outlines the steps to create a basic app."""

import nextpy as xt
import random
import asyncio



class State(xt.State):
    """The app state."""
    emoji_list: list[list] = [[i,"0%"] for i in range(36)]

    count: int = 0
    track: list = []
    score: int = 0
    result:str

    def reveal_emoji(self,emoji,emoji_type):
        index = emoji[0]
        self.emoji_list = [
            [i,"100%"] if i  == index else [i,opacity]
            for i,opacity in self.emoji_list
        ]

        self.count += 1
        self.track.append((emoji_type,emoji))
    
    def reset_game(self):
        """Reset the game state and boart"""
        self.emoji_list = [[i, "0%"] for i in range(36)]
        self.count = 0
        self.track = []
        self.score = 0
        self.result = None 
        
        game.create_board()

    async def check_emoji(self):
        if self.count == 2:
            # Check if two emojis have been revealed
            if self.track[0][0] == self.track[1][0]:
                 # Check if the types of the two revealed emojis match
                self.score += 1
                if (
                    self.score == 8
                ):
                    self.result = "Congrats, you have matched all the emojis"
            else:
                # If the types do not match, hide the emojis again
                indices = [e[1][0] for e in self.track]
                self.emoji_list = [
                    [i,"0%"] if i in indices else [i,opacity]
                    for i,opacity in self.emoji_list
                ]
             # Reset the count and track for the next pair of emojis 
            self.count = 0
            self.track = []
        await asyncio.sleep(2)
        

class MemoryMatch:
    def __init__(self):
        self.stage: int = 2
        self.emoji: list = ["🎅","🎁","🥳","💃"]
        self.game_grid = xt.vstack(spacing = "15px")
        self.create_board()
    
    def create_board(self):
        # This will pair the emojis
        emojis = self.emoji[: self.stage * 2] * self.stage * 2
        random.shuffle(emojis)

        count = 0
        items = []
        for _ in range(self.stage * 2):
            row = xt.hstack(spacing = "15px")
            for __ in range(self.stage * 2):
                row.children.append(
                    xt.container(
                        xt.text(
                        emojis[count],
                        font_size = "32px",
                        cursor = "pointer",
                        transition="opacity 0.55s ease 0.35s",
                        opacity = State.emoji_list[count][1],
                        on_click = lambda: [
                            State.reveal_emoji(
                                State.emoji_list[count],
                                emojis[count],
                            ),
                            State.check_emoji(),
                        ],
                    ),
                    width = "58px",
                    height = "58px",
                    background="#1e293b",
                    border_radius = "6px",
                    center_content = True,
                    cursor = "pointer",
                  ),
                ),

                count += 1
            items.append(row)
        
        self.game_grid.children = items
        return self.game_grid

def index() -> xt.Component:
    '''Main UI components'''
    return xt.container(
       xt.vstack(
           xt.text(
               "Memory game with nextpy",
               font_size = "50px",
               font_weight = "bold",
               color = "black"
           ),
           xt.spacer(),
           game.game_grid,
           xt.spacer(),
           xt.button(
                "Reset Game",
                on_click=lambda:State.reset_game(),
                width="150px",
                height="40px",
                margin="15px",
                color_scheme = "teal",
                color="white",
                font_size="16px",
                cursor="pointer",
            ),
           xt.text(
               State.result,
               font_size = "25px",
               font_weight = "bold",
               color = "black"
           ),
           
           spacing = "25px",
       ),

       bg="#e0e0e0",
       height="100vh",
       max_width = "auto",
       display = "grid",
       position = "relative",
       overlay = "hidden",
       place_items = "center",
    )



# Add state and page to the app.
game = MemoryMatch()

app = xt.App()
app.add_page(index)
app.compile()
