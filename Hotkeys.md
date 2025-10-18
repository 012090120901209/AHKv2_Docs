# Hotkeys [(Mouse, Controller and Keyboard Shortcuts)]{.headnote}

## Table of Contents {#toc}

-   [Introduction and Simple Examples](#Intro)
-   [Hotkey Modifier Symbols](#Symbols)
-   [Context-sensitive Hotkeys](#Context)
-   [Custom Combinations](#combo)
-   [Other Features](#Features)
-   [Mouse Wheel Hotkeys](#Wheel)
-   [Hotkey Tips and Remarks](#Remarks)
-   [Alt-Tab Hotkeys](#alttab)
-   [Named Function Hotkeys](#Function)

## Introduction and Simple Examples {#Intro}

Hotkeys are sometimes referred to as shortcut keys because of their
ability to easily trigger an action (such as launching a program or
[keyboard macro](misc/Macros.htm)). In the following example, the hotkey
[Win]{.kbd}+[N]{.kbd} is configured to launch Notepad. The pound sign
\[#\] stands for [Win]{.kbd}, which is known as a *modifier key*:

    #n::
    {
        Run "notepad"
    }

In the above, the braces serve to define a [function
body](Functions.htm) for the hotkey. The opening brace may also be
specified on the same line as the double-colon to support the [OTB (One
True Brace) style](lib/Block.htm#otb). However, if a hotkey needs to
execute only a single line, that line can be listed to the right of the
double-colon. In other words, the braces are implicit:

    #n::Run "notepad"

When a hotkey is triggered, the name of the hotkey is passed as its
first parameter named `ThisHotkey` (which excludes the trailing colons).
For example:

    #n::MsgBox ThisHotkey  ; Reports #n

With few exceptions, this is similar to the built-in variable
[A_ThisHotkey](Variables.htm#ThisHotkey). The parameter name can be
changed by using a [named function](#Function).

To use more than one modifier with a hotkey, list them consecutively
(the order does not matter). The following example uses `^!s` to
indicate [Ctrl]{.kbd}+[Alt]{.kbd}+[S]{.kbd}:

    ^!s::
    {
        Send "Sincerely,{enter}John Smith"  ; This line sends keystrokes to the active (foremost) window.
    }

## Hotkey Modifier Symbols {#Symbols}

You can use the following modifier symbols to define hotkeys:

+-----------------------------------+-----------------------------------+
| Symbol                            | Description                       |
+===================================+===================================+
| \#                                | [Win]{.kbd} (Windows logo key).   |
|                                   |                                   |
|                                   | Hotkeys that include [Win]{.kbd}  |
|                                   | (e.g. #a) will wait for           |
|                                   | [Win]{.kbd} to be released before |
|                                   | sending any text containing an    |
|                                   | [L]{.kbd} keystroke. This         |
|                                   | prevents usages of                |
|                                   | [Send](lib/Send.htm) within such  |
|                                   | a hotkey from locking the PC.     |
|                                   | This behavior applies to all      |
|                                   | sending modes except              |
|                                   | [SendP                            |
|                                   | lay](lib/Send.htm#SendPlayDetail) |
|                                   | (which doesn\'t need it), [blind  |
|                                   | mode](lib/Send.htm#blind) and     |
|                                   | [text                             |
|                                   | mode](lib/Send.htm#SendText).     |
|                                   |                                   |
|                                   | **Note:** Pressing a hotkey which |
|                                   | includes [Win]{.kbd} may result   |
|                                   | in extra simulated keystrokes     |
|                                   | ([Ctrl]{.kbd} by default). See    |
|                                   | [A_Men                            |
|                                   | uMaskKey](lib/A_MenuMaskKey.htm). |
+-----------------------------------+-----------------------------------+
| !                                 | [Alt]{.kbd}                       |
|                                   |                                   |
|                                   | **Note:** Pressing a hotkey which |
|                                   | includes [Alt]{.kbd} may result   |
|                                   | in extra simulated keystrokes     |
|                                   | ([Ctrl]{.kbd} by default). See    |
|                                   | [A_Men                            |
|                                   | uMaskKey](lib/A_MenuMaskKey.htm). |
+-----------------------------------+-----------------------------------+
| \^                                | [Ctrl]{.kbd}                      |
+-----------------------------------+-----------------------------------+
| \+                                | [Shift]{.kbd}                     |
+-----------------------------------+-----------------------------------+
| &                                 | An ampersand may be used between  |
|                                   | any two keys or mouse buttons to  |
|                                   | combine them into a custom        |
|                                   | hotkey. See [below](#combo) for   |
|                                   | details.                          |
+-----------------------------------+-----------------------------------+
| \<                                | Use the left key of the pair.     |
|                                   | e.g. \<!a is the same as !a       |
|                                   | except that only the left         |
|                                   | [Alt]{.kbd} will trigger it.      |
+-----------------------------------+-----------------------------------+
| \>                                | Use the right key of the pair.    |
+-----------------------------------+-----------------------------------+
| \<\^\>!                           | [AltGr]{.kbd} ([alternate graph,  |
|                                   | or alternate                      |
|                                   | graphic](https://e                |
|                                   | n.wikipedia.org/wiki/AltGr_key)). |
|                                   | If your keyboard layout has       |
|                                   | [AltGr]{.kbd} instead of a right  |
|                                   | [Alt]{.kbd} key, this series of   |
|                                   | symbols can usually be used to    |
|                                   | stand for [AltGr]{.kbd}. For      |
|                                   | example:                          |
|                                   |                                   |
|                                   |     <^>                           |
|                                   | !m::MsgBox "You pressed AltGr+m." |
|                                   |     <^<!m::MsgBox "Yo             |
|                                   | u pressed LeftControl+LeftAlt+m." |
|                                   |                                   |
|                                   | Alternatively, to make            |
|                                   | [AltGr]{.kbd} itself into a       |
|                                   | hotkey, use the following hotkey  |
|                                   | (without any hotkeys like the     |
|                                   | above present):                   |
|                                   |                                   |
|                                   |     LControl & RAlt::M            |
|                                   | sgBox "You pressed AltGr itself." |
+-----------------------------------+-----------------------------------+
| \*                                | Wildcard: Fire the hotkey even if |
|                                   | extra modifiers are being held    |
|                                   | down. This is often used in       |
|                                   | conjunction with                  |
|                                   | [remapping](misc/Remap.htm) keys  |
|                                   | or buttons. For example:          |
|                                   |                                   |
|                                   |     *#c::Run "calc.exe"  ;        |
|                                   | Win+C, Shift+Win+C, Ctrl+Win+C, e |
|                                   | tc. will all trigger this hotkey. |
|                                   |     *ScrollLock                   |
|                                   | ::Run "notepad"  ; Pressing Scrol |
|                                   | lLock will trigger this hotkey ev |
|                                   | en when modifier key(s) are down. |
|                                   |                                   |
|                                   | Wildcard hotkeys always use the   |
|                                   | keyboard hook, as do any hotkeys  |
|                                   | eclipsed by a wildcard hotkey.    |
|                                   | For example, the presence of      |
|                                   | `*a::` would cause `^a::` to      |
|                                   | always use the hook.              |
+-----------------------------------+-----------------------------------+
| \~                                | When the hotkey fires, its key\'s |
|                                   | native function will not be       |
|                                   | blocked (hidden from the system). |
|                                   | In both of the below examples,    |
|                                   | the user\'s click of the mouse    |
|                                   | button will be sent to the active |
|                                   | window:                           |
|                                   |                                   |
|                                   |     ~RButton::MsgBox "You         |
|                                   |  clicked the right mouse button." |
|                                   |     ~RButton & C:                 |
|                                   | :MsgBox "You pressed C while hold |
|                                   | ing down the right mouse button." |
|                                   |                                   |
|                                   | Unlike the other prefix symbols,  |
|                                   | the tilde prefix is allowed to be |
|                                   | present on some of a hotkey\'s    |
|                                   | [                                 |
|                                   | variants](lib/_HotIf.htm#variant) |
|                                   | but absent on others. However, if |
|                                   | a tilde is applied to the [prefix |
|                                   | key](#prefix) of any custom       |
|                                   | combination which has not been    |
|                                   | turned off or suspended, it       |
|                                   | affects the behavior of that      |
|                                   | prefix key for *all*              |
|                                   | combinations.                     |
|                                   |                                   |
|                                   | Special hotkeys that are          |
|                                   | substitutes for                   |
|                                   | [alt-tab](#alttab) always ignore  |
|                                   | the tilde prefix.                 |
|                                   |                                   |
|                                   | If the tilde prefix is applied to |
|                                   | a custom modifier key ([prefix    |
|                                   | key](#prefix)) which is also used |
|                                   | as its own hotkey, that hotkey    |
|                                   | will fire when the key is pressed |
|                                   | instead of being delayed until    |
|                                   | the key is released. For example, |
|                                   | the *\~RButton* hotkey above is   |
|                                   | fired as soon as the button is    |
|                                   | pressed.                          |
|                                   |                                   |
|                                   | If the tilde prefix is applied    |
|                                   | only to the custom combination    |
|                                   | and not the non-combination       |
|                                   | hotkey, the key\'s native         |
|                                   | function will still be blocked.   |
|                                   | For example, in the script below, |
|                                   | holding [Menu]{.kbd} will show    |
|                                   | the tooltip and will not trigger  |
|                                   | a context menu:                   |
|                                   |                                   |
|                                   |     AppsKey::ToolTip "Press       |
|                                   | < or > to cycle through windows." |
|                                   |     AppsKey Up::ToolTip           |
|                                   |     ~AppsKey & <::Send "!+{Esc}"  |
|                                   |     ~AppsKey & >::Send "!{Esc}"   |
|                                   |                                   |
|                                   | If at least one variant of a      |
|                                   | keyboard hotkey has the tilde     |
|                                   | modifier, that hotkey always uses |
|                                   | the keyboard hook.                |
+-----------------------------------+-----------------------------------+
| \$                                | This is usually only necessary if |
|                                   | the script uses the               |
|                                   | [Send](lib/Send.htm) function to  |
|                                   | send the keys that comprise the   |
|                                   | hotkey itself, which might        |
|                                   | otherwise cause it to trigger     |
|                                   | itself. The \$ prefix forces the  |
|                                   | [keyboard                         |
|                                   | hook](lib/InstallKeybdHook.htm)   |
|                                   | to be used to implement this      |
|                                   | hotkey, which as a side-effect    |
|                                   | prevents the [Send](lib/Send.htm) |
|                                   | function from triggering it. The  |
|                                   | \$ prefix is equivalent to having |
|                                   | specified                         |
|                                   | [`#UseHook`](lib/_UseHook.htm)    |
|                                   | somewhere above the definition of |
|                                   | this hotkey.                      |
|                                   |                                   |
|                                   | The \$ prefix has no effect for   |
|                                   | mouse hotkeys, since they always  |
|                                   | use the mouse hook. It also has   |
|                                   | no effect for hotkeys which       |
|                                   | already require the keyboard      |
|                                   | hook, including any keyboard      |
|                                   | hotkeys with the [tilde           |
|                                   | (\~)](#Tilde) or [wildcard        |
|                                   | (\*)](#wildcard) modifiers,       |
|                                   | key-up hotkeys and custom         |
|                                   | combinations. To determine        |
|                                   | whether a particular hotkey uses  |
|                                   | the keyboard hook, use            |
|                                   | [L                                |
|                                   | istHotkeys](lib/ListHotkeys.htm). |
|                                   |                                   |
|                                   | [                                 |
|                                   | #InputLevel](lib/_InputLevel.htm) |
|                                   | and                               |
|                                   | [SendLevel](lib/SendLevel.htm)    |
|                                   | provide additional control over   |
|                                   | which hotkeys and hotstrings are  |
|                                   | triggered by the Send function.   |
+-----------------------------------+-----------------------------------+
| UP                                | The word UP may follow the name   |
|                                   | of a hotkey to cause the hotkey   |
|                                   | to fire upon release of the key   |
|                                   | rather than when the key is       |
|                                   | pressed down. The following       |
|                                   | example [remaps](misc/Remap.htm)  |
|                                   | the left [Win]{.kbd} to become    |
|                                   | the left [Ctrl]{.kbd}:            |
|                                   |                                   |
|                                   |     *LWin::Send "{LControl down}" |
|                                   |                                   |
|                                   |    *LWin Up::Send "{LControl up}" |
|                                   |                                   |
|                                   | \"Up\" can also be used with      |
|                                   | normal hotkeys as in this         |
|                                   | example:                          |
|                                   | `^!r Up::MsgBox "You p            |
|                                   | ressed and released Ctrl+Alt+R"`. |
|                                   | It also works with [combination   |
|                                   | hotkeys](#combo) (e.g.            |
|                                   | `F1 & e Up::`)                    |
|                                   |                                   |
|                                   | Limitations: 1) \"Up\" does not   |
|                                   | work with [controller             |
|                                   | buttons](KeyList.htm#Controller); |
|                                   | and 2) An \"Up\" hotkey without a |
|                                   | normal/down counterpart hotkey    |
|                                   | will completely take over that    |
|                                   | key to prevent it from getting    |
|                                   | stuck down. One way to prevent    |
|                                   | this is to add a [tilde           |
|                                   | prefix](#Tilde) (e.g.             |
|                                   | `~LControl up::`)                 |
|                                   |                                   |
|                                   | \"Up\" hotkeys and their key-down |
|                                   | counterparts (if any) always use  |
|                                   | the keyboard hook.                |
|                                   |                                   |
|                                   | On a related note, a technique    |
|                                   | similar to the above is to make a |
|                                   | hotkey into a prefix key. The     |
|                                   | advantage is that although the    |
|                                   | hotkey will fire upon release, it |
|                                   | will do so only if you did not    |
|                                   | press any other key while it was  |
|                                   | held down. For example:           |
|                                   |                                   |
|                                   |     LControl & F1::return  ; Mak  |
|                                   | e left-control a prefix by using  |
|                                   | it in front of "&" at least once. |
|                                   |     LControl::MsgBox "You         |
|                                   | released LControl without having  |
|                                   | used it to modify any other key." |
+-----------------------------------+-----------------------------------+

**Note:** See the [Key List](KeyList.htm) for a complete list of
keyboard keys and mouse/controller buttons.

Multiple hotkeys can be stacked vertically to have them perform the same
action. For example:

    ^Numpad0::
    ^Numpad1::
    {
        MsgBox "Pressing either Ctrl+Numpad0 or Ctrl+Numpad1 will display this."
    }

A key or key-combination can be disabled for the entire system by having
it do nothing. The following example disables the right-side
[Win]{.kbd}:

    RWin::return

## Context-sensitive Hotkeys {#Context}

The [#HotIf](lib/_HotIf.htm) directive can be used to make a hotkey
perform a different action (or none at all) depending on a specific
condition. For example:

    #HotIf WinActive("ahk_class Notepad")
    ^a::MsgBox "You pressed Ctrl-A while Notepad is active. Pressing Ctrl-A in any other window will pass the Ctrl-A keystroke to that window."
    #c::MsgBox "You pressed Win-C while Notepad is active."

    #HotIf
    #c::MsgBox "You pressed Win-C while any window except Notepad is active."

    #HotIf MouseIsOver("ahk_class Shell_TrayWnd") ; For MouseIsOver, see #HotIf example 1.
    WheelUp::Send "{Volume_Up}"     ; Wheel over taskbar: increase/decrease volume.
    WheelDown::Send "{Volume_Down}" ;

## Custom Combinations {#combo}

Normally shortcut key combinations consist of optional prefix/modifier
keys (Ctrl, Alt, Shift and LWin/RWin) and a single suffix key. The
standard modifier keys are designed to be used in this manner, so
normally have no immediate effect when pressed down.

A custom combination of two keys (including mouse but not controller
buttons) can be defined by using \" & \" between them. Because they are
intended for use with prefix keys that are not normally used as such,
custom combinations have the following special behavior:

-   The prefix key loses its native function, unless it is a standard
    modifier key or toggleable key such as [CapsLock]{.kbd}.
-   If the prefix key is also used as a suffix in another hotkey, by
    default that hotkey is fired upon release, and is not fired at all
    if it was used to activate a custom combination. If there is both a
    key-down hotkey and a [key-up](#keyup) hotkey, both hotkeys are
    fired at once. The fire-on-release effect is disabled if the [tilde
    prefix](#Tilde) is applied to the prefix key in at least one active
    custom combination or the suffix hotkey itself.

**Note:** For combinations with standard modifier keys, it is usually
better to use the standard syntax. For example, use `<+s::` rather than
`LShift & s::`.

In the below example, you would hold down Numpad0 then press the second
key to trigger the hotkey:

``` {#prefix}
Numpad0 & Numpad1::MsgBox "You pressed Numpad1 while holding down Numpad0."
Numpad0 & Numpad2::Run "Notepad"
```

**The prefix key loses its native function:** In the above example,
Numpad0 becomes a *prefix key*; but this also causes Numpad0 to lose its
original/native function when it is pressed by itself. To avoid this, a
script may configure Numpad0 to perform a new action such as one of the
following:

    Numpad0::WinMaximize "A"   ; Maximize the active/foreground window.
    Numpad0::Send "{Numpad0}"  ; Make the release of Numpad0 produce a Numpad0 keystroke. See comment below.

**Fire on release:** The presence of one of the above custom combination
hotkeys causes the *release* of Numpad0 to perform the indicated action,
but only if you did not press any other keys while Numpad0 was being
held down. This behaviour can be avoided by applying the [tilde
prefix](#Tilde) to either hotkey.

**Modifiers:** Unlike a normal hotkey, custom combinations act as though
they have the [wildcard (\*)](#wildcard) modifier by default. For
example, `1 & 2::` will activate even if [Ctrl]{.kbd} or [Alt]{.kbd} is
held down when [1]{.kbd} and [2]{.kbd} are pressed, whereas `^1::` would
be activated only by [Ctrl]{.kbd}+[1]{.kbd} and not
[Ctrl]{.kbd}+[Alt]{.kbd}+[1]{.kbd}.

Combinations of three or more keys are not supported. Combinations which
your keyboard hardware supports can usually be detected by using
[#HotIf](lib/_HotIf.htm) and [GetKeyState](lib/GetKeyState.htm), but the
results may be inconsistent. For example:

    ; Press AppsKey and Alt in any order, then slash (/).
    #HotIf GetKeyState("AppsKey", "P")
    Alt & /::MsgBox "Hotkey activated."

    ; If the keys are swapped, Alt must be pressed first (use one at a time):
    #HotIf GetKeyState("Alt", "P")
    AppsKey & /::MsgBox "Hotkey activated."

    ; [ & ] & \::
    #HotIf GetKeyState("[") && GetKeyState("]")
    \::MsgBox

**Keyboard hook:** Custom combinations involving keyboard keys always
use the keyboard hook, as do any hotkeys which use the prefix key as a
suffix. For example, `a & b::` causes `^a::` to always use the hook.

## Other Features {#Features}

**NumLock, CapsLock, and ScrollLock:** These keys may be forced to be
\"AlwaysOn\" or \"AlwaysOff\". For example:
[`SetNumLockState`](lib/SetNumScrollCapsLockState.htm)` "AlwaysOn"`.

**Overriding Explorer\'s hotkeys:** Windows\' built-in hotkeys such as
[Win]{.kbd}+[E]{.kbd} (#e) and [Win]{.kbd}+[R]{.kbd} (#r) can be
individually overridden simply by assigning them to an action in the
script. See the [override page](misc/Override.htm) for details.

**Substitutes for Alt-Tab:** Hotkeys can provide an alternate means of
alt-tabbing. For example, the following two hotkeys allow you to alt-tab
with your right hand:

    RControl & RShift::AltTab  ; Hold down right-control then press right-shift repeatedly to move forward.
    RControl & Enter::ShiftAltTab  ; Without even having to release right-control, press Enter to reverse direction.

For more details, see [Alt-Tab](#alttab).

## Mouse Wheel Hotkeys {#Wheel}

Hotkeys that fire upon turning the mouse wheel are supported via the key
names WheelDown and WheelUp. Here are some examples of mouse wheel
hotkeys:

    MButton & WheelDown::MsgBox "You turned the mouse wheel down while holding down the middle button."
    ^!WheelUp::MsgBox "You rotated the wheel up while holding down Control+Alt."

If the mouse supports it, horizontal scrolling can be detected via the
key names WheelLeft and WheelRight. Some mice have a single wheel which
can be scrolled up and down or tilted left and right. Generally in those
cases, WheelLeft or WheelRight signals are sent repeatedly while the
wheel is held to one side, to simulate continuous scrolling. This
typically causes the hotkeys to execute repeatedly.

The built-in variable **A_EventInfo** contains the amount by which the
wheel was turned, which is typically 120. However, A_EventInfo can be
greater or less than 120 under the following circumstances:

-   If the mouse hardware reports distances of less than one notch,
    A_EventInfo may be less than 120;
-   If the wheel is being turned quickly (depending on the type of
    mouse), A_EventInfo may be greater than 120. A hotkey like the
    following can help analyze your mouse:
    `~WheelDown::ToolTip A_EventInfo`

Some of the most useful hotkeys for the mouse wheel involve alternate
modes of scrolling a window\'s text. For example, the following pair of
hotkeys scrolls horizontally instead of vertically when you turn the
wheel while holding down the left [Ctrl]{.kbd}:

    ~LControl & WheelUp::  ; Scroll left.
    {
        Loop 2  ; <-- Increase this value to scroll faster.
            SendMessage 0x0114, 0, 0, ControlGetFocus("A")  ; 0x0114 is WM_HSCROLL and the 0 after it is SB_LINELEFT.
    }

    ~LControl & WheelDown::  ; Scroll right.
    {
        Loop 2  ; <-- Increase this value to scroll faster.
            SendMessage 0x0114, 1, 0, ControlGetFocus("A")  ; 0x0114 is WM_HSCROLL and the 1 after it is SB_LINERIGHT.
    }

Finally, since mouse wheel hotkeys generate only down-events (never
up-events), they cannot be used as [key-up hotkeys](#keyup).

## Hotkey Tips and Remarks {#Remarks}

Each numpad key can be made to launch two different hotkey subroutines
depending on the state of [NumLock]{.kbd}. Alternatively, a numpad key
can be made to launch the same subroutine regardless of the state. For
example:

    NumpadEnd::
    Numpad1::
    {
        MsgBox "This hotkey is launched regardless of whether NumLock is on."
    }

If the [tilde (\~) symbol](#Tilde) is used with a [prefix key](#prefix)
even once, it changes the behavior of that prefix key for all
combinations. For example, in both of the below hotkeys, the active
window will receive all right-clicks even though only one of the
definitions contains a tilde:

    ~RButton & LButton::MsgBox "You pressed the left mouse button while holding down the right."
    RButton & WheelUp::MsgBox "You turned the mouse wheel up while holding down the right button."

The [Suspend](lib/Suspend.htm) function can temporarily disable all
hotkeys except for ones you make exempt. For greater selectivity, use
[#HotIf](lib/_HotIf.htm).

By means of the [Hotkey](lib/Hotkey.htm) function, hotkeys can be
created dynamically while the script is running. The Hotkey function can
also modify, disable, or enable the script\'s existing hotkeys
individually.

Controller hotkeys do not currently support modifier prefixes such as \^
(Ctrl) and \# (Win). However, you can use
[GetKeyState](lib/GetKeyState.htm) to mimic this effect as shown in the
following example:

    Joy2::
    {
        if not GetKeyState("Control")  ; Neither the left nor right Control key is down.
            return  ; i.e. Do nothing.
        MsgBox "You pressed the first controller's second button while holding down the Control key."
    }

There may be times when a hotkey should wait for its own modifier keys
to be released before continuing. Consider the following example:

    ^!s::Send "{Delete}"

Pressing [Ctrl]{.kbd}+[Alt]{.kbd}+[S]{.kbd} would cause the system to
behave as though you pressed [Ctrl]{.kbd}+[Alt]{.kbd}+[Del]{.kbd} (due
to the system\'s aggressive detection of this hotkey). To work around
this, use [KeyWait](lib/KeyWait.htm) to wait for the keys to be
released; for example:

    ^!s::
    {
        KeyWait "Control"
        KeyWait "Alt"
        Send "{Delete}"
    }

If a hotkey like `#z::` produces an error like \"Invalid Hotkey\", your
system\'s keyboard layout/language might not have the specified
character (\"Z\" in this case). Try using a different character that you
know exists in your keyboard layout.

A hotkey\'s function can be called explicitly by the script only if the
function has been named. See [Named Function Hotkeys](#Function).

One common use for hotkeys is to start and stop a repeating action, such
as a series of keystrokes or mouse clicks. For an example of this, see
[this FAQ topic](FAQ.htm#repeat).

Finally, each script is [quasi multi-threaded](misc/Threads.htm), which
allows a new hotkey to be launched even when a previous hotkey
subroutine is still running. For example, new hotkeys can be launched
even while a [message box](lib/MsgBox.htm) is being displayed by the
current hotkey.

## []{#AltTabDetail}Alt-Tab Hotkeys {#alttab}

Alt-Tab hotkeys simplify the mapping of new key combinations to the
system\'s Alt-Tab hotkeys, which are used to invoke a menu for switching
tasks (activating windows).

Each Alt-Tab hotkey must be either a single key or a combination of two
keys, which is typically achieved via the ampersand symbol (&). In the
following example, you would hold down the right [Alt]{.kbd} and press
[J]{.kbd} or [K]{.kbd} to navigate the alt-tab menu:

    RAlt & j::AltTab
    RAlt & k::ShiftAltTab

*AltTab* and *ShiftAltTab* are two of the special commands that are only
recognized when used on the same line as a hotkey. Here is the complete
list:

**AltTab:** If the alt-tab menu is visible, move forward in it.
Otherwise, display the menu (only if the hotkey is a combination of two
keys; otherwise, it does nothing).

**ShiftAltTab:** Same as above except move backward in the menu.

**AltTabMenu:** Show or hide the alt-tab menu.

**AltTabAndMenu:** If the alt-tab menu is visible, move forward in it.
Otherwise, display the menu.

**AltTabMenuDismiss:** Close the Alt-tab menu.

To illustrate the above, the mouse wheel can be made into an entire
substitute for Alt-tab. With the following hotkeys in effect, clicking
the middle button displays the menu and turning the wheel navigates
through it:

    MButton::AltTabMenu
    WheelDown::AltTab
    WheelUp::ShiftAltTab

To cancel the Alt-Tab menu without activating the selected window, press
or send [Esc]{.kbd}. In the following example, you would hold the left
[Ctrl]{.kbd} and press [CapsLock]{.kbd} to display the menu and advance
forward in it. Then you would release the left [Ctrl]{.kbd} to activate
the selected window, or press the mouse wheel to cancel. Define the
[AltTabWindow](#AltTabWindow) window group as shown below before running
this example.

    LCtrl & CapsLock::AltTab
    #HotIf WinExist("ahk_group AltTabWindow")  ; Indicates that the alt-tab menu is present on the screen.
    *MButton::Send "{Blind}{Escape}"  ; The * prefix allows it to fire whether or not Alt is held down.
    #HotIf

If the script sent `{Alt Down}` (such as to invoke the Alt-Tab menu), it
might also be necessary to send `{Alt Up}` as shown in the example
further below.

### General Remarks {#AltTabRemarks}

Currently, all special Alt-tab actions must be assigned directly to a
hotkey as in the examples above (i.e. they cannot be used as though they
were functions). They are [not affected by
[#HotIf](lib/_HotIf.htm)]{.red}.

An alt-tab action may take effect on key-down and/or key-up regardless
of whether the `up` keyword is used, and cannot be combined with another
action on the same key. For example, using both `F1::AltTabMenu` and
`F1 up::OtherAction()` is unsupported.

Custom alt-tab actions can also be created via hotkeys. As the identity
of the alt-tab menu differs between OS versions, it may be helpful to
use a window group as shown below. For the examples above and below
which use `ahk_group AltTabWindow`, this window group is expected to be
defined during [script startup](Scripts.htm#auto). Alternatively,
`ahk_group AltTabWindow` can be replaced with the appropriate
`ahk_class` for your system.

    GroupAdd "AltTabWindow", "ahk_class MultitaskingViewFrame"  ; Windows 10
    GroupAdd "AltTabWindow", "ahk_class TaskSwitcherWnd"  ; Windows Vista, 7, 8.1
    GroupAdd "AltTabWindow", "ahk_class #32771"  ; Older, or with classic alt-tab enabled

In the following example, you would press [F1]{.kbd} to display the menu
and advance forward in it. Then you would press [F2]{.kbd} to activate
the selected window, or press [Esc]{.kbd} to cancel:

    *F1::Send "{Alt down}{tab}" ; Asterisk is required in this case.
    !F2::Send "{Alt up}"  ; Release the Alt key, which activates the selected window.
    #HotIf WinExist("ahk_group AltTabWindow")
    ~*Esc::Send "{Alt up}"  ; When the menu is cancelled, release the Alt key automatically.
    ;*Esc::Send "{Esc}{Alt up}"  ; Without tilde (~), Escape would need to be sent.
    #HotIf

## Named Function Hotkeys {#Function}

If the function of a hotkey is ever needed to be called without
triggering the hotkey itself, one or more hotkeys can be assigned a
named [function](Functions.htm) by simply defining it immediately after
the hotkey\'s double-colon as in this example:

    ; Ctrl+Shift+O to open containing folder in Explorer.
    ; Ctrl+Shift+E to open folder with current file selected.
    ; Supports SciTE and Notepad++ (may require title bar setting changes).
    ^+o::
    ^+e::
        editor_open_folder(hk)
        {
            path := WinGetTitle("A")
            if RegExMatch(path, "\*?\K(.*)\\[^\\]+(?= [-*] )", &path)
                if (FileExist(path[0]) && hk = "^+e")
                    Run Format('explorer.exe /select,"{1}"', path[0])
                else
                    Run Format('explorer.exe "{1}"', path[1])
        }

If the function *editor_open_folder* is ever called explicitly by the
script, the first parameter (hk) must be passed a value.

[Hotstrings](Hotstrings.htm) can also be defined this way. Multiple
hotkeys or hotstrings can be stacked together to call the same function.

There must only be whitespace or comments between the hotkey and the
function name.

Naming the function also encourages self-documenting hotkeys, like in
the code above where the function name describes the hotkey.

The [Hotkey](lib/Hotkey.htm) function can also be used to assign a
function or function object to a hotkey.
