# ControlGetClassNN

Returns the ClassNN (class name and sequence number) of the specified
control.

``` Syntax
ClassNN := ControlGetClassNN(Control , WinTitle, WinText, ExcludeTitle, ExcludeText)
```

## Parameters {#Parameters}

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

## Return Value {#Return_Value}

Type: [String](../Concepts.htm#strings)

This function returns the ClassNN (class name and sequence number) of
the specified control.

## Error Handling {#Error_Handling}

A [TargetError](Error.htm#TargetError) is thrown if there is a problem
determining the target window or control.

An [Error](Error.htm) or [OSError](Error.htm#OSError) is thrown if the
ClassNN could not be determined.

## Remarks {#Remarks}

A control\'s ClassNN is the name of its window class followed by its
sequence number within the top-level window which contains it. For
example, \"Edit1\" is the first Edit control on a window and
\"Button12\" is the twelth button.

A control\'s ClassNN can also be determined via Window Spy,
[MouseGetPos](MouseGetPos.htm) or [WinGetControls](WinGetControls.htm).

Some class names include digits which are not part of the control\'s
sequence number. For example, \"SysListView321\" is the window\'s first
ListView control, not its 321st. To retrieve the class name without the
sequence number, pass the control\'s HWND to
[WinGetClass](WinGetClass.htm).

## Related {#Related}

[WinGetClass](WinGetClass.htm), [WinGetControls](WinGetControls.htm),
[ClassNN property (GuiControl object)](GuiControl.htm#ClassNN),
[MouseGetPos](MouseGetPos.htm), [Control functions](Control.htm)

## Examples {#Examples}

::: {#ExBasic .ex}
[](#ExBasic){.ex_number} Retrieves the ClassNN of the currently focused
control.

    classNN := ControlGetClassNN(ControlGetFocus("A"))
:::
