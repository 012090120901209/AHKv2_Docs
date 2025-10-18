# WinHide

Hides the specified window.

``` Syntax
WinHide WinTitle, WinText, ExcludeTitle, ExcludeText
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
be found, except if the [group](#group) mode is used.

## Remarks {#Remarks}

Use [WinShow](WinShow.htm) to unhide a hidden window
([DetectHiddenWindows](DetectHiddenWindows.htm) can be either On or Off
to do this).

This function operates only upon the topmost matching window except when
*WinTitle* is [ahk_group GroupName](GroupAdd.htm), in which case all
windows in the group are affected.

## Related {#Related}

[WinShow](WinShow.htm), [SetTitleMatchMode](SetTitleMatchMode.htm),
[DetectHiddenWindows](DetectHiddenWindows.htm), [Last Found
Window](../misc/WinTitle.htm#LastFoundWindow), [Win functions](Win.htm)

## Examples {#Examples}

::: {#ExBasic .ex}
[](#ExBasic){.ex_number} Opens Notepad, waits until it exists, hides it
for a short time and unhides it.

    Run "notepad.exe"
    WinWait "Untitled - Notepad"
    Sleep 500
    WinHide ; Use the window found by WinWait.
    Sleep 1000
    WinShow ; Use the window found by WinWait.
:::

::: {#ExTaskbar .ex}
[](#ExTaskbar){.ex_number} Temporarily hides the taskbar.

    WinHide "ahk_class Shell_TrayWnd"
    Sleep 1000
    WinShow "ahk_class Shell_TrayWnd"
:::
