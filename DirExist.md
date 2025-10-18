# DirExist

Checks for the existence of a folder and returns its attributes.

``` Syntax
AttributeString := DirExist(FilePattern)
```

## Parameters {#Parameters}

FilePattern

:   Type: [String](../Concepts.htm#strings)

    The name of a single folder or a wildcard pattern such as
    `"C:\Program*"`. *FilePattern* is assumed to be in
    [A_WorkingDir](../Variables.htm#WorkingDir) if an absolute path
    isn\'t specified.

    Both asterisks (`*`) and question marks (`?`) are supported as
    wildcards. `*` matches zero or more characters and `?` matches any
    single character. Usage examples:

    -   `*` matches all folders.
    -   `gr?y` matches e.g. gray and grey.
    -   `*report*` matches any folder name containing the word
        \"report\".

## Return Value {#Return_Value}

Type: [String](../Concepts.htm#strings)

This function returns the attributes of the first matching folder. This
string is a subset of `RASHDOC`, where each letter means the following:

-   R = READONLY
-   A = ARCHIVE
-   S = SYSTEM
-   H = HIDDEN
-   D = DIRECTORY
-   O = OFFLINE
-   C = COMPRESSED

Since this function only checks for the existence of a folder, \"D\" is
always present in the return value. If no folder is found, an empty
string is returned.

## Remarks {#Remarks}

Note that searches such as `DirExist("MyFolder\*")` with *MyFolder*
containing files and subfolders will only tell you whether a folder
exists. If you want to check for the existence of files
[and]{.underline} folders, use [FileExist](FileExist.htm) instead.

Unlike [FileGetAttrib](FileGetAttrib.htm), DirExist supports wildcard
patterns and always returns a non-empty value if a matching folder
exists.

Since an empty string is seen as \"false\", the function\'s return value
can always be used as a quasi-boolean value. For example, the statement
`if DirExist("C:\MyFolder")` would be true if the folder exists and
false otherwise.

Since *FilePattern* may contain wildcards, DirExist may be unsuitable
for validating a folder path which is to be used with another function
or program. For example, `DirExist("Program*")` may return attributes
even though \"Program\*\" is not a valid folder name. In such cases,
[FileGetAttrib](FileGetAttrib.htm) is preferred.

## Related {#Related}

[FileExist](FileExist.htm), [FileGetAttrib](FileGetAttrib.htm), [file
loops](LoopFiles.htm)

## Examples {#Examples}

::: {#ExBasic .ex}
[](#ExBasic){.ex_number} Shows a message box if a folder does exist.

    if DirExist("C:\Windows")
        MsgBox "The target folder does exist."
:::

::: {#ExPattern .ex}
[](#ExPattern){.ex_number} Shows a message box if at least one program
folder does exist.

    if DirExist("C:\Program*")
        MsgBox "At least one program folder exists."
:::

::: {#ExNot .ex}
[](#ExNot){.ex_number} Shows a message box if a folder does
[not]{.underline} exist.

    if not DirExist("C:\Temp")
        MsgBox "The target folder does not exist."
:::

::: {#ExAttr .ex}
[](#ExAttr){.ex_number} Demonstrates how to check a folder for a
specific attribute.

    if InStr(DirExist("C:\System Volume Information"), "H")
        MsgBox "The folder is hidden."
:::
