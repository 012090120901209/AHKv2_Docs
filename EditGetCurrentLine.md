# EditGetCurrentLine

Returns the line number in an Edit control where the caret (text insert
point) resides.

``` Syntax
CurrentLine := EditGetCurrentLine(Control , WinTitle, WinText, ExcludeTitle, ExcludeText)
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

This function returns the line number in an Edit control where the caret
(text insertion point) resides. The first line is 1. If there is text
selected in the control, the return value is the line number where the
selection begins.

## Error Handling {#Error_Handling}

An exception is thrown on failure, or if the window or control could not
be found.

## Related {#Related}

[EditGetCurrentCol](EditGetCurrentCol.htm),
[EditGetLineCount](EditGetLineCount.htm),
[EditGetLine](EditGetLine.htm),
[EditGetSelectedText](EditGetSelectedText.htm),
[EditPaste](EditPaste.htm), [Control functions](Control.htm)
