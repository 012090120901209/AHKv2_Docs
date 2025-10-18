# WinGetIDLast

Returns the unique ID number (HWND) of the last/bottommost window if
there is more than one match.

``` Syntax
HWND := WinGetIDLast(WinTitle, WinText, ExcludeTitle, ExcludeText)
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

This function returns the [window handle
(HWND)](../misc/WinTitle.htm#ahk_id) of the last/bottommost window if
there is more than one match.

## Error Handling {#Error_Handling}

A [TargetError](Error.htm#TargetError) is thrown if the window could not
be found.

## Remarks {#Remarks}

If there is only one match, it performs identically to
[WinGetID](WinGetID.htm).

A window\'s ID number is valid only during its lifetime. In other words,
if an application restarts, all of its windows will get new ID numbers.

The ID of the window under the mouse cursor can be retrieved with
[MouseGetPos](MouseGetPos.htm). To discover the HWND of a control (for
use with [PostMessage](PostMessage.htm), [SendMessage](SendMessage.htm)
or [DllCall](DllCall.htm)), use [ControlGetHwnd](ControlGetHwnd.htm) or
[MouseGetPos](MouseGetPos.htm).

## Related {#Related}

[WinGetID](WinGetID.htm), [ControlGetHwnd](ControlGetHwnd.htm), [Hwnd
property (Gui object)](Gui.htm#Hwnd), [Win functions](Win.htm), [Control
functions](Control.htm)
