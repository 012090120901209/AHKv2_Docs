# Process Functions

Functions for retrieving information about a process or for performing
various operations on a process. Click on a function name for details.

  Function                                       Description
  ---------------------------------------------- ----------------------------------------------------------------------------------
  [ProcessClose](ProcessClose.htm)               Forces the first matching process to close.
  [ProcessExist](ProcessExist.htm)               Checks if the specified process exists.
  [ProcessGetName](ProcessGetName.htm)           Returns the name of the specified process.
  [ProcessGetParent](ProcessGetParent.htm)       Returns the process ID (PID) of the process which created the specified process.
  [ProcessGetPath](ProcessGetName.htm)           Returns the path of the specified process.
  [ProcessSetPriority](ProcessSetPriority.htm)   Changes the priority level of the first matching process.
  [ProcessWait](ProcessWait.htm)                 Waits for the specified process to exist.
  [ProcessWaitClose](ProcessWaitClose.htm)       Waits for all matching processes to close.

## Remarks {#Remarks}

**Process list:** Although there is no *ProcessList* function, [example
#1](#ExList) and [example #2](#ExListCOM) demonstrate how to retrieve a
list of processes via [DllCall](DllCall.htm) or COM.

## Related {#Related}

[Run](Run.htm), [WinClose](WinClose.htm), [WinKill](WinKill.htm),
[WinWait](WinWait.htm), [WinWaitClose](WinWaitClose.htm),
[WinExist](WinExist.htm), [Win functions](Win.htm)

## Examples {#Examples}

::: {#ExList .ex}
[](#ExList){.ex_number} Shows a list of running processes retrieved via
[DllCall](DllCall.htm).

    d := "  |  "  ; string separator
    s := 4096  ; size of buffers and arrays (4 KB)

    ScriptPID := ProcessExist()  ; The PID of this running script.
    ; Get the handle of this script with PROCESS_QUERY_INFORMATION (0x0400):
    h := DllCall("OpenProcess", "UInt", 0x0400, "Int", false, "UInt", ScriptPID, "Ptr")
    ; Open an adjustable access token with this process (TOKEN_ADJUST_PRIVILEGES = 32):
    DllCall("Advapi32.dll\OpenProcessToken", "Ptr", h, "UInt", 32, "PtrP", &t := 0)
    ; Retrieve the locally unique identifier of the debug privilege:
    DllCall("Advapi32.dll\LookupPrivilegeValue", "Ptr", 0, "Str", "SeDebugPrivilege", "Int64P", &luid := 0)
    ti := Buffer(16, 0)  ; structure of privileges
    NumPut( "UInt", 1  ; one entry in the privileges array...
          , "Int64", luid
          , "UInt", 2  ; Enable this privilege: SE_PRIVILEGE_ENABLED = 2
          , ti)
    ; Update the privileges of this process with the new access token:
    r := DllCall("Advapi32.dll\AdjustTokenPrivileges", "Ptr", t, "Int", false, "Ptr", ti, "UInt", 0, "Ptr", 0, "Ptr", 0)
    DllCall("CloseHandle", "Ptr", t)  ; Close the access token handle to save memory.
    DllCall("CloseHandle", "Ptr", h)  ; Close the process handle to save memory.

    hModule := DllCall("LoadLibrary", "Str", "Psapi.dll")  ; Increase performance by preloading the library.
    a := Buffer(s)  ; An array that receives the list of process identifiers:
    c := 0  ; counter for process idendifiers
    l := ""
    DllCall("Psapi.dll\EnumProcesses", "Ptr", a, "UInt", s, "UIntP", &r)
    Loop r // 4  ; Parse array for identifiers as DWORDs (32 bits):
    {
        id := NumGet(a, A_Index * 4, "UInt")
        ; Open process with: PROCESS_VM_READ (0x0010) | PROCESS_QUERY_INFORMATION (0x0400)
        h := DllCall("OpenProcess", "UInt", 0x0010 | 0x0400, "Int", false, "UInt", id, "Ptr")
        if !h
            continue
        n := Buffer(s, 0)  ; A buffer that receives the base name of the module:
        e := DllCall("Psapi.dll\GetModuleBaseName", "Ptr", h, "Ptr", 0, "Ptr", n, "UInt", s//2)
        if !e    ; Fall-back method for 64-bit processes when in 32-bit mode:
            e := DllCall("Psapi.dll\GetProcessImageFileName", "Ptr", h, "Ptr", n, "UInt", s//2)
        SplitPath StrGet(n), &n
        DllCall("CloseHandle", "Ptr", h)  ; Close the process handle to save memory.
        if (n && e)  ; If image is not null add to list:
            l .= n "`n", c++
    }
    DllCall("FreeLibrary", "Ptr", hModule)  ; Unload the library to free memory.
    ;l := Sort(l)  ; Uncomment this line to sort the list alphabetically.
    MsgBox StrReplace(l, "`n", d), c " Processes", 0
:::

::: {#ExListCOM .ex}
[](#ExListCOM){.ex_number} Shows a list of running processes retrieved
via COM and
[Win32_Process](https://learn.microsoft.com/windows/win32/cimwin32prov/win32-process).

    MyGui := Gui(, "Process List")
    LV := MyGui.Add("ListView", "x2 y0 w400 h500", ["Process Name", "Command Line"])
    for process in ComObjGet("winmgmts:").ExecQuery("Select * from Win32_Process")
        LV.Add("", process.Name, process.CommandLine)
    MyGui.Show()
:::
