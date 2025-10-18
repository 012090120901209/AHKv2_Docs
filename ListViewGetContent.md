# ListViewGetContent

Returns a list of items/rows from a ListView.

``` Syntax
List := ListViewGetContent(Options, Control, WinTitle, WinText, ExcludeTitle, ExcludeText)
```

## Parameters {#Parameters}

Options

:   Type: [String](../Concepts.htm#strings)

    Specifices what to retrieve. If blank or omitted, all the text in
    the ListView is retrieved. Otherwise, specify zero or more of the
    following words, each separated from the next with a space or tab:

    **Selected:** Returns only the selected (highlighted) rows rather
    than all rows. If none, the return value is blank.

    **Focused:** Returns only the focused row. If none, the return value
    is blank.

    **Col***N*: Returns only the *N*th column (field) rather than all
    columns. Replace *N* with a number of your choice. For example, Col4
    returns the fourth column.

    **Count:** Returns a single number that is the total number of rows
    in the ListView.

    **Count Selected:** Returns the number of selected (highlighted)
    rows.

    **Count Focused:** Returns the row number (position) of the focused
    row (0 if none).

    **Count Col:** Returns the number of columns in the control (or -1
    if the count cannot be determined).

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

This function returns a list of items/rows. Within each row, each field
(column) except the last will end with a tab character (\`t). To access
the items/rows individually, use a [parsing loop](LoopParse.htm) as in
[example #1](#ExListView).

## Error Handling {#Error_Handling}

A [TargetError](Error.htm#TargetError) is thrown if the window or
control could not be found.

An [OSError](Error.htm#OSError) is thrown if a message could not be sent
to the control, or if the process owning the ListView could not be
opened, perhaps due to a lack of user permissions or because it is
locked.

A [ValueError](Error.htm#ValueError) is thrown if the [Col*N*
option](#ColN) specifies a nonexistent column.

## Remarks {#Remarks}

Some applications store their ListView text privately, which prevents
their text from being retrieved. In these cases, an exception will
usually not be thrown, but all the retrieved fields will be empty.

The columns in a ListView can be resized via
[SendMessage](SendMessage.htm) as shown in this example:

    SendMessage(0x101E, 0, 80, "SysListView321", WinTitle)  ; 0x101E is the message LVM_SETCOLUMNWIDTH.

In the above, 0 indicates the first column (specify 1 for the second, 2
for the third, etc.) Also, 80 is the new width. Replace 80 with -1 to
autosize the column. Replace it with -2 to do the same but also take
into account the header text width.

## Related {#Related}

[ControlGetItems](ControlGetItems.htm), [WinGetList](WinGetList.htm),
[Control functions](Control.htm)

## Examples {#Examples}

::: {#ExListView .ex}
[](#ExListView){.ex_number} Extracts the individual rows and fields out
of a ListView.

    List := ListViewGetContent("Selected", "SysListView321", WinTitle)
    Loop Parse, List, "`n"  ; Rows are delimited by linefeeds (`n).
    {
        RowNumber := A_Index
        Loop Parse, A_LoopField, A_Tab  ; Fields (columns) in each row are delimited by tabs (A_Tab).
            MsgBox "Row #" RowNumber " Col #" A_Index " is " A_LoopField
    }
:::
