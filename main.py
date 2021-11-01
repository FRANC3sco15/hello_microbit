def on_button_pressed_a():
    music.play_melody("G C C D E C B", 120)

def on_button_pressed_b():
    music.play_melody("C B G A B C C", 120)

def on_gesture_shake():
    music.play_melody("C C D E C E D", 120)

input.on_button_pressed(Button.A, on_button_pressed_a)
input.on_button_pressed(Button.B, on_button_pressed_b)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)
