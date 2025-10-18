# Suspend

Disables or enables all or selected [hotkeys](../Hotkeys.htm) and
[hotstrings](../Hotstrings.htm).

``` Syntax
Suspend NewState
```

## Parameters {#Parameters}

NewState

:   Type: [Integer](../Concepts.htm#numbers)

    If omitted, it defaults to -1. Otherwise, specify one of the
    following values:

    `1` or `True`: Suspends all [hotkeys](../Hotkeys.htm) and
    [hotstrings](../Hotstrings.htm) except those explained the Remarks
    section.

    `0` or `False`: Re-enables the hotkeys and hotstrings that were
    disable above.

    `-1`: Changes to the opposite of its previous state (On or Off).

## Remarks {#Remarks}

By default, the script can also be suspended via its [tray
icon](../Program.htm#tray-icon) or [main
window](../Program.htm#main-window).

A hotkey/hotstring can be made exempt from suspension by preceding it
with the [#SuspendExempt](_SuspendExempt.htm) directive. An exempt
hotkey/hotstring will remain enabled even while suspension is ON. This
allows suspension to be turned off via a hotkey, which would otherwise
be impossible since the hotkey would be suspended.

The [keyboard](InstallKeybdHook.htm) and/or
[mouse](InstallMouseHook.htm) hooks will be installed or removed if
justified by the changes made by this function.

To disable selected hotkeys or hotstrings automatically based on any
condition, such as the type of window that is active, use
[#HotIf](_HotIf.htm).

Suspending a script\'s hotkeys does not stop the script\'s
already-running [threads](../misc/Threads.htm) (if any); use
[Pause](Pause.htm) to do that.

When a script\'s hotkeys are suspended, its [tray
icon](../Program.htm#tray-icon) changes to ![a green icon with a
transparent
H](../static/ahk16_suspend.png){style="vertical-align:-.2em;"} (or to
![a green icon with a transparent Pause
symbol](../static/ahk16_pause_suspend.png){style="vertical-align:-.2em;"}
if the script is also [paused](Pause.htm)). This icon change can be
avoided by freezing the icon, which is achieved by using
[`TraySetIcon`](TraySetIcon.htm)`(,, true)`.

The built-in variable **A_IsSuspended** contains 1 if the script is
suspended and 0 otherwise.

## Related {#Related}

[#SuspendExempt](_SuspendExempt.htm), [Hotkeys](../Hotkeys.htm),
[Hotstrings](../Hotstrings.htm), [#HotIf](_HotIf.htm),
[Pause](Pause.htm), [ExitApp](ExitApp.htm)

## Examples {#Examples}

::: {#ExHotkey .ex}
[](#ExHotkey){.ex_number} Press a hotkey once to suspend all hotkeys and
hotstrings. Press it again to unsuspend.

    #SuspendExempt
    ^!s::Suspend  ; Ctrl+Alt+S
    #SuspendExempt False
:::

::: {#ExPostMessage .ex}
[](#ExPostMessage){.ex_number} Sends a Suspend command to another
script.

    DetectHiddenWindows True
    WM_COMMAND := 0x0111
    ID_FILE_SUSPEND := 65404
    PostMessage WM_COMMAND, ID_FILE_SUSPEND,,, "C:\YourScript.ahk ahk_class AutoHotkey"
:::
