# WinSetTransparent

Makes the specified window semi-transparent.

``` Syntax
WinSetTransparent N, WinTitle, WinText, ExcludeTitle, ExcludeText
```

## Parameters {#Parameters}

N

:   Type: [Integer](../Concepts.htm#numbers) or
    [String](../Concepts.htm#strings)

    To enable transparency, specify a number between 0 and 255
    indicating the degree of transparency: 0 makes the window invisible
    while 255 makes it opaque.

    `"Off"` (case-insensitive) or an empty string may be specified to
    completely turn off transparency for a window. This is functionally
    identical to [`WinSetTransColor`](WinSetTransColor.htm)` "Off"`.
    Specifying Off is different than specifying 255 because it may
    improve performance and reduce usage of system resources (but
    probably only when desktop composition is disabled).

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

For example, to make the task bar transparent, use
`WinSetTransparent 150, "ahk_class Shell_TrayWnd"`. Similarly, to make
the classic Start Menu transparent, see [example #2](#ExTransStartMenu).
To make the Start Menu\'s submenus transparent, also include the script
from [example #3](#ExTransMenu).

Setting the transparency level to 255 before using Off might avoid
window redrawing problems such as a black background. If the window
still fails to be redrawn correctly, see [WinRedraw](WinRedraw.htm) for
a possible workaround.

The ID of the window under the mouse cursor can be retrieved with
[MouseGetPos](MouseGetPos.htm).

## Related {#Related}

[WinSetTransColor](WinSetTransColor.htm), [Win functions](Win.htm),
[Control functions](Control.htm)

## Examples {#Examples}

::: {#ExBasic .ex}
[](#ExBasic){.ex_number} Makes Notepad a little bit transparent.

    WinSetTransparent 200, "Untitled - Notepad"
:::

::: {#ExTransStartMenu .ex}
[](#ExTransStartMenu){.ex_number} Makes the classic Start Menu
transparent (to additionally make the Start Menu\'s submenus
transparent, see [example #3](#ExTransMenu)).

    DetectHiddenWindows True
    WinSetTransparent 150, "ahk_class BaseBar"
:::

::: {#ExTransMenu .ex}
[](#ExTransMenu){.ex_number} Makes all or selected menus transparent
throughout the system as soon as they appear. Note that although such a
script cannot make its own menus transparent, it can make those of other
scripts transparent.

    SetTimer WatchForMenu, 5

    WatchForMenu()
    {
        DetectHiddenWindows True  ; Might allow detection of menu sooner.
        if WinExist("ahk_class #32768")
            WinSetTransparent 150  ; Uses the window found by the above line.
    }
:::

::: {#ExTransHotkey .ex}
[](#ExTransHotkey){.ex_number} Demonstrates the effects of
WinSetTransparent and [WinSetTransColor](WinSetTransColor.htm). Note: If
you press one of the hotkeys while the mouse cursor is hovering over a
pixel that is invisible as a result of TransColor, the window visible
beneath that pixel will be acted upon instead!

    #t::  ; Press Win+T to make the color under the mouse cursor invisible.
    {
        MouseGetPos &MouseX, &MouseY, &MouseWin
        MouseRGB := PixelGetColor(MouseX, MouseY)
        ; It seems necessary to turn off any existing transparency first:
        WinSetTransColor "Off", MouseWin
        WinSetTransColor MouseRGB " 220", MouseWin
    }

    #o::  ; Press Win+O to turn off transparency for the window under the mouse.
    {
        MouseGetPos ,, &MouseWin
        WinSetTransColor "Off", MouseWin
    }

    #g::  ; Press Win+G to show the current settings of the window under the mouse.
    {
        MouseGetPos ,, &MouseWin
        TransDegree := WinGetTransparent(MouseWin)
        TransColor := WinGetTransColor(MouseWin)
        ToolTip "Translucency:`t" TransDegree "`nTransColor:`t" TransColor
    }
:::
