# ControlGetHwnd

Returns the unique ID number of the specified control.

``` Syntax
Hwnd := ControlGetHwnd(Control , WinTitle, WinText, ExcludeTitle, ExcludeText)
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

Type: [Integer](../Concepts.htm#numbers)

This function returns the [window handle
(HWND)](../misc/WinTitle.htm#ahk_id) of the specified control.

## Error Handling {#Error_Handling}

A [TargetError](Error.htm#TargetError) is thrown if the window or
control could not be found.

## Remarks {#Remarks}

A control\'s HWND is often used with [PostMessage](PostMessage.htm),
[SendMessage](SendMessage.htm), and [DllCall](DllCall.htm). On a related
note, a control\'s HWND can also be retrieved via
[MouseGetPos](MouseGetPos.htm). Finally, a control\'s HWND can be used
directly in a [WinTitle parameter](../misc/WinTitle.htm#ahk_id). This
also works on hidden controls even when
[DetectHiddenWindows](DetectHiddenWindows.htm) is Off.

## Related {#Related}

[WinGetID](WinGetID.htm), [Hwnd property (GuiControl
object)](GuiControl.htm#Hwnd), [Control functions](Control.htm)

## Examples {#Examples}

::: {#ExBasic .ex}
[](#ExBasic){.ex_number} Retrieves the unique ID number of the
Notepad\'s Edit control.

    editHwnd := ControlGetHwnd("Edit1", "ahk_class Notepad")
:::
