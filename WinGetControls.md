# WinGetControls

Returns an array of names (ClassNNs) for all controls in the specified
window.

``` Syntax
ClassNNs := WinGetControls(WinTitle, WinText, ExcludeTitle, ExcludeText)
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

Type: [Array](Array.htm)

This function returns an array of names for all controls in the
specified window. Each name consists of the control\'s class name
followed immediately by its sequence number (ClassNN), as shown by
Window Spy.

For example, if the return value is assigned to a variable named
`ClassNNs` and two controls are present, `ClassNNs[1]` contains the name
of the first control, `ClassNNs[2]` contains the name of the second
control, and `ClassNNs.`[`Length`](Array.htm#Length) returns the number
2.

Controls are sorted according to their Z-order, which is usually the
same order as the navigation order via [Tab]{.kbd} if the window
supports tabbing.

## Error Handling {#Error_Handling}

A [TargetError](Error.htm#TargetError) is thrown if the window could not
be found.

## Remarks {#Remarks}

The ID of the window or control under the mouse cursor can be retrieved
with [MouseGetPos](MouseGetPos.htm).

## Related {#Related}

[WinGetControlsHwnd](WinGetControlsHwnd.htm), [Win functions](Win.htm),
[Control functions](Control.htm)

## Examples {#Examples}

::: {#ExBasic .ex}
[](#ExBasic){.ex_number} Extracts the individual control names from the
active window\'s control list.

    for n, ctrl in WinGetControls("A")
    {
        Result := MsgBox("Control #" n " is '" ctrl "'. Continue?",, 4)
        if (Result = "No")
            break
    }
:::

::: {#ExRealTime .ex}
[](#ExRealTime){.ex_number} Displays in real time the active window\'s
control list.

    SetTimer WatchActiveWindow, 200

    WatchActiveWindow()
    {
        try
        {
            Controls := WinGetControls("A")
            ControlList := ""
            for ClassNN in Controls
                ControlList .= ClassNN . "`n"
            if (ControlList = "")
                ToolTip "The active window has no controls."
            else
                ToolTip ControlList
        }
        catch TargetError
            ToolTip "No visible window is active."
    }
:::
