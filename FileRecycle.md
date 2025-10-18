# FileRecycle

Sends a file or directory to the recycle bin if possible, or permanently
deletes it.

``` Syntax
FileRecycle FilePattern
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

    To recycle an entire directory, provide its name without a trailing
    backslash.

## Error Handling {#Error_Handling}

An exception is thrown on failure.

## Remarks {#Remarks}

[SHFileOperation](https://learn.microsoft.com/windows/win32/api/shellapi/nf-shellapi-shfileoperationa)
is used to do the actual work. This function may permanently delete the
file if it is too large to be recycled; also, a warning should be shown
before this occurs.

The file may be permanently deleted without warning if the file cannot
be recycled for other reasons, such as:

-   The file is on a removable drive.
-   The Recycle Bin has been disabled, such as via the `NukeOnDelete`
    registry value.

## Related {#Related}

[FileRecycleEmpty](FileRecycleEmpty.htm), [FileDelete](FileDelete.htm),
[FileCopy](FileCopy.htm), [FileMove](FileMove.htm)

## Examples {#Examples}

::: {#ExBasic .ex}
[](#ExBasic){.ex_number} Sends all .tmp files in a directory to the
recycle bin if possible.

    FileRecycle "C:\temp files\*.tmp"
:::
