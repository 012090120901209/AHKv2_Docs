# ControlGetFocus

Retrieves which control of the target window has keyboard focus, if any.

``` Syntax
HWND := ControlGetFocus(WinTitle, WinText, ExcludeTitle, ExcludeText)
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
(HWND)](../misc/WinTitle.htm#ahk_id) of the focused control.

If none of the target window\'s controls has focus, the return value is
0.

## Error Handling {#Error_Handling}

A [TargetError](Error.htm#TargetError) is thrown if there is a problem
determining the target window or control.

An [OSError](Error.htm#OSError) is thrown if there is a problem
determining the focus.

## Remarks {#Remarks}

The control retrieved by this function is the one that has keyboard
focus, that is, the one that would receive keystrokes if the user were
to type any.

The target window must be active to have a focused control, but even the
active window may lack a focused control.

## Related {#Related}

[ControlFocus](ControlFocus.htm), [Control functions](Control.htm)

## Examples {#Examples}

::: {#ExBasic .ex}
[](#ExBasic){.ex_number} Reports the HWND and ClassNN of the active
window\'s focused control.

    FocusedHwnd := ControlGetFocus("A")
    FocusedClassNN := ControlGetClassNN(FocusedHwnd)
    MsgBox 'Control with focus = {Hwnd: ' FocusedHwnd ', ClassNN: "' FocusedClassNN '"}'
:::
