# SetTitleMatchMode

Sets the matching behavior of the [*WinTitle*
parameter](../misc/WinTitle.htm) in built-in functions such as
[WinWait](WinWait.htm).

``` Syntax
SetTitleMatchMode MatchMode
SetTitleMatchMode Speed
```

## Parameters {#Parameters}

MatchMode

:   Type: [Integer](../Concepts.htm#numbers) or
    [String](../Concepts.htm#strings)

    Specify one of the following values:

    **1:** A window\'s title must start with the specified *WinTitle* to
    be a match.

    **2:** Default behavior. A window\'s title can contain *WinTitle*
    anywhere inside it to be a match.

    **3:** A window\'s title must exactly match *WinTitle* to be a
    match.

    **RegEx:** Changes *WinTitle*, *WinText*, *ExcludeTitle*, and
    *ExcludeText* to accept [regular
    expressions](../misc/RegEx-QuickRef.htm), e.g.
    [`WinActivate`](WinActivate.htm)` "Untitled.*Notepad"`. RegEx also
    applies to [ahk_class](../misc/WinTitle.htm#ahk_class) and
    [ahk_exe](../misc/WinTitle.htm#ahk_exe), e.g. `"ahk_class IEFrame"`
    searches for any window whose class name contains *IEFrame* anywhere
    (this is because by default, regular expressions find a match
    *anywhere* in the target string). For *WinTitle*, each component is
    separate, e.g. in
    `"i)^untitled ahk_class i)^notepad$ ahk_pid " mypid`, `i)^untitled`
    and `i)^notepad$` are separate regex patterns and `mypid` is always
    compared numerically (it is not a regex pattern). For *WinText*,
    each text element (i.e. each control\'s text) is matched against the
    RegEx separately, so it is not possible to have a match span more
    than one text element.

    The modes above also affect *ExcludeTitle* in the same way as
    *WinTitle*. For example, mode 3 requires that a window\'s title
    exactly match *ExcludeTitle* for that window to be excluded.

    Of the modes, *only* RegEx mode affects the non-title window
    matching criteria [ahk_class](../misc/WinTitle.htm#ahk_class) and
    [ahk_exe](../misc/WinTitle.htm#ahk_exe). Those matching criteria
    will operate identically in any of the numbered modes.

Speed

:   Type: [String](../Concepts.htm#strings)

    Specify one of the following words to indicate how the *WinText* and
    *ExcludeText* parameters should be matched:

    **Fast:** Default behavior. Performance may be substantially better
    than the slow mode, but certain types of controls are not detected.
    For instance, text is typically detected within Static and Button
    controls, but not Edit controls, unless they are owned by the
    script.

    **Slow:** Can be much slower, but works with all controls which
    respond to the
    [WM_GETTEXT](https://learn.microsoft.com/windows/win32/winmsg/wm-gettext)
    message.

## Return Value {#Return_Value}

Type: [Integer](../Concepts.htm#numbers) or
[String](../Concepts.htm#strings)

This function returns the previous value of whichever setting was
changed (either [A_TitleMatchMode](../Variables.htm#TitleMatchMode) or
[A_TitleMatchModeSpeed](../Variables.htm#TitleMatchModeSpeed)).

## Remarks {#Remarks}

If SetTitleMatchMode is not used, the default match mode is 2 and the
default speed is fast.

This function affects the behavior of all windowing functions, e.g.
[WinExist](WinExist.htm) and [WinActivate](WinActivate.htm).
[WinGetText](WinGetText.htm) and [ControlGetText](ControlGetText.htm)
are affected in the same way as other functions, but they always use the
slow mode to retrieve text.

If a [window group](../misc/WinTitle.htm#ahk_group) is used, the current
title match mode applies to each individual rule in the group.

Generally, the slow mode should be used only if the target window cannot
be uniquely identified by its title and fast-mode text. This is because
the slow mode can be extremely slow if there are any application windows
that are busy or \"not responding\".

Window Spy has an option for *Slow TitleMatchMode* so that its easy to
determine whether the slow mode is needed.

If you wish to change both attributes, run the function twice as in this
example:

    SetTitleMatchMode 2
    SetTitleMatchMode "Slow"

The built-in variables **A_TitleMatchMode** and
**A_TitleMatchModeSpeed** contain the current settings.

Regardless of the current match mode, *WinTitle*, *WinText*,
*ExcludeTitle* and *ExcludeText* are case-sensitive. The only exception
is the [case-insensitive option](../misc/RegEx-QuickRef.htm#Options) of
the RegEx mode, e.g. `"`**`i)`**`untitled - notepad"`.

Every newly launched [thread](../misc/Threads.htm) (such as a
[hotkey](../Hotkeys.htm), [custom menu item](Menu.htm), or
[timed](SetTimer.htm) subroutine) starts off fresh with the default
setting for this function. That default may be changed by using this
function during [script startup](../Scripts.htm#auto).

## Related {#Related}

[The WinTitle Parameter](../misc/WinTitle.htm),
[SetWinDelay](SetWinDelay.htm), [WinExist](WinExist.htm),
[WinActivate](WinActivate.htm), [RegExMatch](RegExMatch.htm)

## Examples {#Examples}

::: {#ExMatchMode .ex}
[](#ExMatchMode){.ex_number} Forces windowing functions to operate upon
windows whose titles contain `WinTitle`{.variable} at the beginning
instead of anywhere.

    SetTitleMatchMode 1
:::

::: {#ExSpeed .ex}
[](#ExSpeed){.ex_number} Allows windowing functions to possibly detect
more control types, but with lower performance. Note that Slow/Fast can
be set independently of all the other modes.

    SetTitleMatchMode "Slow"
:::

::: {#ExRegEx .ex}
[](#ExRegEx){.ex_number} Use RegEx mode to easily exclude multiple
windows. Replace the following ExcludeTitles with actual window titles
that you want to exclude from counting.

    SetTitleMatchMode "RegEx"
    CountAll := WinGetCount()
    CountExcluded := WinGetCount(,, "ExcludeTitle1|ExcludeTitle2")
    MsgBox CountExcluded " out of " CountAll " windows were counted"
:::
