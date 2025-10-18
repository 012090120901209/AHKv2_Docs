# ControlGetIndex

Returns the index of the currently selected entry or tab in a ListBox,
ComboBox or Tab control.

``` Syntax
Index := ControlGetIndex(Control , WinTitle, WinText, ExcludeTitle, ExcludeText)
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

This function returns the index of the currently selected entry or tab.
The first entry or tab is 1, the second is 2, etc. If no entry or tab is
selected, the return value is 0.

## Error Handling {#Error_Handling}

A [TargetError](Error.htm#TargetError) is thrown if the window or
control could not be found, or if the control\'s class name does not
contain \"Combo\", \"List\" or \"Tab\".

An [OSError](Error.htm#OSError) is thrown if a message could not be sent
to the control.

## Remarks {#Remarks}

To instead discover how many tabs (pages) exist in a tab control, follow
this example:

    TabCount := SendMessage(0x1304,,, "SysTabControl321", WinTitle)  ; 0x1304 is TCM_GETITEMCOUNT.

## Related {#Related}

[ControlChooseIndex](ControlChooseIndex.htm),
[ControlGetChoice](ControlGetChoice.htm),
[ControlChooseString](ControlChooseString.htm), [Value property
(GuiControl object)](GuiControl.htm#Value), [Choose method (GuiControl
object)](GuiControl.htm#Choose), [Control functions](Control.htm)

## Examples {#Examples}

::: {#ExTab .ex}
[](#ExTab){.ex_number} Retrieves the active tab number of the first Tab
control.

    WhichTab := ControlGetIndex("SysTabControl321", "Some Window Title")
    MsgBox "Tab #" WhichTab " is active."
:::
