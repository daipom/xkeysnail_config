import re
from xkeysnail.transform import *


def generate_move_keys(input, result):
    return {
        K(f"RC-{input}"): K(result),
        K(f"RC-Shift-{input}"): K(f"Shift-{result}"),
        K(f"RC-Super-{input}"): K(f"Super-{result}"),
        K(f"RC-LC-Super-{input}"): K(f"Super-LC-{result}"),
    }


define_modmap({
    Key.LEFT_SHIFT: Key.RIGHT_SHIFT,
})

define_multipurpose_modmap({
    Key.MUHENKAN: [Key.MUHENKAN, Key.RIGHT_CTRL],
})

define_keymap(None, {
    **generate_move_keys("h", "LEFT"),
    **generate_move_keys("j", "DOWN"),
    **generate_move_keys("k", "UP"),
    **generate_move_keys("l", "RIGHT"),
    **generate_move_keys("w", "C-RIGHT"),
    **generate_move_keys("b", "C-LEFT"),
    **generate_move_keys("EQUAL", "HOME"), # ^
    **generate_move_keys("KEY_4", "END"),
    **generate_move_keys("KEY_6", "END"),
}, "Vim-like cursor")

define_keymap(None, {
    K("RC-x"): Key.BACKSPACE,
    K("RC-y"): K("C-c"),
    K("RC-p"): K("C-v"),
    K("RC-u"): K("C-z"),
    K("RC-o"): [K("END"), K("ENTER")],
    K("RC-d"): {
        K("RC-w"): [K("C-Shift-RIGHT"), K("BACKSPACE")],
        K("RC-d"): [K("END"), K("Shift-HOME"), K("Shift-HOME"), K("BACKSPACE"), K("DELETE")],
    },
}, "Vim-like edit")

define_keymap(None, {
    K("RO"): K("Shift-RO"), # _
}, "default underscore")

define_keymap(None, {
    K("INSERT"): [K("INSERT"), K("INSERT")],
}, "disable insert")

define_keymap(None, {
    K("HENKAN"): Key.GRAVE,
    K("KATAKANAHIRAGANA"): Key.GRAVE,
}, "input method toggle")

define_keymap(re.compile("Gnome-terminal"), {
    K("C-TAB"): K("C-PAGE_UP"),
    K("C-Shift-TAB"): K("C-PAGE_DOWN"),
}, "Gnome-terminal")

# define_modmap({
#     Key.CAPSLOCK: Key.LEFT_CTRL,
#     Key.RIGHT_CTRL: Key.LEFT_CTRL,
# })


# define_multipurpose_modmap({
#     Key.Q: [Key.Q, Key.RIGHT_META],
#     Key.APOSTROPHE: [Key.APOSTROPHE, Key.RIGHT_CTRL],
# })


# define_keymap(None, {
#     # Vim-like
#     K("RSuper-h"): K("Left"),
#     K("RSuper-j"): K("Down"),
#     K("RSuper-k"): K("Up"),
#     K("RSuper-l"): K("Right"),
#     # Emacs-like
#     K("RC-a"): K("Home"),
#     K("RC-e"): K("End"),
#     K("RC-d"): K("Delete"),
#     K("RC-h"): K("Backspace"),
#     K("RC-k"): [K("Shift-End"), K("Delete")],
#     # Mac-like
#     K("Super-Backspace"): [K("Shift-Home"), K("Backspace")],
#     # Eclipse-like
#     K("Shift-Enter"): [K("End"), K("Shift-Enter")],
#     K("C-Shift-Enter"): [K("Up"), K("End"), K("Enter")],
# })