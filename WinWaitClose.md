# WinWaitClose

Waits until no matching windows can be found.

``` Syntax
Boolean := WinWaitClose(WinTitle, WinText, Timeout, ExcludeTitle, ExcludeText)
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

Type: [Integer (boolean)](../Concepts.htm#boolean)

This function returns 0 (false) if the function timed out or 1 (true)
otherwise.

## Remarks {#Remarks}

Whenever no matching windows exist, the function will not wait for
*Timeout* to expire. Instead, it will immediately return 1 and the
script will continue executing. Conversely, the function may continue
waiting even after a matching window is closed, until no more matching
windows can be found.

If *WinTitle* specifies a [pure HWND](../misc/WinTitle.htm#ahk_id) (as
an [Integer](../Concepts.htm#numbers) or an [Object](../Objects.htm)
with a HWND property), hidden windows are detected only when using
[DetectHiddenWindows](DetectHiddenWindows.htm). This only applies to
[WinWait](WinWait.htm) and WinWaitClose; for other windowing functions,
specifying a pure HWND causes hidden windows to be detected regardless
of DetectHiddenWindows.

Since `"A"` matches whichever window is active at any given moment,
`WinWaitClose "A"` typically waits indefinitely. To instead wait for the
current active window to close, specify its title or unique ID as in the
following example:

    WinWaitClose WinExist("A")

WinWaitClose updates the [Last Found
Window](../misc/WinTitle.htm#LastFoundWindow) whenever it finds a
matching window. One use for this is to identify or operate on the
window after the function times out. For example:

    Gui("", "Test window " Random()).Show("w300 h50")  ; Show a test window.
    if !WinWaitClose("Test",, 5)  ; Wait 5 seconds for someone to close it.
    {
        MsgBox "Window not yet closed: " WinGetTitle()
        WinClose  ; Close the window found by WinWaitClose.
    }

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

[WinClose](WinClose.htm), [WinWait](WinWait.htm),
[WinWaitActive](WinWaitActive.htm), [WinExist](WinExist.htm),
[WinActive](WinActive.htm), [ProcessWaitClose](ProcessWaitClose.htm),
[SetTitleMatchMode](SetTitleMatchMode.htm),
[DetectHiddenWindows](DetectHiddenWindows.htm)

## Examples {#Examples}

::: {#ExBasic .ex}
[](#ExBasic){.ex_number} Opens Notepad, waits until it exists and then
waits until it is closed.

    Run "notepad.exe"
    WinWait "Untitled - Notepad"
    WinWaitClose ; Use the window found by WinWait.
    MsgBox "Notepad is now closed."
:::
