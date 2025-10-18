# StatusBarWait

Waits until a window\'s status bar contains the specified string.

``` Syntax
StatusBarWait BarText, Timeout, Part#, WinTitle, WinText, Interval, ExcludeTitle, ExcludeText
```

## Parameters {#Parameters}

BarText

:   Type: [String](../Concepts.htm#strings)

    If blank or omitted, the function waits for the status bar to become
    blank. Otherwise, specify the text or partial text for which the
    function will wait to appear. The text is case-sensitive and the
    matching behavior is determined by
    [SetTitleMatchMode](SetTitleMatchMode.htm), similar to *WinTitle*
    below.

    To instead wait for the bar\'s text to *change*, either use
    [StatusBarGetText](StatusBarGetText.htm) in a loop, or use the RegEx
    example at the bottom of this page.

Timeout

:   Type: [Integer](../Concepts.htm#numbers) or
    [Float](../Concepts.htm#numbers)

    If omitted, the function will wait indefinitely. Otherwise, it will
    wait no longer than this many seconds. To wait for a fraction of a
    second, specify a floating-point number, for example, 0.25 to wait
    for a maximum of 250 milliseconds.

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

Interval

:   Type: [Integer](../Concepts.htm#numbers)

    If omitted, it defaults to 50. Otherwise, specify how often the
    status bar should be checked while the function is waiting (in
    milliseconds).

## Return Value {#Return_Value}

Type: [Integer (boolean)](../Concepts.htm#boolean)

This function returns 1 (true) if a match was found or 0 (false) if the
function timed out.

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
which case such bars are not supported.

Rather than using [StatusBarGetText](StatusBarGetText.htm) in a loop, it
is usually more efficient to use StatusBarWait, which contains
optimizations that avoid the overhead of repeated calls to
[StatusBarGetText](StatusBarGetText.htm).

StatusBarWait determines its target window before it begins waiting for
a match. If that target window is closed, the function will stop waiting
even if there is another window matching the specified *WinTitle* and
*WinText*.

While the function is in a waiting state, new
[threads](../misc/Threads.htm) can be launched via
[hotkey](../Hotkeys.htm), [custom menu item](Menu.htm), or
[timer](SetTimer.htm).

## Related {#Related}

[StatusBarGetText](StatusBarGetText.htm),
[WinGetTitle](WinGetTitle.htm), [WinGetText](WinGetText.htm),
[ControlGetText](ControlGetText.htm)

## Examples {#Examples}

::: {#ExSearch .ex}
[](#ExSearch){.ex_number} Enters a new search pattern into an existing
Explorer/Search window.

    if WinExist("Search Results") ; Sets the Last Found window to simplify the below.
    {
        WinActivate
        Send "{tab 2}!o*.txt{enter}"  ; In the Search window, enter the pattern to search for.
        Sleep 400  ; Give the status bar time to change to "Searching".
        if StatusBarWait("found", 30)
            MsgBox "The search successfully completed."
        else
            MsgBox "The function timed out."
    }
:::

::: {#ExChange .ex}
[](#ExChange){.ex_number} Waits for the status bar of the active window
to change.

    SetTitleMatchMode "RegEx"  ; Accept regular expressions for use below.
    if WinExist("A")  ; Set the last-found window to be the active window (for use below).
    {
        OrigText := StatusBarGetText()
        StatusBarWait "^(?!^\Q" OrigText "\E$)"  ; This regular expression waits for any change to the text.
    }
:::
