import arcade
import os

Sprite_Scaling = 1.5

Screen_Width = 1300
Screen_Height = 600
Screen_Title = "Sprite Face Left or Right Example"

Movement_Speed = 2

Texture_Left = 0
Texture_Right = 1

class Player(arcade.Sprite):

    def __init__(self):
        super().__init__()

        texture = arcade.load_texture("C:/Users/maxwellc/Desktop/Python/Behemoth Brawl With Arcade/venv/Resources/Graphics/Heroes/Jack/Run/JackRun1.png", mirrored=True, scale=Sprite_Scaling)
        self.textures.append(texture)
        texture = arcade.load_texture("C:/Users/maxwellc/Desktop/Python/Behemoth Brawl With Arcade/venv/Resources/Graphics/Heroes/Jack/Run/JackRun1.png", scale=Sprite_Scaling)
        self.textures.append(texture)

        self.set_texture(Texture_Right)

    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y

        if self.change_x < 0:
            self.set_texture(Texture_Left)
        if self.change_x > 0:
            self.set_texture(Texture_Right)

        if self.left < 0:
            self.left = 0
        elif self.right > Screen_Width - 1:
            self.right = Screen_Width - 1

        if self.bottom < 0:
            self.bottom = 0
        elif self.top > Screen_Height - 1:
            self.top = Screen_Height - 1


