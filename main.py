
def on_button_pressed_a():
    basic.show_icon(IconNames.HEART)

def on_button_pressed_b():
    basic.show_icon(IconNames.SKULL)

def on_gesture_shake():
    basic.show_string("FRAN")

input.on_button_pressed(Button.A, on_button_pressed_a)
input.on_button_pressed(Button.B, on_button_pressed_b)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)
