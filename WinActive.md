# WinActive

Checks if the specified window is active and returns its unique ID
(HWND).

``` Syntax
UniqueID := WinActive(WinTitle, WinText, ExcludeTitle, ExcludeText)
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

This function returns the [unique ID
(HWND)](../misc/WinTitle.htm#ahk_id) of the active window if it matches
the specified criteria, or 0 if it does not.

Since all non-zero numbers are seen as \"true\", the statement
`if WinActive(WinTitle)` is true whenever *WinTitle* is active.

## Remarks {#Remarks}

If the active window is a qualified match, the [Last Found
Window](../misc/WinTitle.htm#LastFoundWindow) will be updated to be the
active window.

An easy way to retrieve the unique ID of the active window is with
`ActiveHwnd := WinExist("A")`.

[SetWinDelay](SetWinDelay.htm) does not apply to this function.

## Related {#Related}

[WinExist](WinExist.htm), [SetTitleMatchMode](SetTitleMatchMode.htm),
[DetectHiddenWindows](DetectHiddenWindows.htm), [Last Found
Window](../misc/WinTitle.htm#LastFoundWindow),
[WinActivate](WinActivate.htm), [WinWaitActive](WinWaitActive.htm),
[WinWait](WinWait.htm), [WinWaitClose](WinWaitClose.htm),
[#HotIf](_HotIf.htm)

## Examples {#Examples}

::: {#ExLastFound .ex}
[](#ExLastFound){.ex_number} Closes either Notepad or another window,
depending on which of them was found by the WinActive functions above.
Note that the space between an \"ahk\_\" keyword and its criterion value
can be omitted; this is especially useful when using variables, as shown
by the second WinActive.

    if WinActive("ahk_class Notepad") or WinActive("ahk_class" ClassName)
        WinClose ; Use the window found by WinActive.
:::
