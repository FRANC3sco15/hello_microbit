input.onButtonPressed(Button.A, function on_button_pressed_a() {
    music.playMelody("G C C D E C B", 120)
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    music.playMelody("C B G A B C C", 120)
})
input.onGesture(Gesture.Shake, function on_gesture_shake() {
    music.playMelody("C C D E C E D", 120)
})
