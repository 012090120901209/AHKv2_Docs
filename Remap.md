# Remapping Keys [(Keyboard, Mouse and Controller)]{.headnote}

## Table of Contents {#toc}

-   [Introduction](#intro)
-   [Remapping the Keyboard and Mouse](#Remap)
-   [Remarks](#remarks)
-   [Moving the Mouse Cursor via the Keyboard](#moving-the-mouse-cursor)
-   [Remapping via the Registry\'s \"Scancode Map\"](#registry)
-   [Related Topics](#related)

## Introduction {#intro}

**Limitation:** AutoHotkey\'s remapping feature described below is
generally not as pure and effective as remapping directly via the
Windows registry. For the advantages and disadvantages of each approach,
see [registry remapping](#registry).

## Remapping the Keyboard and Mouse {#Remap}

The syntax for the built-in remapping feature is
`OriginKey::DestinationKey`. For example, a [script](../Scripts.htm)
consisting only of the following line would make [A]{.kbd} behave like
[B]{.kbd}:

    a::b

The above example does not alter [B]{.kbd} itself. [B]{.kbd} would
continue to send the \"b\" keystroke unless you remap it to something
else as shown in the following example:

    a::b
    b::a

The examples above use lowercase, which is recommended for most purposes
because it also remaps the corresponding uppercase letters (that is, it
will send uppercase when [CapsLock]{.kbd} is \"on\" or [Shift]{.kbd} is
held down). By contrast, specifying an uppercase letter on the right
side forces uppercase. For example, the following line would produce an
uppercase B when you type either \"a\" or \"A\" (as long as
[CapsLock]{.kbd} is off):

    a::B

Conversely, any modifiers included on the left side but not the right
side are automatically released when the key is sent. For example, the
following two lines would produce a lowercase \"b\" when you press
either [Shift]{.kbd}+[A]{.kbd} or [Ctrl]{.kbd}+[A]{.kbd}:

    A::b
    ^a::b

### Mouse Remapping {#RemapMouse}

To remap the mouse instead of the keyboard, use the same approach. For
example:

  Example               Description
  --------------------- ------------------------------------------------------------------
  `MButton::Shift`      Makes the middle button behave like [Shift]{.kbd}.
  `XButton1::LButton`   Makes the fourth mouse button behave like the left mouse button.
  `RAlt::RButton`       Makes the right [Alt]{.kbd} behave like the right mouse button.

### Other Useful Remappings

  Example                Description
  ---------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  `CapsLock::Ctrl`       Makes [CapsLock]{.kbd} become [Ctrl]{.kbd}. To retain the ability to turn [CapsLock]{.kbd} on and off, add the remapping `+CapsLock::CapsLock` first. This toggles [CapsLock]{.kbd} on and off when you hold down [Shift]{.kbd} and press [CapsLock]{.kbd}. Because both remappings allow additional modifier keys to be held down, the more specific `+CapsLock::CapsLock` remapping must be placed first for it to work.
  `XButton2::^LButton`   Makes the fifth mouse button (XButton2) produce a control-click.
  `RAlt::AppsKey`        Makes the right [Alt]{.kbd} become [Menu]{.kbd} (which is the key that opens the context menu).
  `RCtrl::RWin`          Makes the right [Ctrl]{.kbd} become the right [Win]{.kbd}.
  `Ctrl::Alt`            Makes both [Ctrl]{.kbd} behave like [Alt]{.kbd}. However, see [alt-tab issues](#AltTab).
  `^x::^c`               Makes [Ctrl]{.kbd}+[X]{.kbd} produce [Ctrl]{.kbd}+[C]{.kbd}. It also makes [Ctrl]{.kbd}+[Alt]{.kbd}+[X]{.kbd} produce [Ctrl]{.kbd}+[Alt]{.kbd}+[C]{.kbd}, etc.
  `RWin::Return`         Disables the right [Win]{.kbd} by having it simply [return](../lib/Return.htm).

You can try out any of these examples by copying them into a new text
file such as \"Remap.ahk\", then launching the file.

See the [Key List](../KeyList.htm) for a complete list of key and mouse
button names.

## Remarks

The [#HotIf](../lib/_HotIf.htm) directive can be used to make selected
remappings active only in the windows you specify (or while any given
condition is met). For example:

    #HotIf WinActive("ahk_class Notepad")
    a::b  ; Makes the 'a' key send a 'b' key, but only in Notepad.
    #HotIf  ; This puts subsequent remappings and hotkeys in effect for all windows.

Remapping a key or button is \"complete\" in the following respects:

-   Holding down a modifier such as [Ctrl]{.kbd} or [Shift]{.kbd} while
    typing the origin key will put that modifier into effect for the
    destination key. For example, `b::a` would produce
    [Ctrl]{.kbd}+[A]{.kbd} if you press [Ctrl]{.kbd}+[B]{.kbd}.
-   [CapsLock]{.kbd} generally affects remapped keys in the same way as
    normal keys.
-   The destination key or button is held down for as long as you
    continue to hold down the origin key. However, some games do not
    support remapping; in such cases, the keyboard and mouse will behave
    as though not remapped.
-   Remapped keys will auto-repeat while being held down (except keys
    remapped to become mouse buttons).

Although a remapped key can trigger normal hotkeys, by default it cannot
trigger mouse hotkeys or [hook hotkeys](../lib/_UseHook.htm) (use
[ListHotkeys](../lib/ListHotkeys.htm) to discover which hotkeys are
\"hook\"). For example, if the remapping `a::b` is in effect, pressing
[Ctrl]{.kbd}+[Alt]{.kbd}+[A]{.kbd} would trigger the `^!b` hotkey only
if `^!b` is not a hook hotkey. If `^!b` is a hook hotkey, you can define
`^!a` as a hotkey if you want [Ctrl]{.kbd}+[Alt]{.kbd}+[A]{.kbd} to
perform the same action as [Ctrl]{.kbd}+[Alt]{.kbd}+[B]{.kbd}. For
example:

    a::b
    ^!a::
    ^!b::ToolTip "You pressed " ThisHotkey

Alternatively, [#InputLevel](../lib/_InputLevel.htm) can be used to
override the default behaviour. For example:

    #InputLevel 1
    a::b

    #InputLevel 0
    ^!b::ToolTip "You pressed " ThisHotkey

If [SendMode](../lib/SendMode.htm) is used during [script
startup](../Scripts.htm#auto), it affects all remappings. However, since
remapping uses [Send \"{Blind}\"](../lib/Send.htm#blind) and since the
[SendPlay mode](../lib/SendMode.htm#Play) does not fully support
{Blind}, some remappings might not function properly in SendPlay mode
(especially [Ctrl]{.kbd}, [Shift]{.kbd}, [Alt]{.kbd}, and [Win]{.kbd}).
To work around this, avoid using `SendMode "Play"` during [script
startup](../Scripts.htm#auto) when you have remappings; then use the
function [SendPlay](../lib/Send.htm#SendPlay) vs. Send in other places
throughout the script. Alternatively, you could translate your
remappings into hotkeys (as described below) that explicitly call
SendEvent vs. Send.

If *DestinationKey* is meant to be `{`, it has to be
[escaped](EscapeChar.htm), for example, `` x::`{ ``. Otherwise it is
interpreted as the opening brace for the [hotkey](../Hotkeys.htm)\'s
function.

When a script is launched, each remapping is translated into a pair of
[hotkeys](../Hotkeys.htm). For example, a script containing `a::b`
actually contains the following two hotkeys instead:

    *a::
    {
        SetKeyDelay -1   ; If the destination key is a mouse button, SetMouseDelay is used instead.
        Send "{Blind}{b DownR}"  ; DownR is like Down except that other Send functions in the script won't assume "b" should stay down during their Send.
    }

    *a up::
    {
        SetKeyDelay -1  ; See note below for why press-duration is not specified with either of these SetKeyDelays.
        Send "{Blind}{b Up}"
    }

However, the above hotkeys vary under the following circumstances:

1.  When the source key is the left [Ctrl]{.kbd} and the destination key
    is [Alt]{.kbd}, the line `Send "{Blind}{LAlt DownR}"` is replaced by
    `Send "{Blind}`**`{LCtrl up}`**`{LAlt DownR}"`. The same is true if
    the source is the right [Ctrl]{.kbd}, except that `{RCtrl up}` is
    used. This is done to ensure that the system translates Alt-key
    combinations as though [Ctrl]{.kbd} is not being held down, but it
    also causes the remapping to override any prior {Ctrl down}.
    [\[v2.0.8+\]]{.ver}: The unsuppressed Ctrl key-up is still sent for
    backward-compatibility, but is no longer needed for its original
    purpose. The side effect can be avoided by replacing the remapping
    with an explicit pair of hotkeys as demonstrated above.

2.  When a keyboard key is being remapped to become a mouse button (e.g.
    `RCtrl::RButton`), the hotkeys above use SetMouseDelay in place of
    SetKeyDelay. In addition, the first hotkey above is replaced by the
    following, which prevents the keyboard\'s auto-repeat feature from
    generating repeated mouse clicks:

        *RCtrl::
        {
            SetMouseDelay -1
            if not GetKeyState("RButton")  ; i.e. the right mouse button isn't down yet.
                Send "{Blind}{RButton DownR}"
        }

3.  When the source is a [custom combination](../Hotkeys.htm#combo), the
    wildcard modifier (\*) is omitted to allow the hotkeys to work.

4.  If any of the modifier symbols in `!#^+` are applied to the source
    key and not the destination key, they are inserted after the word
    \"Blind\" to allow those modifiers to be released by Send. For
    example, `^a::b` would use `{Blind^}`. `<^a::b` would also use
    `{Blind^}`, which may produce unexpected results if used in
    combination with RCtrl. For details, see [Blind
    mode](../lib/Send.htm#blind).

Note that SetKeyDelay\'s second parameter ([press
duration](../lib/SetKeyDelay.htm#dur)) is omitted in the hotkeys above.
This is because press-duration does not apply to down-only or up-only
events such as `{b down}` and `{b up}`. However, it does apply to
changes in the state of the modifier keys (Shift, Ctrl, Alt, and Win),
which affects remappings such as `a::B` or `a::^b`. Consequently, any
press-duration a script puts into effect during [script
startup](../Scripts.htm#auto) will apply to all such remappings.

Since remappings are translated into hotkeys as described above, the
[Suspend](../lib/Suspend.htm) function affects them. Similarly, the
[Hotkey](../lib/Hotkey.htm) function can disable or modify a remapping.
For example, the following two functions would disable the remapping
`a::b`.

    Hotkey "*a", "Off"
    Hotkey "*a up", "Off"

Alt-tab issues: If you remap a key or mouse button to become
[Alt]{.kbd}, that key will probably not be able to alt-tab properly. A
possible work-around is to add the hotkey `*Tab::Send "{Blind}{Tab}"`
\-- but be aware that it will likely interfere with using the real
[Alt]{.kbd} to alt-tab. Therefore, it should be used only when you
alt-tab solely by means of remapped keys and/or [alt-tab
hotkeys](../Hotkeys.htm#alttab).

In addition to the keys and mouse buttons on the [Key
List](../KeyList.htm) page, the source key may also be a virtual key
(VKnn) or scan code (SCnnn) as described in the [Special
Keys](../KeyList.htm#SpecialKeys) section. The same is true for the
destination key except that it may optionally specify a scan code after
the virtual key. For example, `sc01e::vk42sc030` is equivalent to `a::b`
on most keyboard layouts.

To disable a key rather than remapping it, make it a hotkey that simply
[returns](../lib/Return.htm). For example, `F1::return` would disable
[F1]{.kbd}.

The following keys are not supported by the built-in remapping method:

-   The mouse wheel (WheelUp/Down/Left/Right).
-   \"Pause\" as a destination key name (since it matches the name of a
    built-in function). Instead use `vk13` or the corresponding scan
    code.
-   Curly braces {} as destination keys. Instead use the [VK/SC
    method](../lib/Send.htm#vk); e.g. `x::+sc01A` and `y::+sc01B`.

## Moving the Mouse Cursor via the Keyboard {#moving-the-mouse-cursor}

The keyboard can be used to move the mouse cursor as demonstrated by the
fully-featured [Keyboard-To-Mouse
script](../scripts/index.htm#NumpadMouse). Since that script offers
smooth cursor movement, acceleration, and other features, it is the
recommended approach if you plan to do a lot of mousing with the
keyboard. By contrast, the following example is a simpler demonstration:

    *#up::MouseMove 0, -10, 0, "R"  ; Win+UpArrow hotkey => Move cursor upward
    *#Down::MouseMove 0, 10, 0, "R"  ; Win+DownArrow => Move cursor downward
    *#Left::MouseMove -10, 0, 0, "R"  ; Win+LeftArrow => Move cursor to the left
    *#Right::MouseMove 10, 0, 0, "R"  ; Win+RightArrow => Move cursor to the right

    *<#RCtrl::  ; LeftWin + RightControl => Left-click (hold down Control/Shift to Control-Click or Shift-Click).
    {
        SendEvent "{Blind}{LButton down}"
        KeyWait "RCtrl"  ; Prevents keyboard auto-repeat from repeating the mouse click.
        SendEvent "{Blind}{LButton up}"
    }

    *<#AppsKey::  ; LeftWin + AppsKey => Right-click
    {
        SendEvent "{Blind}{RButton down}"
        KeyWait "AppsKey"  ; Prevents keyboard auto-repeat from repeating the mouse click.
        SendEvent "{Blind}{RButton up}"
    }

## Remapping via the Registry\'s \"Scancode Map\" {#registry}

**Advantages:**

-   Registry remapping is generally more pure and effective than
    [AutoHotkey\'s remapping](#Remap). For example, it works in a
    broader variety of games, it has no known [alt-tab issues](#AltTab),
    and it is capable of firing AutoHotkey\'s hook hotkeys (whereas
    AutoHotkey\'s remapping requires a [workaround](#HookHotkeys)).
-   If you choose to make the registry entries manually (explained
    below), absolutely no external software is needed to remap your
    keyboard. Even if you use
    [KeyTweak](https://www.bleepingcomputer.com/download/keytweak/) to
    make the registry entries for you, KeyTweak does not need to stay
    running all the time (unlike AutoHotkey).

**Disadvantages:**

-   Registry remapping is relatively permanent: a reboot is required to
    undo the changes or put new ones into effect.
-   Its effect is global: it cannot create remappings specific to a
    particular user, application, or locale.
-   It cannot send keystrokes that are modified by [Shift]{.kbd},
    [Ctrl]{.kbd}, [Alt]{.kbd}, or [AltGr]{.kbd}. For example, it cannot
    remap a lowercase character to an uppercase one.
-   It supports only the keyboard (AutoHotkey has [mouse
    remapping](#RemapMouse) and some [limited controller
    remapping](RemapController.htm)).

**How to Apply Changes to the Registry:** There are at least two methods
to remap keys via the registry:

1.  Use a program like
    [KeyTweak](https://www.bleepingcomputer.com/download/keytweak/)
    (freeware) to visually remap your keys. It will change the registry
    for you.
2.  Remap keys manually by creating a .reg file (plain text) and loading
    it into the registry. This is demonstrated in the [archived
    forums](https://www.autohotkey.com/board/index.php?showtopic=8359#entry52760).

## Related Topics {#related}

-   [List of keys, mouse buttons and controller
    controls](../KeyList.htm)
-   [GetKeyState](../lib/GetKeyState.htm)
-   [Remapping a controller](RemapController.htm)
