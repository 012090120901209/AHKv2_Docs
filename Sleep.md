# Sleep

Waits the specified amount of time before continuing.

``` Syntax
Sleep Delay
```

## Parameters {#Parameters}

Delay

:   Type: [Integer](../Concepts.htm#numbers)

    The amount of time to pause (in milliseconds) between 0 and
    2147483647 (24 days).

## Remarks {#Remarks}

Due to the granularity of the OS\'s time-keeping system, *Delay* is
typically rounded up to the nearest multiple of 10 or 15.6 milliseconds
(depending on the type of hardware and drivers installed). To achieve a
shorter delay, see [Examples](#ExShorterSleep).

The actual delay time might wind up being longer than what was requested
if the CPU is under load. This is because the OS gives each needy
process a slice of CPU time (typically 20 milliseconds) before giving
another timeslice to the script.

A delay of 0 yields the remainder of the script\'s current timeslice to
any other processes that need it (as long as they are not significantly
lower in [priority](ProcessSetPriority.htm) than the script). Thus, a
delay of 0 produces an actual delay between 0 and 20 ms (or more),
depending on the number of needy processes (if there are no needy
processes, there will be no delay at all). However, a *Delay* of 0
should always wind up being shorter than any longer *Delay* would have
been.

While sleeping, new [threads](../misc/Threads.htm) can be launched via
[hotkey](../Hotkeys.htm), [custom menu item](Menu.htm), or
[timer](SetTimer.htm).

**Sleep -1:** A delay of -1 does not sleep but instead makes the script
immediately check its message queue. This can be used to force any
pending [interruptions](../misc/Threads.htm) to occur at a specific
place rather than somewhere more random. See [Critical](Critical.htm)
for more details.

## Related {#Related}

[SetKeyDelay](SetKeyDelay.htm), [SetMouseDelay](SetMouseDelay.htm),
[SetControlDelay](SetControlDelay.htm), [SetWinDelay](SetWinDelay.htm)

## Examples {#Examples}

::: {#ExBasic .ex}
[](#ExBasic){.ex_number} Waits 1 second before continuing execution.

    Sleep 1000
:::

::: {#ExExpr .ex}
[](#ExExpr){.ex_number} Waits 30 minutes before continuing execution.

    MyVar := 30 * 60000 ; 30 means minutes and times 60000 gives the time in milliseconds.
    Sleep MyVar ; Sleep for 30 minutes.
:::

::: {#ExShorterSleep .ex}
[](#ExShorterSleep){.ex_number} Demonstrates how to sleep for less time
than the normal 10 or 15.6 milliseconds. Note: While a script like this
is running, the entire operating system and all applications are
affected by timeBeginPeriod below.

    SleepDuration := 1  ; This can sometimes be finely adjusted (e.g. 2 is different than 3) depending on the value below.
    TimePeriod := 3 ; Try 7 or 3.  See comment below.
    ; On a PC whose sleep duration normally rounds up to 15.6 ms, try TimePeriod=7 to allow
    ; somewhat shorter sleeps, and try TimePeriod=3 or less to allow the shortest possible sleeps.

    DllCall("Winmm\timeBeginPeriod", "UInt", TimePeriod)  ; Affects all applications, not just this script's DllCall("Sleep"...), but does not affect SetTimer.
    Iterations := 50
    StartTime := A_TickCount

    Loop Iterations
        DllCall("Sleep", "UInt", SleepDuration)  ; Must use DllCall instead of the Sleep function.

    DllCall("Winmm\timeEndPeriod", "UInt", TimePeriod)  ; Should be called to restore system to normal.
    MsgBox "Sleep duration = " . (A_TickCount - StartTime) / Iterations
:::
