# WinGetText

Retrieves the text from the specified window.

``` Syntax
Text := WinGetText(WinTitle, WinText, ExcludeTitle, ExcludeText)
```

## Parameters {#Parameters}

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

This function returns the text of the specified window.

## Error Handling {#Error_Handling}

A [TargetError](Error.htm#TargetError) is thrown if the window could not
be found.

An [Error](Error.htm) is thrown if there was a problem retrieving the
window\'s text.

## Remarks {#Remarks}

The text retrieved is generally the same as what Window Spy shows for
that window. However, if [DetectHiddenText](DetectHiddenText.htm) has
been turned off, hidden text is omitted from the return value.

Each text element ends with a carriage return and linefeed (CR+LF),
which can be represented in the script as \`r\`n. To extract individual
lines or substrings, use functions such as [InStr](InStr.htm) and
[SubStr](SubStr.htm). A [parsing loop](LoopParse.htm) can also be used
to examine each line or word one by one.

If the retrieved text appears to be truncated (incomplete), it may be
necessary to retrieve the text by sending the WM_GETTEXT message via
[SendMessage](SendMessage.htm) instead. This is because some
applications do not respond properly to the WM_GETTEXTLENGTH message,
which causes AutoHotkey to make the return value too small to fit all
the text.

This function might use a large amount of RAM if the target window (e.g.
an editor with a large document open) contains a large quantity of text.
To avoid this, it might be possible to retrieve only portions of the
window\'s text by using [ControlGetText](ControlGetText.htm) instead. In
any case, a variable\'s memory can be freed later by assigning it to
nothing, i.e. `Text := ""`.

It is not necessary to do `SetTitleMatchMode "Slow"` because WinGetText
always retrieves the text using the slow mode (since it works on a
broader range of control types).

To retrieve an array of all controls in a window, use
[WinGetControls](WinGetControls.htm) or
[WinGetControlsHwnd](WinGetControlsHwnd.htm).

## Related {#Related}

[ControlGetText](ControlGetText.htm), [WinGetTitle](WinGetTitle.htm),
[WinGetPos](WinGetPos.htm)

## Examples {#Examples}

::: {#ExBasic .ex}
[](#ExBasic){.ex_number} Opens the calculator, waits until it exists,
and retrieves and reports its text.

    Run "calc.exe"
    WinWait "Calculator"
    MsgBox "The text is:`n" WinGetText() ; Use the window found by WinWait.
:::
