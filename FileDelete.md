# FileDelete

Deletes one or more files permanently.

``` Syntax
FileDelete FilePattern
```

## Parameters {#Parameters}

FilePattern

:   Type: [String](../Concepts.htm#strings)

    The name of a single file or a wildcard pattern such as
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

    To remove an entire folder, along with all its sub-folders and
    files, use [DirDelete](DirDelete.htm).

## Error Handling {#Error_Handling}

An [Error](Error.htm) is thrown if any files failed to be deleted, with
its [Extra](Error.htm#Extra) property set to the number of failures.
Deleting a wildcard pattern such as `"*.tmp"` is considered a success
even if it does not match any files.

If files were found, [A_LastError](../Variables.htm#LastError) is set to
0 (zero) or the result of the operating system\'s GetLastError()
function immediately after the last failure. Otherwise A_LastError
contains an error code that might indicate why no files were found.

## Remarks {#Remarks}

To send a file to the recycle bin, use the
[FileRecycle](FileRecycle.htm) function.

To delete a read-only file, first remove the read-only attribute. For
example: [`FileSetAttrib`](FileSetAttrib.htm)` "-R", "C:\My File.txt"`.

## Related {#Related}

[FileRecycle](FileRecycle.htm), [DirDelete](DirDelete.htm),
[FileCopy](FileCopy.htm), [FileMove](FileMove.htm)

## Examples {#Examples}

::: {#ExBasic .ex}
[](#ExBasic){.ex_number} Deletes all .tmp files in a directory.

    FileDelete "C:\temp files\*.tmp"
:::
