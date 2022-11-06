@namespace
class SpriteKind:
    Mom = SpriteKind.create()
def Follow():
    pass

def on_up_pressed():
    animation.run_image_animation(mySprite,
        [img("""
                . . . . f f f f . . . . 
                        . . f f e e e e f f . . 
                        . f e e e e e e e f f . 
                        f f e f e e e e e e f f 
                        f f f e e e e e e e e f 
                        f f f e e e e e e f e f 
                        f f f f e e e e f f f f 
                        f f f f f f f f f f f f 
                        f f f f f f f f f f f f 
                        . f f f f f f f f f f . 
                        . e f f f f f f f f e . 
                        e 9 f 9 9 9 9 9 9 f 9 e 
                        4 d f 9 9 9 9 9 9 c d 4 
                        4 4 f 9 9 9 9 9 9 f 4 4 
                        . . . f f f f f f . . . 
                        . . . f f . . f f . . .
            """),
            img("""
                . . . . . . . . . . . . 
                        . . . . f f f f . . . . 
                        . . f f e e e e f f . . 
                        . f e e e e e e e f f . 
                        f e e f e e e e e e f f 
                        f f f e e e e e e e e f 
                        f f e e e e e e e f e f 
                        f f f e e e e f f f f f 
                        f f f f f f f f f f f f 
                        f f f f f f f f f f f f 
                        . f f f f f f f f f f . 
                        . e f f f f f f f f e . 
                        . 4 f 9 9 9 9 9 f e 9 e 
                        . 4 f 9 9 9 9 9 e d d 4 
                        . e f f f f f f e e 4 . 
                        . . f f f . . . . . . .
            """),
            img("""
                . . . . . . . . . . . . 
                        . . . . f f f f . . . . 
                        . . f f e e e e f f . . 
                        . f e e e e e e e f f . 
                        f f e f e e e e e e f f 
                        f f f e e e e e e e e f 
                        f f f f e e e e e f e f 
                        f f f f f e e e e f f f 
                        f f f f f f f f f f f f 
                        f f f f f f f f f f f f 
                        . f f f f f f f f f f . 
                        . e f f f f f f f f e . 
                        e 9 e f 9 9 9 9 9 f 4 . 
                        4 d d e 9 9 9 9 9 f 4 . 
                        . 4 e e f f f f f f e . 
                        . . . . . . . f f f . .
            """)],
        200,
        True)
controller.up.on_event(ControllerButtonEvent.PRESSED, on_up_pressed)

