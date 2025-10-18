# Run / RunWait

Runs an external program. Unlike Run, RunWait will wait until the
program finishes before continuing.

``` Syntax
Run Target , WorkingDir, Options, &OutputVarPID
ExitCode := RunWait(Target , WorkingDir, Options, &OutputVarPID)
```

## Parameters {#Parameters}

Target

:   Type: [String](../Concepts.htm#strings)

    A document, URL, executable file (.exe, .com, .bat, etc.), shortcut
    (.lnk), [CLSID](#CLSID), or [system verb](#verbs) to launch (see
    remarks). If *Target* is a local file and no path was specified with
    it, how the file is located typically depends on the type of file
    and other conditions. See [Interpretation of
    Target](#Interpretation_of_Target) for details.

    To pass parameters, add them immediately after the program or
    document name as follows:

        Run 'MyProgram.exe Param1 Param2'

    If the program/document name or a parameter contains spaces, it is
    safest to enclose it in double quotes as follows (even though it may
    work without them in some cases):

        Run '"My Program.exe" "param with spaces"'

WorkingDir

:   Type: [String](../Concepts.htm#strings)

    If blank or omitted, the script\'s own working directory
    ([A_WorkingDir](../Variables.htm#WorkingDir)) will be used.
    Otherwise, specify the initial working directory to be used by the
    new process. This typically also affects relative paths in *Target*,
    but interpretation of command-line parameters depends on the target
    program.

Options

:   Type: [String](../Concepts.htm#strings)

    If blank or omitted, *Target* will be launched normally. Otherwise,
    specify one or more of the following options:

    **Max:** launch maximized

    **Min:** launch minimized

    **Hide:** launch hidden (cannot be used in combination with either
    of the above)

    **Note:** Some applications (e.g. Calc.exe) do not obey the
    requested startup state and thus Max/Min/Hide will have no effect.

&OutputVarPID

:   Type: [VarRef](../Concepts.htm#variable-references)

    If omitted, the corresponding value will not be stored. Otherwise,
    specify a reference to the output variable in which to store the
    newly launched program\'s unique [Process ID
    (PID)](../misc/WinTitle.htm#ahk_pid). The variable will be made
    blank if the PID could not be determined, which usually happens if a
    system verb, document, or shortcut is launched rather than a direct
    executable file. RunWait also supports this parameter, though its
    *OutputVarPID* must be checked in [another
    thread](../misc/Threads.htm) (otherwise, the PID will be invalid
    because the process will have terminated by the time the line
    following RunWait executes).

    After the Run function retrieves a PID, any windows to be created by
    the process might not exist yet. To wait for at least one window to
    be created, use [`WinWait`](WinWait.htm)` "ahk_pid " OutputVarPID`.

## Return Value {#Return_Value}

Type: [Integer](../Concepts.htm#numbers)

Unlike Run, RunWait will wait until *Target* is closed or exits, at
which time the return value will be the program\'s exit code (as a
signed 32-bit integer). Some programs will appear to return immediately
even though they are still running; these programs spawn another
process.

## Error Handling {#Error_Handling}

If *Target* cannot be launched, an exception is thrown (that is, an
error window is displayed) and the current thread is exited, unless the
error is caught by a [Try](Try.htm)/[Catch](Catch.htm) statement. For
example:

    try
        Run "NonExistingFile"
    catch
        MsgBox "File does not exist."

The built-in variable [A_LastError](../Variables.htm#LastError) is set
to the result of the operating system\'s GetLastError() function.

## Interpretation of Target {#Interpretation_of_Target}

Run/RunWait itself does not interpret command-line parameters or search
for the target file. Instead, it attempts to execute the target as
follows:

-   If no verb is specified, *Target* is passed as-is to the
    *lpCommandLine* parameter of
    [CreateProcess](https://learn.microsoft.com/windows/win32/api/processthreadsapi/nf-processthreadsapi-createprocessw).
-   If a verb is specified or CreateProcess fails, and
    [RunAs](RunAs.htm) is not in effect,
    [ShellExecuteEx](https://learn.microsoft.com/windows/win32/api/shellapi/nf-shellapi-shellexecuteexw)
    is attempted.

If *Target* specifies a name but not a directory, the system will search
for and launch the file if it is integrated (\"known\"), e.g. by being
contained in one of the PATH folders. The exact search order depends on
whether CreateProcess and/or ShellExecuteEx is called. If CreateProcess
is called, the application directory (which contains the AutoHotkey
interpreter or compiled script) takes precedence over the working
directory specified by *WorkingDir*. To avoid this, specify the
directory; e.g. `.\program.exe`.

When ShellExecuteEx is being attempted, *Target* is interpreted as
follows:

-   The substring of *Target* ending at the first space or tab may be
    either a [predefined verb name](#verbs) or an asterisk followed by a
    verb name. If present, the optional asterisk, verb name and a single
    delimiting space or tab are excluded from further consideration.
    Verb names containing spaces or tabs are not supported, but symbols
    such as hyphen are permitted.
-   If a leading double-quote mark is present, the substring between
    that and the next double-quote mark is considered to be the target
    file or action.
-   Otherwise, the first substring which ends at a space and is either
    an existing file (specified by absolute path or relative to
    *WorkingDir*) or ends in .exe, .bat, .com, .cmd or .hta is
    considered the action. This allows file types such as .ahk, .vbs or
    .lnk to accept parameters while still allowing \"known\" executables
    such as wordpad.exe to be launched without an absolute path.
-   A single delimiting space is ignored, if present, and the remainder
    of *Target* is passed as-is to CreateProcess or ShellExecuteEx as
    command-line parameters.

## Remarks {#Remarks}

When running a program via [ComSpec](../Variables.htm#ComSpec) (cmd.exe)
\-- perhaps because you need to redirect the program\'s input or output
\-- if the path or name of the executable contains spaces, the entire
string should be enclosed in an outer pair of quotes. In the following
example, the outer quotes are highlighted in yellow:

    Run A_ComSpec ' /c ""C:\My Utility.exe" "param 1" "second param" >"C:\My File.txt""'

Performance may be slightly improved if *Target* is an exact path, e.g.
`Run 'C:\Windows\Notepad.exe "C:\My Documents\Test.txt"'` rather than
`Run "C:\My Documents\Test.txt"`.

Special [CLSIDs](../misc/CLSID-List.htm) may be opened via Run. Most of
them can be opened by using the shell: prefix. Some can be opened
without it. For example:

    Run "shell:::{D20EA4E1-3957-11D2-A40B-0C5020524153}"  ; Windows Tools.
    Run "::{20D04FE0-3AEA-1069-A2D8-08002B30309D}"  ; This PC (formerly My Computer or Computer).
    Run "::{645FF040-5081-101B-9F08-00AA002F954E}"  ; Recycle Bin.

System verbs correspond to actions available in a file\'s right-click
menu in the Explorer. If a file is launched without a verb, the default
verb (usually \"open\") for that particular file type will be used. If
specified, the verb should be followed by the name of the target file.
The following verbs are currently supported:

+-----------------------------------+-----------------------------------+
| Verb                              | Description                       |
+===================================+===================================+
| \**verb*                          | Any system-defined or custom      |
|                                   | verb. For example:                |
|                                   | `R                                |
|                                   | un "*Compile " A_ScriptFullPath`. |
|                                   | The [\*RunAs](#RunAs) verb may be |
|                                   | used in place of the *Run as      |
|                                   | administrator* right-click menu   |
|                                   | item.                             |
+-----------------------------------+-----------------------------------+
| properties                        | Displays the Explorer\'s          |
|                                   | properties window for the         |
|                                   | indicated file. For example:      |
|                                   | `R                                |
|                                   | un 'properties "C:\My File.txt"'` |
|                                   |                                   |
|                                   | **Note:** The properties window   |
|                                   | will automatically close when the |
|                                   | script terminates. To prevent     |
|                                   | this, use [WinWait](WinWait.htm)  |
|                                   | to wait for the window to appear, |
|                                   | then use                          |
|                                   | [WinWaitClose](WinWaitClose.htm)  |
|                                   | to wait for the user to close it. |
+-----------------------------------+-----------------------------------+
| find                              | Opens an instance of the          |
|                                   | Explorer\'s Search Companion or   |
|                                   | Find File window at the indicated |
|                                   | folder. For example:              |
|                                   | `Run "find D:\"`                  |
+-----------------------------------+-----------------------------------+
| explore                           | Opens an instance of Explorer at  |
|                                   | the indicated folder. For         |
|                                   | example:                          |
|                                   | `Run "explore " A_ProgramFiles`.  |
+-----------------------------------+-----------------------------------+
| edit                              | Opens the indicated file for      |
|                                   | editing. It might not work if the |
|                                   | indicated file\'s type does not   |
|                                   | have an \"edit\" action           |
|                                   | associated with it. For example:  |
|                                   | `Run 'edit "C:\My File.txt"'`     |
+-----------------------------------+-----------------------------------+
| open                              | Opens the indicated file          |
|                                   | (normally not needed because it   |
|                                   | is the default action for most    |
|                                   | file types). For example:         |
|                                   | `Run 'open "My File.txt"'`.       |
+-----------------------------------+-----------------------------------+
| print                             | Prints the indicated file with    |
|                                   | the associated application, if    |
|                                   | any. For example:                 |
|                                   | `Run 'print "My File.txt"'`       |
+-----------------------------------+-----------------------------------+

While RunWait is in a waiting state, new [threads](../misc/Threads.htm)
can be launched via [hotkey](../Hotkeys.htm), [custom menu
item](Menu.htm), or [timer](SetTimer.htm).

## Run as Administrator {#RunAs}

For an executable file, the *\*RunAs* verb is equivalent to selecting
*Run as administrator* from the right-click menu of the file. For
example, the following code attempts to restart the current script as
admin:

    full_command_line := DllCall("GetCommandLine", "str")

    if not (A_IsAdmin or RegExMatch(full_command_line, " /restart(?!\S)"))
    {
        try
        {
            if A_IsCompiled
                Run '*RunAs "' A_ScriptFullPath '" /restart'
            else
                Run '*RunAs "' A_AhkPath '" /restart "' A_ScriptFullPath '"'
        }
        ExitApp
    }

    MsgBox "A_IsAdmin: " A_IsAdmin "`nCommand line: " full_command_line

If the user cancels the [User Account Control
(UAC)](https://en.wikipedia.org/wiki/User_Account_Control) dialog or Run
fails for some other reason, the script will simply exit.

Using [/restart](../Scripts.htm#SlashR) ensures that a [single
instance](_SingleInstance.htm) prompt is not shown if the new instance
of the script starts before ExitApp is called.

If UAC is disabled, *\*RunAs* will launch the process without elevating
it. Checking for `/restart` in the command line ensures that the script
does not enter a runaway loop in that case. Note that `/restart` is a
built-in switch, so is not included in the [array of command-line
parameters](../Scripts.htm#cmd_args).

The example can be modified to fit the script\'s needs:

-   If the script absolutely requires admin rights, check
    [A_IsAdmin](../Variables.htm#IsAdmin) a second time in case
    *\*RunAs* failed to elevate the script (i.e. because UAC is
    disabled).
-   To keep the script running even if the user cancels the UAC prompt,
    move [ExitApp](ExitApp.htm) into the try block.
-   To keep the script running even if it failed to restart (i.e.
    because the script file has been changed or deleted), remove ExitApp
    and use RunWait instead of Run. On success, `/restart` causes the
    new instance to terminate the old one. On failure, the new instance
    exits and RunWait returns.

AutoHotkey\'s installer registers the *RunAs* verb for *.ahk* files,
which allows `Run "*RunAs script.ahk"` to launch a script as admin.

## Related {#Related}

[RunAs](RunAs.htm), [Process functions](Process.htm), [Exit](Exit.htm),
[CLSID List](../misc/CLSID-List.htm), [DllCall](DllCall.htm)

## Examples {#Examples}

::: {#ExBasic .ex}
[](#ExBasic){.ex_number} Run is able to launch Windows system programs
from any directory. Note that executable file extensions such as .exe
can be omitted.

    Run "notepad"
:::

::: {#ExURL .ex}
[](#ExURL){.ex_number} Run is able to launch URLs:

The following opens an internet address in the user\'s default web
browser.

    Run "https://www.google.com"

The following opens the default e-mail application with the recipient
filled in.

    Run "mailto:someone@somedomain.com"

The following does the same as above, plus the subject and body.

    Run "mailto:someone@somedomain.com?subject=This is the subject line&body=This is the message body's text."
:::

::: {#ExErrorLevel .ex}
[](#ExErrorLevel){.ex_number} Opens a document in a maximized
application and displays a custom error message on failure.

    try Run("ReadMe.doc", , "Max")
    if A_LastError
        MsgBox "The document could not be launched."
:::

::: {#ExVerb .ex}
[](#ExVerb){.ex_number} Runs the dir command in minimized state and
stores the output in a text file. After that, the text file and its
properties dialog will be opened.

    RunWait A_ComSpec " /c dir C:\ >>C:\DirTest.txt", , "Min"
    Run "C:\DirTest.txt"
    Run "properties C:\DirTest.txt"
    Persistent  ; Keep the script from exiting, otherwise the properties dialog will close.
:::

::: {#ExCLSID .ex}
[](#ExCLSID){.ex_number} Run is able to launch
[CLSIDs](../misc/CLSID-List.htm):

The following opens the Recycle Bin.

    Run "::{645FF040-5081-101B-9F08-00AA002F954E}"

The following opens This PC (formerly My Computer or Computer).

    Run "::{20D04FE0-3AEA-1069-A2D8-08002B30309D}"
:::

::: {#ExMultipleCmds .ex}
[](#ExMultipleCmds){.ex_number} To run multiple commands consecutively,
use \"&&\" between each.

    Run A_ComSpec "/c dir /b > C:\list.txt && type C:\list.txt && pause"
:::

::: {#ExStdOut .ex}
[](#ExStdOut){.ex_number} The following custom functions can be used to
run a command and retrieve its output or to run multiple commands in one
go and retrieve their output. For the WshShell object, see [Microsoft
Docs](https://learn.microsoft.com/previous-versions/aew9yb99(v=vs.85)).

    MsgBox RunWaitOne("dir " A_ScriptDir)

    MsgBox RunWaitMany("
    (
    echo Put your commands here,
    echo each one will be run,
    echo and you'll get the output.
    )")

    RunWaitOne(command) {
        shell := ComObject("WScript.Shell")
        ; Execute a single command via cmd.exe
        exec := shell.Exec(A_ComSpec " /C " command)
        ; Read and return the command's output
        return exec.StdOut.ReadAll()
    }

    RunWaitMany(commands) {
        shell := ComObject("WScript.Shell")
        ; Open cmd.exe with echoing of commands disabled
        exec := shell.Exec(A_ComSpec " /Q /K echo off")
        ; Send the commands to execute, separated by newline
        exec.StdIn.WriteLine(commands "`nexit")  ; Always exit at the end!
        ; Read and return the output of all commands
        return exec.StdOut.ReadAll()
    }
:::

::: {#ExecScript .ex}
[](#ExecScript){.ex_number} Executes the given code as a new AutoHotkey
process.

    ExecScript(Script, Wait:=true)
    {
        shell := ComObject("WScript.Shell")
        exec := shell.Exec("AutoHotkey.exe /ErrorStdOut *")
        exec.StdIn.Write(Script)
        exec.StdIn.Close()
        if Wait
            return exec.StdOut.ReadAll()
    }

    ; Example:
    ib := InputBox("Enter an expression to evaluate as a new script.",,, 'Ord("*")')
    if ib.result = "Cancel"
        return
    result := ExecScript('FileAppend ' ib.value ', "*"')
    MsgBox "Result: " result
:::
