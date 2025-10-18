# WinMoveTop

Brings the specified window to the top of the stack without explicitly
activating it.

``` Syntax
WinMoveTop WinTitle, WinText, ExcludeTitle, ExcludeText
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

## Error Handling {#Error_Handling}

A [TargetError](Error.htm#TargetError) is thrown if the window could not
be found.

An [OSError](Error.htm#OSError) may be thrown on failure.

## Remarks {#Remarks}

However, the system default settings will probably cause it to activate
in most cases. In addition, this function may have no effect due to the
operating system\'s protection against applications that try to steal
focus from the user (it may depend on factors such as what type of
window is currently active and what the user is currently doing). One
possible work-around is to make the window briefly
[always-on-top](WinSetAlwaysOnTop.htm), then turn off always-on-top.

The ID of the window under the mouse cursor can be retrieved with
[MouseGetPos](MouseGetPos.htm).

## Related {#Related}

[WinMoveBottom](WinMoveBottom.htm),
[WinSetAlwaysOnTop](WinSetAlwaysOnTop.htm), [Win functions](Win.htm),
[Control functions](Control.htm)
