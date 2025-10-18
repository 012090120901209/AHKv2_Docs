# FileGetVersion

Retrieves the version of a file.

``` Syntax
Version := FileGetVersion(Filename)
```

## Parameters {#Parameters}

Filename

:   Type: [String](../Concepts.htm#strings)

    If omitted, the current file of the innermost enclosing [file
    loop](LoopFiles.htm) will be used. Otherwise, specify the name of
    the target file. If a full path is not specified, this function uses
    the search sequence specified by the system
    [LoadLibrary](https://learn.microsoft.com/windows/win32/api/libloaderapi/nf-libloaderapi-loadlibrarya)
    function.

## Return Value {#Return_Value}

Type: [String](../Concepts.htm#strings)

This function returns the version number of the specified file.

## Error Handling {#Error_Handling}

An [OSError](Error.htm#OSError) is thrown on failure, such as if the
file lacks version information.

[A_LastError](../Variables.htm#LastError) is set to the result of the
operating system\'s GetLastError() function.

## Remarks {#Remarks}

Most non-executable files (and even some EXEs) have no version, and thus
an error will be thrown.

## Related {#Related}

[FileGetAttrib](FileGetAttrib.htm), [FileSetAttrib](FileSetAttrib.htm),
[FileGetTime](FileGetTime.htm), [FileSetTime](FileSetTime.htm),
[FileGetSize](FileGetSize.htm), [file loop](LoopFiles.htm)

## Examples {#Examples}

::: {#ExBasic .ex}
[](#ExBasic){.ex_number} Retrieves the version of a file and stores it
in `Version`{.variable}.

    Version := FileGetVersion("C:\My Application.exe")
:::

::: {#ExBIV .ex}
[](#ExBIV){.ex_number} Retrieves the version of the file
\"AutoHotkey.exe\" located in AutoHotkey\'s installation directory and
stores it in `Version`{.variable}.

    Version := FileGetVersion(A_ProgramFiles "\AutoHotkey\AutoHotkey.exe")
:::
