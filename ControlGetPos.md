# ControlGetPos

Retrieves the position and size of a control.

``` Syntax
ControlGetPos &OutX, &OutY, &OutWidth, &OutHeight, Control, WinTitle, WinText, ExcludeTitle, ExcludeText
```

## Parameters {#Parameters}

&OutX, &OutY

:   Type: [VarRef](../Concepts.htm#variable-references)

    If omitted, the corresponding value will not be stored. Otherwise,
    specify references to the output variables in which to store the X
    and Y coordinates (in pixels) of the control\'s upper left corner.
    These coordinates are relative to the upper-left corner of the
    target window\'s [client area](CoordMode.htm#Client) and thus are
    the same as those used by [ControlMove](ControlMove.htm).

&OutWidth, &OutHeight

:   Type: [VarRef](../Concepts.htm#variable-references)

    If omitted, the corresponding value will not be stored. Otherwise,
    specify references to the output variables in which to store the
    control\'s width and height (in pixels).

Control

:   Type: [String](../Concepts.htm#strings),
    [Integer](../Concepts.htm#numbers) or
    [Object](../Concepts.htm#objects)

    The control\'s ClassNN, text or HWND, or an object with a `Hwnd`
    property. For details, see [The Control
    Parameter](Control.htm#Parameter).

WinTitle, WinText, ExcludeTitle, ExcludeText

:   Type: [String](../Concepts.htm#strings),
    [Integer](../Concepts.htm#numbers) or
    [Object](../Concepts.htm#objects)

    If each of these is blank or omitted, the [Last Found
    Window](../misc/WinTitle.htm#LastFoundWindow) will be used.
    Otherwise, specify for *WinTitle* a [window title or other
    criteria](../misc/WinTitle.htm) to identify the target window and/or
    for *WinText* a substring from a single text element of the target
    window (as revealed by the included Window Spy utility).

    *ExcludeTitle* and *ExcludeText* can be used to exclude one or more
    windows by their title or text. Their specification is similar to
    *WinTitle* and *WinText*, except that *ExcludeTitle* does not
    recognize any criteria other than the window title.

    Window titles and text are case-sensitive. By default, hidden
    windows are not detected and hidden text elements are detected,
    unless changed with [DetectHiddenWindows](DetectHiddenWindows.htm)
    and [DetectHiddenText](DetectHiddenText.htm); however, when using
    [pure HWNDs](../misc/WinTitle.htm#ahk_id), hidden windows are always
    detected regardless of DetectHiddenWindows. By default, a window
    title can contain *WinTitle* or *ExcludeTitle* anywhere inside it to
    be a match, unless changed with
    [SetTitleMatchMode](SetTitleMatchMode.htm).

## Error Handling {#Error_Handling}

A [TargetError](Error.htm#TargetError) is thrown if the window or
control could not be found.

## Remarks {#Remarks}

Unlike functions that change a control, ControlGetPos does not have an
automatic delay ([SetControlDelay](SetControlDelay.htm) does not affect
it).

## Related {#Related}

[ControlMove](ControlMove.htm), [WinGetPos](WinGetPos.htm), [Control
functions](Control.htm)

## Examples {#Examples}

::: {#ExBasic .ex}
[](#ExBasic){.ex_number} Continuously updates and displays the name and
position of the control currently under the mouse cursor.

    Loop
    {
        Sleep 100
        MouseGetPos ,, &WhichWindow, &WhichControl
        try ControlGetPos &x, &y, &w, &h, WhichControl, WhichWindow
        ToolTip WhichControl "`nX" X "`tY" Y "`nW" W "`t" H
    }
:::
