# ControlSetChecked

Turns on (checks) or turns off (unchecks) a checkbox or radio button.

``` Syntax
ControlSetChecked NewSetting, Control , WinTitle, WinText, ExcludeTitle, ExcludeText
```

## Parameters {#Parameters}

NewSetting

:   Type: [Integer](../Concepts.htm#numbers)

    One of the following values:

    -   `1` or `True` turns on the setting
    -   `0` or `False` turns off the setting
    -   `-1` toggles the setting (sets it to the opposite of its current
        state)

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

An [OSError](Error.htm#OSError) is thrown if a message could not be sent
to the control.

## Remarks {#Remarks}

To ensure correct functionality, this function also sets the input focus
to the control.

To improve reliability, a delay is done automatically after each use of
this function. That delay can be changed via
[SetControlDelay](SetControlDelay.htm) or by assigning a value to
[A_ControlDelay](../Variables.htm#ControlDelay). For details, see
[SetControlDelay remarks](SetControlDelay.htm#Remarks).

## Related {#Related}

[ControlGetChecked](ControlGetChecked.htm), [Value property (GuiControl
object)](GuiControl.htm#Value), [Control functions](Control.htm)
