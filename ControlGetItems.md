# ControlGetItems

Returns an array of items/rows from a ListBox, ComboBox, or
DropDownList.

``` Syntax
Items := ControlGetItems(Control , WinTitle, WinText, ExcludeTitle, ExcludeText)
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

Type: [Array](Array.htm)

This function returns an array containing the text of each item or row.

## Error Handling {#Error_Handling}

A [TargetError](Error.htm#TargetError) is thrown if the window or
control could not be found, or if the control\'s class name does not
contain \"Combo\" or \"List\".

An [Error](Error.htm) is thrown on failure, such as if a message
returned a failure code or could not be sent.

## Remarks {#Remarks}

Some applications store their item data privately, which prevents their
text from being retrieved. In these cases, an exception will usually not
be thrown, but all the retrieved fields will be empty.

## Related {#Related}

[ListViewGetContent](ListViewGetContent.htm),
[WinGetList](WinGetList.htm), [Control functions](Control.htm)

## Examples {#Examples}

::: {#ExFor .ex}
[](#ExFor){.ex_number} Accesses the items one by one.

    for item in ControlGetItems("ComboBox1", WinTitle)
        MsgBox "Item number " A_Index " is " item
:::

::: {#ExIndex .ex}
[](#ExIndex){.ex_number} Accesses a specific item by index.

    items := ControlGetItems("ListBox1", WinTitle)
    MsgBox "The first item is " items[1]
    MsgBox "The last item is " items[-1]
:::
