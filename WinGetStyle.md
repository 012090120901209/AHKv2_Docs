# WinGetStyle / WinGetExStyle

Returns the style or extended style (respectively) of the specified
window.

``` Syntax
Style := WinGetStyle(WinTitle, WinText, ExcludeTitle, ExcludeText)
ExStyle := WinGetExStyle(WinTitle, WinText, ExcludeTitle, ExcludeText)
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

Type: [Integer](../Concepts.htm#numbers)

These functions return the style or extended style (respectively) of the
specified window.

## Error Handling {#Error_Handling}

A [TargetError](Error.htm#TargetError) is thrown if the window could not
be found.

## Remarks {#Remarks}

See the [styles table](../misc/Styles.htm) for a partial listing of
styles.

The ID of the window under the mouse cursor can be retrieved with
[MouseGetPos](MouseGetPos.htm).

## Related {#Related}

[WinSetStyle / WinSetExStyle](WinSetStyle.htm), [ControlGetStyle /
ControlGetExStyle](ControlGetStyle.htm), [styles
table](../misc/Styles.htm), [Win functions](Win.htm), [Control
functions](Control.htm)

## Examples {#Examples}

::: {#ExStyle .ex}
[](#ExStyle){.ex_number} Determines whether a window has the WS_DISABLED
style.

    Style := WinGetStyle("My Window Title")
    if (Style & 0x8000000)  ; 0x8000000 is WS_DISABLED.
        MsgBox "The window is disabled."
:::

::: {#ExExStyle .ex}
[](#ExExStyle){.ex_number} Determines whether a window has the
WS_EX_TOPMOST style (always-on-top).

    ExStyle := WinGetExStyle("My Window Title")
    if (ExStyle & 0x8)  ; 0x8 is WS_EX_TOPMOST.
        MsgBox "The window is always-on-top."
:::
