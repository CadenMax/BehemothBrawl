import wx

app = wx.App(False)
ScreenWidth, ScreenHeight = wx.GetDisplaySize()

ScreenTitle = "Behemoth Brawl"
WinGame = "You have Won!\nThe game will close."
DeadGame= "Bad luck, you've been got\n The game will close."

CharacterScaling = 1
TileScaling = 0.5
SpritePixelSize = 128
GridPixelSize = (SpritePixelSize * TileScaling)

MovementSpeed = 3
Gravity = 0.9
JumpSpeed = 15
SpriteSpeed = 2
BulletSpeed = 5

LeftViewpointMargin = 200
RightViewpointMargin = 200
BottomViewpointMargin = 150
TopViewpointMargin = 100

PlayerStartX = 512
PlayerStartY = 400

TextureRight = 1
TextureLeft = 0

InstructionText = "Welcome to Behemoth Brawl! Below are the keybindings to play the game\nW=Jump\nA=Move Left\n" \
                  "D=Move Right\nC=Shoot\nThe objective of the game is to deplete the enemy aliens health to 0.\n" \
                  "Double jump and shoot your way around making sure not to get hit by the aliens goop.\n" \
                  "If your health depletes to 0, you've been got and will have to re-open the game after it closes.\n" \
                  "If you deplete the Aliens health to 0, the game will close and you have won."

Player1Text = "Player 1"
