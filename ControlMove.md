# ControlMove

Moves or resizes a control.

``` Syntax
ControlMove X, Y, Width, Height, Control, WinTitle, WinText, ExcludeTitle, ExcludeText
```

## Parameters {#Parameters}

X, Y

:   Type: [Integer](../Concepts.htm#numbers)

    If either is omitted, the control\'s position in that dimension will
    not be changed. Otherwise, specify the X and Y coordinates (in
    pixels) of the upper left corner of the control\'s new location. The
    coordinates are relative to the upper-left corner of the target
    window\'s [client area](CoordMode.htm#Client);
    [ControlGetPos](ControlGetPos.htm) can be used to determine them.

Width, Height

:   Type: [Integer](../Concepts.htm#numbers)

    If either is omitted, the control\'s size in that dimension will not
    be changed. Otherwise, specify the new width and height of the
    control (in pixels).

Control

:   Type: [String](../Concepts.htm#strings),
    [Integer](../Concepts.htm#numbers) or
    [Object](../Concepts.htm#objects)

    The control\'s ClassNN, text or HWND, or an object with a `Hwnd`
    property. For details, see [The Control
    Parameter](Control.htm#Parameter).

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

A [TargetError](Error.htm#TargetError) is thrown if the window or
control could not be found.

An [OSError](Error.htm#OSError) is thrown if the control\'s current
position could not be determined.

## Remarks {#Remarks}

To improve reliability, a delay is done automatically after each use of
this function. That delay can be changed via
[SetControlDelay](SetControlDelay.htm) or by assigning a value to
[A_ControlDelay](../Variables.htm#ControlDelay). For details, see
[SetControlDelay remarks](SetControlDelay.htm#Remarks).

## Related {#Related}

[ControlGetPos](ControlGetPos.htm), [WinMove](WinMove.htm),
[SetControlDelay](SetControlDelay.htm), [Control functions](Control.htm)

## Examples {#Examples}

::: {#ExControlMoveTimer .ex}
[](#ExControlMoveTimer){.ex_number} Demonstrates how to manipulate the
OK button of an input box while the script is waiting for user input.

    SetTimer ControlMoveTimer
    IB := InputBox(, "My Input Box")

    ControlMoveTimer()
    {
        if !WinExist("My Input Box")
            return
        ; Otherwise the above set the "last found" window for us:
        SetTimer , 0
        WinActivate
        ControlMove 10,, 200,, "OK"  ; Move the OK button to the left and increase its width.
    }
:::
