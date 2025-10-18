# #NoTrayIcon

Disables the showing of a [tray icon](../Program.htm#tray-icon).

``` Syntax
#NoTrayIcon
```

Specifying this anywhere in a script will prevent the showing of a tray
icon for that script when it is launched (even if the script is compiled
into an EXE).

If you use this for a script that has hotkeys, you might want to bind a
hotkey to the [ExitApp](ExitApp.htm) function. Otherwise, there will be
no easy way to exit the program (without restarting the computer or
killing the process). For example: `#x::ExitApp`.

The tray icon can be made to disappear or reappear at any time during
the execution of the script by assigning a true or false value to
[A_IconHidden](../Variables.htm#IconHidden). The only drawback of using
[`A_IconHidden`](../Variables.htm#IconHidden)` := true` at the very top
of the script is that the tray icon might be briefly visible when the
script is first launched. To avoid that, use #NoTrayIcon instead.

The built-in variable **A_IconHidden** contains 1 if the tray icon is
currently hidden or 0 otherwise, and can be assigned a value to show or
hide the icon.

Like other directives, #NoTrayIcon cannot be executed conditionally.

## Related {#Related}

[Tray Icon](../Program.htm#tray-icon), [TraySetIcon](TraySetIcon.htm),
[A_IconHidden](../Variables.htm#IconHidden),
[A_IconTip](../Variables.htm#IconTip), [ExitApp](ExitApp.htm)

## Examples {#Examples}

::: {#ExBasic .ex}
[](#ExBasic){.ex_number} Causes the script to launch without a tray
icon.

    #NoTrayIcon
:::
