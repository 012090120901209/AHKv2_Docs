# WinGetTransColor

Returns the color that is marked transparent in the specified window.

``` Syntax
TransColor := WinGetTransColor(WinTitle, WinText, ExcludeTitle, ExcludeText)
```

## Parameters {#Parameters}

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

## Return Value {#Return_Value}

Type: [String](../Concepts.htm#strings)

This function returns the six-digit RGB color such as 0x00CC99 that is
marked transparent in the specified window.

The return value is an empty string in the following cases:

-   The window has no transparency color.
-   Under other conditions (caused by OS behavior) such as the window
    having been minimized, restored, and/or resized since it was made
    transparent.

## Error Handling {#Error_Handling}

A [TargetError](Error.htm#TargetError) is thrown if the window could not
be found.

## Remarks {#Remarks}

To mark a color as transparent, use
[WinSetTransColor](WinSetTransColor.htm).

The ID of the window under the mouse cursor can be retrieved with
[MouseGetPos](MouseGetPos.htm).

## Related {#Related}

[WinSetTransColor](WinSetTransColor.htm),
[WinGetTransparent](WinGetTransparent.htm), [Win functions](Win.htm),
[Control functions](Control.htm)

## Examples {#Examples}

::: {#ExBasic .ex}
[](#ExBasic){.ex_number} Retrieves the transparent color of a window
under the mouse cursor.

    MouseGetPos ,, &MouseWin
    TransColor := WinGetTransColor(MouseWin)
:::
