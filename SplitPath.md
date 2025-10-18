# SplitPath

Separates a file name or URL into its name, directory, extension, and
drive.

``` Syntax
SplitPath Path , &OutFileName, &OutDir, &OutExtension, &OutNameNoExt, &OutDrive
```

## Parameters {#Parameters}

Path

:   Type: [String](../Concepts.htm#strings)

    The file name or URL to be analyzed.

    Note that this function expects filename paths to contain
    backslashes (\\) only and URLs to contain forward slashes (/) only.

&OutFileName

:   Type: [VarRef](../Concepts.htm#variable-references)

    If omitted, the corresponding value will not be stored. Otherwise,
    specify a reference to the output variable in which to store the
    file name without its path. The file\'s extension is included.

&OutDir

:   Type: [VarRef](../Concepts.htm#variable-references)

    If omitted, the corresponding value will not be stored. Otherwise,
    specify a reference to the output variable in which to store the
    directory of the file, including drive letter or share name (if
    present). The final backslash is not included even if the file is
    located in a drive\'s root directory.

&OutExtension

:   Type: [VarRef](../Concepts.htm#variable-references)

    If omitted, the corresponding value will not be stored. Otherwise,
    specify a reference to the output variable in which to store the
    file\'s extension (e.g. TXT, DOC, or EXE). The dot is not included.

&OutNameNoExt

:   Type: [VarRef](../Concepts.htm#variable-references)

    If omitted, the corresponding value will not be stored. Otherwise,
    specify a reference to the output variable in which to store the
    file name without its path, dot and extension.

&OutDrive

:   Type: [VarRef](../Concepts.htm#variable-references)

    If omitted, the corresponding value will not be stored. Otherwise,
    specify a reference to the output variable in which to store the
    drive letter or server name of the file. If the file is on a local
    or mapped drive, the variable will be set to the drive letter
    followed by a colon (no backslash). If the file is on a network path
    (UNC), the variable will be set to the share name, e.g.
    \\\\Workstation01

## Remarks {#Remarks}

Any of the output variables may be omitted if the corresponding
information is not needed.

If *Path* contains a filename that lacks a drive letter (that is, it has
no path or merely a relative path), *OutDrive* will be made blank but
all the other output variables will be set correctly. Similarly, if
there is no path present, *OutDir* will be made blank; and if there is a
path but no file name present, *OutFileName* and *OutNameNoExt* will be
made blank.

Actual files and directories in the file system are not checked by this
function. It simply analyzes the provided string.

Wildcards (\* and ?) and other characters illegal in filenames are
treated the same as legal characters, with the exception of colon,
backslash, and period (dot), which are processed according to their
nature in delimiting the drive letter, directory, and extension of the
file.

**Support for URLs:** If *Path* contains a colon-double-slash, such as
in `"https://domain.com"` or `"ftp://domain.com"`, *OutDir* is set to
the protocol prefix + domain name + directory (e.g.
https://domain.com/images) and *OutDrive* is set to the protocol
prefix + domain name (e.g. https://domain.com). All other variables are
set according to their definitions above.

## Related {#Related}

[A_LoopFileExt](LoopFiles.htm#LoopFileExt), [StrSplit](StrSplit.htm),
[InStr](InStr.htm), [SubStr](SubStr.htm), [FileSelect](FileSelect.htm),
[DirSelect](DirSelect.htm)

## Examples {#Examples}

::: {#ExBasic .ex}
[](#ExBasic){.ex_number} Demonstrates different usages.

    FullFileName := "C:\My Documents\Address List.txt"
       
    ; To fetch only the bare filename from the above:
    SplitPath FullFileName, &name

    ; To fetch only its directory:
    SplitPath FullFileName,, &dir

    ; To fetch all info:
    SplitPath FullFileName, &name, &dir, &ext, &name_no_ext, &drive
       
    ; The above will set the variables as follows:
    ; name = Address List.txt
    ; dir = C:\My Documents
    ; ext = txt
    ; name_no_ext = Address List
    ; drive = C:
:::
