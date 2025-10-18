# ProcessClose

Forces the first matching process to close.

``` Syntax
ProcessClose PIDOrName
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

## Return Value {#Return_Value}

Type: [Integer](../Concepts.htm#numbers)

This function returns the [Process ID
(PID)](../misc/WinTitle.htm#ahk_pid) of the specified process. If a
matching process is not found or cannot be manipulated, zero is
returned.

## Remarks {#Remarks}

Since the process will be abruptly terminated \-- possibly interrupting
its work at a critical point or resulting in the loss of unsaved data in
its windows (if it has any) \-- this function should be used only if a
process cannot be closed by using [WinClose](WinClose.htm) on one of its
windows.

## Related {#Related}

[Run](Run.htm), [WinClose](WinClose.htm), [WinKill](WinKill.htm),
[Process functions](Process.htm), [Win functions](Win.htm)

## Examples {#Examples}

::: {#ExBasic .ex}
[](#ExBasic){.ex_number} Forces the first matching process to close (be
warned that any unsaved data will be lost).

    ProcessClose "notepad.exe"
:::

::: {#ExCloseAll .ex}
[](#ExCloseAll){.ex_number} Forces [all]{.underline} matching processes
to close.

    ProcessCloseAll(PIDOrName)
    {
        While ProcessExist(PIDOrName)
            ProcessClose PIDOrName
    }

    ; Example:
    Loop 3
        Run "notepad.exe"
    Sleep 3000
    ProcessCloseAll "notepad.exe"
:::