class MyGame(arcade.Window):

    def __init__(self, width, height, title):

        super().__init__(width, height, title)

        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        self.all_sprites_list = None

        self.player_sprite = None

        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False

        arcade.set_background_color(arcade.color.AMAZON)

    def setup(self):

        self.all_sprites_list = arcade.SpriteList()

        self.player_sprite = arcade.AnimatedWalkingSprite()

        character_scale = 0.75
        self.player_sprite.stand_right_textures = []
        self.player_sprite.stand_right_textures.append(arcade.load_texture("C:/Users/maxwellc/Desktop/Python/Behemoth Brawl With Arcade/venv/Resources/Graphics/Heroes/Jack/Run/JackRun1.png",scale=character_scale))

        self.player_sprite.stand_left_textures = []
        self.player_sprite.stand_left_textures.append(arcade.load_texture("C:/Users/maxwellc/Desktop/Python/Behemoth Brawl With Arcade/venv/Resources/Graphics/Heroes/Jack/Run/JackRun1.png", scale=character_scale, mirrored=True))


        self.player_sprite.walk_right_textures = []

        self.player_sprite.walk_right_textures.append(arcade.load_texture("C:/Users/maxwellc/Desktop/Python/Behemoth Brawl With Arcade/venv/Resources/Graphics/Heroes/Jack/Run/JackRun1.png",
                                                                          scale=character_scale))
        self.player_sprite.walk_right_textures.append(arcade.load_texture("C:/Users/maxwellc/Desktop/Python/Behemoth Brawl With Arcade/venv/Resources/Graphics/Heroes/Jack/Run/JackRun2.png",
                                                                          scale=character_scale))
        self.player_sprite.walk_right_textures.append(arcade.load_texture("C:/Users/maxwellc/Desktop/Python/Behemoth Brawl With Arcade/venv/Resources/Graphics/Heroes/Jack/Run/JackRun3.png",
                                                                          scale=character_scale))
        self.player_sprite.walk_right_textures.append(arcade.load_texture("C:/Users/maxwellc/Desktop/Python/Behemoth Brawl With Arcade/venv/Resources/Graphics/Heroes/Jack/Run/JackRun4.png",
                                                                          scale=character_scale))
        self.player_sprite.walk_right_textures.append(arcade.load_texture("C:/Users/maxwellc/Desktop/Python/Behemoth Brawl With Arcade/venv/Resources/Graphics/Heroes/Jack/Run/JackRun5.png",
                                                                          scale=character_scale))
        self.player_sprite.walk_right_textures.append(arcade.load_texture("C:/Users/maxwellc/Desktop/Python/Behemoth Brawl With Arcade/venv/Resources/Graphics/Heroes/Jack/Run/JackRun6.png",
                                                                          scale=character_scale))
        self.player_sprite.walk_right_textures.append(arcade.load_texture("C:/Users/maxwellc/Desktop/Python/Behemoth Brawl With Arcade/venv/Resources/Graphics/Heroes/Jack/Run/JackRun7.png",
                                                                          scale=character_scale))
        self.player_sprite.walk_right_textures.append(arcade.load_texture("C:/Users/maxwellc/Desktop/Python/Behemoth Brawl With Arcade/venv/Resources/Graphics/Heroes/Jack/Run/JackRun8.png",
                                                                          scale=character_scale))

        self.player_sprite.walk_left_textures = []

        self.player_sprite.walk_right_textures.append(arcade.load_texture("C:/Users/maxwellc/Desktop/Python/Behemoth Brawl With Arcade/venv/Resources/Graphics/Heroes/Jack/Run/JackRun1.png",
                                                                          scale=character_scale, mirrored=True))
        self.player_sprite.walk_right_textures.append(arcade.load_texture("C:/Users/maxwellc/Desktop/Python/Behemoth Brawl With Arcade/venv/Resources/Graphics/Heroes/Jack/Run/JackRun2.png",
                                                                          scale=character_scale, mirrored=True))
        self.player_sprite.walk_right_textures.append(arcade.load_texture("C:/Users/maxwellc/Desktop/Python/Behemoth Brawl With Arcade/venv/Resources/Graphics/Heroes/Jack/Run/JackRun3.png",
                                                                          scale=character_scale, mirrored=True))
        self.player_sprite.walk_right_textures.append(arcade.load_texture("C:/Users/maxwellc/Desktop/Python/Behemoth Brawl With Arcade/venv/Resources/Graphics/Heroes/Jack/Run/JackRun4.png",
                                                                          scale=character_scale, mirrored=True))
        self.player_sprite.walk_right_textures.append(arcade.load_texture("C:/Users/maxwellc/Desktop/Python/Behemoth Brawl With Arcade/venv/Resources/Graphics/Heroes/Jack/Run/JackRun5.png",
                                                                          scale=character_scale, mirrored=True))
        self.player_sprite.walk_right_textures.append(arcade.load_texture("C:/Users/maxwellc/Desktop/Python/Behemoth Brawl With Arcade/venv/Resources/Graphics/Heroes/Jack/Run/JackRun6.png",
                                                                          scale=character_scale, mirrored=True))
        self.player_sprite.walk_right_textures.append(arcade.load_texture("C:/Users/maxwellc/Desktop/Python/Behemoth Brawl With Arcade/venv/Resources/Graphics/Heroes/Jack/Run/JackRun7.png",
                                                                          scale=character_scale, mirrored=True))
        self.player_sprite.walk_right_textures.append(arcade.load_texture("C:/Users/maxwellc/Desktop/Python/Behemoth Brawl With Arcade/venv/Resources/Graphics/Heroes/Jack/Run/JackRun8.png",
                                                                          scale=character_scale, mirrored=True))

        self.player_sprite.texture_change_distance = 50

        self.player_sprite = Player()
        self.player_sprite.center_x = Screen_Width / 2
        self.player_sprite.center_y = Screen_Height / 2
        self.player_sprite.scale=1.5

        self.all_sprites_list.append(self.player_sprite)

    def on_draw(self):

        arcade.start_render()

        self.all_sprites_list.draw()

    def update(self, delta_time):

        self.all_sprites_list.update()
        self.all_sprites_list.update_animation()

        self.player_sprite.change_x = 0
        self.player_sprite.change_y = 0

        if self.up_pressed and not self.down_pressed:
            self.player_sprite.change_y = Movement_Speed
        elif self.down_pressed and not self.up_pressed:
            self.player_sprite.change_y = -Movement_Speed
        if self.left_pressed and not self.right_pressed:
            self.player_sprite.change_x = -Movement_Speed
        elif self.right_pressed and not self.left_pressed:
            self.player_sprite.change_x = Movement_Speed

        self.all_sprites_list.update()

    def on_key_press(self, key, modifiers):

        if key == arcade.key.UP:
            self.up_pressed = True
        elif key == arcade.key.DOWN:
            self.down_pressed = True
        elif key == arcade.key.LEFT:
            self.left_pressed = True
        elif key == arcade.key.RIGHT:
            self.right_pressed = True

    def on_key_release(self, key, modifiers):

        if key == arcade.key.UP:
            self.up_pressed = False
        elif key == arcade.key.DOWN:
            self.down_pressed = False
        elif key == arcade.key.LEFT:
            self.left_pressed = False
        elif key == arcade.key.RIGHT:
            self.right_pressed = False


def main():
    window = MyGame(Screen_Width, Screen_Height, Screen_Title)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()