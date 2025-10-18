# DirMove

Moves a folder along with all its sub-folders and files. It can also
rename a folder.

``` Syntax
DirMove Source, Dest , OverwriteOrRename
```

## Parameters {#Parameters}

Source

:   Type: [String](../Concepts.htm#strings)

    Name of the source directory (with no trailing backslash), which is
    assumed to be in [A_WorkingDir](../Variables.htm#WorkingDir) if an
    absolute path isn\'t specified. For example: C:\\My Folder

Dest

:   Type: [String](../Concepts.htm#strings)

    The new path and name of the directory (with no trailing baskslash),
    which is assumed to be in
    [A_WorkingDir](../Variables.htm#WorkingDir) if an absolute path
    isn\'t specified. For example: D:\\My Folder.

    **Note:** *Dest* is the actual path and name that the directory will
    have after it is moved; it is *not* the directory into which
    *Source* is moved (except for the known limitation mentioned below).

OverwriteOrRename

:   Type: [String](../Concepts.htm#strings)

    If omitted, it defaults to 0. Otherwise, specify one of the
    following values to indicate whether to overwrite or rename existing
    files:

    **0:** Do not overwrite existing files. The operation will fail if
    *Dest* already exists as a file or directory.

    **1:** Overwrite existing files. However, any files or subfolders
    inside *Dest* that do not have a counterpart in *Source* will not be
    deleted. **Known limitation:** If *Dest* already exists as a folder
    and it is on the same volume as *Source*, *Source* will be moved
    into it rather than overwriting it. To avoid this, see the next
    option.

    **2:** The same as mode 1 above except that the limitation is
    absent.

    **R:** Rename the directory rather than moving it. Although renaming
    normally has the same effect as moving, it is helpful in cases where
    you want \"all or none\" behavior; that is, when you don\'t want the
    operation to be only partially successful when *Source* or one of
    its files is locked (in use). Although this method cannot move
    *Source* onto a different volume, it can move it to any other
    directory on its own volume. The operation will fail if *Dest*
    already exists as a file or directory.

## Error Handling {#Error_Handling}

An exception is thrown if an error occurs.

## Remarks {#Remarks}

DirMove moves a single folder to a new location. To instead move the
contents of a folder (all its files and subfolders), see the examples
section of [FileMove](FileMove.htm).

If the source and destination are on different volumes or UNC paths, a
copy/delete operation will be performed rather than a move.

## Related {#Related}

[DirCopy](DirCopy.htm), [FileCopy](FileCopy.htm),
[FileMove](FileMove.htm), [FileDelete](FileDelete.htm), [file
loops](LoopFiles.htm), [DirSelect](DirSelect.htm),
[SplitPath](SplitPath.htm)

## Examples {#Examples}

::: {#ExNewDrive .ex}
[](#ExNewDrive){.ex_number} Moves a directory to a new drive.

    DirMove "C:\My Folder", "D:\My Folder"
:::

::: {#ExRename .ex}
[](#ExRename){.ex_number} Performs a simple rename.

    DirMove "C:\My Folder", "C:\My Folder (renamed)", "R"
:::

::: {#ExNewLocation .ex}
[](#ExNewLocation){.ex_number} Directories can be \"renamed into\"
another location as long as it\'s on the same volume.

    DirMove "C:\My Folder", "C:\New Location\My Folder", "R"
:::
