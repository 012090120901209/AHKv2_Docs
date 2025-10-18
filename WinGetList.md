# WinGetList

Returns an array of unique ID numbers (HWNDs) for all existing windows
that match the specified criteria.

``` Syntax
HWNDs := WinGetList(WinTitle, WinText, ExcludeTitle, ExcludeText)
```

## Parameters {#Parameters}

WinTitle, WinText, ExcludeTitle, ExcludeText

:   Type: [String](../Concepts.htm#strings),
    [Integer](../Concepts.htm#numbers) or
    [Object](../Concepts.htm#objects)

    If each of these is blank or omitted, all windows on the entire
    system will be retrieved. Otherwise, specify for *WinTitle* a
    [window title or other criteria](../misc/WinTitle.htm) to identify
    the target window and/or for *WinText* a substring from a single
    text element of the target window (as revealed by the included
    Window Spy utility).

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

This function returns an array of unique ID numbers for all existing
windows that match the specified criteria. Each number is a [window
handle (HWND)](../misc/WinTitle.htm#ahk_id). If there is no matching
window, an empty array is returned.

For example, if the return value is assigned to a variable named `HWNDs`
and two matching windows are discovered, `HWNDs[1]` contains the ID of
the first window, `HWNDs[2]` contains the ID of the second window, and
`HWNDs.`[`Length`](Array.htm#Length) returns the number 2.

Windows are retrieved in order from topmost to bottommost (according to
how they are stacked on the desktop).

## Remarks {#Remarks}

The ID of the window under the mouse cursor can be retrieved with
[MouseGetPos](MouseGetPos.htm).

## Related {#Related}

[WinGetCount](WinGetCount.htm), [Win functions](Win.htm), [Control
functions](Control.htm)

## Examples {#Examples}

::: {#ExBasic .ex}
[](#ExBasic){.ex_number} Visits all windows on the entire system and
displays info about each of them.

    ids := WinGetList(,, "Program Manager")
    for this_id in ids
    {
        WinActivate this_id
        this_class := WinGetClass(this_id)
        this_title := WinGetTitle(this_id)
        Result := MsgBox(
        (
            "Visiting All Windows
            " A_Index " of " ids.Length "
            ahk_id " this_id "
            ahk_class " this_class "
            " this_title "

            Continue?"
        ),, 4)
        if (Result = "No")
            break
    }
:::
