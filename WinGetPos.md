# WinGetPos

Retrieves the position and size of the specified window.

``` Syntax
WinGetPos &OutX, &OutY, &OutWidth, &OutHeight, WinTitle, WinText, ExcludeTitle, ExcludeText
```

## Parameters {#Parameters}

&OutX, &OutY

:   Type: [VarRef](../Concepts.htm#variable-references)

    If omitted, the corresponding value will not be stored. Otherwise,
    specify references to the output variables in which to store the X
    and Y coordinates of the target window\'s upper left corner.

&OutWidth, &OutHeight

:   Type: [VarRef](../Concepts.htm#variable-references)

    If omitted, the corresponding value will not be stored. Otherwise,
    specify references to the output variables in which to store the
    width and height of the target window.

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

A [TargetError](Error.htm#TargetError) is thrown if the window could not
be found.

## Remarks {#Remarks}

If *WinTitle* is `"Program Manager"`, the function will retrieve the
size of the desktop, which is usually the same as the current screen
resolution.

A minimized window will still have a position and size. The values
returned in this case may vary depending on OS and configuration, but
are usually -32000 for the X and Y coordinates and zero for the width
and height.

To discover the name of the window and control that the mouse is
currently hovering over, use [MouseGetPos](MouseGetPos.htm).

As the coordinates returned by this function include the window\'s title
bar, menu and borders, they may be dependent on OS version and theme. To
get more consistent values across different systems, consider using
[WinGetClientPos](WinGetClientPos.htm) instead.

On systems with multiple screens which have different DPI settings, the
returned position and size may be different than expected due to [OS DPI
scaling](../misc/DPIScaling.htm).

## Related {#Related}

[WinMove](WinMove.htm), [WinGetClientPos](WinGetClientPos.htm),
[ControlGetPos](ControlGetPos.htm), [WinGetTitle](WinGetTitle.htm),
[WinGetText](WinGetText.htm), [ControlGetText](ControlGetText.htm)

## Examples {#Examples}

::: {#ExBasic .ex}
[](#ExBasic){.ex_number} Retrieves and reports the position and size of
the calculator.

    WinGetPos &X, &Y, &W, &H, "Calculator"
    MsgBox "Calculator is at " X "," Y " and its size is " W "x" H
:::

::: {#ExA .ex}
[](#ExA){.ex_number} Retrieves and reports the position of the active
window.

    WinGetPos &X, &Y,,, "A"
    MsgBox "The active window is at " X "," Y
:::

::: {#ExLastFound .ex}
[](#ExLastFound){.ex_number} If Notepad does exist, retrieve and report
its position.

    if WinExist("Untitled - Notepad")
    {
        WinGetPos &Xpos, &Ypos ; Use the window found by WinExist.
        MsgBox "Notepad is at " Xpos "," Ypos
    }
:::
