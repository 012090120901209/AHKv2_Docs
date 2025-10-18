# MouseGetPos

Retrieves the current position of the mouse cursor, and optionally which
window and control it is hovering over.

``` Syntax
MouseGetPos &OutputVarX, &OutputVarY, &OutputVarWin, &OutputVarControl, Flag
```

## Parameters {#Parameters}

&OutputVarX, &OutputVarY

:   Type: [VarRef](../Concepts.htm#variable-references)

    If omitted, the corresponding value will not be stored. Otherwise,
    specify references to the output variables in which to store the X
    and Y coordinates. The retrieved coordinates are relative to the
    active window\'s client area unless [CoordMode](CoordMode.htm) was
    used to change to screen coordinates.

&OutputVarWin

:   Type: [VarRef](../Concepts.htm#variable-references)

    If omitted, the corresponding value will not be stored. Otherwise,
    specify a reference to the output variable in which to store the
    [unique ID number](../misc/WinTitle.htm#ahk_id) of the window under
    the mouse cursor. If the window cannot be determined, this variable
    will be made blank.

    The window does not have to be active to be detected. Hidden windows
    cannot be detected.

&OutputVarControl

:   Type: [VarRef](../Concepts.htm#variable-references)

    If omitted, the corresponding value will not be stored. Otherwise,
    specify a reference to the output variable in which to store the
    name (ClassNN) of the control under the mouse cursor. If the control
    cannot be determined, this variable will be made blank.

    The names of controls should always match those shown by the Window
    Spy. The window under the mouse cursor does not have to be active
    for a control to be detected.

Flag

:   Type: [Integer](../Concepts.htm#numbers)

    If omitted, it defaults to 0, meaning the function uses the default
    method to determine *OutputVarControl* and stores the control\'s
    ClassNN. Otherwise, specify a combination (sum) of the following
    numbers:

    **1:** Uses a simpler method to determine *OutputVarControl*. This
    method correctly retrieves the active/topmost child window of an
    Multiple Document Interface (MDI) application such as SysEdit or
    TextPad. However, it is less accurate for other purposes such as
    detecting controls inside a GroupBox control.

    **2:** Stores the [control\'s HWND](ControlGetHwnd.htm) in
    *OutputVarControl* rather than the [control\'s
    ClassNN](ControlGetClassNN.htm).

    For example, to put both options into effect, the *Flag* parameter
    must be set to 3.

## Remarks {#Remarks}

Any of the output variables may be omitted if the corresponding
information is not needed.

On systems with multiple screens which have different DPI settings, the
returned position may be different than expected due to [OS DPI
scaling](../misc/DPIScaling.htm).

## Related {#Related}

[CoordMode](CoordMode.htm), [Win functions](Win.htm),
[SetDefaultMouseSpeed](SetDefaultMouseSpeed.htm), [Click](Click.htm)

## Examples {#Examples}

::: {#ExBasic .ex}
[](#ExBasic){.ex_number} Reports the position of the mouse cursor.

    MouseGetPos &xpos, &ypos 
    MsgBox "The cursor is at X" xpos " Y" ypos
:::

::: {#ExWatchCursor .ex}
[](#ExWatchCursor){.ex_number} Shows the HWND, class name, title and
controls of the window currently under the mouse cursor.

    SetTimer WatchCursor, 100

    WatchCursor()
    {
        MouseGetPos , , &id, &control
        ToolTip
        (
            "ahk_id " id "
            ahk_class " WinGetClass(id) "
            " WinGetTitle(id) "
            Control: " control
        )
    }
:::
