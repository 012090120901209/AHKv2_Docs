# FileExist

Checks for the existence of a file or folder and returns its attributes.

``` Syntax
AttributeString := FileExist(FilePattern)
```

## Parameters {#Parameters}

FilePattern

:   Type: [String](../Concepts.htm#strings)

    The name of a single file or folder, or a wildcard pattern such as
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

## Return Value {#Return_Value}

Type: [String](../Concepts.htm#strings)

This function returns the attributes of the first matching file or
folder. This string is a subset of `RASHNDOCTL`, where each letter means
the following:

-   R = READONLY
-   A = ARCHIVE
-   S = SYSTEM
-   H = HIDDEN
-   N = NORMAL
-   D = DIRECTORY
-   O = OFFLINE
-   C = COMPRESSED
-   T = TEMPORARY
-   L = REPARSE_POINT (typically a symbolic link)

If the file has no attributes (rare), \"X\" is returned. If no file or
folder is found, an empty string is returned.

## Remarks {#Remarks}

Note that a wildcard check like `InStr(FileExist("MyFolder\*"), "D")`
with *MyFolder* containing files and subfolders will only tell you
whether the [first]{.underline} matching file is a folder, not whether a
folder exists. To check for the latter, use [DirExist](DirExist.htm),
e.g. `DirExist("MyFolder\*")`.

Unlike [FileGetAttrib](FileGetAttrib.htm), FileExist supports wildcard
patterns and always returns a non-empty value if a matching file exists.

Since an empty string is seen as \"false\", the function\'s return value
can always be used as a quasi-boolean value. For example, the statement
`if FileExist("C:\My File.txt")` would be true if the file exists and
false otherwise.

Since *FilePattern* may contain wildcards, FileExist may be unsuitable
for validating a file path which is to be used with another function or
program. For example, `FileExist("*.txt")` may return attributes even
though \"\*.txt\" is not a valid filename. In such cases,
[FileGetAttrib](FileGetAttrib.htm) is preferred.

## Related {#Related}

[DirExist](DirExist.htm), [FileGetAttrib](FileGetAttrib.htm), [file
loops](LoopFiles.htm)

## Examples {#Examples}

::: {#ExDrive .ex}
[](#ExDrive){.ex_number} Shows a message box if the D drive does exist.

    if FileExist("D:\")
        MsgBox "The drive exists."
:::

::: {#ExPattern .ex}
[](#ExPattern){.ex_number} Shows a message box if at least one text file
does exist in a directory.

    if FileExist("D:\Docs\*.txt")
        MsgBox "At least one .txt file exists."
:::

::: {#ExNot .ex}
[](#ExNot){.ex_number} Shows a message box if a file does
[not]{.underline} exist.

    if not FileExist("C:\Temp\FlagFile.txt")
        MsgBox "The target file does not exist."
:::

::: {#ExAttr .ex}
[](#ExAttr){.ex_number} Demonstrates how to check a file for a specific
attribute.

    if InStr(FileExist("C:\My File.txt"), "H")
        MsgBox "The file is hidden."
:::
