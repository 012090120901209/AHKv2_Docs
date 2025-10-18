# WinSetTransColor

Makes all pixels of the chosen color invisible inside the specified
window.

``` Syntax
WinSetTransColor Color , WinTitle, WinText, ExcludeTitle, ExcludeText
```

## Parameters {#Parameters}

Color

:   Type: [String](../Concepts.htm#strings) or
    [Integer](../Concepts.htm#numbers)

    Specify a color name or RGB value (see the [color
    chart](../misc/Colors.htm) for guidance, or use
    [PixelGetColor](PixelGetColor.htm) in its RGB mode). To additionally
    make the visible part of the window partially transparent, append a
    space (not a comma) followed by the transparency level (0-255). For
    example: `WinSetTransColor "EEAA99 150"`.

    If the value is a string, any numeric color value must be in
    hexadecimal format. The color value can be omitted; for example,
    `WinSetTransColor " 150"` (with the leading space) is equivalent to
    `WinSetTransparent 150`.

    `"Off"` (case-insensitive) or an empty string may be specified to
    completely turn off transparency for a window. This is functionally
    identical to [`WinSetTransparent`](WinSetTransparent.htm)` "Off"`.
    Specifying Off is different than specifying 255 because it may
    improve performance and reduce usage of system resources (but
    probably only when desktop composition is disabled).

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

An [OSError](Error.htm#OSError) is thrown if the change could not be
applied.

## Remarks {#Remarks}

This allows the contents of the window behind it to show through. If the
user clicks on an invisible pixel, the click will \"fall through\" to
the window behind it.

To change a window\'s existing TransColor, it may be necessary to turn
off transparency before making the change.

The ID of the window under the mouse cursor can be retrieved with
[MouseGetPos](MouseGetPos.htm).

This function is often used to create on-screen displays and other
visual effects. There is an example of an on-screen display [at the
bottom of the Gui object page](Gui.htm#ExOSD). For a simple
demonstration via hotkeys, see [WinSetTransparent example
#4](WinSetTransparent.htm#ExTransHotkey).

## Related {#Related}

[WinSetTransparent](WinSetTransparent.htm), [Win functions](Win.htm),
[Control functions](Control.htm)

## Examples {#Examples}

::: {#ExBasic .ex}
[](#ExBasic){.ex_number} Makes all white pixels in Notepad invisible.
This example may not work well with the new Notepad on Windows 11 or
later.

    WinSetTransColor "White", "Untitled - Notepad"
:::
