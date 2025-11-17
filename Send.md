# Send / SendText / SendInput / SendPlay / SendEvent

Sends simulated keystrokes and mouse clicks to the
[active](WinActivate.htm) window.

``` Syntax
Send Keys
SendText Keys
SendInput Keys
SendPlay Keys
SendEvent Keys
```

## Parameters {#Parameters}

Keys

:   Type: [String](../Concepts.htm#strings)

    The sequence of keys to send.

    By default (that is, if neither SendText nor the [Raw mode](#Raw) or
    [Text mode](#Text) is used), the characters `^+!#{}` have a special
    meaning. The characters `^+!#` represent the modifier keys
    [Ctrl]{.kbd}, [Shift]{.kbd}, [Alt]{.kbd} and [Win]{.kbd}. They
    affect only the very next key. To send the corresponding modifier
    key on its own, enclose the key name in braces. To just press (hold
    down) or release the key, follow the key name with the word \"down\"
    or \"up\" as shown below.

      -------------------------------------------------------------------------------------------------
      Symbol         Key            Press          Release        Examples
      -------------- -------------- -------------- -------------- -------------------------------------
      \^             {Ctrl}         {Ctrl down}    {Ctrl up}      `Send "^{Home}"` presses
                                                                  [Ctrl]{.kbd}+[Home]{.kbd}

      \+             {Shift}        {Shift down}   {Shift up}     `Send "+abC"` sends the text \"AbC\"\
                                                                  `Send "!+a"` presses
                                                                  [Alt]{.kbd}+[Shift]{.kbd}+[A]{.kbd}

      !              {Alt}          {Alt down}     {Alt up}       `Send "!a"` presses
                                                                  [Alt]{.kbd}+[A]{.kbd}

      \#             {LWin}\        {LWin down}\   {LWin up}\     `Send "#e"` holds down [Win]{.kbd}
                     {RWin}         {RWin down}    {RWin up}      and presses [E]{.kbd}
      -------------------------------------------------------------------------------------------------

    **Note:** As capital letters are produced by sending [Shift]{.kbd},
    `A` produces a different effect in some programs than `a`. For
    example, `!A` presses [Alt]{.kbd}+[Shift]{.kbd}+[A]{.kbd} and `!a`
    presses [Alt]{.kbd}+[A]{.kbd}. If in doubt, use lowercase.

    The characters `{}` are used to enclose [key names and other
    options](#keynames), and to send special characters literally. For
    example, `{Tab}` is [Tab]{.kbd} and `{!}` is a literal exclamation
    mark.

    Enclosing a plain ASCII letter (a-z or A-Z) in braces forces it to
    be sent as the corresponding virtual keycode, even if the character
    does not exist on the current keyboard layout. In other words,
    `Send "a"` produces the letter \"a\" while `Send "{a}"` may or may
    not produce \"a\", depending on the keyboard layout. For details,
    see the [remarks below](#AZ).

## Send variants {#Send_variants}

**Send:** By default, Send is synonymous with SendInput; but it can be
made a synonym for SendEvent or SendPlay via [SendMode](SendMode.htm).

**SendText:** Similar to Send, except that all characters in *Keys* are
interpreted and sent literally. See [Text mode](#Text) for details.

**SendInput:** SendInput uses the same syntax as SendEvent but is
generally faster and more reliable. In addition, it buffers any physical
keyboard or mouse activity during the send, which prevents the user\'s
keystrokes from being interspersed with those being sent.
[SendMode](SendMode.htm) can be used to make Send synonymous with
SendInput. See [SendInput](#SendInputDetail) for details.

**SendPlay:** Deprecated. Similar to SendInput, except that it may have
no effect at all on Windows 11 and later, or if [User Account Control
(UAC)](https://en.wikipedia.org/wiki/User_Account_Control) is enabled,
even if the script is running as an administrator. See
[SendPlay](#SendPlayDetail "Deprecated. Use SendInput instead."){.deprecated}
for details.

**SendEvent:** SendEvent sends keystrokes using the Windows keybd_event
function (search Microsoft Docs for details). The rate at which
keystrokes are sent is determined by [SetKeyDelay](SetKeyDelay.htm).
[SendMode](SendMode.htm) can be used to make Send synonymous with
SendEvent.

## Special modes {#Special_modes}

The following modes affect the interpretation of the characters in
*Keys* or the behavior of key-sending functions such as Send, SendInput,
SendPlay, SendEvent and [ControlSend](ControlSend.htm). These modes must
be specified as `{x}` in *Keys*, where x is either Raw, Text, or Blind.
For example, `{Raw}`.

### Raw mode {#Raw}

The Raw mode can be enabled with `{Raw}`, which causes all subsequent
characters, including the special characters `^+!#{}`, to be interpreted
literally rather than translating `{Enter}` to [Enter]{.kbd}, `^c` to
[Ctrl]{.kbd}+[C]{.kbd}, etc. For example, `Send "{Raw}{Tab}"` sends
`{Tab}` instead of [Tab]{.kbd}.

The Raw mode does not affect the interpretation of [escape
sequences](../misc/EscapeChar.htm) and
[expressions](../Variables.htm#Expressions). For example,
``` Send "{Raw}``100`%" ``` sends the string `` `100% ``{.no-highlight}.

### Text mode {#Text}

The Text mode can be either enabled with `{Text}`, SendText or
[ControlSendText](ControlSend.htm), which is similar to the Raw mode,
except that no attempt is made to translate characters (other than
`` `r ``, `` `n ``, `` `t `` and `` `b ``) to keycodes; instead, the
[fallback method](#fallback) is used for all of the remaining
characters. For SendEvent, SendInput and [ControlSend](ControlSend.htm),
this improves reliability because the characters are much less dependent
on correct modifier state. This mode can be combined with the Blind mode
to avoid releasing any modifier keys: `Send "{Blind}{Text}your text"`.
However, some applications require that the modifier keys be released.

`` `n ``, `` `r `` and `` `r`n `` are all translated to a single
[Enter]{.kbd}, unlike the default behavior and Raw mode, which translate
`` `r`n `` to two [Enter]{.kbd}. `` `t `` is translated to [Tab]{.kbd}
and `` `b `` to [Backspace]{.kbd}, but all other characters are sent
without translation.

Like the Blind mode, the Text mode ignores
[SetStoreCapsLockMode](SetStoreCapsLockMode.htm) (that is, the state of
[CapsLock]{.kbd} is not changed) and does not [wait for [Win]{.kbd} to
be released](../Hotkeys.htm#win-l). This is because the Text mode
typically does not depend on the state of [CapsLock]{.kbd} and cannot
trigger the system [Win]{.kbd}+[L]{.kbd} hotkey. However, this only
applies when *Keys* begins with `{Text}` or `{Blind}{Text}`.

### Blind mode {#Blind}

The Blind mode can be enabled with `{Blind}`, which gives the script
more control by disabling a number of things that are normally done
automatically to make things work as expected. `{Blind}` must be the
first item in the string to enable the Blind mode. It has the following
effects:

-   The Blind mode avoids releasing the modifier keys (Alt, Ctrl, Shift,
    and Win) if they started out in the down position, unless the
    modifier is [excluded](#blind-exclude). For example, the hotkey
    `+s::Send "{Blind}abc"` would send ABC rather than abc because the
    user is holding down [Shift]{.kbd}.
-   Modifier keys are restored differently to allow a Send to turn off a
    hotkey\'s modifiers even if the user is still physically holding
    them down. For example, `^space::Send "{Ctrl up}"` automatically
    pushes [Ctrl]{.kbd} back down if the user is still physically
    holding [Ctrl]{.kbd}, whereas `^space::Send "{Blind}{Ctrl up}"`
    allows [Ctrl]{.kbd} to be logically up even though it is physically
    down.
-   [SetStoreCapsLockMode](SetStoreCapsLockMode.htm) is ignored; that
    is, the state of [CapsLock]{.kbd} is not changed.
-   [Menu masking](A_MenuMaskKey.htm) is disabled. That is, Send omits
    the extra keystrokes that would otherwise be sent in order to
    prevent: 1) Start Menu appearance during Win keystrokes
    (LWin/RWin); 2) menu bar activation during Alt keystrokes. However,
    the Blind mode does not prevent masking performed by the keyboard
    hook following activation of a hook hotkey.
-   Send does not wait for [Win]{.kbd} to be released even if the text
    contains an [L]{.kbd} keystroke. This would normally be done to
    prevent Send from triggering the system \"lock workstation\" hotkey
    ([Win]{.kbd}+[L]{.kbd}). See [Hotkeys](../Hotkeys.htm#win-l) for
    details.

The word \"Blind\" may be followed by one or more modifier symbols
(`!#^+`) to allow those modifiers to be released automatically if
needed. For example, `*^a::Send "{Blind^}b"` would send
[Shift]{.kbd}+[B]{.kbd} instead of [Ctrl]{.kbd}+[Shift]{.kbd}+[B]{.kbd}
if [Ctrl]{.kbd}+[Shift]{.kbd}+[A]{.kbd} was pressed. `{Blind!#^+}`
allows all modifiers to be released if needed, but enables the other
effects of the Blind mode.

The Blind mode is used internally when [remapping a
key](../misc/Remap.htm). For example, the remapping `a::b` would
produce: 1) \"b\" when you type \"a\"; 2) uppercase \"B\" when you type
uppercase \"A\"; and 3) [Ctrl]{.kbd}+[B]{.kbd} when you type
[Ctrl]{.kbd}+[A]{.kbd}. If any modifiers are specified for the source
key (including [Shift]{.kbd} if the source key is an uppercase letter),
they are excluded as described above. For example `^a::b` produces
normal [B]{.kbd}, not [Ctrl]{.kbd}+[B]{.kbd}.

`{Blind}` is not supported by SendText or
[ControlSendText](ControlSend.htm); use `{Blind}{Text}` instead.

The Blind mode is not completely supported by
[SendPlay](#SendPlayDetail "Deprecated. Use SendInput instead."){.deprecated},
especially when dealing with the modifier keys (Ctrl, Alt, Shift, and
Win).

## Key names {#keynames}

The following table lists the special keys that can be sent (each key
name must be enclosed in braces):

+-----------------------------------+-----------------------------------+
| Key name                          | Description                       |
+===================================+===================================+
| {F1} - {F24}                      | Function keys. For example: {F12} |
|                                   | is [F12]{.kbd}.                   |
+-----------------------------------+-----------------------------------+
| {!}                               | !                                 |
+-----------------------------------+-----------------------------------+
| {#}                               | \#                                |
+-----------------------------------+-----------------------------------+
| {+}                               | \+                                |
+-----------------------------------+-----------------------------------+
| {\^}                              | \^                                |
+-----------------------------------+-----------------------------------+
| `{ {`                             | {                                 |
+-----------------------------------+-----------------------------------+
| `} }`                             | }                                 |
+-----------------------------------+-----------------------------------+
| {Enter}                           | [Enter]{.kbd} on the main         |
|                                   | keyboard                          |
+-----------------------------------+-----------------------------------+
| {Escape} or {Esc}                 | [Esc]{.kbd}                       |
+-----------------------------------+-----------------------------------+
| {Space}                           | [Space]{.kbd} (this is only       |
|                                   | needed for spaces that appear     |
|                                   | either at the beginning or the    |
|                                   | end of the string to be sent \--  |
|                                   | ones in the middle can be literal |
|                                   | spaces)                           |
+-----------------------------------+-----------------------------------+
| {Tab}                             | [Tab]{.kbd}                       |
+-----------------------------------+-----------------------------------+
| {Backspace} or {BS}               | [Backspace]{.kbd}                 |
+-----------------------------------+-----------------------------------+
| {Delete} or {Del}                 | [Del]{.kbd}                       |
+-----------------------------------+-----------------------------------+
| {Insert} or {Ins}                 | [Ins]{.kbd}                       |
+-----------------------------------+-----------------------------------+
| {Up}                              | [↑]{.kbd} (up arrow) on main      |
|                                   | keyboard                          |
+-----------------------------------+-----------------------------------+
| {Down}                            | [↓]{.kbd} (down arrow) on main    |
|                                   | keyboard                          |
+-----------------------------------+-----------------------------------+
| {Left}                            | [←]{.kbd} (left arrow) on main    |
|                                   | keyboard                          |
+-----------------------------------+-----------------------------------+
| {Right}                           | [→]{.kbd} (right arrow) on main   |
|                                   | keyboard                          |
+-----------------------------------+-----------------------------------+
| {Home}                            | [Home]{.kbd} on main keyboard     |
+-----------------------------------+-----------------------------------+
| {End}                             | [End]{.kbd} on main keyboard      |
+-----------------------------------+-----------------------------------+
| {PgUp}                            | [PgUp]{.kbd} on main keyboard     |
+-----------------------------------+-----------------------------------+
| {PgDn}                            | [PgDn]{.kbd} on main keyboard     |
+-----------------------------------+-----------------------------------+
| {CapsLock}                        | [CapsLock]{.kbd} (using           |
|                                   | [SetCapsLockStat                  |
|                                   | e](SetNumScrollCapsLockState.htm) |
|                                   | is more reliable). Sending        |
|                                   | {CapsLock} might require          |
|                                   | [`SetStoreCapsLockMode`](         |
|                                   | SetStoreCapsLockMode.htm)` False` |
|                                   | beforehand.                       |
+-----------------------------------+-----------------------------------+
| {ScrollLock}                      | [ScrollLock]{.kbd} (see also:     |
|                                   | [SetScrollLockState               |
|                                   | ](SetNumScrollCapsLockState.htm)) |
+-----------------------------------+-----------------------------------+
| {NumLock}                         | [NumLock]{.kbd} (see also:        |
|                                   | [SetNumLockState                  |
|                                   | ](SetNumScrollCapsLockState.htm)) |
+-----------------------------------+-----------------------------------+
| {Control} or {Ctrl}               | [Ctrl]{.kbd} (technical info:     |
|                                   | sends the neutral virtual key but |
|                                   | the left scan code)               |
+-----------------------------------+-----------------------------------+
| {LControl} or {LCtrl}             | Left [Ctrl]{.kbd} (technical      |
|                                   | info: sends the left virtual key  |
|                                   | rather than the neutral one)      |
+-----------------------------------+-----------------------------------+
| {RControl} or {RCtrl}             | Right [Ctrl]{.kbd}                |
+-----------------------------------+-----------------------------------+
| {Control down} or {Ctrl down}     | Holds [Ctrl]{.kbd} down until     |
|                                   | {Ctrl up} is sent. To hold down   |
|                                   | the left or right key instead,    |
|                                   | replace Ctrl with LCtrl or RCtrl. |
+-----------------------------------+-----------------------------------+
| {Alt}                             | [Alt]{.kbd} (technical info:      |
|                                   | sends the neutral virtual key but |
|                                   | the left scan code)               |
+-----------------------------------+-----------------------------------+
| {LAlt}                            | Left [Alt]{.kbd} (technical info: |
|                                   | sends the left virtual key rather |
|                                   | than the neutral one)             |
+-----------------------------------+-----------------------------------+
| {RAlt}                            | Right [Alt]{.kbd} (or             |
|                                   | [AltGr]{.kbd}, depending on       |
|                                   | keyboard layout)                  |
+-----------------------------------+-----------------------------------+
| {Alt down}                        | Holds [Alt]{.kbd} down until {Alt |
|                                   | up} is sent. To hold down the     |
|                                   | left or right key instead,        |
|                                   | replace Alt with LAlt or RAlt.    |
+-----------------------------------+-----------------------------------+
| {Shift}                           | [Shift]{.kbd} (technical info:    |
|                                   | sends the neutral virtual key but |
|                                   | the left scan code)               |
+-----------------------------------+-----------------------------------+
| {LShift}                          | Left [Shift]{.kbd} (technical     |
|                                   | info: sends the left virtual key  |
|                                   | rather than the neutral one)      |
+-----------------------------------+-----------------------------------+
| {RShift}                          | Right [Shift]{.kbd}               |
+-----------------------------------+-----------------------------------+
| {Shift down}                      | Holds [Shift]{.kbd} down until    |
|                                   | {Shift up} is sent. To hold down  |
|                                   | the left or right key instead,    |
|                                   | replace Shift with LShift or      |
|                                   | RShift.                           |
+-----------------------------------+-----------------------------------+
| {LWin}                            | Left [Win]{.kbd}                  |
+-----------------------------------+-----------------------------------+
| {RWin}                            | Right [Win]{.kbd}                 |
+-----------------------------------+-----------------------------------+
| {LWin down}                       | Holds the left [Win]{.kbd} down   |
|                                   | until {LWin up} is sent           |
+-----------------------------------+-----------------------------------+
| {RWin down}                       | Holds the right [Win]{.kbd} down  |
|                                   | until {RWin up} is sent           |
+-----------------------------------+-----------------------------------+
| {AppsKey}                         | [Menu]{.kbd} (invokes the         |
|                                   | right-click or context menu)      |
+-----------------------------------+-----------------------------------+
| {Sleep}                           | [Sleep]{.kbd}                     |
+-----------------------------------+-----------------------------------+
| {ASC nnnnn}                       | Sends an [Alt]{.kbd}+nnnnn keypad |
|                                   | combination, which can be used to |
|                                   | generate special characters that  |
|                                   | don\'t exist on the keyboard. To  |
|                                   | generate printable ASCII          |
|                                   | characters or other characters    |
|                                   | from [code page                   |
|                                   | 437](https://en.w                 |
|                                   | ikipedia.org/wiki/Code_page_437), |
|                                   | specify a number between 1 and    |
|                                   | 255. To generate ANSI characters  |
|                                   | (standard in most languages),     |
|                                   | specify a number between 128 and  |
|                                   | 255, but precede it with a        |
|                                   | leading zero, e.g. {Asc 0133}.    |
|                                   |                                   |
|                                   | Unicode characters may be         |
|                                   | generated by specifying a number  |
|                                   | between 256 and 65535 (without a  |
|                                   | leading zero). However, this is   |
|                                   | not supported by all              |
|                                   | applications. For alternatives,   |
|                                   | see the section below.            |
+-----------------------------------+-----------------------------------+
| {U+nnnn}                          | Sends a Unicode character where   |
|                                   | *nnnn* is the hexadecimal value   |
|                                   | of the character excluding the 0x |
|                                   | prefix. This typically isn\'t     |
|                                   | needed, because Send and          |
|                                   | ControlSend automatically support |
|                                   | Unicode text.                     |
|                                   |                                   |
|                                   | [SendInput()](https://l           |
|                                   | earn.microsoft.com/windows/win32/ |
|                                   | api/winuser/nf-winuser-sendinput) |
|                                   | or                                |
|                                   | [WM                               |
|                                   | _CHAR](https://learn.microsoft.co |
|                                   | m/windows/win32/inputdev/wm-char) |
|                                   | is used to send the character and |
|                                   | the current Send mode has no      |
|                                   | effect. Characters sent this way  |
|                                   | usually do not trigger shortcut   |
|                                   | keys or hotkeys.                  |
+-----------------------------------+-----------------------------------+
| {vkXX}\                           | Sends a keystroke that has        |
| {scYYY}\                          | virtual key XX and scan code YYY. |
| {vkXXscYYY}                       | For example:                      |
|                                   | `Send "{vkFFsc159}"`. If the sc   |
|                                   | or vk portion is omitted, the     |
|                                   | most appropriate value is sent in |
|                                   | its place.                        |
|                                   |                                   |
|                                   | The values for XX and YYY are     |
|                                   | hexadecimal and can usually be    |
|                                   | determined from the [main         |
|                                   | windo                             |
|                                   | w](../Program.htm#main-window)\'s |
|                                   | View-\>[Key                       |
|                                   | history](KeyHistory.htm) menu     |
|                                   | item. See also: [Special          |
|                                   | Keys](../KeyList.htm#SpecialKeys) |
|                                   |                                   |
|                                   | **Warning:** Combining vk and sc  |
|                                   | in this manner is valid only with |
|                                   | Send.                             |
+-----------------------------------+-----------------------------------+
| {Numpad0} - {Numpad9}             | Numpad digit keys (as seen when   |
|                                   | [NumLock]{.kbd} is ON). For       |
|                                   | example: {Numpad5} is [5]{.kbd}.  |
+-----------------------------------+-----------------------------------+
| {NumpadDot}                       | [.]{.kbd} (numpad period) (as     |
|                                   | seen when [NumLock]{.kbd} is ON). |
+-----------------------------------+-----------------------------------+
| {NumpadEnter}                     | [Enter]{.kbd} on keypad           |
+-----------------------------------+-----------------------------------+
| {NumpadMult}                      | [\*]{.kbd} (numpad                |
|                                   | multiplication)                   |
+-----------------------------------+-----------------------------------+
| {NumpadDiv}                       | [/]{.kbd} (numpad division)       |
+-----------------------------------+-----------------------------------+
| {NumpadAdd}                       | [+]{.kbd} (numpad addition)       |
+-----------------------------------+-----------------------------------+
| {NumpadSub}                       | [-]{.kbd} (numpad subtraction)    |
+-----------------------------------+-----------------------------------+
| {NumpadDel}                       | [Del]{.kbd} on keypad (this key   |
|                                   | and the following Numpad keys are |
|                                   | used when [NumLock]{.kbd} is OFF) |
+-----------------------------------+-----------------------------------+
| {NumpadIns}                       | [Ins]{.kbd} on keypad             |
+-----------------------------------+-----------------------------------+
| {NumpadClear}                     | Clear key on keypad (usually      |
|                                   | [5]{.kbd} when [NumLock]{.kbd} is |
|                                   | OFF).                             |
+-----------------------------------+-----------------------------------+
| {NumpadUp}                        | [↑]{.kbd} (up arrow) on keypad    |
+-----------------------------------+-----------------------------------+
| {NumpadDown}                      | [↓]{.kbd} (down arrow) on keypad  |
+-----------------------------------+-----------------------------------+
| {NumpadLeft}                      | [←]{.kbd} (left arrow) on keypad  |
+-----------------------------------+-----------------------------------+
| {NumpadRight}                     | [→]{.kbd} (right arrow) on keypad |
+-----------------------------------+-----------------------------------+
| {NumpadHome}                      | [Home]{.kbd} on keypad            |
+-----------------------------------+-----------------------------------+
| {NumpadEnd}                       | [End]{.kbd} on keypad             |
+-----------------------------------+-----------------------------------+
| {NumpadPgUp}                      | [PgUp]{.kbd} on keypad            |
+-----------------------------------+-----------------------------------+
| {NumpadPgDn}                      | [PgDn]{.kbd} on keypad            |
+-----------------------------------+-----------------------------------+
| {Browser_Back}                    | Select the browser \"back\"       |
|                                   | button                            |
+-----------------------------------+-----------------------------------+
| {Browser_Forward}                 | Select the browser \"forward\"    |
|                                   | button                            |
+-----------------------------------+-----------------------------------+
| {Browser_Refresh}                 | Select the browser \"refresh\"    |
|                                   | button                            |
+-----------------------------------+-----------------------------------+
| {Browser_Stop}                    | Select the browser \"stop\"       |
|                                   | button                            |
+-----------------------------------+-----------------------------------+
| {Browser_Search}                  | Select the browser \"search\"     |
|                                   | button                            |
+-----------------------------------+-----------------------------------+
| {Browser_Favorites}               | Select the browser \"favorites\"  |
|                                   | button                            |
+-----------------------------------+-----------------------------------+
| {Browser_Home}                    | Launch the browser and go to the  |
|                                   | home page                         |
+-----------------------------------+-----------------------------------+
| {Volume_Mute}                     | Mute/unmute the master volume.    |
|                                   | Usually equivalent to             |
|                                   | [`Sound                           |
|                                   | SetMute`](SoundSetMute.htm)` -1`. |
+-----------------------------------+-----------------------------------+
| {Volume_Down}                     | Reduce the master volume. Usually |
|                                   | equivalent to                     |
|                                   | [`SoundSetV                       |
|                                   | olume`](SoundSetVolume.htm)` -5`. |
+-----------------------------------+-----------------------------------+
| {Volume_Up}                       | Increase the master volume.       |
|                                   | Usually equivalent to             |
|                                   | [`SoundSetVol                     |
|                                   | ume`](SoundSetVolume.htm)` "+5"`. |
+-----------------------------------+-----------------------------------+
| {Media_Next}                      | Select next track in media player |
+-----------------------------------+-----------------------------------+
| {Media_Prev}                      | Select previous track in media    |
|                                   | player                            |
+-----------------------------------+-----------------------------------+
| {Media_Stop}                      | Stop media player                 |
+-----------------------------------+-----------------------------------+
| {Media_Play_Pause}                | Play/pause media player           |
+-----------------------------------+-----------------------------------+
| {Launch_Mail}                     | Launch the email application      |
+-----------------------------------+-----------------------------------+
| {Launch_Media}                    | Launch media player               |
+-----------------------------------+-----------------------------------+
| {Launch_App1}                     | Launch user app1                  |
+-----------------------------------+-----------------------------------+
| {Launch_App2}                     | Launch user app2                  |
+-----------------------------------+-----------------------------------+
| {PrintScreen}                     | [PrtSc]{.kbd}                     |
+-----------------------------------+-----------------------------------+
| {CtrlBreak}                       | [Ctrl]{.kbd}+[Pause]{.kbd}        |
+-----------------------------------+-----------------------------------+
| {Pause}                           | [Pause]{.kbd}                     |
+-----------------------------------+-----------------------------------+
| {Click \[Options\]}               | Sends a mouse click using the     |
|                                   | same options available in the     |
|                                   | [Click function](Click.htm). For  |
|                                   | example, `Send "{Click}"` would   |
|                                   | click the left mouse button once  |
|                                   | at the mouse cursor\'s current    |
|                                   | position, and                     |
|                                   | `Send "{Click 100 200}"` would    |
|                                   | click at coordinates 100, 200     |
|                                   | (based on                         |
|                                   | [CoordMode](CoordMode.htm)). To   |
|                                   | move the mouse without clicking,  |
|                                   | specify 0 after the coordinates;  |
|                                   | for example:                      |
|                                   | `Send "{Click 100 200 0}"`. The   |
|                                   | delay between mouse clicks is     |
|                                   | determined by                     |
|                                   | [                                 |
|                                   | SetMouseDelay](SetMouseDelay.htm) |
|                                   | (not                              |
|                                   | [SetKeyDelay](SetKeyDelay.htm)).  |
+-----------------------------------+-----------------------------------+
| {WheelDown}, {WheelUp},           | Sends a mouse button event at the |
| {WheelLeft}, {WheelRight},        | cursor\'s current position (to    |
| {LButton}, {RButton}, {MButton},  | have control over position and    |
| {XButton1}, {XButton2}            | other options, use                |
|                                   | [{Click}](Click.htm) above). The  |
|                                   | delay between mouse clicks is     |
|                                   | determined by                     |
|                                   | [S                                |
|                                   | etMouseDelay](SetMouseDelay.htm). |
|                                   |                                   |
|                                   | LButton and RButton correspond to |
|                                   | the primary and secondary mouse   |
|                                   | buttons. Normally the primary     |
|                                   | mouse button (LButton) is on the  |
|                                   | left, but the user may swap the   |
|                                   | buttons via system settings.      |
+-----------------------------------+-----------------------------------+
| {Blind}                           | Enables the [Blind mode](#blind), |
|                                   | which gives the script more       |
|                                   | control by disabling a number of  |
|                                   | things that are normally done     |
|                                   | automatically to make things      |
|                                   | generally work as expected.       |
|                                   | `{Blind}` must occur at the       |
|                                   | beginning of the string.          |
+-----------------------------------+-----------------------------------+
| {Raw}                             | Enables the [Raw mode](#SendRaw), |
|                                   | which causes the following        |
|                                   | characters to be interpreted      |
|                                   | literally: `^+!#{}`. Although     |
|                                   | `{Raw}` need not occur at the     |
|                                   | beginning of the string, once     |
|                                   | specified, it stays in effect for |
|                                   | the remainder of the string.      |
+-----------------------------------+-----------------------------------+
| {Text}                            | Enables the [Text                 |
|                                   | mode](#SendText), which sends a   |
|                                   | stream of characters rather than  |
|                                   | keystrokes. Like the Raw mode,    |
|                                   | the Text mode causes the          |
|                                   | following characters to be        |
|                                   | interpreted literally: `^+!#{}`.  |
|                                   | Although `{Text}` need not occur  |
|                                   | at the beginning of the string,   |
|                                   | once specified, it stays in       |
|                                   | effect for the remainder of the   |
|                                   | string.                           |
+-----------------------------------+-----------------------------------+

## Repeating or Holding Down a Key {#Repeating_or_Holding_Down_a_Key}

**To repeat a keystroke:** Enclose in braces the name of the key
followed by the number of times to repeat it. For example:

    Send "{DEL 4}"  ; Presses the Delete key 4 times.
    Send "{S 30}"   ; Sends 30 uppercase S characters.
    Send "+{TAB 4}"  ; Presses Shift-Tab 4 times.

**To hold down or release a key:** Enclose in braces the name of the key
followed by the word **Down** or **Up**. For example:

    Send "{b down}{b up}"
    Send "{TAB down}{TAB up}"
    Send "{Up down}"  ; Presses down the up-arrow key.
    Sleep 1000  ; Keeps it down for one second.
    Send "{Up up}"  ; Releases the up-arrow key.

When a key is held down via the method above, it does not begin
auto-repeating like it would if you were physically holding it down
(this is because auto-repeat is a driver/hardware feature). However, a
[Loop](Loop.htm) can be used to simulate auto-repeat. The following
example sends 20 tab keystrokes:

    Loop 20
    {
        Send "{Tab down}"  ; Auto-repeat consists of consecutive down-events (with no up-events).
        Sleep 30  ; The number of milliseconds between keystrokes (or use SetKeyDelay).
    }
    Send "{Tab up}"  ; Release the key.

By default, Send will not automatically release a modifier key (Control,
Shift, Alt, and Win) if that modifier key was \"pressed down\" by
sending it. For example, `Send "a"` may behave similar to
`Send "`[`{Blind}`](#blind)`{Ctrl up}a{Ctrl down}"` if the user is
physically holding [Ctrl]{.kbd}, but `Send "{Ctrl Down}"` followed by
`Send "a"` will produce [Ctrl]{.kbd}+[A]{.kbd}. *DownTemp* and *DownR*
can be used to override this behavior. *DownTemp* and *DownR* have the
same effect as *Down* except for the modifier keys (Control, Shift, Alt,
and Win).

**DownTemp** tells subsequent sends that the key is not permanently
down, and may be released whenever a keystroke calls for it. For
example, `Send "{Control DownTemp}"` followed later by `Send "a"` would
produce [A]{.kbd}, not [Ctrl]{.kbd}+[A]{.kbd}. Any use of Send may
potentially release the modifier permanently, so *DownTemp* is not ideal
for [remapping](../misc/Remap.htm) modifier keys.

**DownR** (where \"R\" stands for [remapping](../misc/Remap.htm), which
is its main use) tells subsequent sends that if the key is automatically
released, it should be pressed down again when send is finished. For
example, `Send "{Control DownR}"` followed later by `Send "a"` would
produce [A]{.kbd}, not [Ctrl]{.kbd}+[A]{.kbd}, but will leave
[Ctrl]{.kbd} in the pressed state for use with keyboard shortcuts. In
other words, *DownR* has an effect similar to physically pressing the
key.

If a character does not correspond to a virtual key on the current
keyboard layout, it cannot be \"pressed\" or \"released\". For example,
`Send "{µ up}"` has no effect on most layouts, and `Send "{µ down}"` is
equivalent to `Send "µ"`.

## General Remarks {#Remarks}

**Characters vs. keys:** By default, characters are sent by first
translating them to keystrokes. If this translation is not possible
(that is, if the current keyboard layout does not contain a key or key
combination which produces that character), the character is sent by one
of following fallback methods:

-   SendEvent and SendInput use
    [SendInput()](https://learn.microsoft.com/windows/win32/api/winuser/nf-winuser-sendinput)
    with the [KEYEVENTF_UNICODE
    flag](https://learn.microsoft.com/windows/win32/api/winuser/ns-winuser-keybdinput#keyeventf_unicode).
-   SendPlay uses the [Alt+nnnnn](#asc) method, which produces Unicode
    only if supported by the target application.
-   ControlSend posts a
    [WM_CHAR](https://learn.microsoft.com/windows/win32/inputdev/wm-char)
    message.

**Note:** Characters sent using any of the above methods usually do not
trigger keyboard shortcuts or hotkeys.

For characters in the range a-z or A-Z (plain ASCII letters), each
character which does not exist in the current keyboard layout may be
sent either as a character or as the corresponding virtual keycode
(vk41-vk5A):

-   If a naked letter is sent (that is, without modifiers or braces), or
    if [Raw](#Raw) mode is in effect, it is sent as a character. For
    example, `Send "{Raw}Regards"` sends the expected text, even though
    pressing [R]{.kbd} (vk52) produces some other character (such as
    [К]{.kbd} on the Russian layout). `{Raw}` can be omitted in this
    case, unless a modifier key was put into effect by a prior Send.
-   If one or more modifier keys have been put into effect by the Send
    function, or if the letter is wrapped in braces, it is sent as a
    keycode (modified with [Shift]{.kbd} if the letter is upper-case).
    This allows the script to easily activate standard keyboard
    shortcuts. For example, `^c` and `{Ctrl down}c{Ctrl up}` activate
    the standard [Ctrl]{.kbd}+[C]{.kbd} shortcut and `{c}` is equivalent
    to `{vk43}`.

If the letter exists in the current keyboard layout, it is always sent
as whichever keycode the layout associates with that letter (unless the
[Text mode](#SendText) is used, in which case the character is sent by
other means). In other words, the section above is only relevant for
non-Latin based layouts such as Russian.

**Modifier State:** When Send is required to change the state of the
[Win]{.kbd} or [Alt]{.kbd} modifier keys (such as if the user was
holding one of those keys), it may inject additional keystrokes
([Ctrl]{.kbd} by default) to prevent the Start menu or window menu from
appearing. For details, see [A_MenuMaskKey](A_MenuMaskKey.htm).

**BlockInput Compared to SendInput/SendPlay:** Although the
[BlockInput](BlockInput.htm) function can be used to prevent any
keystrokes physically typed by the user from disrupting the flow of
simulated keystrokes, it is often better to use
[SendInput](#SendInputDetail) or
[SendPlay](#SendPlayDetail "Deprecated. Use SendInput instead."){.deprecated}
so that keystrokes and mouse clicks become uninterruptible. This is
because unlike BlockInput, SendInput/Play does not discard what the user
types during the send; instead, such keystrokes are buffered and sent
afterward.

When sending a large number of keystrokes, a [continuation
section](../Scripts.htm#continuation) can be used to improve readability
and maintainability.

Since the operating system does not allow simulation of the
[Ctrl]{.kbd}+[Alt]{.kbd}+[Del]{.kbd} combination, doing something like
`Send "^!{Delete}"` will have no effect.

**Send may have no effect** if the active window is running with
administrative privileges and the script is not. This is due to a
security mechanism called User Interface Privilege Isolation.

## SendInput {#SendInputDetail}

SendInput is generally the preferred method to send keystrokes and mouse
clicks because of its superior speed and reliability. Under most
conditions, SendInput is nearly instantaneous, even when sending long
strings. Since SendInput is so fast, it is also more reliable because
there is less opportunity for some other window to pop up unexpectedly
and intercept the keystrokes. Reliability is further improved by the
fact that anything the user types during a SendInput is postponed until
afterward.

Unlike the other sending modes, the operating system limits SendInput to
about 5000 characters (this may vary depending on the operating
system\'s version and performance settings). Characters and events
beyond this limit are not sent.

**Note:** SendInput ignores SetKeyDelay because the operating system
does not support a delay in this mode. However, when SendInput reverts
to [SendEvent](#SendEvent) under the conditions described below, it uses
[`SetKeyDelay`](SetKeyDelay.htm)` -1, 0` (unless SendEvent\'s KeyDelay
is `-1,-1`, in which case `-1,-1` is used). When SendInput reverts to
[SendPlay](#SendPlayDetail "Deprecated. Use SendInput instead."){.deprecated},
it uses SendPlay\'s KeyDelay.

If the script has a [low-level keyboard hook](InstallKeybdHook.htm)
installed, SendInput automatically uninstalls it prior to executing and
reinstalls it afterward. As a consequence, SendInput generally cannot
trigger the script\'s own hook hotkeys or [InputHooks](InputHook.htm).
The hook is temporarily uninstalled because its presence would otherwise
disable all of SendInput\'s advantages, making it inferior to both
SendPlay and SendEvent. However, this can only be done for the script\'s
own hook, and is not done if an external hook is detected as described
below.

If a script *other than* the one executing SendInput has a [low-level
keyboard hook](InstallKeybdHook.htm) installed, SendInput automatically
reverts to [SendEvent](#SendEvent) (or
[SendPlay](#SendPlayDetail "Deprecated. Use SendInput instead."){.deprecated}
if [`SendMode`](SendMode.htm)` "InputThenPlay"` is in effect). This is
done because the presence of an external hook disables all of
SendInput\'s advantages, making it inferior to both SendPlay and
SendEvent. However, since SendInput is unable to detect a low-level hook
in programs other than AutoHotkey v1.0.43+, it will not revert in these
cases, making it less reliable than SendPlay/Event.

When SendInput sends mouse clicks by means such as [{Click}](#Click),
and [`CoordMode`](CoordMode.htm)` "Mouse", "Window"` or
`CoordMode "Mouse", "Client"` is in effect, every click will be relative
to the window that was active at the start of the send. Therefore, if
SendInput intentionally activates another window (by means such as
alt-tab), the coordinates of subsequent clicks within the same function
will be wrong if they were intended to be relative to the new window
rather than the old one.

## SendPlay {#SendPlayDetail}

**Deprecated:** SendPlay may have no effect at all on Windows 11 and
later, or if [User Account Control
(UAC)](https://en.wikipedia.org/wiki/User_Account_Control) is enabled,
even if the script is running as an administrator (for more information,
refer to the [FAQ](../FAQ.htm#uac)).

SendPlay\'s biggest advantage is its ability to \"play back\" keystrokes
and mouse clicks in a broader variety of games than the other modes. For
example, a particular game may accept
[hotstrings](../Hotstrings.htm#SendMode) only when they have the
[SendPlay option](../Hotstrings.htm#SendMode).

Of the three sending modes, SendPlay is the most unusual because it does
not simulate keystrokes and mouse clicks per se. Instead, it creates a
series of events (messages) that flow directly to the active window
(similar to [ControlSend](ControlSend.htm), but at a lower level).
Consequently, SendPlay does not trigger hotkeys or hotstrings.

Like [SendInput](#SendInputDetail), SendPlay\'s keystrokes do not get
interspersed with keystrokes typed by the user. Thus, if the user
happens to type something during a SendPlay, those keystrokes are
postponed until afterward.

Although SendPlay is considerably slower than SendInput, it is usually
faster than the traditional [SendEvent](#SendEvent) mode (even when
[KeyDelay](SetKeyDelay.htm) is -1).

Both [Win]{.kbd} (LWin and RWin) are automatically blocked during a
SendPlay if the [keyboard hook](InstallKeybdHook.htm) is installed. This
prevents the Start Menu from appearing if the user accidentally presses
[Win]{.kbd} during the send. By contrast, keys other than LWin and RWin
do not need to be blocked because the operating system automatically
postpones them until after the SendPlay (via buffering).

SendPlay does not use the standard settings of
[SetKeyDelay](SetKeyDelay.htm) and [SetMouseDelay](SetMouseDelay.htm).
Instead, it defaults to no delay at all, which can be changed as shown
in the following examples:

    SetKeyDelay 0, 10, "Play"  ; Note that both 0 and -1 are the same in SendPlay mode.
    SetMouseDelay 10, "Play"

SendPlay is unable to turn on or off [CapsLock]{.kbd}, [NumLock]{.kbd},
or [ScrollLock]{.kbd}. Similarly, it is unable to change a key\'s state
as seen by [GetKeyState](GetKeyState.htm) unless the keystrokes are sent
to one of the script\'s own windows. Even then, any changes to the
left/right modifier keys (e.g. RControl) can be detected only via their
neutral counterparts (e.g. Control). Also, SendPlay has other
limitations described on the [SendMode page](SendMode.htm).

Unlike [SendInput](#SendInputDetail) and [SendEvent](#SendEvent), the
user may interrupt a SendPlay by pressing
[Ctrl]{.kbd}+[Alt]{.kbd}+[Del]{.kbd} or [Ctrl]{.kbd}+[Esc]{.kbd}. When
this happens, the remaining keystrokes are not sent but the script
continues executing as though the SendPlay had completed normally.

Although SendPlay can send LWin and RWin events, they are sent directly
to the active window rather than performing their native operating
system function. To work around this, use [SendEvent](#SendEvent). For
example, `SendEvent "#r"` would show the Start Menu\'s Run dialog.

## Related {#Related}

[SendMode](SendMode.htm), [SetKeyDelay](SetKeyDelay.htm),
[SetStoreCapsLockMode](SetStoreCapsLockMode.htm), [Escape sequences
(e.g. \`n)](../misc/EscapeChar.htm), [ControlSend](ControlSend.htm),
[BlockInput](BlockInput.htm), [Hotstrings](../Hotstrings.htm),
[WinActivate](WinActivate.htm)

## Examples {#Examples}

::: {#ExBasic .ex}
[](#ExBasic){.ex_number} Types a two-line signature.

    Send "Sincerely,{enter}John Smith"
:::

::: {#ExModifier .ex}
[](#ExModifier){.ex_number} Selects the File-\>Save menu (Alt+F followed
by S).

    Send "!fs"
:::

::: {#ExBrace .ex}
[](#ExBrace){.ex_number} Jumps to the end of the text then send four
shift+left-arrow keystrokes.

    Send "{End}+{Left 4}"
:::

::: {#ExSendInputRaw .ex}
[](#ExSendInputRaw){.ex_number} Sends a long series of [raw
characters](#Raw) via the fastest method.

    SendInput "{Raw}A long series of raw characters sent via the fastest method."
:::

::: {#ExVar .ex}
[](#ExVar){.ex_number} Holds down a key contained in a
[variable](../Variables.htm).

    MyKey := "Shift"
    Send "{" MyKey " down}"  ; Holds down the Shift key.
:::
