namespace SpriteKind {
    export const Mom = SpriteKind.create()
}
function Follow () {
	
}
controller.up.onEvent(ControllerButtonEvent.Pressed, function () {
    animation.runImageAnimation(
    mySprite,
    [img`
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
        `,img`
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
        `,img`
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
        `],
    200,
    true
    )
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`myTile`, function (sprite, location) {
    pause(500)
    controller.startLightAnimation(light.runningLightsAnimation, 5000)
    tiles.setCurrentTilemap(tilemap`level3`)
    mySprite.setPosition(14, 84)
    game.showLongText("Tom must protect his family, he must go fight in the war.", DialogLayout.Bottom)
})
controller.down.onEvent(ControllerButtonEvent.Released, function () {
    animation.stopAnimation(animation.AnimationTypes.All, mySprite)
})
scene.onOverlapTile(SpriteKind.Player, sprites.dungeon.floorDark0, function (sprite, location) {
    tiles.setCurrentTilemap(tilemap`level3`)
    mySprite.setPosition(121, 5)
    mySprite3.destroy()
})
controller.left.onEvent(ControllerButtonEvent.Pressed, function () {
    animation.runImageAnimation(
    mySprite,
    [img`
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
        `,img`
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
        `,img`
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
        `],
    200,
    true
    )
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`myTile3`, function (sprite, location) {
    mySprite.setPosition(92, 39)
    tiles.setCurrentTilemap(tilemap`level5`)
})
controller.right.onEvent(ControllerButtonEvent.Released, function () {
    animation.stopAnimation(animation.AnimationTypes.All, mySprite)
})
controller.left.onEvent(ControllerButtonEvent.Released, function () {
    animation.stopAnimation(animation.AnimationTypes.All, mySprite)
})
scene.onOverlapTile(SpriteKind.Player, sprites.dungeon.chestClosed, function (sprite, location) {
    tiles.setCurrentTilemap(tilemap`level2`)
    game.showLongText("Found a key.", DialogLayout.Bottom)
})
controller.right.onEvent(ControllerButtonEvent.Pressed, function () {
    animation.runImageAnimation(
    mySprite,
    [img`
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
        `,img`
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
        `,img`
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
        `],
    200,
    true
    )
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Mom, function (sprite, otherSprite) {
    mySprite3.sayText("Please come back safely! (sniff sniff) please! (cry cry)", 3000, false)
    pause(3001)
    mySprite.sayText("I will, I promise.", 2500, false)
})
controller.up.onEvent(ControllerButtonEvent.Released, function () {
    animation.stopAnimation(animation.AnimationTypes.All, mySprite)
})
controller.down.onEvent(ControllerButtonEvent.Pressed, function () {
    animation.runImageAnimation(
    mySprite,
    [img`
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
        `,img`
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
        `,img`
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
        `],
    200,
    true
    )
})
info.onLifeZero(function () {
    game.over(false, effects.splatter)
    music.wawawawaa.play()
    game.reset()
})
info.player2.onLifeZero(function () {
	
})
controller.player2.onEvent(ControllerEvent.Connected, function () {
    mySprite2 = sprites.create(img`
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
        `, SpriteKind.Player)
    controller.player2.moveSprite(mySprite)
})
scene.onOverlapTile(SpriteKind.Player, sprites.dungeon.floorMixed, function (sprite, location) {
    tiles.setCurrentTilemap(tilemap`level4`)
    mySprite.setPosition(75, 111)
    mySprite3 = sprites.create(img`
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
        `, SpriteKind.Mom)
    mySprite3.setPosition(123, 61)
})
let mySprite2: Sprite = null
let mySprite3: Sprite = null
let mySprite: Sprite = null
mySprite = sprites.create(img`
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
    `, SpriteKind.Player)
controller.moveSprite(mySprite, 100, 100)
game.splash("This is an adventure about a boy named Tom.")
scene.cameraFollowSprite(mySprite)
tiles.setCurrentTilemap(tilemap`level1`)
mySprite.setPosition(69, 59)
info.setLife(3)
info.setScore(0)
forever(function () {
    music.playMelody("C D E D C D E D ", 120)
})
