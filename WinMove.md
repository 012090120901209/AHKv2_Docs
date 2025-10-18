# WinMove

Changes the position and/or size of the specified window.

``` Syntax
WinMove X, Y, Width, Height, WinTitle, WinText, ExcludeTitle, ExcludeText
```

## Parameters {#Parameters}

X, Y

:   Type: [Integer](../Concepts.htm#numbers)

    If either is omitted, the position in that dimension will not be
    changed. Otherwise, specify the X and Y coordinates (in pixels) of
    the upper left corner of the target window\'s new location. The
    upper-left pixel of the screen is at 0, 0.

Width, Height

:   Type: [Integer](../Concepts.htm#numbers)

    If either is omitted, the size in that dimension will not be
    changed. Otherwise, specify the new width and height of the window
    (in pixels).

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

An [OSError](Error.htm#OSError) is thrown if an internal function call
reported failure. However, success may be reported even if the window
has not moved, such as if the window restricts its own movement.

## Remarks {#Remarks}

If *Width* or *Height* is small (or negative), most windows with a title
bar will generally go no smaller than 112 x 27 pixels (however, some
types of windows may have a different minimum size). If *Width* or
*Height* is large, most windows will go no larger than approximately 12
pixels beyond the dimensions of the desktop.

Negative X and Y coordinates are allowed to support multi-monitor
systems and to move a window entirely off-screen.

Although WinMove cannot move minimized windows, it can move hidden
windows if [DetectHiddenWindows](DetectHiddenWindows.htm) is on.

The speed of WinMove is affected by [SetWinDelay](SetWinDelay.htm).

On systems with multiple screens which have different DPI settings, the
final position and size of the window may differ from the requested
values due to [OS DPI scaling](../misc/DPIScaling.htm).

## Related {#Related}

[ControlMove](ControlMove.htm), [WinGetPos](WinGetPos.htm),
[WinHide](WinHide.htm), [WinMinimize](WinMinimize.htm),
[WinMaximize](WinMaximize.htm), [Win functions](Win.htm)

## Examples {#Examples}

::: {#ExLastFound .ex}
[](#ExLastFound){.ex_number} Opens the calculator, waits until it exists
and moves it to the upper-left corner of the screen.

    Run "calc.exe"
    WinWait "Calculator"
    WinMove 0, 0 ; Use the window found by WinWait.
:::

::: {#ExBasic .ex}
[](#ExBasic){.ex_number} Creates a fixed-size popup window that shows
the contents of the clipboard, and moves it to the upper-left corner of
the screen.

    MyGui := Gui("ToolWindow -Sysmenu Disabled", "The clipboard contains:")
    MyGui.Add("Text",, A_Clipboard)
    MyGui.Show("w400 h300")
    WinMove 0, 0,,, MyGui
    MsgBox "Press OK to dismiss the popup window"
    MyGui.Destroy()
:::

::: {#ExCenter .ex}
[](#ExCenter){.ex_number} Centers a window on the screen.

    CenterWindow("ahk_class Notepad")

    CenterWindow(WinTitle)
    {
        WinGetPos ,, &Width, &Height, WinTitle
        WinMove (A_ScreenWidth/2)-(Width/2), (A_ScreenHeight/2)-(Height/2),,, WinTitle
    }
:::