def on_overlap_tile(sprite, location):
    pause(500)
    controller.start_light_animation(light.running_lights_animation, 5000)
    tiles.set_current_tilemap(tilemap("""
        level3
    """))
    mySprite.set_position(14, 84)
    game.show_long_text("Tom must protect his family, he must go fight in the war.",
        DialogLayout.BOTTOM)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile
    """),
    on_overlap_tile)

def on_down_released():
    animation.stop_animation(animation.AnimationTypes.ALL, mySprite)
controller.down.on_event(ControllerButtonEvent.RELEASED, on_down_released)

def on_overlap_tile2(sprite2, location2):
    tiles.set_current_tilemap(tilemap("""
        level3
    """))
    mySprite.set_position(121, 5)
    mySprite3.destroy()
scene.on_overlap_tile(SpriteKind.player,
    sprites.dungeon.floor_dark0,
    on_overlap_tile2)

def on_left_pressed():
    animation.run_image_animation(mySprite,
        [img("""
                . . . f f f f f . . . . 
                        . . f e e e e e f f . . 
                        . f e e e e e e e f f . 
                        f e e e e e e e f f f f 
                        f e e 4 e e e f f f f f 
                        f e e 4 4 e e e f f f f 
                        f f e 4 4 4 4 4 f f f f 
                        f f e 4 4 f f 4 e 4 f f 
                        . f f 4 4 4 4 4 4 4 f . 
                        . . f b b 4 4 4 f f f . 
                        . . f e 4 4 4 e e f . . 
                        . . f 9 9 9 e 9 9 4 . . 
                        . . f 9 9 9 e 4 4 e . . 
                        . . f 9 9 9 f e e f . . 
                        . . . f f f f f f . . . 
                        . . . . . f f f . . . .
            """),
            img("""
                . . . . . . . . . . . . 
                        . . . f f f f f f . . . 
                        . . f e e e e e f f f . 
                        . f e e e e e e e f f f 
                        f e e e e e e e f f f f 
                        f e e 4 e e e f f f f f 
                        f e e 4 4 e e e f f f f 
                        f f e 4 4 4 4 4 f f f f 
                        . f e 4 4 f f 4 e 4 f f 
                        . . f 4 4 4 4 4 4 4 f . 
                        . . f b b 4 e e f f f . 
                        . . f e 4 e 9 9 4 f . . 
                        . . f 9 9 e 4 4 e f . . 
                        . f f 9 9 f e e f f f . 
                        . f f f f f f f f f f . 
                        . . f f f . . . f f . .
            """),
            img("""
                . . . . . . . . . . . . 
                        . . . f f f f f f . . . 
                        . . f e e e e e f f f . 
                        . f e e e e e e e f f f 
                        f e e e e e e e f f f f 
                        f e e 4 e e e f f f f f 
                        f e e 4 4 e e e f f f f 
                        f f e 4 4 4 4 4 f f f f 
                        . f e 4 4 f f 4 e 4 f f 
                        . . f 4 4 4 4 4 4 4 f f 
                        . . f b b 4 4 4 f f f . 
                        . . f e 4 4 4 e 9 9 4 . 
                        . . f 9 9 9 9 e 4 4 e . 
                        . f f 9 9 9 9 f e e f . 
                        . f f f f f f f f f f . 
                        . . f f f . . . f f . .
            """)],
        200,
        True)
controller.left.on_event(ControllerButtonEvent.PRESSED, on_left_pressed)

def on_overlap_tile3(sprite3, location3):
    mySprite.set_position(92, 39)
    tiles.set_current_tilemap(tilemap("""
        level5
    """))
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile3
    """),
    on_overlap_tile3)

def on_right_released():
    animation.stop_animation(animation.AnimationTypes.ALL, mySprite)
controller.right.on_event(ControllerButtonEvent.RELEASED, on_right_released)

def on_left_released():
    animation.stop_animation(animation.AnimationTypes.ALL, mySprite)
controller.left.on_event(ControllerButtonEvent.RELEASED, on_left_released)

def on_overlap_tile4(sprite4, location4):
    tiles.set_current_tilemap(tilemap("""
        level2
    """))
    game.show_long_text("Found a key.", DialogLayout.BOTTOM)
scene.on_overlap_tile(SpriteKind.player,
    sprites.dungeon.chest_closed,
    on_overlap_tile4)

def on_right_pressed():
    animation.run_image_animation(mySprite,
        [img("""
                . . . . . . . . . . . . 
                        . . . f f f f f f . . . 
                        . f f f e e e e e f . . 
                        f f f e e e e e e e f . 
                        f f f f e e e e e e e f 
                        f f f f f e e e 4 e e f 
                        f f f f e e e 4 4 e e f 
                        f f f f 4 4 4 4 4 e f f 
                        f f 4 e 4 f f 4 4 e f . 
                        f f 4 4 4 4 4 4 4 f . . 
                        . f f f 4 4 4 b b f . . 
                        . 4 9 9 e 4 4 4 e f . . 
                        . e 4 4 e 9 9 9 9 f . . 
                        . f e e f 9 9 9 9 f f . 
                        . f f f f f f f f f f . 
                        . . f f . . . f f f . .
            """),
            img("""
                . . . . . . . . . . . . 
                        . . . f f f f f f . . . 
                        . f f f e e e e e f . . 
                        f f f e e e e e e e f . 
                        f f f f e e e e e e e f 
                        f f f f f e e e 4 e e f 
                        f f f f e e e 4 4 e e f 
                        f f f f 4 4 4 4 4 e f f 
                        f f 4 e 4 f f 4 4 e f . 
                        . f 4 4 4 4 4 4 4 f . . 
                        . f f f e e 4 b b f . . 
                        . . f 4 9 9 e 4 e f . . 
                        . . f e 4 4 e 9 9 f . . 
                        . f f f e e f 9 9 f f . 
                        . f f f f f f f f f f . 
                        . . f f . . . f f f . .
            """),
            img("""
                . . . . f f f f f . . . 
                        . . f f e e e e e f . . 
                        . f f e e e e e e e f . 
                        f f f f e e e e e e e f 
                        f f f f f e e e 4 e e f 
                        f f f f e e e 4 4 e e f 
                        f f f f 4 4 4 4 4 e f f 
                        f f 4 e 4 f f 4 4 e f f 
                        . f 4 4 4 4 4 4 4 f f . 
                        . f f f 4 4 4 b b f . . 
                        . . f e e 4 4 4 e f . . 
                        . . 4 9 9 e 9 9 9 f . . 
                        . . e 4 4 e 9 9 9 f . . 
                        . . f e e f 9 9 9 f . . 
                        . . . f f f f f f . . . 
                        . . . . f f f . . . . .
            """)],
        200,
        True)
