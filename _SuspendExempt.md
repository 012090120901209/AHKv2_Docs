# #SuspendExempt

Exempts subsequent [hotkeys](../Hotkeys.htm) and
[hotstrings](../Hotstrings.htm) from [suspension](Suspend.htm).

``` Syntax
#SuspendExempt Setting
```

## Parameters {#Parameters}

Setting

:   Type: [String](../Concepts.htm#strings) or
    [Integer](../Concepts.htm#numbers)

    If omitted, it defaults to *True*. Otherwise, specify one of the
    following literal values:

    **True** or **1**: Enables exemption for subsequent hotkeys and
    hotstrings.

    **False** or **0**: Disables exemption.

## Remarks {#Remarks}

If this directive is unspecified in the script, all hotkeys or
hotstrings are disabled when the script is suspended, even those which
call the [Suspend](Suspend.htm) function.

Hotkeys and hotstrings can be suspended by the [Suspend](Suspend.htm)
function or via the [tray icon](../Program.htm#tray-icon) or [main
window](../Program.htm#main-window).

This directive does not affect the [Hotkey](Hotkey.htm) or
[Hotstring](Hotstring.htm) functions, for which the [S hotkey
option](Hotkey.htm#SuspendExempt) or [S hotstring
option](../Hotstrings.htm#SuspendExempt) can be used instead.

Like other directives, #SuspendExempt cannot be executed conditionally.

## Related {#Related}

[Suspend](Suspend.htm), [Hotkeys](../Hotkeys.htm),
[Hotstrings](../Hotstrings.htm)

## Examples {#Examples}

::: {#ExBasic .ex}
[](#ExBasic){.ex_number} The first hotkey in this example toggles the
suspension. To prevent this hotkey from being suspended after the
suspension has been turned on and thus no longer being able to turn it
off, it must be exempted.

    #SuspendExempt  ; Exempt the following hotkey from Suspend.
    #Esc::Suspend -1
    #SuspendExempt False  ; Disable exemption for any hotkeys/hotstrings below this.
    ^1::MsgBox "This hotkey is affected by Suspend."
:::
