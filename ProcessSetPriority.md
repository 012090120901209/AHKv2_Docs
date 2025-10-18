# ProcessSetPriority

Changes the priority level of the first matching process.

``` Syntax
ProcessSetPriority Level , PIDOrName
```

## Parameters {#Parameters}

Level

:   Type: [String](../Concepts.htm#strings)

    Specify one of the following words or letters:

    -   Low (or L)
    -   BelowNormal (or B)
    -   Normal (or N)
    -   AboveNormal (or A)
    -   High (or H)
    -   Realtime (or R)

    Note that any process not designed to run at Realtime priority might
    reduce system stability if set to that level.

PIDOrName

:   Type: [Integer](../Concepts.htm#numbers) or
    [String](../Concepts.htm#strings)

    If omitted, the script\'s own process is used. Otherwise, specify
    either a number (the PID) or a process name:

    **PID:** The Process ID, which is a number that uniquely identifies
    one specific process (this number is valid only during the lifetime
    of that process). The PID of a newly launched process can be
    determined via the [Run](Run.htm) function. Similarly, the PID of a
    window can be determined with [WinGetPID](WinGetPID.htm).
    [ProcessExist](ProcessExist.htm) can also be used to discover a PID.

    **Name:** The name of a process is usually the same as its
    executable (without path), e.g. notepad.exe or winword.exe. Since a
    name might match multiple running processes, only the first process
    will be operated upon. The name is not case-sensitive.

## Return Value {#Return_Value}

Type: [Integer](../Concepts.htm#numbers)

This function returns the [Process ID
(PID)](../misc/WinTitle.htm#ahk_pid) of the specified process. If a
matching process is not found or cannot be manipulated, zero is
returned.

## Remarks {#Remarks}

The current priority level of a process can be seen in the Windows Task
Manager.

## Related {#Related}

[Run](Run.htm), [Process functions](Process.htm), [Win
functions](Win.htm)

## Examples {#Examples}

::: {#ExBasic .ex}
[](#ExBasic){.ex_number} Launches Notepad, sets its priority to high and
reports its current PID.

    Run "notepad.exe", , , &NewPID
    ProcessSetPriority "High", NewPID
    MsgBox "The newly launched Notepad's PID is " NewPID
:::

::: {#ExHotkey .ex}
[](#ExHotkey){.ex_number} Press a hotkey to change the priority of the
active window\'s process.

    #z:: ; Win+Z hotkey
    {
        active_pid := WinGetPID("A")
        active_title := WinGetTitle("A")
        MyGui := Gui(, "Set Priority")
        MyGui.Add("Text",, "
        (
            Press ESCAPE to cancel, or double-click a new
            priority level for the following window:
        )")
        MyGui.Add("Text", "wp", active_title)
        LB := MyGui.Add("ListBox", "r5 Choose1", ["Normal", "High", "Low", "BelowNormal", "AboveNormal"])
        LB.OnEvent("DoubleClick", SetPriority)
        MyGui.Add("Button", "default", "OK").OnEvent("Click", SetPriority)
        MyGui.OnEvent("Escape", (*) => MyGui.Destroy())
        MyGui.OnEvent("Close", (*) => MyGui.Destroy())
        MyGui.Show()

        SetPriority(*)
        {
            new_prio := LB.Text
            MyGui.Destroy()
            if ProcessSetPriority(new_prio, active_pid)
                MsgBox "Success: Its priority was changed to " new_prio
            else
                MsgBox "Error: Its priority could not be changed to " new_prio
        }
    }
:::
