# #HotIf

Creates context-sensitive [hotkeys](../Hotkeys.htm) and
[hotstrings](../Hotstrings.htm). They perform a different action (or
none at all) depending on any condition (an
[expression](../Language.htm#expressions)).

``` Syntax
#HotIf Expression
```

## Parameters {#Parameters}

Expression

:   Type: [Boolean](../Concepts.htm#boolean)

    If omitted, subsequently-created hotkeys and hotstrings are not
    context-sensitive. Otherwise, specify any valid
    [expression](../Variables.htm#Expressions). This becomes the return
    value of an implicit function which has one parameter
    ([ThisHotkey](../Hotkeys.htm#ThisHotkey)). The function cannot
    modify global variables directly (as it is
    [assume-local](../Functions.htm#AssumeLocal) as usual, and cannot
    contain declarations), but can call other functions which do.

## Basic Operation {#howto}

The #HotIf directive sets the expression which will be used by
subsequently created [hotkeys](../Hotkeys.htm) and
[hotstrings](../Hotstrings.htm) to determine whether they should
activate. This expression is evaluated when the hotkey\'s key, mouse
button or combination is pressed, when the hotstring\'s abbreviation is
typed, or at other times when the program needs to know whether the
hotkey or hotstring is active.

To make context-sensitive hotkeys and hotstrings, simply precede them
with the #HotIf directive. For example:

    #HotIf WinActive("ahk_class Notepad") or WinActive(MyWindowTitle)
    #Space::MsgBox "You pressed Win+Spacebar in Notepad or " MyWindowTitle
    :X:btw::MsgBox "You typed btw in Notepad or " MyWindowTitle

The #HotIf directive is positional: it affects all hotkeys and
hotstrings physically beneath it in the script, until the next #HotIf
directive.

**Note:** Unlike [if statements](If.htm), braces have no effect with the
#HotIf directive.

The #HotIf directive only affects hotkeys and hotstrings created via the
double-colon syntax, such as `^!c::` or `::btw::`. For hotkeys and
hotstrings created via the [Hotkey](Hotkey.htm) or
[Hotstring](Hotstring.htm) function, use the [HotIf](HotIf.htm)
function.

To turn off context sensitivity, specify #HotIf without any expression.
For example:

    #HotIf

Like other directives, #HotIf cannot be executed conditionally.

When a mouse or keyboard hotkey is disabled via #HotIf, it performs its
native function; that is, it passes through to the active window as
though there is no such hotkey. There is one exception: Controller
hotkeys: although #HotIf works, it never prevents other programs from
seeing the press of a button.

#HotIf can also be used to alter the behavior of an ordinary key like
[Enter]{.kbd} or [Space]{.kbd}. This is useful when a particular window
ignores that key or performs some action you find undesirable. For
example:

    #HotIf WinActive("Reminders ahk_class #32770")  ; The "reminders" window in Outlook.
    Enter::Send "!o"  ; Have an "Enter" keystroke open the selected reminder rather than snoozing it.
    #HotIf

## Variants (Duplicates) {#variant}

A particular [hotkey](../Hotkeys.htm) or [hotstring](../Hotstrings.htm)
can be defined more than once in the script if each definition has
different HotIf criteria. These are known as *hotkey variants* or
*hotstring variants*. For example:

    #HotIf WinActive("ahk_class Notepad")
    ^!c::MsgBox "You pressed Control+Alt+C in Notepad."
    #HotIf WinActive("ahk_class WordPadClass")
    ^!c::MsgBox "You pressed Control+Alt+C in WordPad."
    #HotIf
    ^!c::MsgBox "You pressed Control+Alt+C in a window other than Notepad/WordPad."

If more than one variant is eligible to fire, only the one closest to
the top of the script will fire. The exception to this is the global
variant (the one with no HotIf criteria): It always has the lowest
precedence; therefore, it will fire only if no other variant is eligible
(this exception does not apply to [hotstrings](../Hotstrings.htm)).

When creating duplicate hotkeys, the order of [modifier
symbols](../Hotkeys.htm#Symbols) such as `^!+#` does not matter. For
example, `^!c` is the same as `!^c`. However, keys must be spelled
consistently. For example, *Esc* is not the same as *Escape* for this
purpose (though the case does not matter). Also, any hotkey with a
[wildcard prefix (\*)](../Hotkeys.htm#wildcard) is entirely separate
from a non-wildcard one; for example, `*F1` and `F1` would each have
their own set of variants.

A [window group](GroupAdd.htm) can be used to make a hotkey or hotstring
execute for a group of windows. For example:

    GroupAdd "MyGroup", "ahk_class Notepad"
    GroupAdd "MyGroup", "ahk_class WordPadClass"

    #HotIf WinActive("ahk_group MyGroup")
    #z::MsgBox "You pressed Win+Z in either Notepad or WordPad."

To create hotkey or hotstring variants dynamically (while the script is
running), see [HotIf](HotIf.htm).

## Expression Evaluation

When the hotkey\'s key, mouse or controller button combination is
pressed or the hotstring\'s abbreviation is typed, the #HotIf expression
is evaluated to determine if the hotkey or hotstring should activate.

**Note:** Scripts should not assume that the expression is only
evaluated when the hotkey\'s key is pressed (see below).

The expression may also be evaluated whenever the program needs to know
whether the hotkey is active. For example, the #HotIf expression for a
custom combination like `a & b::` might be evaluated when the prefix key
(`a` in this example) is pressed, to determine whether it should act as
a custom modifier key.

**Note:** Use of #HotIf in an unresponsive script may cause input lag or
break hotkeys and hotstrings (see below).

There are several more caveats to the #HotIf directive:

-   Keyboard or mouse input is typically buffered (delayed) until
    expression evaluation completes or [times out](_HotIfTimeout.htm).
-   Expression evaluation can only be performed by the script\'s main
    thread (at the OS level, not a [quasi-thread](../misc/Threads.htm)),
    not directly by the keyboard/mouse hook. If the script is busy or
    unresponsive, such as if a FileCopy is in progress, expression
    evaluation is delayed and may time out.
-   If the [system-defined
    timeout](_HotIfTimeout.htm#LowLevelHooksTimeout) is reached, the
    system may stop notifying the script of keyboard or mouse input (see
    #HotIfTimeout for details).
-   Sending keystrokes or mouse clicks while the expression is being
    evaluated (such as from a function which it calls) may cause
    complications and should be avoided.

[ThisHotkey](../Hotkeys.htm#ThisHotkey),
[A_ThisHotkey](../Variables.htm#ThisHotkey) and
[A_TimeSinceThisHotkey](../Variables.htm#TimeSinceThisHotkey) are set
based on the hotkey or non-auto-replace hotstring for which the current
#HotIf expression is being evaluated.

[A_PriorHotkey](../Variables.htm#PriorHotkey) and
[A_TimeSincePriorHotkey](../Variables.htm#TimeSincePriorHotkey)
temporarily contain the previous values of the corresponding \"This\"
variables.

## Optimization

#HotIf is optimized to avoid expression evaluation for simple calls to
[WinActive](WinActive.htm) or [WinExist](WinExist.htm), thereby reducing
the [risk of lag](#lag) or other issues in such cases. Specifically:

-   The expression must contain exactly one call to
    [WinExist](WinExist.htm) or [WinActive](WinActive.htm).
-   Each parameter must be a single quoted string, and no more than two
    parameters may be used.
-   The result may be inverted with `not` or `!`, but no other operators
    may be used.
-   Whitespace and parentheses are fully handled when the expression is
    pre-compiled and therefore do not affect this optimization.

If the expression meets these criteria, it is evaluated directly by the
program and does not appear in [ListLines](ListLines.htm).

Before the [Hotkey](Hotkey.htm) or [Hotstring](Hotstring.htm) function
is used to modify an existing hotkey or hotstring variant, typically the
[HotIf](HotIf.htm) function must be used with the original expression
text. However, the first unique expression with a given combination of
criteria can also be referenced by that criteria. For example:

    HotIfWinExist "ahk_class Notepad"
    Hotkey "#n", "Off"  ; Turn the hotkey off.
    HotIf 'WinExist("ahk_class Notepad")'
    Hotkey "#n", "On"   ; Turn the same hotkey back on.

    #HotIf WinExist("ahk_class Notepad")
    #n::WinActivate

Note that any use of variables will disqualify the expression. If the
variable\'s value never changes after the hotkey or hotstring is
created, there are two strategies for minimizing the risk of lag or
other issues inherent to #HotIf:

-   Use
    [`HotIfWin...`{.no-highlight}](HotIf.htm#IfWin)`(MyTitleVar)`{.no-highlight}
    to set the criteria and
    [`Hotkey`{.no-highlight}](Hotkey.htm)`(KeyName, Action)`{.no-highlight}
    or
    [`Hotstring`{.no-highlight}](Hotstring.htm)`(String, Replacement)`{.no-highlight}
    to create the hotkey or hotstring variant.
-   Use a constant expression such as
    `#HotIf WinActive("ahk_group MyGroup")` and define the window group
    with [`GroupAdd`](GroupAdd.htm)` "MyGroup", MyTitleVar` elsewhere in
    the script.

## General Remarks

#HotIf also restores prefix keys to their native function when
appropriate (a [prefix key](../Hotkeys.htm#prefix) is [A]{.kbd} in a
hotkey such as `a & b`). This occurs whenever there are no enabled
hotkeys for a given prefix.

When a hotkey is currently disabled via #HotIf, its key or mouse button
will appear with a \"#\" character in [KeyHistory\'s](KeyHistory.htm)
\"Type\" column. This can help [debug a script](../Scripts.htm#debug).

[Alt-tab hotkeys](../Hotkeys.htm#alttab) are not affected by #HotIf:
they are in effect for all windows.

The [Last Found Window](../misc/WinTitle.htm#LastFoundWindow) can be set
by #HotIf. For example:

    #HotIf WinExist("ahk_class Notepad")
    #n::WinActivate  ; Activates the window found by WinExist().

## Related {#Related}

[#HotIfTimeout](_HotIfTimeout.htm) may be used to override the default
timeout value.

[Hotkey function](Hotkey.htm), [Hotkeys](../Hotkeys.htm), [Hotstring
function](Hotstring.htm), [Hotstrings](../Hotstrings.htm),
[Suspend](Suspend.htm), [WinActive](WinActive.htm),
[WinExist](WinExist.htm), [SetTitleMatchMode](SetTitleMatchMode.htm),
[DetectHiddenWindows](DetectHiddenWindows.htm)

## Examples {#Examples}

::: {#ExBasic .ex}
[](#ExBasic){.ex_number} Creates two hotkeys and one hotstring which
only work when Notepad is active, and one hotkey which works for any
window except Notepad.

    #HotIf WinActive("ahk_class Notepad")
    ^!a::MsgBox "You pressed Ctrl-Alt-A while Notepad is active."
    #c::MsgBox "You pressed Win-C while Notepad is active."
    ::btw::This replacement text for "btw" will occur only in Notepad.
    #HotIf
    #c::MsgBox "You pressed Win-C in a window other than Notepad."
:::

::: {#ExVolume .ex}
[](#ExVolume){.ex_number} Allows the volume to be adjusted by scrolling
the mouse wheel over the taskbar.

    #HotIf MouseIsOver("ahk_class Shell_TrayWnd")
    WheelUp::Send "{Volume_Up}"
    WheelDown::Send "{Volume_Down}"

    MouseIsOver(WinTitle) {
        MouseGetPos ,, &Win
        return WinExist(WinTitle " ahk_id " Win)
    }
:::

::: {#ExWordDelete .ex}
[](#ExWordDelete){.ex_number} Simple word-delete shortcuts for all Edit
controls.

    #HotIf ActiveControlIsOfClass("Edit")
    ^BS::Send "^+{Left}{Del}"
    ^Del::Send "^+{Right}{Del}"

    ActiveControlIsOfClass(Cls) {
        FocusedControl := 0
        try FocusedControl := ControlGetFocus("A")
        FocusedControlClass := ""
        try FocusedControlClass := WinGetClass(FocusedControl)
        return (FocusedControlClass=Cls)
    }
:::

::: {#ExContextInsens .ex}
[](#ExContextInsens){.ex_number} Context-insensitive Hotkey.

    #HotIf
    Esc::ExitApp
:::

::: {#ExDynamic .ex}
[](#ExDynamic){.ex_number} Dynamic Hotkeys. This example should be
combined with [example #2](#ExVolume) before running it.

    NumpadAdd::
    {
        static toggle := false
        HotIf 'MouseIsOver("ahk_class Shell_TrayWnd")'
        if (toggle := !toggle)
            Hotkey "WheelUp", DoubleUp
        else
            Hotkey "WheelUp", "WheelUp"
        return
        ; Nested function:  
        DoubleUp(ThisHotkey) => Send("{Volume_Up 2}")
    }
:::
