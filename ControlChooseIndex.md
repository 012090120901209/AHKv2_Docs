# ControlChooseIndex

Sets the selection in a ListBox, ComboBox or Tab control to be the Nth
item.

``` Syntax
ControlChooseIndex N, Control , WinTitle, WinText, ExcludeTitle, ExcludeText
```

## Parameters {#Parameters}

N

:   Type: [Integer](../Concepts.htm#numbers)

    The index of the item, where 1 is the first item, 2 is the second,
    etc. To deselect all entries in a ListBox or ComboBox, specify 0.

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
control could not be found, or if the control\'s class name does not
contain \"Combo\", \"List\" or \"Tab\".

An [Error](Error.htm) or [OSError](Error.htm#OSError) is thrown if the
change could not be applied.

## Remarks {#Remarks}

To select all items in a *multi-select* listbox, follow this example:

``` NoIndent
PostMessage(0x0185, 1, -1, "ListBox1", WinTitle)  ; Select all listbox items. 0x0185 is LB_SETSEL.
```

Unlike [GuiControl.Choose()](GuiControl.htm#Choose), this function
raises a [Change](GuiOnEvent.htm#Change) or
[DoubleClick](GuiOnEvent.htm#DoubleClick) event.

To improve reliability, a delay is done automatically after each use of
this function. That delay can be changed via
[SetControlDelay](SetControlDelay.htm) or by assigning a value to
[A_ControlDelay](../Variables.htm#ControlDelay). For details, see
[SetControlDelay remarks](SetControlDelay.htm#Remarks).

## Related {#Related}

[ControlGetIndex](ControlGetIndex.htm),
[ControlChooseString](ControlChooseString.htm), [Choose method
(GuiControl object)](GuiControl.htm#Choose), [Control
functions](Control.htm)
