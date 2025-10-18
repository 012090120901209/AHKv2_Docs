# Pause

Pauses the script\'s [current thread](../misc/Threads.htm) or sets the
pause state of the underlying thread.

``` Syntax
Pause UnderlyingThreadState
```

## Parameters {#Parameters}

UnderlyingThreadState

:   Type: [Integer](../Concepts.htm#numbers)

    If omitted, the [current thread](../misc/Threads.htm) is paused.
    Otherwise, specify one of the following values:

    `1` or `True`: Marks the underlying thread as paused. The current
    thread is not paused and continues running. When the current thread
    finishes, the underlying thread resumes any interrupted function the
    underlying thread was running. Once the underlying thread finishes
    the function (if any), it enters a paused state. If there is no
    thread underneath the current thread, the script itself is paused,
    which prevents [timers](SetTimer.htm) from running (this effect is
    the same as having used the menu item \"Pause Script\" while the
    script has no threads).

    `0` or `False`: Unpauses the underlying thread.

    `-1`: Toggles the pause state of the underlying thread.

## Remarks {#Remarks}

By default, the script can also be paused via its [tray
icon](../Program.htm#tray-icon) or [main
window](../Program.htm#main-window).

Unlike [Suspend](Suspend.htm) \-- which disables
[hotkeys](../Hotkeys.htm) and [hotstrings](../Hotstrings.htm) \--
turning on pause will freeze the thread (the [current
thread](../misc/Threads.htm) if *UnderlyingThreadState* was omitted,
otherwise the underlying thread). As a side-effect, any interrupted
threads underneath it will lie dormant until the current thread is
unpaused and finishes.

Whenever any thread or the script itself is paused,
[timers](SetTimer.htm) will not run. By contrast, explicitly launched
threads such as [hotkeys](../Hotkeys.htm) and [menu items](Menu.htm) can
still be launched; but when their [threads](../misc/Threads.htm) finish,
the underlying thread will still be paused. In other words, each thread
can be paused independently of the others.

The [tray icon](../Program.htm#tray-icon) changes to ![a green icon with
a Pause
symbol](../static/ahk16_pause.png){style="vertical-align:-.2em;"} (or to
![a green icon with a transparent Pause
symbol](../static/ahk16_pause_suspend.png){style="vertical-align:-.2em;"}
if the script is also [suspended](Suspend.htm)), whenever the script\'s
[current thread](../misc/Threads.htm) is in a paused state. This icon
change can be avoided by freezing the icon, which is achieved by using
[`TraySetIcon`](TraySetIcon.htm)`(,, true)`.

To disable [timers](SetTimer.htm) without pausing the script, use
[Thread NoTimers](Thread.htm#NoTimers).

A script is always halted (though not officially paused) while it is
displaying any kind of [menu](Menu.htm) (tray menu, menu bar, GUI
context menu, etc.)

The built-in variable **A_IsPaused** contains 1 if the thread
immediately underneath the current thread is paused and 0 otherwise.

## Related {#Related}

[Suspend](Suspend.htm), [Menu object](Menu.htm), [ExitApp](ExitApp.htm),
[Threads](../misc/Threads.htm), [SetTimer](SetTimer.htm)

## Examples {#Examples}

::: {#ExHalt .ex}
[](#ExHalt){.ex_number} Use Pause to halt the script, such as to inspect
variables.

    ListVars
    Pause
    ExitApp ; This line will not execute until the user unpauses the script.
:::

::: {#ExHotkey .ex}
[](#ExHotkey){.ex_number} Press a hotkey once to pause the script. Press
it again to unpause.

    Pause::Pause -1  ; The Pause/Break key.
    #p::Pause -1  ; Win+P
:::

::: {#ExPostMessage .ex}
[](#ExPostMessage){.ex_number} Sends a Pause command to another script.

    DetectHiddenWindows True
    WM_COMMAND := 0x0111
    ID_FILE_PAUSE := 65403
    PostMessage WM_COMMAND, ID_FILE_PAUSE,,, "C:\YourScript.ahk ahk_class AutoHotkey"
:::
