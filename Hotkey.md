# Hotkey

Creates, modifies, enables, or disables a hotkey while the script is
running.

``` Syntax
Hotkey KeyName , Action, Options
```

## Parameters {#Parameters}

KeyName

:   Type: [String](../Concepts.htm#strings)

    Name of the hotkey\'s activation key, including any [modifier
    symbols](../Hotkeys.htm#Symbols). For example, specify `#c` for the
    [Win]{.kbd}+[C]{.kbd} hotkey.

    If *KeyName* already exists as a hotkey \-- either by the Hotkey
    function or a [double-colon label](../Hotkeys.htm) in the script \--
    that hotkey will be updated with the values of the function\'s other
    parameters.

    When specifying an *existing* hotkey, *KeyName* is not
    case-sensitive. However, the names of keys must be spelled the same
    as in the existing hotkey (e.g. Esc is not the same as Escape for
    this purpose). Also, the order of [modifier
    symbols](../Hotkeys.htm#Symbols) such as `^!+#` does not matter.
    [GetKeyName](GetKeyName.htm) can be used to retrieve the standard
    spelling of a key name.

    When a hotkey is first created \-- either by the Hotkey function or
    the [double-colon syntax](../Hotkeys.htm) in the script \-- its key
    name and the ordering of its modifier symbols becomes the permanent
    name of that hotkey as reflected by
    [ThisHotkey](../Hotkeys.htm#ThisHotkey). This name is shared by all
    [variants](_HotIf.htm#variant) of the hotkey, and does not change
    even if the Hotkey function later accesses the hotkey with a
    different symbol ordering.

    If the hotkey variant already exists, its behavior is updated
    according to whether *KeyName* includes or excludes the [tilde (\~)
    prefix](../Hotkeys.htm#Tilde).

    The [use hook (\$) prefix](../Hotkeys.htm#prefixdollar) can be added
    to existing hotkeys. This prefix affects all variants of the hotkey
    and cannot be removed.

Action

:   Type: [Function Object](../misc/Functor.htm) or
    [String](../Concepts.htm#strings)

    If omitted and *KeyName* already exists as a hotkey, its action will
    not be changed. This is useful to change only the hotkey\'s
    *Options*. Otherwise, specify a callback, a [hotkey](../Hotkeys.htm)
    name without trailing colons, or one of the special values listed
    below.

    ------------------------------------------------------------------------

    Specify the function to call (as a new
    [thread](../misc/Threads.htm)) when the hotkey is pressed.

    The callback accepts one parameter and can be
    [defined](../Functions.htm#intro) as follows:

    ``` NoIndent
    MyCallback(HotkeyName) { ...
    ```

    Although the name you give the parameter does not matter, it is
    assigned the [hotkey name](../Hotkeys.htm#ThisHotkey).

    You can omit the callback\'s parameter if the corresponding
    information is not needed, but in this case an asterisk must be
    specified, e.g. `MyCallback(*)`.

    Hotkeys defined with the [double-colon syntax](../Hotkeys.htm)
    automatically use the parameter name `ThisHotkey`. Hotkeys can also
    be [assigned a function name](../Hotkeys.htm#Function) without the
    Hotkey function.

    **Note:** If a callback is specified but the hotkey is disabled from
    a previous use of the Hotkey function, the hotkey will remain
    disabled. To prevent this, include the word ON in *Options*.

    ------------------------------------------------------------------------

    Specify a hotkey name to use its original function; specifically,
    the original function of the hotkey variant corresponding to the
    current [HotIf](HotIf.htm) criteria. This is usually used to restore
    a hotkey\'s original function after having changed it, but can be
    used to assign the function of a different hotkey, provided that
    both hotkeys use the same HotIf criteria.

    ------------------------------------------------------------------------

    Specify one of the following special values:

    **On:** The hotkey becomes enabled. No action is taken if the hotkey
    is already On.

    **Off:** The hotkey becomes disabled. No action is taken if the
    hotkey is already Off.

    **Toggle:** The hotkey is set to the opposite state (enabled or
    disabled).

    **AltTab** (and others): These are special Alt-Tab hotkey actions
    that are described [here](../Hotkeys.htm#alttab).

Options

:   Type: [String](../Concepts.htm#strings)

    A string of zero or more of the following options with optional
    spaces in between. For example: `"On B0"`.

    **On:** Enables the hotkey if it is currently disabled.

    **Off:** Disables the hotkey if it is currently enabled. This is
    typically used to create a hotkey in an initially-disabled state.

    **B** or **B0**: Specify the letter B to buffer the hotkey as
    described in [#MaxThreadsBuffer](_MaxThreadsBuffer.htm). Specify
    `B0` (B with the number 0) to disable this type of buffering.

    **P***n*: Specify the letter P followed by the hotkey\'s [thread
    priority](../misc/Threads.htm). If the P option is omitted when
    creating a hotkey, 0 will be used.

    **S** or **S0**: Specify the letter S to make the hotkey
    [exempt](_SuspendExempt.htm) from [Suspend](Suspend.htm), which
    allows the hotkey to be used to turn Suspend off. Specify S0 (S with
    the number 0) to remove the exemption, allowing the hotkey to be
    suspended.

    **T***n*: Specify the letter T followed by a the number of threads
    to allow for this hotkey as described in
    [#MaxThreadsPerHotkey](_MaxThreadsPerHotkey.htm). For example: `T5`.

    **I***n* (InputLevel): Specify the letter I (or i) followed by the
    hotkey\'s [input level](_InputLevel.htm). For example: `I1`.

    If any of the option letters are omitted and the hotkey already
    exists, those options will not be changed. But if the hotkey does
    not yet exist \-- that is, it is about to be created by this
    function \-- the options will default to those most recently in
    effect. For example, the instance of
    [#MaxThreadsBuffer](_MaxThreadsBuffer.htm) that occurs closest to
    the bottom of the script will be used. If
    [#MaxThreadsBuffer](_MaxThreadsBuffer.htm) does not appear in the
    script, its default setting (OFF in this case) will be used.

## Error Handling {#Error_Handling}

An exception is thrown if a parameter is invalid or memory allocation
fails.

One of the following exceptions may be thrown if the hotkey is invalid
or could not be created:

  Error Class                            .Message                                                    Description
  -------------------------------------- ----------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [ValueError](Error.htm#ValueError)     Invalid key name.                                           The *KeyName* parameter specifies one or more keys that are either not recognized or not supported by the current keyboard layout/language. [Exception.Extra](Error.htm#Extra) contains the key name; e.g. \"Entre\" from `!Entre`.
                                         Unsupported prefix key.                                     For example, using the mouse wheel as a prefix in a hotkey such as `WheelDown & Enter` is not supported. [Exception.Extra](Error.htm#Extra) contains the prefix key.
                                         This AltTab hotkey must have exactly one modifier/prefix.   The *KeyName* parameter is not suitable for use with the [AltTab or ShiftAltTab](../Hotkeys.htm#alttab) actions. A combination of (at most) two keys is required. For example: `RControl & RShift::AltTab`. [Exception.Extra](Error.htm#Extra) contains *KeyName*.
                                         This AltTab hotkey must specify which key (L or R).         
  [TargetError](Error.htm#TargetError)   Nonexistent hotkey.                                         The function attempted to modify a nonexistent hotkey. [Exception.Extra](Error.htm#Extra) contains *KeyName*.
                                         Nonexistent hotkey variant (IfWin).                         The function attempted to modify a nonexistent [variant](#variant) of an existing hotkey. To solve this, use [HotIf](HotIf.htm) to set the criteria to match those of the hotkey to be modified. [Exception.Extra](Error.htm#Extra) contains *KeyName*.
  [Error](Error.htm)                     Max hotkeys.                                                Creating this hotkey would exceed the limit of 32762 hotkeys per script (however, each hotkey can have an unlimited number of [variants](#variant), and there is no limit to the number of [hotstrings](../Hotstrings.htm)).

Tip: [Try](Try.htm)-[Catch](Catch.htm) can be used to test for the
existence of a hotkey variant. For example:

    try
        Hotkey "^!p"
    catch TargetError
        MsgBox "The hotkey does not exist or it has no variant for the current HotIf criteria."

## Remarks {#Remarks}

The [current HotIf setting](HotIf.htm) determines the
[variant](#variant) of a hotkey upon which the Hotkey function will
operate.

If the goal is to disable selected hotkeys or hotstrings automatically
based on the type of window that is active, `Hotkey "^!c", "Off"` is
usually less convenient than using [#HotIf](_HotIf.htm) with
[WinActive](WinActive.htm)/[WinExist](WinExist.htm) (or their dynamic
counterparts [HotIfWinActive/Exist](HotIf.htm#IfWin)).

Creating hotkeys via the [double-colon syntax](../Hotkeys.htm) performs
better than using the Hotkey function because the hotkeys can all be
enabled as a batch when the script starts (rather than one by one).
Therefore, it is best to use this function to create only those hotkeys
whose key names are not known until after the script has started
running. One such case is when a script\'s hotkeys for various actions
are configurable via an [INI file](IniRead.htm).

If the script is [suspended](Suspend.htm), newly added/enabled hotkeys
will also be suspended until the suspension is turned off (unless they
are exempt as described in the [Suspend](Suspend.htm) section).

The [keyboard](InstallKeybdHook.htm) and/or
[mouse](InstallMouseHook.htm) hooks will be installed or removed if
justified by the changes made by this function.

Although the Hotkey function cannot directly enable or disable hotkeys
in scripts other than its own, in most cases it can
[override](../misc/Override.htm) them by creating or enabling the same
hotkeys. Whether this works depends on a combination of factors: 1)
Whether the hotkey to be overridden is a [hook hotkey](ListHotkeys.htm)
in the other script (non-hook hotkeys can always be overridden); 2) The
fact that the most recently started script\'s hotkeys generally take
precedence over those in other scripts (therefore, if the script
intending to override was started most recently, its override should
always succeed); 3) Whether the enabling or creating of this hotkey will
newly activate the [keyboard](InstallKeybdHook.htm) or
[mouse](InstallMouseHook.htm) hook (if so, the override will always
succeed).

Once a script has at least one hotkey, it becomes
[persistent](../Scripts.htm#persistent), meaning that
[ExitApp](ExitApp.htm) rather than [Exit](Exit.htm) should be used to
terminate it.

## Variant (Duplicate) Hotkeys {#variant}

A particular hotkey can be created more than once if each definition has
different [HotIf](HotIf.htm) criteria. These are known as *hotkey
variants*. For example:

    HotIfWinActive "ahk_class Notepad"
    Hotkey "^!c", MyFuncForNotepad
    HotIfWinActive "ahk_class WordPadClass"
    Hotkey "^!c", MyFuncForWordPad
    HotIfWinActive
    Hotkey "^!c", MyFuncForAllOtherWindows

If more than one variant of a hotkey is eligible to fire, only the one
created earliest will fire. The exception to this is the global variant
(the one with no HotIf criteria): It always has the lowest precedence,
and thus will fire only if no other variant is eligible.

When creating duplicate hotkeys, the order of [modifier
symbols](../Hotkeys.htm#Symbols) such as `^!+#` does not matter. For
example, `"^!c"` is the same as `"!^c"`. However, keys must be spelled
consistently. For example, *Esc* is not the same as *Escape* for this
purpose (though the case does not matter). Finally, any hotkey with a
[wildcard prefix (\*)](../Hotkeys.htm#wildcard) is entirely separate
from a non-wildcard one; for example, `"*F1"` and `"F1"` would each have
their own set of variants.

For more information, see [HotIf](HotIf.htm) and [#HotIf\'s General
Remarks](_HotIf.htm#general-remarks).

## Related {#Related}

[Hotkeys](../Hotkeys.htm), [HotIf](HotIf.htm),
[A_ThisHotkey](../Variables.htm#ThisHotkey),
[#MaxThreadsBuffer](_MaxThreadsBuffer.htm),
[#MaxThreadsPerHotkey](_MaxThreadsPerHotkey.htm),
[Suspend](Suspend.htm), [Threads](../misc/Threads.htm),
[Thread](Thread.htm), [Critical](Critical.htm), [Return](Return.htm),
[Menu object](Menu.htm), [SetTimer](SetTimer.htm), [Hotstring
function](Hotstring.htm)

## Examples

::: {#ExBasic .ex}
[](#ExBasic){.ex_number} Creates a Ctrl-Alt-Z hotkey.

    Hotkey "^!z", MyFunc

    MyFunc(ThisHotkey)
    {
        MsgBox "You pressed " ThisHotkey
    }
:::

::: {#ExAltTab .ex}
[](#ExAltTab){.ex_number} Makes RCtrl & RShift operate like Alt-Tab.

    Hotkey "RCtrl & RShift", "AltTab"
:::

::: {#ExOff .ex}
[](#ExOff){.ex_number} Disables the Shift-Win-C hotkey.

    Hotkey "$+#c", "Off"
:::

::: {#ExT .ex}
[](#ExT){.ex_number} Changes a hotkey to allow 5 threads.

    Hotkey "^!a",, "T5"
:::

::: {#ExIfWin .ex}
[](#ExIfWin){.ex_number} Creates [Alt]{.kbd}+[W]{.kbd} as a hotkey that
works only in Notepad.

    HotIfWinActive "ahk_class Notepad"
    Hotkey "!w", ToggleWordWrap  ; !w = Alt+W

    ToggleWordWrap(ThisHotkey)
    {
        MenuSelect "A",, "Format", "Word Wrap"
    }
:::

::: {#ExampleIfFn .ex}
[](#ExampleIfFn){.ex_number} Creates a GUI that allows to register
primitive three-key combination hotkeys.

    HkGui := Gui()
    HkGui.Add("Text", "xm", "Prefix key:")
    HkGui.Add("Edit", "yp x100 w100 vPrefix", "Space")
    HkGui.Add("Text", "xm", "Suffix hotkey:")
    HkGui.Add("Edit", "yp x100 w100 vSuffix", "f & j")
    HkGui.Add("Button", "Default", "Register").OnEvent("Click", RegisterHotkey)
    HkGui.OnEvent("Close", (*) => ExitApp())
    HkGui.OnEvent("Escape", (*) => ExitApp())
    HkGui.Show()

    RegisterHotkey(*)
    {
        Saved := HkGui.Submit(false)
        HotIf (*) => GetKeyState(Saved.Prefix)
        Hotkey Saved.Suffix, (ThisHotkey) => MsgBox(ThisHotkey)
    }
:::
