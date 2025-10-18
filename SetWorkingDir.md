# SetWorkingDir

Changes the script\'s current working directory.

``` Syntax
SetWorkingDir DirName
```

## Parameters {#Parameters}

DirName

:   Type: [String](../Concepts.htm#strings)

    The name of the new working directory, which is assumed to be a
    subfolder of the current [A_WorkingDir](../Variables.htm#WorkingDir)
    if an absolute path isn\'t specified.

## Error Handling {#Error_Handling}

An [OSError](Error.htm#OSError) is thrown on failure.

## Remarks {#Remarks}

The script\'s working directory is the default directory that is used to
access files and folders when an absolute path has not been specified.
In the following example, the file *My Filename.txt* is assumed to be in
A_WorkingDir:
[`FileAppend`](FileAppend.htm)` "A Line of Text", "My Filename.txt"`.

The script\'s working directory defaults to
[A_ScriptDir](../Variables.htm#ScriptDir), regardless of how the script
was launched. By contrast, the value of
[A_InitialWorkingDir](../Variables.htm#InitialWorkingDir) is determined
by how the script was launched. For example, if it was run via shortcut
\-- such as on the Start Menu \-- its initial working directory is
determined by the \"Start in\" field within the shortcut\'s properties.

Once changed, the new working directory is instantly and globally in
effect throughout the script. All interrupted, [paused](Pause.htm), and
newly launched [threads](../misc/Threads.htm) are affected, including
[Timers](SetTimer.htm).

## Related {#Related}

[A_WorkingDir](../Variables.htm#WorkingDir),
[A_InitialWorkingDir](../Variables.htm#InitialWorkingDir),
[A_ScriptDir](../Variables.htm#ScriptDir), [DirSelect](DirSelect.htm)

## Examples {#Examples}

::: {#ExBasic .ex}
[](#ExBasic){.ex_number} Changes the script\'s current working
directory.

    SetWorkingDir "D:\My Folder\Temp"
:::

::: {#ExInitial .ex}
[](#ExInitial){.ex_number} Forces the script to use the folder it was
initially launched from as its working directory.

    SetWorkingDir A_InitialWorkingDir
:::
