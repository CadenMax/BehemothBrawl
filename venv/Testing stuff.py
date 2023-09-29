import arcade
import random
import os

SCREEN_WIDTH = 1300
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Move with a Sprite Animation Example"

MOVEMENT_SPEED = 2


class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height, title):
        """
        Initializer
        """
        super().__init__(width, height, title)

        # Sprite lists
        self.player_list = None
        self.coin_list = None

        # Set up the player
        self.score = 0
        self.player = None

        arcade.set_background_color(arcade.color.AMAZON)

    def setup(self):
        self.player_list = arcade.SpriteList()

        # Set up the player
        self.player = arcade.AnimatedWalkingSprite()

        character_scale = 5
        self.player.stand_right_textures = []
        self.player.stand_right_textures.append(arcade.load_texture("C:/Users/maxwellc/Desktop/Python/Behemoth Brawl With Arcade/venv/Resources/Graphics/Heroes/Jack/idle.gif",
                                                                    scale=character_scale))
        self.player.stand_left_textures = []
        self.player.stand_left_textures.append(arcade.load_texture("C:/Users/maxwellc/Desktop/Python/Behemoth Brawl With Arcade/venv/Resources/Graphics/Heroes/Jack/idle.gif",
                                                                   scale=character_scale, mirrored=True))

        self.player.walk_right_textures = []

        self.player.walk_right_textures.append(arcade.load_texture("C:/Users/maxwellc/Desktop/Python/Behemoth Brawl With Arcade/venv/Resources/Graphics/Heroes/Jack/Run/JackRun1.png",
                                                                   scale=character_scale))
        self.player.walk_right_textures.append(arcade.load_texture("C:/Users/maxwellc/Desktop/Python/Behemoth Brawl With Arcade/venv/Resources/Graphics/Heroes/Jack/Run/JackRun2.png",
                                                                   scale=character_scale))
        self.player.walk_right_textures.append(arcade.load_texture("C:/Users/maxwellc/Desktop/Python/Behemoth Brawl With Arcade/venv/Resources/Graphics/Heroes/Jack/Run/JackRun3.png",
                                                                   scale=character_scale))
        self.player.walk_right_textures.append(arcade.load_texture("C:/Users/maxwellc/Desktop/Python/Behemoth Brawl With Arcade/venv/Resources/Graphics/Heroes/Jack/Run/JackRun4.png",
                                                                   scale=character_scale))

        self.player.walk_left_textures = []

        self.player.walk_left_textures.append(arcade.load_texture("C:/Users/maxwellc/Desktop/Python/Behemoth Brawl With Arcade/venv/Resources/Graphics/Heroes/Jack/Run/JackRun1.png",
                                                                  scale=character_scale, mirrored=True))
        self.player.walk_left_textures.append(arcade.load_texture("C:/Users/maxwellc/Desktop/Python/Behemoth Brawl With Arcade/venv/Resources/Graphics/Heroes/Jack/Run/JackRun2.png",
                                                                  scale=character_scale, mirrored=True))
        self.player.walk_left_textures.append(arcade.load_texture("C:/Users/maxwellc/Desktop/Python/Behemoth Brawl With Arcade/venv/Resources/Graphics/Heroes/Jack/Run/JackRun3.png",
                                                                  scale=character_scale, mirrored=True))
        self.player.walk_left_textures.append(arcade.load_texture("C:/Users/maxwellc/Desktop/Python/Behemoth Brawl With Arcade/venv/Resources/Graphics/Heroes/Jack/Run/JackRun4.png",
                                                                  scale=character_scale, mirrored=True))

        self.player.texture_change_distance = 20

        self.player.center_x = SCREEN_WIDTH // 2
        self.player.center_y = SCREEN_HEIGHT // 2
        self.player.scale = 1

        self.player_list.append(self.player)

    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        arcade.start_render()

        # Draw all the sprites.
        self.player_list.draw()

        # Put the text on the screen.

    def on_key_press(self, key, modifiers):
        """
        Called whenever the mouse moves.
        """
        if key == arcade.key.UP:
            self.player.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.player.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.player.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player.change_x = MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """
        Called when the user presses a mouse button.
        """
        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player.change_x = 0

    def update(self, delta_time):
        self.player_list.update()
        self.player_list.update_animation()

def main():
    """ Main method """
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()