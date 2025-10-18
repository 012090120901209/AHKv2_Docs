# WinGetTransparent

Returns the degree of transparency of the specified window.

``` Syntax
TransDegree := WinGetTransparent(WinTitle, WinText, ExcludeTitle, ExcludeText)
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

Type: [Integer](../Concepts.htm#numbers) or [String
(empty)](../Concepts.htm#nothing)

This function returns a number between 0 and 255 representing the degree
of transparency of the specified window, where 0 indicates an invisible
window and 255 indicates an opaque window.

The return value is an empty string in the following cases:

-   The window has no transparency level.
-   Under other conditions (caused by OS behavior) such as the window
    having been minimized, restored, and/or resized since it was made
    transparent.

## Error Handling {#Error_Handling}

A [TargetError](Error.htm#TargetError) is thrown if the window could not
be found.

## Remarks {#Remarks}

To set transparency, use [WinSetTransparent](WinSetTransparent.htm).

The ID of the window under the mouse cursor can be retrieved with
[MouseGetPos](MouseGetPos.htm).

## Related {#Related}

[WinSetTransparent](WinSetTransparent.htm),
[WinGetTransColor](WinGetTransColor.htm), [Win functions](Win.htm),
[Control functions](Control.htm)

## Examples {#Examples}

::: {#ExBasic .ex}
[](#ExBasic){.ex_number} Retrieves the degree of transparency of the
window under the mouse cursor.

    MouseGetPos ,, &MouseWin
    TransDegree := WinGetTransparent(MouseWin)
:::
