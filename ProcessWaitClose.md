# ProcessWaitClose

Waits for all matching processes to close.

``` Syntax
PID := ProcessWaitClose(PIDOrName , Timeout)
```

## Parameters {#Parameters}

PIDOrName

:   Type: [Integer](../Concepts.htm#numbers) or
    [String](../Concepts.htm#strings)

    Specify either a number (the PID) or a process name:

    **PID:** The Process ID, which is a number that uniquely identifies
    one specific process (this number is valid only during the lifetime
    of that process). The PID of a newly launched process can be
    determined via the [Run](Run.htm) function. Similarly, the PID of a
    window can be determined with [WinGetPID](WinGetPID.htm).
    [ProcessExist](ProcessExist.htm) can also be used to discover a PID.

    **Name:** The name of a process is usually the same as its
    executable (without path), e.g. notepad.exe or winword.exe. Since a
    name might match multiple running processes, only the first process
    will be operated upon. The name is not case-sensitive.

Timeout

:   Type: [Integer](../Concepts.htm#numbers) or
    [Float](../Concepts.htm#numbers)

    If omitted, the function will wait indefinitely. Otherwise, specify
    the number of seconds (can contain a decimal point) to wait before
    timing out.

## Return Value {#Return_Value}

Type: [Integer](../Concepts.htm#numbers)

If all matching processes are closed, zero is returned. If this function
times out, it returns the [Process ID
(PID)](../misc/WinTitle.htm#ahk_pid) of the first matching process that
still exists.

## Remarks {#Remarks}

Processes are checked every 100 milliseconds; the moment the condition
is satisfied, the function stops waiting. In other words, rather than
waiting for the timeout to expire, it immediately returns and continues
execution of the script. Also, while the function is in a waiting state,
new [threads](../misc/Threads.htm) can be launched via
[hotkey](../Hotkeys.htm), [custom menu item](Menu.htm), or
[timer](SetTimer.htm).

## Related {#Related}

[ProcessWait](ProcessWait.htm), [Run](Run.htm),
[WinWaitClose](WinWaitClose.htm), [Process functions](Process.htm), [Win
functions](Win.htm)

## Examples {#Examples}

See [example #1](ProcessWait.htm#ExBasic) on the
[ProcessWait](ProcessWait.htm) page.
