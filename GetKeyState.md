# GetKeyState

Returns 1 (true) or 0 (false) depending on whether the specified
keyboard key or mouse/controller button is down or up. Also retrieves
controller status.

``` Syntax
IsDown := GetKeyState(KeyName , Mode)
```

## Parameters {#Parameters}

KeyName

:   Type: [String](../Concepts.htm#strings)

    This can be just about any single character from the keyboard or one
    of the key names from the [key list](../KeyList.htm), such as a
    mouse/controller button. Examples: B, 5, LWin, RControl, Alt, Enter,
    Escape, LButton, MButton, Joy1.

    Alternatively, an explicit virtual key code such as vkFF may be
    specified. This is useful in the rare case where a key has no name.
    The code of such a key can be determined by following the steps at
    the bottom of the [key list page](../KeyList.htm#SpecialKeys). Note
    that this code must be in hexadecimal.

    **Known limitation:** This function cannot differentiate between two
    keys which share the same virtual key code, such as Left and
    NumpadLeft.

Mode

:   Type: [String](../Concepts.htm#strings)

    This parameter is ignored when retrieving controller status.

    If omitted, it defaults to that which retrieves the logical state of
    the key. This is the state that the OS and the active window believe
    the key to be in, but is not necessarily the same as the physical
    state.

    Otherwise, specify one of the following letters:

    **P:** Retrieve the physical state (i.e. whether the user is
    physically holding it down). The physical state of a key or mouse
    button will usually be the same as the logical state unless the
    keyboard and/or mouse hooks are installed, in which case it will
    accurately reflect whether or not the user is physically holding
    down the key or button (as long as it was pressed down while the
    script was running). You can determine if your script is using the
    hooks via the [KeyHistory](KeyHistory.htm) function or menu item.
    You can force the hooks to be installed by calling
    [InstallKeybdHook](InstallKeybdHook.htm) and/or
    [InstallMouseHook](InstallMouseHook.htm).

    **T:** Retrieve the toggle state. For keys other than
    [CapsLock]{.kbd}, [NumLock]{.kbd} and [ScrollLock]{.kbd}, the toggle
    state is generally 0 when the script starts and is not synchronized
    between processes.

## Return Value {#Return_Value}

Type: [Integer (boolean)](../Concepts.htm#boolean),
[Float](../Concepts.htm#numbers), [Integer](../Concepts.htm#numbers) or
[String (empty)](../Concepts.htm#nothing)

This function returns 1 (true) if the key is down (or toggled on) or 0
(false) if it is up (or toggled off).

When *KeyName* is a stick axis such as JoyX, this function returns a
floating-point number between 0 and 100 to indicate the stick\'s
position as a percentage of that axis\'s range of motion. This [test
script](../scripts/index.htm#ControllerTest) can be used to analyze your
controller(s).

When *KeyName* is JoyPOV, this function returns an integer between 0 and
35900. The following approximate POV values are used by many
controllers:

-   -1: no angle to report
-   0: forward POV
-   9000 (i.e. 90 degrees): right POV
-   27000 (i.e. 270 degrees): left POV
-   18000 (i.e. 180 degrees): backward POV

When *KeyName* is JoyName, JoyButtons, JoyAxes or JoyInfo, the retrieved
value will be the name, number of buttons, number of axes or
capabilities of the controller. For details, see [Game
Controller](../KeyList.htm#Controller).

When *KeyName* is a button or control of a controller that could not be
detected, this function returns an empty string.

## Error Handling {#Error_Handling}

A [ValueError](Error.htm#ValueError) is thrown if invalid parameters are
detected, e.g. when *KeyName* does not exist on the current keyboard
layout.

## Remarks {#Remarks}

To wait for a key or mouse/controller button to achieve a new state, it
is usually easier to use [KeyWait](KeyWait.htm) instead of a GetKeyState
loop.

Systems with unusual keyboard drivers might be slow to update the state
of their keys, especially the toggle-state of keys like
[CapsLock]{.kbd}. A script that checks the state of such a key
immediately after it changed may use [Sleep](Sleep.htm) beforehand to
give the system time to update the key state.

For examples of using GetKeyState with a controller, see the [controller
remapping page](../misc/RemapController.htm) and the
[Controller-To-Mouse script](../scripts/index.htm#ControllerMouse).

## Related {#Related}

[GetKeyVK](GetKeyVK.htm), [GetKeySC](GetKeySC.htm),
[GetKeyName](GetKeyName.htm), [KeyWait](KeyWait.htm), [Key
List](../KeyList.htm), [Controller
remapping](../misc/RemapController.htm), [KeyHistory](KeyHistory.htm),
[InstallKeybdHook](InstallKeybdHook.htm),
[InstallMouseHook](InstallMouseHook.htm)

## Examples {#Examples}

::: {#ExBasic .ex}
[](#ExBasic){.ex_number} Retrieves the current state of the right mouse
button.

    state := GetKeyState("RButton")
:::

::: {#ExBasic2 .ex}
[](#ExBasic2){.ex_number} Retrieves the current state of the first
controller\'s second button.

    state := GetKeyState("Joy2")
:::

::: {#ExIfElse .ex}
[](#ExIfElse){.ex_number} Checks if at least one [Shift]{.kbd} is down.

    if GetKeyState("Shift")
        MsgBox "At least one Shift key is down."
    else
        MsgBox "Neither Shift key is down."
:::

::: {#ExToggle .ex}
[](#ExToggle){.ex_number} Retrieves the current toggle state of
[CapsLock]{.kbd}.

    state := GetKeyState("CapsLock", "T")
:::

::: {#ExRemap .ex}
[](#ExRemap){.ex_number} Remapping. (This example is only for
illustration because it would be easier to use the [built-in remapping
feature](../misc/Remap.htm).) In the following hotkey, the mouse button
is kept held down while NumpadAdd is down, which effectively transforms
NumpadAdd into a mouse button. This method can also be used to repeat an
action while the user is holding down a key or button.

    *NumpadAdd::
    {
        MouseClick "left",,, 1, 0, "D"  ; Hold down the left mouse button.
        Loop
        {
            Sleep 10
            if !GetKeyState("NumpadAdd", "P")  ; The key has been released, so break out of the loop.
                break
            ; ... insert here any other actions you want repeated.
        }
        MouseClick "left",,, 1, 0, "U"  ; Release the mouse button.
    }
:::

::: {#ExController .ex}
[](#ExController){.ex_number} Makes controller button behavior depend on
stick axis position.

    joy2::
    {
        JoyX := GetKeyState("JoyX")
        if JoyX > 75
            MsgBox "Action #1 (button pressed while stick was pushed to the right)."
        else if JoyX < 25
            MsgBox "Action #2 (button pressed while stick was pushed to the left)."
        else
            MsgBox "Action #3 (button pressed while stick was centered horizontally)."
    }
:::

See the [controller remapping page](../misc/RemapController.htm) and the
[Controller-To-Mouse script](../scripts/index.htm#ControllerMouse) for
other examples.
