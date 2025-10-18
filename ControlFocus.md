# ControlFocus

Sets input focus to a given control on a window.

``` Syntax
ControlFocus Control , WinTitle, WinText, ExcludeTitle, ExcludeText
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

## Error Handling {#Error_Handling}

A [TargetError](Error.htm#TargetError) is thrown if the window or
control could not be found.

## Remarks {#Remarks}

To be effective, the control\'s window generally must not be minimized
or hidden.

To improve reliability, a delay is done automatically after each use of
this function. That delay can be changed via
[SetControlDelay](SetControlDelay.htm) or by assigning a value to
[A_ControlDelay](../Variables.htm#ControlDelay). For details, see
[SetControlDelay remarks](SetControlDelay.htm#Remarks).

When a control is focused in response to user input (such as pressing
the Tab key), the dialog manager applies additional effects which are
independent of the control having focus. These effects are not applied
by ControlFocus, and therefore the following limitations apply:

-   Focusing a button does not automatically make it the default button,
    as would normally happen if a button is focused by user input. The
    default button can usually be activated by pressing Enter.
-   If user input previously caused the default button to be temporarily
    changed, focusing a non-button control does not automatically
    restore the default highlight to the actual default button. Pressing
    Enter may then activate the default button even though it is not
    highlighted.
-   Focusing an edit control does not automatically select its text.
    Instead, the insertion point (caret) is typically positioned
    wherever it was last time the control had focus.

The
[WM_NEXTDLGCTL](https://learn.microsoft.com/windows/win32/dlgbox/wm-nextdlgctl)
message can be used to focus the control and apply these additional
effects. For example:

    WinExist("A") ; Set the Last Found Window to the active window
    hWndControl := ControlGetHwnd("Button1")  ; Get HWND of first Button
    SendMessage 0x0028, hWndControl, True  ; 0x0028 is WM_NEXTDLGCTL

## Related {#Related}

[SetControlDelay](SetControlDelay.htm),
[ControlGetFocus](ControlGetFocus.htm), [Control functions](Control.htm)

## Examples {#Examples}

::: {#ExBasic .ex}
[](#ExBasic){.ex_number} Sets the input focus to the OK button.

    ControlFocus "OK", "Some Window Title"
:::