controller.right.on_event(ControllerButtonEvent.PRESSED, on_right_pressed)

def on_on_overlap(sprite5, otherSprite):
    mySprite3.say_text("Please come back safely! (sniff sniff) please! (cry cry)",
        3000,
        False)
    pause(3001)
    mySprite.say_text("I will, I promise.", 2500, False)
sprites.on_overlap(SpriteKind.player, SpriteKind.Mom, on_on_overlap)

def on_up_released():
    animation.stop_animation(animation.AnimationTypes.ALL, mySprite)
controller.up.on_event(ControllerButtonEvent.RELEASED, on_up_released)

def on_down_pressed():
    animation.run_image_animation(mySprite,
        [img("""
                . . . . f f f f . . . . 
                        . . f f e e e e f f . . 
                        . f f e e e e e e f f . 
                        f f f f 4 e e e f f f f 
                        f f f 4 4 4 e e f f f f 
                        f f f 4 4 4 4 e e f f f 
                        f 4 e 4 4 4 4 4 4 e 4 f 
                        f 4 4 f f 4 4 f f 4 4 f 
                        f e 4 4 4 4 4 4 4 4 e f 
                        . f e 4 4 b b 4 4 e f . 
                        . f f e 4 4 4 4 e f f . 
                        e 9 f 9 9 9 9 9 9 f 9 e 
                        4 d f 9 9 9 9 9 9 f d 4 
                        4 4 f 9 9 9 9 9 9 f 4 4 
                        . . . f f f f f f . . . 
                        . . . f f . . f f . . .
            """),
            img("""
                . . . . . . . . . . . . 
                        . . . f f f f f f . . . 
                        . f f f e e e e f f f . 
                        f f f e e e e e e f f f 
                        f f f f 4 e e e f f f f 
                        f f f 4 4 4 e e f f f f 
                        f f f 4 4 4 4 e e f f f 
                        f 4 e 4 4 4 4 4 4 e 4 f 
                        f 4 4 f f 4 4 f f 4 4 f 
                        f e 4 4 4 4 4 4 4 4 e f 
                        . f e 4 4 b b 4 4 e f e 
                        f f f e 4 4 4 4 d d 9 e 
                        e 9 f b 9 9 9 e d d e . 
                        . . f 9 9 9 9 f e e . . 
                        . . f f f f f f f . . . 
                        . . f f f . . . . . . .
            """),
            img("""
                . . . . . . . . . . . . 
                        . . . f f f f f f . . . 
                        . f f f e e e e f f f . 
                        f f f e e e e e e f f f 
                        f f f f 4 e e e f f f f 
                        f f f 4 4 4 e e f f f f 
                        f f f 4 4 4 4 e e f f f 
                        f 4 e 4 4 4 4 4 4 e 4 f 
                        f 4 4 f f 4 4 f f 4 4 f 
                        f e 4 4 4 4 4 4 4 4 e f 
                        e f e 4 4 b b 4 4 e f . 
                        e 9 d d 4 4 4 4 e f f f 
                        . e d d e 1 1 1 b f 9 e 
                        . . e e f 6 6 6 6 f . . 
                        . . . f f f f f f f . . 
                        . . . . . . . f f f . .
            """)],
        200,
        True)
controller.down.on_event(ControllerButtonEvent.PRESSED, on_down_pressed)

