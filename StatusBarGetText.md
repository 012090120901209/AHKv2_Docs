# StatusBarGetText

Retrieves the text from a standard status bar control.

``` Syntax
Text := StatusBarGetText(Part#, WinTitle, WinText, ExcludeTitle, ExcludeText)
```

## Parameters {#Parameters}

Part#

:   Type: [Integer](../Concepts.htm#numbers)

    If omitted, it defaults to 1, which is usually the part that
    contains the text of interest. Otherwise, specify the part number of
    the bar to retrieve.

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

This function returns the text from a single part of the status bar
control.

## Error Handling {#Error_Handling}

A [TargetError](Error.htm#TargetError) is thrown if the target window
could not be found or does not contain a standard status bar.

An [OSError](Error.htm#OSError) is thrown if there was a problem sending
the SB_GETPARTS message or no reply was received within 2000 ms, or if
memory could not be allocated within the process which owns the status
bar.

## Remarks {#Remarks}

This function attempts to read the first *standard* status bar on a
window (Microsoft common control: msctls_statusbar32). Some programs use
their own status bars or special versions of the MS common control, in
which case the text cannot be retrieved.

Rather than using StatusBarGetText in a loop, it is usually more
efficient to use [StatusBarWait](StatusBarWait.htm), which contains
optimizations that avoid the overhead of repeated calls to
StatusBarGetText.

## Related {#Related}

[StatusBarWait](StatusBarWait.htm), [WinGetTitle](WinGetTitle.htm),
[WinGetText](WinGetText.htm), [ControlGetText](ControlGetText.htm)

## Examples {#Examples}

::: {#ExBasic .ex}
[](#ExBasic){.ex_number} Retrieves and analyzes the text from the first
part of a status bar.

    RetrievedText := StatusBarGetText(1, "Search Results")
    if InStr(RetrievedText, "found")
        MsgBox "Search results have been found."
:::
