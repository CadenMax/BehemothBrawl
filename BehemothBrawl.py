import arcade
import random
import math
from Variables import *



class Enemy(arcade.Sprite):

    def follow_sprite(self, player_sprite):
        self.center_x += self.change_x
        self.center_y += self.change_y

        if random.randrange(100) == 0:
            start_x = self.center_x
            start_y = self.center_y

            dest_x = player_sprite.center_x
            dest_y = player_sprite.center_y

            x_diff = dest_x - start_x
            y_diff = dest_y - start_y
            angle = math.atan2(y_diff, x_diff)

            self.change_x = math.cos(angle) * SpriteSpeed
            self.change_y = math.sin(angle) * SpriteSpeed


class MyGame(arcade.Window):

    def __init__(self):
        super().__init__(ScreenWidth, ScreenHeight, ScreenTitle, fullscreen=True)

    def setup(self):

        self.left_pressed = False
        self.right_pressed = False
        self.down_pressed = False

        self.player_list = arcade.SpriteList()
        self.player = arcade.AnimatedWalkingSprite()

        self.health = 100
        self.lives = 3

        self.EnemyHealth = 200

        self.player.stand_right_textures = []
        self.player.stand_right_textures.append(arcade.load_texture("Graphics/Black Sparrow/Black Sparrow Idle.png"))

        self.player.stand_left_textures = []
        self.player.stand_left_textures.append(
            arcade.load_texture("Graphics/Black Sparrow/Black Sparrow Idle.png", mirrored=True))

        self.player.walk_right_textures = []
        self.player.walk_right_textures.append(
            arcade.load_texture("Graphics/Black Sparrow/Walk/Black Sparrow Walk1.png"))
        self.player.walk_right_textures.append(
            arcade.load_texture("Graphics/Black Sparrow/Walk/Black Sparrow Walk2.png"))
        self.player.walk_right_textures.append(
            arcade.load_texture("Graphics/Black Sparrow/Walk/Black Sparrow Walk3.png"))
        self.player.walk_right_textures.append(
            arcade.load_texture("Graphics/Black Sparrow/Walk/Black Sparrow Walk4.png"))

        self.player.walk_left_textures = []
        self.player.walk_left_textures.append(
            arcade.load_texture("Graphics/Black Sparrow/Walk/Black Sparrow Walk1.png", mirrored=True))
        self.player.walk_left_textures.append(
            arcade.load_texture("Graphics/Black Sparrow/Walk/Black Sparrow Walk2.png", mirrored=True))
        self.player.walk_left_textures.append(
            arcade.load_texture("Graphics/Black Sparrow/Walk/Black Sparrow Walk3.png", mirrored=True))
        self.player.walk_left_textures.append(
            arcade.load_texture("Graphics/Black Sparrow/Walk/Black Sparrow Walk4.png", mirrored=True))

        self.player.center_x = ScreenWidth // 4
        self.player.center_y = ScreenHeight // 2.5
        self.player.scale = 1

        self.enemy_list = arcade.SpriteList()
        self.EnemyBullet_list = arcade.SpriteList()
        self.FriendlyBullet_list = arcade.SpriteList()

        self.enemy = Enemy("Graphics/Jeffery/Jeffery idle.png", 2)
        self.enemy.center_x = ScreenWidth // 1.2
        self.enemy.center_y = ScreenHeight // 2.5
        self.enemy.angle = 0
        self.enemy_list.append(self.enemy)

        self.EnemyBullet = arcade.Sprite("Graphics/Weapons/Laser Pew/Laser Pew Goop.png", 2.5)
        self.FriendlyBullet = arcade.Sprite("Graphics/Weapons/Laser Pew/Laser Pew Goop Good.png", 2)

        self.player_list.append(self.player)

        self.player.texture_change_distance = 20

        ConstructionMap = 'Forest.tmx'

        ConstructionLayerName = 'Platform'

        my_map = arcade.read_tiled_map(ConstructionMap, TileScaling)

        map_array = my_map.layers_int_data[ConstructionLayerName]

        self.end_of_map = len(map_array[0]) * GridPixelSize

        self.WallList = arcade.generate_sprites(my_map, ConstructionLayerName, TileScaling)

        self.physics_engine = arcade.PhysicsEnginePlatformer(self.player, self.WallList, Gravity)

        self.physics_engine.enable_multi_jump(3)

        self.Background = arcade.load_texture('Graphics/BG/Forest.png')

    def on_draw(self):

        arcade.start_render()

        arcade.draw_texture_rectangle(ScreenWidth // 2, ScreenHeight // 2, ScreenWidth, ScreenHeight, self.Background)

        self.WallList.draw()
        self.FriendlyBullet_list.draw()
        self.player_list.draw()
        self.EnemyBullet_list.draw()
        self.enemy_list.draw()

        HealthDisplay = f'Health: {self.health}'
        arcade.draw_text(HealthDisplay, 1, ScreenHeight - 20, arcade.color.WHITE, 18)

        Lives = f'Lives: {self.lives}'
        arcade.draw_text(Lives, 1, ScreenHeight - 40, arcade.color.WHITE, 18)

        self.EnemyHealthText = f'Health: {self.EnemyHealth}'
        arcade.draw_text(self.EnemyHealthText, self.enemy.center_x - 20, self.enemy.center_y + 20,
                         arcade.color.BLACK, 10)

    def on_key_press(self, key, modifiers):
        if key == arcade.key.W:
            if self.physics_engine.can_jump():
                self.physics_engine.increment_jump_counter()
                self.player.change_y = JumpSpeed
        elif key == arcade.key.S:
            self.down_pressed = True
        if key == arcade.key.A:
            self.left_pressed = True
        elif key == arcade.key.D:
            self.right_pressed = True
        if key == arcade.key.C:
            goodstart_x = self.player.center_x
            goodstart_y = self.player.center_y
            self.FriendlyBullet.center_x = goodstart_x
            self.FriendlyBullet.center_y = goodstart_y

            dest_x = self.enemy.center_x
            dest_y = self.enemy.center_y

            goodx_diff = dest_x - goodstart_x
            goody_diff = dest_y - goodstart_y
            goodangle = math.atan2(goody_diff, goodx_diff)
            self.FriendlyBullet.angle = math.degrees(goodangle)

            self.FriendlyBullet.change_x = math.cos(goodangle) * BulletSpeed
            self.FriendlyBullet.change_y = math.sin(goodangle) * BulletSpeed
            self.FriendlyBullet_list.append(self.FriendlyBullet)
        if key == arcade.key.F:
            self.set_fullscreen(not self.fullscreen)

    def on_key_release(self, key, modifiers):
        if key == arcade.key.A:
            self.left_pressed = False
        elif key == arcade.key.D:
            self.right_pressed = False

    def update(self, delta_time):

        self.player.change_x = 0

        if self.left_pressed and not self.right_pressed:
            self.player.change_x = -MovementSpeed
        elif self.right_pressed and not self.left_pressed:
            self.player.change_x = MovementSpeed

        start_x = self.enemy.center_x
        start_y = self.enemy.center_y

        dest_x = self.player.center_x
        dest_y = self.player.center_y

        x_diff = dest_x - start_x
        y_diff = dest_y - start_y
        angle = math.atan2(y_diff, x_diff)

        for enemy in self.enemy_list:

            if random.randrange(50) == 0:
                self.EnemyBullet = arcade.Sprite("Graphics/Weapons/Laser Pew/Laser Pew Goop.png", 2)
                self.EnemyBullet.center_x = enemy.center_x
                self.EnemyBullet.angle = -90
                self.EnemyBullet.top = enemy.bottom
                self.EnemyBullet.change_y = -2
                self.EnemyBullet_list.append(self.EnemyBullet)

        self.EnemyBullet.angle = math.degrees(angle)

        self.EnemyBullet.change_x = math.cos(angle) * BulletSpeed
        self.EnemyBullet.change_y = math.sin(angle) * BulletSpeed

        self.FriendlyBullet_list.update()

        for self.FriendlyBullet in self.FriendlyBullet_list:
            goodhit_list = arcade.check_for_collision_with_list(self.FriendlyBullet, self.enemy_list)

            if len(goodhit_list) > 0:
                self.EnemyHealth -= 10
                self.FriendlyBullet.kill()

        if self.FriendlyBullet.bottom > self.width or self.FriendlyBullet.top < 0 or self.FriendlyBullet.right < 0 or \
                self.FriendlyBullet.left > self.width:
            self.FriendlyBullet.kill()

        if self.EnemyBullet.bottom > self.width or self.EnemyBullet.top < 0 or self.EnemyBullet.right < 0 or \
                self.EnemyBullet.left > self.width:
            self.EnemyBullet.kill()

        self.EnemyBullet.center_x = start_x
        self.EnemyBullet.center_y = start_y

        for self.EnemyBullet in self.EnemyBullet_list:
            if self.EnemyBullet.top < 0:
                self.EnemyBullet.kill()
            hit_list = arcade.check_for_collision_with_list(self.EnemyBullet, self.player_list)
            if len(hit_list) > 0:
                self.health -= 50
                self.EnemyBullet.kill()

        for enemy in self.enemy_list:
            enemy.follow_sprite(self.player)

        self.EnemyBullet_list.update()

        if self.player.center_y < -100:
            self.player.center_x = PlayerStartX
            self.player.center_y = PlayerStartY
            self.lives -= 1

        if self.player.center_x < -100 or self.player.center_x > ScreenWidth + 100:
            self.player.center_x = PlayerStartX
            self.player.center_y = PlayerStartY
            self.lives -= 1

        if self.health <= 0:
            self.lives -= 1
            self.health = 100
            self.player.center_x = PlayerStartX
            self.player.center_y = PlayerStartY

        if self.EnemyHealth <= 0:
            self.enemy.kill()
            self.EnemyBullet.kill()
            exit()

        if self.lives <= 0:
            self.player.center_x = PlayerStartX
            self.player.center_y = PlayerStartY
            exit()

        self.physics_engine.update()
        self.player_list.update_animation()


def main():
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
