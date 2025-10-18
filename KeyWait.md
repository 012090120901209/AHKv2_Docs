# KeyWait

Waits for a key or mouse/controller button to be released or pressed
down.

``` Syntax
KeyWait KeyName , Options
```

## Parameters {#Parameters}

KeyName

:   Type: [String](../Concepts.htm#strings)

    This can be just about any single character from the keyboard or one
    of the key names from the [key list](../KeyList.htm), such as a
    mouse/controller button. Controller attributes other than buttons
    are not supported.

    An explicit virtual key code such as `vkFF` may also be specified.
    This is useful in the rare case where a key has no name and produces
    no visible character when pressed. Its virtual key code can be
    determined by following the steps at the bottom of the [key list
    page](../KeyList.htm#SpecialKeys).

Options

:   Type: [String](../Concepts.htm#strings)

    If blank or omitted, the function will wait indefinitely for the
    specified key or mouse/controller button to be physically released
    by the user. However, if the [keyboard hook](InstallKeybdHook.htm)
    is not installed and *KeyName* is a keyboard key released
    artificially by means such as the [Send](Send.htm) function, the key
    will be seen as having been physically released. The same is true
    for mouse buttons when the [mouse hook](InstallMouseHook.htm) is not
    installed.

    Otherwise, specify a string of one or more of the following options
    (in any order, with optional spaces in between):

    **D:** Wait for the key to be pushed down.

    **L:** Check the logical state of the key, which is the state that
    the OS and the active window believe the key to be in (not
    necessarily the same as the physical state). This option is ignored
    for controller buttons.

    **T:** Timeout (e.g. `T3`). The number of seconds to wait before
    timing out and returning 0. If the key or button achieves the
    specified state, the function will not wait for the timeout to
    expire. Instead, it will immediately return 1.

    The timeout value can be a floating point number such as 2.5, but it
    should not be a hexadecimal value such as 0x03.

## Return Value {#Return_Value}

Type: [Integer (boolean)](../Concepts.htm#boolean)

This function returns 0 (false) if the function timed out or 1 (true)
otherwise.

## Remarks {#Remarks}

The physical state of a key or mouse button will usually be the same as
the logical state unless the keyboard and/or mouse hooks are installed,
in which case it will accurately reflect whether or not the user is
physically holding down the key. You can determine if your script is
using the hooks via the [KeyHistory](KeyHistory.htm) function or menu
item. You can force either or both of the hooks to be installed by
adding the [InstallKeybdHook](InstallKeybdHook.htm) and
[InstallMouseHook](InstallMouseHook.htm) functions to the script.

While the function is in a waiting state, new
[threads](../misc/Threads.htm) can be launched via
[hotkey](../Hotkeys.htm), [custom menu item](Menu.htm), or
[timer](SetTimer.htm).

To wait for two or more keys to be released, use KeyWait consecutively.
For example:

    KeyWait "Control"  ; Wait for both Control and Alt to be released.
    KeyWait "Alt"

To wait for any one key among a set of keys to be pressed down, see
[InputHook example #4](InputHook.htm#ExAnyKey).

## Related {#Related}

[GetKeyState](GetKeyState.htm), [Key List](../KeyList.htm),
[InputHook](InputHook.htm), [KeyHistory](KeyHistory.htm),
[InstallKeybdHook](InstallKeybdHook.htm),
[InstallMouseHook](InstallMouseHook.htm), [ClipWait](ClipWait.htm),
[WinWait](WinWait.htm)

## Examples {#Examples}

::: {#ExBasic .ex}
[](#ExBasic){.ex_number} Waits for the A key to be released.

    KeyWait "a"
:::

::: {#ExDown .ex}
[](#ExDown){.ex_number} Waits for the left mouse button to be pressed
down.

    KeyWait "LButton", "D"
:::

::: {#ExTimeout .ex}
[](#ExTimeout){.ex_number} Waits up to 3 seconds for the first
controller button to be pressed down.

    KeyWait "Joy1", "D T3"
:::

::: {#ExLogical .ex}
[](#ExLogical){.ex_number} Waits for the left Alt key to be logically
released.

    KeyWait "LAlt", "L"
:::

::: {#ExHotkey .ex}
[](#ExHotkey){.ex_number} When pressing this hotkey, KeyWait waits for
the user to physically release the CapsLock key. As a result, subsequent
statements are performed on release instead of press. This behavior is
similar to `~CapsLock up::`.

    ~CapsLock::
    {
        KeyWait "CapsLock"  ; Wait for user to physically release it.
        MsgBox "You pressed and released the CapsLock key."
    }
:::

::: {#ExRemap .ex}
[](#ExRemap){.ex_number} Remaps a key or mouse button. (This example is
only for illustration because it would be easier to use the [built-in
remapping feature](../misc/Remap.htm).) In the following hotkey, the
mouse button is kept held down while NumpadAdd is down, which
effectively transforms NumpadAdd into a mouse button.

    *NumpadAdd::
    {
        MouseClick "left",,, 1, 0, "D"  ; Hold down the left mouse button.
        KeyWait "NumpadAdd"  ; Wait for the key to be released.
        MouseClick "left",,, 1, 0, "U"  ; Release the mouse button.
    }
:::

::: {#ExDouble .ex}
[](#ExDouble){.ex_number} Detects when a key has been double-pressed
(similar to double-click). KeyWait is used to stop the keyboard\'s
auto-repeat feature from creating an unwanted double-press when you hold
down the RControl key to modify another key. It does this by keeping the
hotkey\'s thread running, which blocks the auto-repeats by relying upon
#MaxThreadsPerHotkey being at its default setting of 1. For a more
elaborate script that distinguishes between single, double and
triple-presses, see [SetTimer example #3](SetTimer.htm#ExampleCount).

    ~RControl::
    {
        if (A_PriorHotkey != "~RControl" or A_TimeSincePriorHotkey > 400)
        {
            ; Too much time between presses, so this isn't a double-press.
            KeyWait "RControl"
            return
        }
        MsgBox "You double-pressed the right control key."
    }
:::
