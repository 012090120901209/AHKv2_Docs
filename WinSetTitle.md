# WinSetTitle

Changes the title of the specified window.

``` Syntax
WinSetTitle NewTitle , WinTitle, WinText, ExcludeTitle, ExcludeText
```

## Parameters {#Parameters}

NewTitle

:   Type: [String](../Concepts.htm#strings)

    The new title for the window. If this is the only parameter given,
    the [Last Found Window](../misc/WinTitle.htm#LastFoundWindow) will
    be used.

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

A change to a window\'s title might be merely temporary if the
application that owns the window frequently changes the title.

## Related {#Related}

[WinMove](WinMove.htm), [WinGetTitle](WinGetTitle.htm),
[WinGetText](WinGetText.htm), [ControlGetText](ControlGetText.htm),
[WinGetPos](WinGetPos.htm), [Win functions](Win.htm)

## Examples {#Examples}

::: {#ExBasic .ex}
[](#ExBasic){.ex_number} Changes the title of Notepad. This example may
fail on Windows 11 or later, as it requires the classic version of
Notepad.

    WinSetTitle("This is a new title", "Untitled - Notepad")
:::

::: {#ExLastFound .ex}
[](#ExLastFound){.ex_number} Opens Notepad, waits until it is active and
changes its title. This example may fail on Windows 11 or later, as it
requires the classic version of Notepad.

    Run "notepad.exe"
    WinWaitActive "Untitled - Notepad"
    WinSetTitle "This is a new title" ; Use the window found by WinWaitActive.
:::

::: {#ExMainWin .ex}
[](#ExMainWin){.ex_number} Opens the [main
window](../Program.htm#main-window), waits until it is active and
changes its title.

    ListVars
    WinWaitActive "ahk_class AutoHotkey"
    WinSetTitle "This is a new title" ; Use the window found by WinWaitActive.
:::
