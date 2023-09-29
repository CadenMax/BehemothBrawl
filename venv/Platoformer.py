import arcade
import tkinter as tk

root = tk.Tk()

Screen_Width = root.winfo_screenwidth()
Screen_Height = root.winfo_screenheight()
Screen_Title = "Behemoth Brawl"

Character_Scaling = 1
Tile_Scaling = 0.5

Movement_Speed = 5
Gravity = 1
Jump_Speed = 15

class MyGame(arcade.Window):


    def __init__(self):

        super().__init__(Screen_Width, Screen_Height, Screen_Title)

        self.wall_list = None
        self.player_list = None

        self.player_sprite = None

        self.physics_engine = None

        self.health = 0

        arcade.set_background_color(arcade.color.CORNFLOWER_BLUE)

    def setup(self):

        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()

        self.player_sprite = arcade.Sprite("Resources\Graphics\Heroes\Jack\idle.png", Character_Scaling)
        self.player_sprite.center_x = 512
        self.player_sprite.center_y = 96
        self.player_list.append(self.player_sprite)

        self.health = 0

        for x in range(0, 1250, 64):
            wall = arcade.Sprite("Resources\Graphics\Arenas\Stadium\Strucutre Platofrm.png", Tile_Scaling)
            wall.center_x = x
            wall.center_y = 32
            self.wall_list.append(wall)

        coordinate_list = [[512, 96],
                           [256, 96],
                           [768, 96]]

        for coordinate in coordinate_list:
            wall = arcade.Sprite("Resources\Graphics\Arenas\Stadium\Strucutre Platofrm.png", Tile_Scaling)
            wall.position = coordinate
            self.wall_list.append(wall)

        self.physics_engine = arcade.PhysicsEnginePlatformer(self.player_sprite, self.wall_list, Gravity)

    def on_draw(self):

        arcade.start_render()

        self.wall_list.draw()
        self.player_list.draw()

        health_display = f"P1 Health: {self.health}"
        arcade.draw_text(health_display, 1, 750, arcade.color.WHITE, 18)

    def on_key_press(self, key, modifiers):
        if key == arcade.key.W:
            if self.physics_engine.can_jump():
                self.player_sprite.change_y = Jump_Speed
        elif key == arcade.key.A:
            self.player_sprite.change_x = -Movement_Speed
        elif key == arcade.key.D:
            self.player_sprite.change_x = Movement_Speed

    def on_key_release(self, key, modifiers):
        if key == arcade.key.A:
            self.player_sprite.change_x = 0
        elif key == arcade.key.D:
            self.player_sprite.change_x = 0

    def update(self, delta_time):

        self.physics_engine.update()

def main():
    window = MyGame()
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()
