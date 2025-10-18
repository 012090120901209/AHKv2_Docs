# WinWait

Waits until the specified window exists.

``` Syntax
HWND := WinWait(WinTitle, WinText, Timeout, ExcludeTitle, ExcludeText)
```

## Parameters {#Parameters}

WinTitle, WinText, ExcludeTitle, ExcludeText

:   Type: [String](../Concepts.htm#strings),
    [Integer](../Concepts.htm#numbers) or
    [Object](../Concepts.htm#objects)

    At least one of these is required. Specify for *WinTitle* a [window
    title or other criteria](../misc/WinTitle.htm) to identify the
    target window and/or for *WinText* a substring from a single text
    element of the target window (as revealed by the included Window Spy
    utility).

    *ExcludeTitle* and *ExcludeText* can be used to exclude one or more
    windows by their title or text. Their specification is similar to
    *WinTitle* and *WinText*, except that *ExcludeTitle* does not
    recognize any criteria other than the window title.

    Window titles and text are case-sensitive. By default, hidden
    windows are not detected and hidden text elements are detected,
    unless changed with [DetectHiddenWindows](DetectHiddenWindows.htm)
    and [DetectHiddenText](DetectHiddenText.htm). By default, a window
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

Type: [Integer](../Concepts.htm#numbers)

This function returns the [HWND (unique
ID)](../misc/WinTitle.htm#ahk_id) of a matching window if one was found,
or 0 if the function timed out.

## Remarks {#Remarks}

If a matching window comes into existence, the function will not wait
for *Timeout* to expire. Instead, it will update the [Last Found
Window](../misc/WinTitle.htm#LastFoundWindow) and return, allowing the
script to continue execution.

If *WinTitle* specifies a [pure HWND](../misc/WinTitle.htm#ahk_id) (as
an [Integer](../Concepts.htm#numbers) or an [Object](../Objects.htm)
with a HWND property), hidden windows are detected only when using
[DetectHiddenWindows](DetectHiddenWindows.htm). This only applies to
WinWait and [WinWaitClose](WinWaitClose.htm); for other windowing
functions, specifying a pure HWND causes hidden windows to be detected
regardless of DetectHiddenWindows.

If *WinTitle* specifies an invalid pure HWND, the function returns
immediately, without waiting for *Timeout* to expire. Waiting for
another window to be created with the same HWND value would not be
meaningful, as there would likely be no relation between the two
windows.

While the function is in a waiting state, new
[threads](../misc/Threads.htm) can be launched via
[hotkey](../Hotkeys.htm), [custom menu item](Menu.htm), or
[timer](SetTimer.htm).

If another [thread](../misc/Threads.htm) changes the contents of any
variable(s) that were used for this function\'s parameters, the function
will not see the change \-- it will continue to use the title and text
that were originally present in the variables when the function first
started waiting.

Unlike [WinWaitActive](WinWaitActive.htm), the [Last Found
Window](../misc/WinTitle.htm#LastFoundWindow) cannot be used. Therefore,
at least one of the window parameters (*WinTitle*, *WinText*,
*ExcludeTitle*, *ExcludeText*) must be non-blank.

## Related {#Related}

[WinWaitActive](WinWaitActive.htm), [WinWaitClose](WinWaitClose.htm),
[WinExist](WinExist.htm), [WinActive](WinActive.htm),
[ProcessWait](ProcessWait.htm),
[SetTitleMatchMode](SetTitleMatchMode.htm),
[DetectHiddenWindows](DetectHiddenWindows.htm)

## Examples {#Examples}

::: {#ExBasic .ex}
[](#ExBasic){.ex_number} Opens Notepad and waits a maximum of 3 seconds
until it exists. If WinWait times out, an error message is shown,
otherwise Notepad is minimized.

    Run "notepad.exe"
    if WinWait("Untitled - Notepad", , 3)
        WinMinimize ; Use the window found by WinWait.
    else
        MsgBox "WinWait timed out."
:::
