# HotIf / HotIfWin\...

Specifies the criteria for subsequently created or modified [hotkey
variants](Hotkey.htm#variant) and [hotstring
variants](Hotstring.htm#variant).

## HotIf {#If}

``` Syntax
HotIf "Expression"
HotIf Callback
```

### Parameters {#HotIf_Parameters}

\"Expression\"

:   Type: [String](../Concepts.htm#strings)

    If omitted, blank criteria will be set (turns off
    context-sensitivity). Otherwise, the criteria will be set to an
    existing [#HotIf](_HotIf.htm) expression. The expression is usually
    written as a [quoted string](../Language.htm#strings), but can also
    be a variable or expression which returns text matching a #HotIf
    expression.

    **Note:** The HotIf function uses the string that you pass to it,
    not the original source code. [Escape
    sequences](../misc/EscapeChar.htm) are resolved when the script
    loads, so only the resulting characters are considered; for example,
    `` HotIf 'x = "`t"' `` and `HotIf 'x = "' A_Tab '"'` both correspond
    to `` #HotIf x = "`t" ``.

    For an example, see [#HotIf example #5](_HotIf.htm#ExDynamic).

Callback

:   Type: [Function Object](../misc/Functor.htm)

    If omitted, blank criteria will be set (turns off
    context-sensitivity). Otherwise, the criteria will be set to a given
    function object. Subsequently-created hotkeys and hotstrings will
    only execute if the callback returns a non-zero number. This is like
    `HotIf "Expression"`, except that each hotkey and hotstring can have
    many [hotkey variants](Hotkey.htm#variant) or [hotstring
    variants](Hotstring.htm#variant) (one per object).

    The callback accepts one parameter and can be
    [defined](../Functions.htm#intro) as follows:

    ``` NoIndent
    MyCallback(HotkeyName) { ...
    ```

    Although the name you give the parameter does not matter, it is
    assigned the [hotkey name](../Hotkeys.htm#ThisHotkey) or [hotstring
    name](../Hotstrings.htm#ThisHotkey).

    You can omit the callback\'s parameter if the corresponding
    information is not needed, but in this case an asterisk must be
    specified, e.g. `MyCallback(*)`.

    Once passed to the HotIf function, the object will never be deleted
    (but memory will be reclaimed by the OS when the process exits).

    For an example, see [example #2](#ExHotIfCallback) below or [Hotkey
    example #6](Hotkey.htm#ExampleIfFn).

## HotIfWin\... {#IfWin}

``` Syntax
HotIfWinActive WinTitle, WinText
HotIfWinExist WinTitle, WinText
HotIfWinNotActive WinTitle, WinText
HotIfWinNotExist WinTitle, WinText
```

### Parameters {#HotIfWin_Parameters}

WinTitle, WinText

:   Type: [String](../Concepts.htm#strings)

    If both are omitted, blank criteria will be set (turns off
    context-sensitivity). Otherwise, specify for *WinTitle* a [window
    title or other criteria](../misc/WinTitle.htm) to identify the
    target window and/or for *WinText* a substring from a single text
    element of the target window (as revealed by the included Window Spy
    utility). Depending on which function is called, affected hotkeys
    and hotstrings are in effect only while the target window is active,
    exists, is not active, or does not exist.

    Since the parameters are evaluated before the function is called,
    any variable reference becomes permanent at that moment. In other
    words, subsequent changes to the contents of the variable are not
    seen by existing hotkeys and hotstrings.

    *WinTitle* and *WinText* have the same meaning as for
    [WinActive](WinActive.htm) or [WinExist](WinExist.htm), but only
    strings can be used, and they are evaluated according to the default
    settings for [SetTitleMatchMode](SetTitleMatchMode.htm) and
    [DetectHiddenWindows](DetectHiddenWindows.htm) as set by the
    [auto-execute thread](../Scripts.htm#auto).

    For an example, see [example #1](#ExHotIfWin) below.

## Error Handling {#Error_Handling}

An exception is thrown if HotIf\'s parameter is invalid, such as if it
does not match an existing expression or is not a valid callback
function.

## General Remarks {#remarks}

The HotIf and HotIfWin functions allow context-sensitive
[hotkeys](../Hotkeys.htm) and [hotstrings](../Hotstrings.htm) to be
created and modified while the script is running (by contrast, the
[#HotIf](_HotIf.htm) directive is positional and takes effect before the
script begins executing). For example:

    HotIfWinActive "ahk_class Notepad"
    Hotkey "^!e", MyFuncForNotepad  ; Creates a hotkey that works only in Notepad.

Using HotIf or one of the HotIfWin functions puts context sensitivity
into effect for all subsequently created [hotkeys](../Hotkeys.htm) and
[hotstrings](../Hotstrings.htm) in the current
[thread](../misc/Threads.htm), and affects which hotkey or hotstring
variants the [Hotkey](Hotkey.htm) or [Hotstring](Hotstring.htm) function
modifies. Only the most recent call to the HotIf or HotIfWin function in
the current thread will be in effect.

To turn off context sensitivity (such as to make subsequently-created
hotkeys and hotstrings work in all windows), call HotIf or one of the
HotIfWin functions but omit the parameters. For example: `HotIf` or
`HotIfWinActive`.

Before HotIf or one of the HotIfWin functions is used in a hotkey or
hotstring [thread](../misc/Threads.htm), the [Hotkey](Hotkey.htm) and
[Hotstring](Hotstring.htm) functions default to the same context as the
hotkey or hotstring that launched the thread. In other words,
`Hotkey A_ThisHotkey, "Off"` turns off the current hotkey even if it is
context-sensitive. All other threads default to creating or modifying
global hotkeys and hotstrings, unless that default is overridden by
using HotIf or one of the HotIfWin functions during [script
startup](../Scripts.htm#auto).

When a mouse or keyboard hotkey is disabled via HotIf, one of the
HotIfWin functions, or the [#HotIf](_HotIf.htm) directive, it performs
its native function; that is, it passes through to the active window as
though there is no such hotkey. However, controller hotkeys always pass
through, whether they are disabled or not.

## Related {#Related}

[Hotkeys](../Hotkeys.htm), [Hotstrings](../Hotstrings.htm), [Hotkey
function](Hotkey.htm), [Hotstring function](Hotstring.htm),
[#HotIf](_HotIf.htm), [Threads](../misc/Threads.htm)

## Examples

::: {#ExHotIfWin .ex}
[](#ExHotIfWin){.ex_number} Similar to [#HotIf example
#1](_HotIf.htm#ExBasic), this creates two hotkeys and one hotstring
which only work when Notepad is active, and one hotkey which works for
any window except Notepad. The main difference is that this example
creates context-sensitive hotkeys and hotstrings at runtime, while the
#HotIf example creates them at loadtime.

    HotIfWinActive "ahk_class Notepad"
    Hotkey "^!a", ShowMsgBox
    Hotkey "#c", ShowMsgBox
    Hotstring "::btw", "This replacement text will occur only in Notepad."
    HotIfWinActive
    Hotkey "#c", (*) => MsgBox("You pressed Win-C in a window other than Notepad.")

    ShowMsgBox(HotkeyName)
    {
        MsgBox "You pressed " HotkeyName " while Notepad is active."
    }
:::

::: {#ExHotIfCallback .ex}
[](#ExHotIfCallback){.ex_number} Similar to the example above, but with
a callback.

    HotIf MyCallback
    Hotkey "^!a", ShowMsgBox
    Hotkey "#c", ShowMsgBox
    Hotstring "::btw", "This replacement text will occur only in Notepad."
    HotIf
    Hotkey "#c", (*) => MsgBox("You pressed Win-C in a window other than Notepad.")

    MyCallback(*)
    {
        if WinActive("ahk_class Notepad")
            return true
        else
            return false
    }

    ShowMsgBox(HotkeyName)
    {
        MsgBox "You pressed " HotkeyName " while Notepad is active."
    }
:::
