# ControlSetStyle / ControlSetExStyle

Changes the style or extended style of the specified control,
respectively.

``` Syntax
ControlSetStyle Value, Control , WinTitle, WinText, ExcludeTitle, ExcludeText
ControlSetExStyle Value, Control , WinTitle, WinText, ExcludeTitle, ExcludeText
```

## Parameters {#Parameters}

Value

:   Type: [Integer](../Concepts.htm#numbers) or
    [String](../Concepts.htm#strings)

    Pass a positive integer to completely overwrite the window\'s style;
    that is, to set it to *Value*.

    To easily add, remove or toggle styles, pass a numeric string
    prefixed with a plus sign (+), minus sign (-) or caret (\^),
    respectively. The new style value is calculated as shown below
    (where *CurrentStyle* could be retrieved with
    [ControlGetStyle](ControlGetStyle.htm),
    [ControlGetExStyle](ControlGetStyle.htm),
    [WinGetStyle](WinGetStyle.htm) or [WinGetExStyle](WinGetStyle.htm)):

      Operation   Prefix   Example     Formula
      ----------- -------- ----------- -------------------------------------
      Add         \+       `"+0x80"`   `NewStyle := CurrentStyle | Value`
      Remove      \-       `"-0x80"`   `NewStyle := CurrentStyle & ~Value`
      Toggle      \^       `"^0x80"`   `NewStyle := CurrentStyle ^ Value`

    If *Value* is a negative integer, it is treated the same as the
    corresponding numeric string.

    To use the + or \^ prefix literally in an expression, the prefix or
    value must be enclosed in quote marks. For example:
    `ControlSetStyle("+0x80")` or `ControlSetStyle("^" StylesToToggle)`.
    This is because the [expression](../Variables.htm#Expressions)
    [`+123`](../Variables.htm#unary) produces 123 (without a prefix) and
    `^123` is a syntax error.

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

An [OSError](Error.htm#OSError) is thrown if the style could not be
changed. Partial change is considered a success.

## Remarks {#Remarks}

See the [styles table](../misc/Styles.htm) for a partial listing of
styles.

Certain style changes require that the entire window be redrawn using
[WinRedraw](WinRedraw.htm).

## Related {#Related}

[ControlGetStyle / ControlGetExStyle](ControlGetStyle.htm), [WinSetStyle
/ WinSetExStyle](WinSetStyle.htm), [styles table](../misc/Styles.htm),
[Control functions](Control.htm)

## Examples {#Examples}

::: {#ExBasic .ex}
[](#ExBasic){.ex_number} Sets the WS_BORDER style of the Notepad\'s Edit
control to its opposite state.

    ControlSetStyle("^0x800000", "Edit1", "ahk_class Notepad")
:::
