# ProcessExist

Checks if the specified process exists.

``` Syntax
PID := ProcessExist(PIDOrName)
```

## Parameters {#Parameters}

PIDOrName

:   Type: [Integer](../Concepts.htm#numbers) or
    [String](../Concepts.htm#strings)

    If omitted, the script\'s own process is used. Otherwise, specify
    either a number (the PID) or a process name:

    **PID:** The Process ID, which is a number that uniquely identifies
    one specific process (this number is valid only during the lifetime
    of that process). The PID of a newly launched process can be
    determined via the [Run](Run.htm) function. Similarly, the PID of a
    window can be determined with [WinGetPID](WinGetPID.htm).

    **Name:** The name of a process is usually the same as its
    executable (without path), e.g. notepad.exe or winword.exe. Since a
    name might match multiple running processes, only the first process
    will be operated upon. The name is not case-sensitive.

## Return Value {#Return_Value}

Type: [Integer](../Concepts.htm#numbers)

This function returns the [Process ID
(PID)](../misc/WinTitle.htm#ahk_pid) of the specified process. If there
is no matching process, zero is returned.

## Related {#Related}

[Run](Run.htm), [WinExist](WinExist.htm), [Process
functions](Process.htm), [Win functions](Win.htm)

## Examples {#Examples}

::: {#ExBasic .ex}
[](#ExBasic){.ex_number} Checks if a process of Notepad exists.

    if (PID := ProcessExist("notepad.exe"))
        MsgBox "Notepad exists and has the Process ID " PID "."
    else
        MsgBox "Notepad does not exist."
:::
