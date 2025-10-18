# WinClose

Closes the specified window.

``` Syntax
WinClose WinTitle, WinText, SecondsToWait, ExcludeTitle, ExcludeText
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

SecondsToWait

:   Type: [Integer](../Concepts.htm#numbers) or
    [Float](../Concepts.htm#numbers)

    If omitted, the function will not wait at all. Otherwise, specify
    the number of seconds (can contain a decimal point) to wait for the
    window to close. If the window does not close within that period,
    the script will continue.

## Error Handling {#Error_Handling}

A [TargetError](Error.htm#TargetError) is thrown if the window could not
be found, except if the [group](#group) mode is used.

No exception is thrown if a window is found but cannot be closed, so use
[WinExist](WinExist.htm) or [WinWaitClose](WinWaitClose.htm) if you need
to determine for certain that a window has closed.

## Remarks {#Remarks}

This function sends a close message to a window. The result depends on
the window (it may ask to save data, etc.)

If a matching window is active, that window will be closed in preference
to any other matching window. In general, if more than one window
matches, the topmost (most recently used) will be closed.

This function operates only upon a single window except when *WinTitle*
is [ahk_group GroupName](GroupAdd.htm) (with no other criteria
specified), in which case all windows in the group are affected.

While the function is in a waiting state, new
[threads](../misc/Threads.htm) can be launched via
[hotkey](../Hotkeys.htm), [custom menu item](Menu.htm), or
[timer](SetTimer.htm).

WinClose sends a WM_CLOSE message to the target window, which is a
somewhat forceful method of closing it. An alternate method of closing
is to send the following message. It might produce different behavior
because it is similar in effect to pressing [Alt]{.kbd}+[F4]{.kbd} or
clicking the window\'s close button in its title bar:

    PostMessage 0x0112, 0xF060,,, WinTitle, WinText  ; 0x0112 = WM_SYSCOMMAND, 0xF060 = SC_CLOSE

If a window does not close via WinClose, you can force it to close with
[WinKill](WinKill.htm).

## Related {#Related}

[WinKill](WinKill.htm), [WinWaitClose](WinWaitClose.htm),
[ProcessClose](ProcessClose.htm), [WinActivate](WinActivate.htm),
[SetTitleMatchMode](SetTitleMatchMode.htm),
[DetectHiddenWindows](DetectHiddenWindows.htm), [Last Found
Window](../misc/WinTitle.htm#LastFoundWindow), [WinExist](WinExist.htm),
[WinActive](WinActive.htm), [WinWaitActive](WinWaitActive.htm),
[WinWait](WinWait.htm), [GroupActivate](GroupActivate.htm)

## Examples {#Examples}

::: {#ExBasic .ex}
[](#ExBasic){.ex_number} If Notepad does exist, close it, otherwise
close the calculator.

    if WinExist("Untitled - Notepad")
        WinClose ; Use the window found by WinExist.
    else
        WinClose "Calculator"
:::
