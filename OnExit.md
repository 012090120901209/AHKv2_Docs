# OnExit

Registers a [function](../Functions.htm) to be called automatically
whenever the script exits.

``` Syntax
OnExit Callback , AddRemove
```

## Parameters {#Parameters}

Callback

:   Type: [Function Object](../misc/Functor.htm)

    The function to call.

    The callback accepts two parameters and can be
    [defined](../Functions.htm#intro) as follows:

    ``` NoIndent
    MyCallback(ExitReason, ExitCode) { ...
    ```

    Although the names you give the parameters do not matter, the
    following values are sequentially assigned to them:

    1.  The exit reason (one of the words from the [table
        below](#ExitReason)).
    2.  The exit code passed to [Exit](Exit.htm) or
        [ExitApp](ExitApp.htm).

    You can omit one or more parameters from the end of the callback\'s
    parameter list if the corresponding information is not needed, but
    in this case an asterisk must be specified as the final parameter,
    e.g. `MyCallback(Param1, *)`.

    The callback can return a non-zero integer to prevent the script
    from exiting (with some [rare exceptions](#close)) and calling more
    callbacks. Otherwise, the script exits after all registered
    callbacks are called.

AddRemove

:   Type: [Integer](../Concepts.htm#numbers)

    If omitted, it defaults to 1. Otherwise, specify one of the
    following numbers:

    -   1 = Call the callback after any previously registered callbacks.
    -   -1 = Call the callback before any previously registered
        callbacks.
    -   0 = Do not call the callback.

## Remarks {#Remarks}

Any number of callbacks can be registered. A callback usually should not
call ExitApp; if it does, the script terminates immediately.

The callbacks are called when the script exits by any means (except when
it is killed by something like \"End Task\"). It is also called whenever
[#SingleInstance](_SingleInstance.htm) and [Reload](Reload.htm) ask a
previous instance to terminate.

A script can detect and optionally abort a system shutdown or logoff via
`OnMessage(0x0011, On_WM_QUERYENDSESSION)` (see [OnMessage example
#2](OnMessage.htm#ExShutdown) for a working script).

The OnExit [thread](../misc/Threads.htm) does not obey
[#MaxThreads](_MaxThreads.htm) (it will always launch when needed). In
addition, while it is running, it cannot be interrupted by any
[thread](../misc/Threads.htm), including [hotkeys](../Hotkeys.htm),
[custom menu items](Menu.htm), and [timed subroutines](SetTimer.htm).
However, it will be interrupted (and the script will terminate) if the
user chooses Exit from the tray menu or main menu, or the script is
asked to terminate as a result of [Reload](Reload.htm) or
[#SingleInstance](_SingleInstance.htm). Because of this, a callback
should be designed to finish quickly unless the user is aware of what it
is doing.

If the OnExit [thread](../misc/Threads.htm) encounters a failure
condition such as a runtime error, the script will terminate.

If the OnExit [thread](../misc/Threads.htm) was launched due to
[Exit](Exit.htm) or [ExitApp](ExitApp.htm) that specified an exit code,
that exit code is used unless a callback returns 1 (true) to prevent
exit or calls ExitApp.

Whenever an exit attempt is made, each callback starts off fresh with
the default values for settings such as [SendMode](SendMode.htm). These
defaults can be changed during [script startup](../Scripts.htm#auto).

## Exit Reasons {#ExitReason}

+-----------------------------------+-----------------------------------+
| Reason                            | Description                       |
+===================================+===================================+
| Logoff                            | The user is logging off.          |
+-----------------------------------+-----------------------------------+
| Shutdown                          | The system is being shut down or  |
|                                   | restarted, such as by the         |
|                                   | [Shutdown](Shutdown.htm)          |
|                                   | function.                         |
+-----------------------------------+-----------------------------------+
| Close                             | The script was sent a WM_CLOSE or |
|                                   | WM_QUIT message, had a critical   |
|                                   | error, or is being closed in some |
|                                   | other way. Although all of these  |
|                                   | are unusual, WM_CLOSE might be    |
|                                   | caused by                         |
|                                   | [WinClose](WinClose.htm) having   |
|                                   | been used on the script\'s main   |
|                                   | window. To close (hide) the       |
|                                   | window without terminating the    |
|                                   | script, use                       |
|                                   | [WinHide](WinHide.htm).           |
|                                   |                                   |
|                                   | If the script is exiting due to a |
|                                   | critical error or its [main       |
|                                   | wi                                |
|                                   | ndow](../Program.htm#main-window) |
|                                   | being destroyed, it will          |
|                                   | unconditionally terminate after   |
|                                   | the OnExit thread completes.      |
|                                   |                                   |
|                                   | If the main window is being       |
|                                   | destroyed, it may still exist but |
|                                   | cannot be displayed. This         |
|                                   | condition can be detected by      |
|                                   | monitoring the WM_DESTROY message |
|                                   | with [OnMessage](OnMessage.htm).  |
+-----------------------------------+-----------------------------------+
| Error                             | A runtime error occurred in a     |
|                                   | script that is not                |
|                                   | [persis                           |
|                                   | tent](../Scripts.htm#persistent). |
|                                   | An example of a runtime error is  |
|                                   | [Run/RunWait](Run.htm) being      |
|                                   | unable to launch the specified    |
|                                   | program or document.              |
+-----------------------------------+-----------------------------------+
| Menu                              | The user selected Exit from the   |
|                                   | [main                             |
|                                   | windo                             |
|                                   | w](../Program.htm#main-window)\'s |
|                                   | menu or from the [standard tray   |
|                                   | menu](../Program.htm#tray-icon).  |
+-----------------------------------+-----------------------------------+
| Exit                              | [Exit](Exit.htm) or               |
|                                   | [ExitApp](ExitApp.htm) was used   |
|                                   | (includes [custom menu            |
|                                   | items](Menu.htm)).                |
+-----------------------------------+-----------------------------------+
| Reload                            | The script is being reloaded via  |
|                                   | the [Reload](Reload.htm) function |
|                                   | or menu item.                     |
+-----------------------------------+-----------------------------------+
| Single                            | The script is being replaced by a |
|                                   | new instance of itself as a       |
|                                   | result of                         |
|                                   | [#Sing                            |
|                                   | leInstance](_SingleInstance.htm). |
+-----------------------------------+-----------------------------------+

## Related {#Related}

[OnError](OnError.htm), [OnMessage](OnMessage.htm),
[CallbackCreate](CallbackCreate.htm),
[OnClipboardChange](OnClipboardChange.htm), [ExitApp](ExitApp.htm),
[Shutdown](Shutdown.htm), [Persistent](Persistent.htm),
[Threads](../misc/Threads.htm), [Return](Return.htm)

## Examples {#Examples}

::: {#ExBasic .ex}
[](#ExBasic){.ex_number} Asks the user before exiting the script. To
test this example, right-click the [tray icon](../Program.htm#tray-icon)
and click Exit.

``` NoIndent
Persistent  ; Prevent the script from exiting automatically.
OnExit ExitFunc

ExitFunc(ExitReason, ExitCode)
{
    if ExitReason != "Logoff" and ExitReason != "Shutdown"
    {
        Result := MsgBox("Are you sure you want to exit?",, 4)
        if Result = "No"
            return 1  ; Callbacks must return non-zero to avoid exit.
    }
    ; Do not call ExitApp -- that would prevent other callbacks from being called.
}
```
:::

::: {#ExFnObj .ex}
[](#ExFnObj){.ex_number} Registers a method to be called on exit.

    Persistent  ; Prevent the script from exiting automatically.
    OnExit MyObject.Exiting

    class MyObject
    {
        static Exiting(*)
        {
            MsgBox "MyObject is cleaning up prior to exiting..."
            /*
            this.SayGoodbye()
            this.CloseNetworkConnections()
            */
        }
    }
:::
