# ProcessGetName / ProcessGetPath

Returns the name or path of the specified process.

``` Syntax
Name := ProcessGetName(PIDOrName)
Path := ProcessGetPath(PIDOrName)
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

Type: [String](../Concepts.htm#strings)

ProcessGetName returns the name of the specified process. For example:
notepad.exe.

ProcessGetPath returns the path of the specified process. For example:
C:\\Windows\\notepad.exe.

## Error Handling {#Error_Handling}

A [TargetError](Error.htm#TargetError) is thrown if the process could
not be found.

An [OSError](Error.htm) is thrown if the name/path could not be
retrieved.

## Related {#Related}

[Process functions](Process.htm), [Run](Run.htm),
[WinGetProcessName](WinGetProcessName.htm),
[WinGetProcessPath](WinGetProcessPath.htm)

## Examples {#Examples}

::: {#ExBasic .ex}
[](#ExBasic){.ex_number} Get the name and path of a process used to open
a document.

    Run "license.rtf",,, &pid  ; This is likely to exist in C:\Windows\System32.
    try {
        name := ProcessGetName(pid)
        path := ProcessGetPath(pid)
    }
    MsgBox "Name: " (name ?? "could not be retrieved") "`n"
        .  "Path: " (path ?? "could not be retrieved")
:::
