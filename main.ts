input.onButtonPressed(Button.A, function on_button_pressed_a() {
    basic.showIcon(IconNames.Heart)
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    basic.showIcon(IconNames.Skull)
})
input.onGesture(Gesture.Shake, function on_gesture_shake() {
    basic.showString("FRAN")
})
