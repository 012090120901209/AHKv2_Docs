# FileCopy

Copies one or more files.

``` Syntax
FileCopy SourcePattern, DestPattern , Overwrite
```

## Parameters {#Parameters}

SourcePattern

:   Type: [String](../Concepts.htm#strings)

    The name of a single file or folder, or a wildcard pattern such as
    `"C:\Temp\*.tmp"`. *SourcePattern* is assumed to be in
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

DestPattern

:   Type: [String](../Concepts.htm#strings)

    The name or pattern of the destination, which is assumed to be in
    [A_WorkingDir](../Variables.htm#WorkingDir) if an absolute path
    isn\'t specified.

    If present, the first asterisk (`*`) in the filename is replaced
    with the source filename excluding its extension, while the first
    asterisk after the last full stop (`.`) is replaced with the source
    file\'s extension. If an asterisk is present but the extension is
    omitted, the source file\'s extension is used.

    To perform a simple copy \-- retaining the existing file name(s) \--
    specify only the folder name as shown in these mostly equivalent
    examples:

        FileCopy "C:\*.txt", "C:\My Folder"

        FileCopy "C:\*.txt", "C:\My Folder\*.*"

    The destination directory must already exist. If *My Folder* does
    not exist, the first example above will use \"My Folder\" as the
    target filename, while the second example will copy no files.

Overwrite

:   Type: [Integer](../Concepts.htm#numbers)

    If omitted, it defaults to 0. Otherwise, specify one of the
    following numbers to indicate whether to overwrite files if they
    already exist:

    **0:** Do not overwrite existing files. The operation will fail and
    have no effect if *DestPattern* already exists as a file or
    directory.

    **1:** Overwrite existing files. However, any files or subfolders
    inside *DestPattern* that do not have a counterpart in
    *SourcePattern* will not be deleted.

    Other values are reserved for future use.

## Error Handling {#Error_Handling}

An [Error](Error.htm) is thrown if any files failed to be copied, with
its [Extra](Error.htm#Extra) property set to the number of failures. If
no files were found, an error is thrown only if *SourcePattern* lacks
the wildcards `*` and `?`. In other words, copying a wildcard pattern
such as `"*.txt"` is considered a success when it does not match any
files.

Unlike [FileMove](FileMove.htm), copying a file onto itself is always
counted as an error, even if the overwrite mode is in effect.

If files were found, [A_LastError](../Variables.htm#LastError) is set to
0 (zero) or the result of the operating system\'s GetLastError()
function immediately after the last failure. Otherwise A_LastError
contains an error code that might indicate why no files were found.

## Remarks {#Remarks}

FileCopy copies files only. To instead copy the contents of a folder
(all its files and subfolders), see the examples section below. To copy
a single folder (including its subfolders), use [DirCopy](DirCopy.htm).

The operation will continue even if error(s) are encountered.

## Related {#Related}

[FileMove](FileMove.htm), [DirCopy](DirCopy.htm),
[DirMove](DirMove.htm), [FileDelete](FileDelete.htm)

## Examples {#Examples}

::: {#ExKeepOrigName .ex}
[](#ExKeepOrigName){.ex_number} Makes a copy but keep the original file
name.

    FileCopy "C:\My Documents\List1.txt", "D:\Main Backup\"
:::

::: {#ExNewName .ex}
[](#ExNewName){.ex_number} Copies a file into the same directory by
providing a new name.

    FileCopy "C:\My File.txt", "C:\My File New.txt"
:::

::: {#ExNewExt .ex}
[](#ExNewExt){.ex_number} Copies text files to a new location and gives
them a new extension.

    FileCopy "C:\Folder1\*.txt", "D:\New Folder\*.bkp"
:::

::: {#ExCopyAll .ex}
[](#ExCopyAll){.ex_number} Copies all files and folders inside a folder
to a different folder.

    ErrorCount := CopyFilesAndFolders("C:\My Folder\*.*", "D:\Folder to receive all files & folders")
    if ErrorCount != 0
        MsgBox ErrorCount " files/folders could not be copied."

    CopyFilesAndFolders(SourcePattern, DestinationFolder, DoOverwrite := false)
    ; Copies all files and folders matching SourcePattern into the folder named DestinationFolder and
    ; returns the number of files/folders that could not be copied.
    {
        ErrorCount := 0
        ; First copy all the files (but not the folders):
        try
            FileCopy SourcePattern, DestinationFolder, DoOverwrite
        catch as Err
            ErrorCount := Err.Extra
        ; Now copy all the folders:
        Loop Files, SourcePattern, "D"  ; D means "retrieve folders only".
        {
            try
                DirCopy A_LoopFilePath, DestinationFolder "\" A_LoopFileName, DoOverwrite
            catch
            {
                ErrorCount += 1
                ; Report each problem folder by name.
                MsgBox "Could not copy " A_LoopFilePath " into " DestinationFolder
            }
        }
        return ErrorCount
    }
:::
