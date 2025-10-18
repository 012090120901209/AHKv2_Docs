# WinSetStyle / WinSetExStyle

Changes the style or extended style of the specified window,
respectively.

``` Syntax
WinSetStyle Value , WinTitle, WinText, ExcludeTitle, ExcludeText
WinSetExStyle Value , WinTitle, WinText, ExcludeTitle, ExcludeText
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
    `WinSetStyle("+0x80")` or `WinSetStyle("^" StylesToToggle)`. This is
    because the [expression](../Variables.htm#Expressions)
    [`+123`](../Variables.htm#unary) produces 123 (without a prefix) and
    `^123` is a syntax error.

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

A [TargetError](Error.htm#TargetError) is thrown if the window could not
be found.

An [OSError](Error.htm#OSError) is thrown if the change could not be
applied.

## Remarks {#Remarks}

See the [styles table](../misc/Styles.htm) for a partial listing of
styles.

After applying certain style changes to a visible window, it might be
necessary to redraw the window using [WinRedraw](WinRedraw.htm).

The ID of the window under the mouse cursor can be retrieved with
[MouseGetPos](MouseGetPos.htm).

## Related {#Related}

[WinGetStyle / WinGetExStyle](WinGetStyle.htm), [ControlSetStyle /
ControlSetExStyle](ControlSetStyle.htm), [styles
table](../misc/Styles.htm), [Win functions](Win.htm), [Control
functions](Control.htm)

## Examples {#Examples}

::: {#ExStyle .ex}
[](#ExStyle){.ex_number} Removes the active window\'s title bar
(WS_CAPTION).

    WinSetStyle "-0xC00000", "A"
:::

::: {#ExExStyle .ex}
[](#ExExStyle){.ex_number} Toggles the WS_EX_TOOLWINDOW attribute, which
removes/adds Notepad from the alt-tab list.

    WinSetExStyle "^0x80", "ahk_class Notepad"
:::
