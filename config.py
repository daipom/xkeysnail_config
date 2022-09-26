import re
from xkeysnail.transform import *


def generate_move_keys(input, result):
    return {
        K(f"RC-{input}"): K(result),
        K(f"RC-Shift-{input}"): K(f"Shift-{result}"),
        K(f"RC-Super-{input}"): K(f"Super-{result}"),
        K(f"RC-LC-Super-{input}"): K(f"Super-LC-{result}"),
    }

def map_emacs_to_vim():
    return {
        K("RC-w"): K("Alt-f"),
        K("RC-b"): K("Alt-b"),
        K("RC-EQUAL"): K("C-a"), # ^
        K("RC-KEY_4"): K("C-e"),
        K("RC-KEY_6"): K("C-e"),
        K("RC-u"): K("C-Shift-RO"),
        K("RC-Shift-d"): K("C-k"),
        K("RC-d"): {
            K("RC-w"): K("Alt-d"),
            K("RC-d"): [K("C-e"), K("C-u")],
        },
    }

define_modmap({
    Key.LEFT_SHIFT: Key.RIGHT_SHIFT,
})

define_multipurpose_modmap({
    Key.MUHENKAN: [Key.MUHENKAN, Key.RIGHT_CTRL],
})

define_keymap(re.compile("Gnome-terminal"), {
    K("C-TAB"): K("C-PAGE_DOWN"),
    K("C-Shift-TAB"): K("C-PAGE_UP"),
    K("RC-y"): K("C-Shift-c"),
    K("RC-p"): K("C-Shift-v"),
    **map_emacs_to_vim(),
}, "Gnome-terminal")

define_keymap(re.compile("Code"), {
    K("RC-s"): K("Alt-Shift-RIGHT"),
    K("RC-Alt-l"): K("Alt-RIGHT"),
    K("RC-Alt-h"): K("Alt-LEFT"),
    K("RC-Alt-j"): K("C-Alt-DOWN"), # go to next change
    K("RC-Alt-k"): K("C-Alt-UP"), # go to previous change
}, "Code")


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
    K("RC-Shift-d"): [K("Shift-END"), K("BACKSPACE")],
}, "Vim-like edit")

define_keymap(None, {
    K("RO"): K("Shift-RO"), # _
}, "default underscore")

define_keymap(None, {
    K("INSERT"): [K("INSERT"), K("INSERT")],
}, "disable insert")

define_keymap(None, {
    K("HENKAN"): K("ENTER"),
    K("KATAKANAHIRAGANA"): Key.GRAVE,
}, "input method toggle")