def on_life_zero():
    game.over(False, effects.splatter)
    music.wawawawaa.play()
    game.reset()
info.on_life_zero(on_life_zero)

def on_player2_life_zero():
    pass
info.player2.on_life_zero(on_player2_life_zero)

def on_player2_connected():
    global mySprite2
    mySprite2 = sprites.create(img("""
            . . 4 4 4 . . . . 4 4 4 . . . . 
                    . 4 5 5 5 e . . e 5 5 5 4 . . . 
                    4 5 5 5 5 5 e e 5 5 5 5 5 4 . . 
                    4 5 5 4 4 5 5 5 5 4 4 5 5 4 . . 
                    e 5 4 4 5 5 5 5 5 5 4 4 5 e . . 
                    . e e 5 5 5 5 5 5 5 5 e e . . . 
                    . . e 5 f 5 5 5 5 f 5 e . . . . 
                    . . f 5 5 5 4 4 5 5 5 f . . f f 
                    . . f 4 5 5 f f 5 5 6 f . f 5 f 
                    . . . f 6 6 6 6 6 6 4 4 f 5 5 f 
                    . . . f 4 5 5 5 5 5 5 4 4 5 f . 
                    . . . f 5 5 5 5 5 4 5 5 f f . . 
                    . . . f 5 f f f 5 f f 5 f . . . 
                    . . . f f . . f f . . f f . . .
        """),
        SpriteKind.player)
    controller.player2.move_sprite(mySprite)
controller.player2.on_event(ControllerEvent.CONNECTED, on_player2_connected)

def on_overlap_tile5(sprite6, location5):
    global mySprite3
    tiles.set_current_tilemap(tilemap("""
        level4
    """))
    mySprite.set_position(75, 111)
    mySprite3 = sprites.create(img("""
            . . . . . f f f f f . . . . 
                    . . . f f e e e e f f . . . 
                    . f f f b e e e e e e f . . 
                    f e e e 5 e e e e e e f . . 
                    f e 5 5 e e e e e e e e f . 
                    f e f f e e e e e 4 e e f . 
                    f e f f f e e e 4 4 e f f . 
                    f e f 4 4 f b f 4 4 e f f . 
                    . f f 4 4 4 1 f 4 4 f f . . 
                    . . f f f 4 4 4 2 2 f . . . 
                    . . . f e e 4 4 4 e f . . . 
                    . . . 4 c c e c c c f . . . 
                    . . . e c c e c c c f . . . 
                    . . . f e e f c c c f . . . 
                    . . . . f f f f f f . . . . 
                    . . . . . f f f . . . . . .
        """),
        SpriteKind.Mom)
    mySprite3.set_position(123, 61)
scene.on_overlap_tile(SpriteKind.player,
    sprites.dungeon.floor_mixed,
    on_overlap_tile5)

mySprite2: Sprite = None
mySprite3: Sprite = None
mySprite: Sprite = None
mySprite = sprites.create(img("""
        . . . . f f f f . . . . 
            . . f f e e e e f f . . 
            . f f e e e e e e f f . 
            f f f f 4 e e e f f f f 
            f f f 4 4 4 e e f f f f 
            f f f 4 4 4 4 e e f f f 
            f 4 e 4 4 4 4 4 4 e 4 f 
            f 4 4 f f 4 4 f f 4 4 f 
            f e 4 4 4 4 4 4 4 4 e f 
            . f e 4 4 b b 4 4 e f . 
            . f f e 4 4 4 4 e f f . 
            e 4 f b 9 9 9 9 b f 4 e 
            4 d f 9 9 9 9 9 9 f d 4 
            4 4 f 9 9 9 9 9 9 f 4 4 
            . . . f f f f f f . . . 
            . . . f f . . f f . . .
    """),
    SpriteKind.player)
controller.move_sprite(mySprite, 100, 100)
game.splash("This is an adventure about a boy named Tom.")
scene.camera_follow_sprite(mySprite)
tiles.set_current_tilemap(tilemap("""
    level1
"""))
mySprite.set_position(69, 59)
info.set_life(3)
info.set_score(0)

def on_forever():
    music.play_melody("C D E D C D E D ", 120)
forever(on_forever)
