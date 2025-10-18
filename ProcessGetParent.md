# ProcessGetParent

Returns the process ID (PID) of the process which created the specified
process.

``` Syntax
PID := ProcessGetParent(PIDOrName)
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
    [ProcessExist](ProcessExist.htm) can also be used to discover a PID.

    **Name:** The name of a process is usually the same as its
    executable (without path), e.g. notepad.exe or winword.exe. Since a
    name might match multiple running processes, only the first process
    will be operated upon. The name is not case-sensitive.

## Return Value {#Return_Value}

Type: [Integer](../Concepts.htm#numbers)

This function returns the process ID (PID) of the process which created
the specified process.

## Error Handling {#Error_Handling}

A [TargetError](Error.htm#TargetError) is thrown if the specified
process could not be found.

## Remarks {#Remarks}

If the parent process is no longer running, there is some risk that the
returned PID has been reused by the system, and now identifies a
different process.

## Related {#Related}

[Process functions](Process.htm)

## Examples {#Examples}

::: {#ExBasic .ex}
[](#ExBasic){.ex_number} Display the name of the process which launched
the script.

    try
        MsgBox ProcessGetName(ProcessGetParent())
    catch
        MsgBox "Unable to retrieve parent process name; the process has likely exited."
:::
