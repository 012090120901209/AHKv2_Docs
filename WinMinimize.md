# WinMinimize

Collapses the specified window into a button on the task bar.

``` Syntax
WinMinimize WinTitle, WinText, ExcludeTitle, ExcludeText
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

Use [WinRestore](WinRestore.htm) to unminimize a window or
[WinMaximize](WinMaximize.htm) to maximize it.

WinMinimize minimizes the window using a direct method, bypassing the
window message which is usually sent when the minimize button, window
menu or taskbar is used to minimize the window. This prevents the window
from overriding the action (such as to \"minimize\" to the taskbar by
hiding the window), but may also prevent the window from responding
correctly, such as to save the [current focus](ControlGetFocus.htm) for
when the window is restored. It also prevents the \"minimize\" system
sound from being played.

If a particular type of window does not respond correctly to
WinMinimize, try using the following instead:

    PostMessage 0x0112, 0xF020,,, WinTitle, WinText ; 0x0112 = WM_SYSCOMMAND, 0xF020 = SC_MINIMIZE

This function operates only upon the topmost matching window except when
*WinTitle* is [ahk_group GroupName](GroupAdd.htm), in which case all
windows in the group are affected.

## Related {#Related}

[WinRestore](WinRestore.htm), [WinMaximize](WinMaximize.htm),
[WinMinimizeAll](WinMinimizeAll.htm)

## Examples {#Examples}

::: {#ExBasic .ex}
[](#ExBasic){.ex_number} Opens Notepad, waits until it exists and
minimizes it.

    Run "notepad.exe"
    WinWait "Untitled - Notepad"
    WinMinimize ; Use the window found by WinWait.
:::

::: {#ExHotkey .ex}
[](#ExHotkey){.ex_number} Press a hotkey to minimize the active window.

    ^Down::WinMinimize "A"  ; Ctrl+Down
:::
