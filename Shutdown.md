# Shutdown

Shuts down, restarts, or logs off the system.

``` Syntax
Shutdown Flag
```

## Parameters {#Parameters}

Flag

:   Type: [Integer](../Concepts.htm#numbers)

    A combination (sum) of the following numbers:

    -   0 = Logoff
    -   1 = Shutdown
    -   2 = Reboot
    -   4 = Force
    -   8 = Power down

    Add the required values together. For example, to shutdown and power
    down the flag would be 9 (shutdown + power down = 1 + 8 = 9).

    The \"Force\" value (4) forces all open applications to close. It
    should only be used in an emergency because it may cause any open
    applications to lose data.

    The \"Power down\" value (8) shuts down the system and turns off the
    power.

## Remarks {#Remarks}

To have the system suspend or hibernate, see [example #2](#ExSuspend) at
the bottom of this page.

To turn off the monitor, see [SendMessage example
#1](SendMessage.htm#ExMonitorPower).

On a related note, a script can detect when the system is shutting down
or the user is logging off via [OnExit](OnExit.htm).

## Related {#Related}

[Run](Run.htm), [ExitApp](ExitApp.htm), [OnExit](OnExit.htm)

## Examples {#Examples}

::: {#ExBasic .ex}
[](#ExBasic){.ex_number} Forces a reboot (reboot + force = 2 + 4 = 6).

    Shutdown 6
:::

::: {#ExSuspend .ex}
[](#ExSuspend){.ex_number} Calls the Windows API function
\"SetSuspendState\" to have the system suspend or hibernate. Note that
the second parameter may have no effect at all on newer systems.

    ; Parameter #1: Pass 1 instead of 0 to hibernate rather than suspend.
    ; Parameter #2: Pass 1 instead of 0 to suspend immediately rather than asking each application for permission.
    ; Parameter #3: Pass 1 instead of 0 to disable all wake events.
    DllCall("PowrProf\SetSuspendState", "Int", 0, "Int", 0, "Int", 0)
:::
