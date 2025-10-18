# WinWaitActive / WinWaitNotActive

Waits until the specified window is active or not active.

``` Syntax
HWND := WinWaitActive(WinTitle, WinText, Timeout, ExcludeTitle, ExcludeText)
Boolean := WinWaitNotActive(WinTitle, WinText, Timeout, ExcludeTitle, ExcludeText)
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

Timeout

:   Type: [Integer](../Concepts.htm#numbers) or
    [Float](../Concepts.htm#numbers)

    If omitted, the function will wait indefinitely. Otherwise, it will
    wait no longer than this many seconds. To wait for a fraction of a
    second, specify a floating-point number, for example, 0.25 to wait
    for a maximum of 250 milliseconds.

## Return Value {#Return_Value}

Type: [Integer](../Concepts.htm#numbers) or [Integer
(boolean)](../Concepts.htm#boolean)

WinWaitActive returns the [HWND (unique
ID)](../misc/WinTitle.htm#ahk_id) of the active window if it matches the
criteria, or 0 if the function timed out.

WinWaitNotActive returns 1 (true) if the active window does not match
the criteria, or 0 (false) if the function timed out.

## Remarks {#Remarks}

If the active window satisfies the function\'s expectation, the function
will not wait for *Timeout* to expire. Instead, it will immediately
return, allowing the script to resume.

Since `"A"` matches whichever window is active at any given moment,
`WinWaitNotActive "A"` typically waits indefinitely. To instead wait for
a different window to become active, specify its unique ID as in the
following example:

    WinWaitNotActive WinExist("A")

Both WinWaitActive and WinWaitNotActive will update the [Last Found
Window](../misc/WinTitle.htm#LastFoundWindow) if a matching window is
active when the function begins or becomes active while the function is
waiting.

While the function is in a waiting state, new
[threads](../misc/Threads.htm) can be launched via
[hotkey](../Hotkeys.htm), [custom menu item](Menu.htm), or
[timer](SetTimer.htm).

If another [thread](../misc/Threads.htm) changes the contents of any
variable(s) that were used for this function\'s parameters, the function
will not see the change \-- it will continue to use the title and text
that were originally present in the variables when the function first
started waiting.

## Related {#Related}

[WinWait](WinWait.htm), [WinWaitClose](WinWaitClose.htm),
[WinExist](WinExist.htm), [WinActive](WinActive.htm),
[SetTitleMatchMode](SetTitleMatchMode.htm),
[DetectHiddenWindows](DetectHiddenWindows.htm)

## Examples {#Examples}

::: {#ExBasic .ex}
[](#ExBasic){.ex_number} Opens Notepad and waits a maximum of 2 seconds
until it is active. If WinWait times out, an error message is shown,
otherwise Notepad is minimized.

    Run "notepad.exe"
    if WinWaitActive("Untitled - Notepad", , 2)
        WinMinimize ; Use the window found by WinWaitActive.
    else
        MsgBox "WinWaitActive timed out."
:::
