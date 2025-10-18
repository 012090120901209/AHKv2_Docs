# WinActivate

Activates the specified window.

``` Syntax
WinActivate WinTitle, WinText, ExcludeTitle, ExcludeText
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

## Remarks {#Remarks}

When an inactive window becomes active, the operating system also makes
it foremost (brings it to the top of the stack). This does not occur if
the window is already active.

If the window is minimized and inactive, it is automatically restored
prior to being activated. If *WinTitle* is the letter \"A\" and the
other parameters are omitted, the active window is restored. The window
is restored even if it was already active.

Six attempts will be made to activate the target window over the course
of 60 ms. If all six attempts fail, WinActivate automatically sends
`{Alt 2}`{.no-highlight} as a workaround for possible restrictions
enforced by the operating system, and then makes a seventh attempt.
Thus, it is usually unnecessary to follow WinActivate with
[WinWaitActive](WinWaitActive.htm) or
`if not `[`WinActive`](WinActive.htm)`(...)`.

After WinActivate\'s first failed attempt, it automatically sends
`{Alt up}`. Testing has shown that this may improve the reliability of
all subsequent attempts, reducing the number of instances where the
first attempt fails and causes the taskbar button to flash. No more than
one `{Alt up}` is sent for this purpose for the lifetime of each script.
If this or any other (AutoHotkey v1.1.27+) script has a keyboard hook
installed, the `{Alt up}` is blocked from the active window, minimizing
the already small risk of side-effects.

In general, if more than one window matches, the topmost matching window
(typically the one most recently used) will be activated. If the window
is already active, it will be kept active rather than activating any
other matching window beneath it. However, if the active window is moved
to the bottom of the stack with [WinMoveBottom](WinMoveBottom.htm), some
other window may be activated even if the active window is a match.

[WinActivateBottom](WinActivateBottom.htm) activates the bottommost
matching window (typically the one least recently used).

[GroupActivate](GroupActivate.htm) activates the next window that
matches criteria specified by a window group.

If the active window is hidden and
[DetectHiddenWindows](DetectHiddenWindows.htm) is turned off, it is
never considered a match. Instead, a visible matching window is
activated if one exists.

When a window is activated immediately after the activation of some
other window, task bar buttons might start flashing on some systems
(depending on OS and settings). To prevent this, use
[#WinActivateForce](_WinActivateForce.htm).

**Known issue:** If the script is running on a computer or server being
accessed via remote desktop, WinActivate may hang if the remote desktop
client is minimized. One workaround is to use built-in functions which
don\'t require window activation, such as [ControlSend](ControlSend.htm)
and [ControlClick](ControlClick.htm). Another possible workaround is to
apply the following registry setting on the local/client computer:

    ; Change HKCU to HKLM to affect all users on this system.
    RegWrite "REG_DWORD", "HKCU\Software\Microsoft\Terminal Server Client"
        , "RemoteDesktop_SuppressWhenMinimized", 2

## Related {#Related}

[WinActivateBottom](WinActivateBottom.htm),
[#WinActivateForce](_WinActivateForce.htm),
[SetTitleMatchMode](SetTitleMatchMode.htm),
[DetectHiddenWindows](DetectHiddenWindows.htm), [Last Found
Window](../misc/WinTitle.htm#LastFoundWindow), [WinExist](WinExist.htm),
[WinActive](WinActive.htm), [WinWaitActive](WinWaitActive.htm),
[WinWait](WinWait.htm), [WinWaitClose](WinWaitClose.htm),
[WinClose](WinClose.htm), [GroupActivate](GroupActivate.htm), [Win
functions](Win.htm)

## Examples {#Examples}

::: {#ExBasic .ex}
[](#ExBasic){.ex_number} If Notepad does exist, activate it, otherwise
activate the calculator.

    if WinExist("Untitled - Notepad")
        WinActivate ; Use the window found by WinExist.
    else
        WinActivate "Calculator"
:::
