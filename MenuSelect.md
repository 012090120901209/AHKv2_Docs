# MenuSelect

Invokes a menu item from the menu bar of the specified window.

``` Syntax
MenuSelect WinTitle, WinText, Menu , SubMenu1, SubMenu2, SubMenu3, SubMenu4, SubMenu5, SubMenu6, ExcludeTitle, ExcludeText
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

Menu

:   Type: [String](../Concepts.htm#strings)

    The name (or a prefix of the name) of the top-level menu item, e.g.
    `"File"`, `"Edit"`, `"View"`. It can also be the position of the
    desired menu item by using `"1&"` to represent the first menu,
    `"2&"` the second, and so on.

    The search is case-insensitive according to the rules of the current
    user\'s locale, and stops at the first matching item. The use of
    ampersand (&) to indicate the underlined letter in a menu item is
    *usually* not necessary (i.e. `"&File"` is the same as `"File"`).

    **Known limitation:** If the parameter contains an ampersand, it
    must match the item name exactly, including all non-literal
    ampersands (which are hidden or displayed as an underline). If the
    parameter does not contain an ampersand, all ampersands are ignored,
    including literal ones. For example, an item displayed as \"a & b\"
    may match a parameter value of `a && b` or `a b`.

    Specify `"0&"` to use the window\'s [system menu](#sys).

SubMenu1

:   Type: [String](../Concepts.htm#strings)

    The name of the menu item to select or its position. This can be
    omitted if the top-level item does not contain a menu (rare).

SubMenu2, SubMenu3, SubMenu4, SubMenu5, SubMenu6

:   Type: [String](../Concepts.htm#strings)

    If the previous submenu itself contains a menu, this is the name of
    the menu item inside, or its position.

## Error Handling {#Error_Handling}

A [TargetError](Error.htm#TargetError) is thrown if the window or
control could not be found, or does not have a standard Win32 menu.

A [ValueError](Error.htm#ValueError) is thrown if a menu, submenu or
menu item could not be found, or if the final menu parameter corresponds
to a menu item which opens a submenu.

## Remarks {#Remarks}

For this function to work, the target window need not be active.
However, some windows might need to be in a
[non-minimized](WinRestore.htm) state.

This function **will not work** with applications that use non-standard
menu bars. Examples include Microsoft Outlook and Outlook Express, which
use disguised toolbars for their menu bars. In these cases, consider
using [ControlSend](ControlSend.htm) or [PostMessage](PostMessage.htm),
which should be able to interact with some of these non-standard menu
bars.

The menu name parameters can also specify positions. This method exists
to support menus that don\'t contain text (perhaps because they contain
pictures of text rather than actual text). Position 1& is the first menu
item (e.g. the File menu), position 2& is the second menu item (e.g. the
Edit menu), and so on. Menu separator lines count as menu items for the
purpose of determining the position of a menu item.

## System Menu {#sys}

*Menu* can be `"0&"` to select an item within the window\'s system menu,
which typically appears when the user presses [Alt]{.kbd}+[Space]{.kbd}
or clicks on the icon in the window\'s title bar. For example:

    ; Paste a command into cmd.exe without activating the window.
    A_Clipboard := "echo Hello, world!`r"
    MenuSelect "ahk_exe cmd.exe",, "0&", "Edit", "Paste"

**Caution:** Use this only on windows which have custom items in their
system menu.

If the window does not already have a custom system menu, a copy of the
standard system menu will be created and assigned to the target window
as a side effect. This copy is destroyed by the system when the script
exits, leaving other scripts unable to access it. Therefore, avoid using
0& for the standard items which appear on all windows. Instead, post the
[WM_SYSCOMMAND](https://learn.microsoft.com/windows/win32/menurc/wm-syscommand)
message directly. For example:

    ; Like [WinMinimize "A"], but also play the system sound for minimizing.
    WM_SYSCOMMAND := 0x0112
    SC_MINIMIZE := 0xF020
    PostMessage WM_SYSCOMMAND, SC_MINIMIZE, 0,, "A"

## Related {#Related}

[ControlSend](ControlSend.htm), [PostMessage](PostMessage.htm)

## Examples {#Examples}

::: {#ExBasic .ex}
[](#ExBasic){.ex_number} Selects `File -> Open`{.no-highlight} in
Notepad. This example may fail on Windows 11 or later, as it requires
the classic version of Notepad.

    MenuSelect "Untitled - Notepad",, "File", "Open"
:::

::: {#ExPos .ex}
[](#ExPos){.ex_number} Same as above except it is done by position
instead of name. On Windows 10, 2& must be replaced with 3& due to the
new \"New Window\" menu item. This example may fail on Windows 11 or
later, as it requires the classic version of Notepad.

    MenuSelect "Untitled - Notepad",, "1&", "2&"
:::

::: {#ExMainWin .ex}
[](#ExMainWin){.ex_number} Selects
`View -> Lines most recently executed`{.no-highlight} in the [main
window](../Program.htm#main-window).

    WinShow "ahk_class AutoHotkey"
    MenuSelect "ahk_class AutoHotkey",, "View", "Lines most recently executed"
:::
