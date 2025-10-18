# FileSetAttrib

Changes the attributes of one or more files or folders. Wildcards are
supported.

``` Syntax
FileSetAttrib Attributes , FilePattern, Mode
```

## Parameters {#Parameters}

Attributes

:   Type: [String](../Concepts.htm#strings)

    The attributes to change. For example, `"+HA-R"`.

    To easily turn on, turn off or toggle attributes, prefix one or more
    of the following attribute letters with a plus (+), minus (-) or
    caret (\^) symbol, respectively:

    -   R = READONLY
    -   A = ARCHIVE
    -   S = SYSTEM
    -   H = HIDDEN
    -   N = NORMAL (this is valid only when used without any other
        attributes)
    -   O = OFFLINE
    -   T = TEMPORARY

    If no symbol precedes the attribute letters, the file\'s attributes
    are replaced with the given attributes. See [example
    #5](#ExReplace). To remove all attributes, use `"N"` on its own.

FilePattern

:   Type: [String](../Concepts.htm#strings)

    If omitted, the current file of the innermost enclosing [file
    loop](LoopFiles.htm) will be used. Otherwise, specify the name of a
    single file or folder, or a wildcard pattern such as
    `"C:\Temp\*.tmp"`. *FilePattern* is assumed to be in
    [A_WorkingDir](../Variables.htm#WorkingDir) if an absolute path
    isn\'t specified.

    Both asterisks (`*`) and question marks (`?`) are supported as
    wildcards. `*` matches zero or more characters and `?` matches any
    single character. Usage examples:

    -   `*.*` or `*` matches all files.
    -   `*.htm` matches files with the extension .htm, .html, etc.
    -   `*.` matches files without an extension.
    -   `log?.txt` matches e.g. log1.txt but not log10.txt.
    -   `*report*` matches any filename containing the word \"report\".

Mode

:   Type: [String](../Concepts.htm#strings)

    If blank or omitted, only files are operated upon and subdirectories
    are not recursed into. Otherwise, specify one or more of the
    following letters:

    -   D = Include directories (folders).
    -   F = Include files. If both F and D are omitted, files are
        included but not folders.
    -   R = Subfolders are recursed into so that files and folders
        contained therein are operated upon if they match *FilePattern*.
        All subfolders will be recursed into, not just those whose names
        match *FilePattern*. If R is omitted, files and folders in
        subfolders are not included.

## Error Handling {#Error_Handling}

An [Error](Error.htm) is thrown if any files failed to be changed, with
its [Extra](Error.htm#Extra) property set to the number of failures.

If files were found, [A_LastError](../Variables.htm#LastError) is set to
0 (zero) or the result of the operating system\'s GetLastError()
function immediately after the last failure. Otherwise A_LastError
contains an error code that might indicate why no files were found.

## Remarks {#Remarks}

The compression state of files cannot be changed with this function.

## Related {#Related}

[FileGetAttrib](FileGetAttrib.htm), [FileGetTime](FileGetTime.htm),
[FileSetTime](FileSetTime.htm), [FileGetSize](FileGetSize.htm),
[FileGetVersion](FileGetVersion.htm), [file loop](LoopFiles.htm)

## Examples {#Examples}

::: {#ExTurnOnMultiple .ex}
[](#ExTurnOnMultiple){.ex_number} Turns on the \"read-only\" and
\"hidden\" attributes of all files and directories (subdirectories are
not recursed into).

    FileSetAttrib "+RH", "C:\MyFiles\*.*", "DF"  ; +RH is identical to +R+H
:::

::: {#ExToggle .ex}
[](#ExToggle){.ex_number} Toggles the \"hidden\" attribute of a single
directory.

    FileSetAttrib "^H", "C:\MyFiles"
:::

::: {#ExMixed .ex}
[](#ExMixed){.ex_number} Turns off the \"read-only\" attribute and turns
on the \"archive\" attribute of a single file.

    FileSetAttrib "-R+A", "C:\New Text File.txt"
:::

::: {#ExRecurse .ex}
[](#ExRecurse){.ex_number} Recurses through all .ini files on the C
drive and turns on their \"archive\" attribute.

    FileSetAttrib "+A", "C:\*.ini", "R"
:::

::: {#ExReplace .ex}
[](#ExReplace){.ex_number} Copies the attributes of *file2* to *file1*,
i.e. it adds any attributes that *file2* has and removes any attributes
that *file2* does not have.

    FileSetAttrib(FileGetAttrib(file2), file1)
:::
