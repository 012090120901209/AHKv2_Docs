# Persistent

Prevents the script from exiting automatically when its last thread
completes, allowing it to stay running in an idle state.

``` Syntax
Persistent Persist
```

## Parameters {#Parameters}

Persist

:   Type: [Boolean](../Concepts.htm#boolean)

    If omitted, it defaults to true.

    If **true**, the script will be kept running after all threads have
    exited, even if none of the other conditions for keeping the script
    running are met.

    If **false**, the default behaviour is restored.

## Return Value {#Return_Value}

Type: [Integer (boolean)](../Concepts.htm#boolean)

This function returns the previous setting; either 0 (false) or 1
(true).

## Remarks {#Remarks}

If Persistent is not used, the default setting is 0 (false).

If the script is *persistent*, it will stay running after
[startup](../Scripts.htm#auto) completes and all other
[threads](../misc/Threads.htm) have exited. It is usually unnecessary to
call this function because the script is [automatically
persistent](../Scripts.htm#persistent) in most of the common cases where
the user would want it to keep running, such as to respond to
[hotkeys](../Hotkeys.htm), execute [timers](SetTimer.htm) or display a
[GUI](Gui.htm).

Some cases where this function might be needed (if it is intended to
stay running when there are no running threads or hotkeys, timers, etc.)
include:

-   Scripts which use [OnMessage](OnMessage.htm) or
    [CallbackCreate](CallbackCreate.htm) and [DllCall](DllCall.htm) to
    respond to events, since those functions don\'t make the script
    persistent.
-   Scripts that are executed by selecting a custom tray menu item.
-   Scripts which [create](ComObject.htm) or
    [retrieve](ComObjActive.htm) COM objects and use
    [ComObjConnect](ComObjConnect.htm) to respond to the object\'s
    events.

If this function is added to an existing script, some or all occurrences
of [Exit](Exit.htm) might need to be changed to [ExitApp](ExitApp.htm).
This is because [Exit](Exit.htm) will not terminate a persistent script;
it terminates only the [current thread](../misc/Threads.htm).

## Related {#Related}

[Exit](Exit.htm), [ExitApp](ExitApp.htm)

## Examples {#Examples}

::: {#ExBasic .ex}
[](#ExBasic){.ex_number} Prevent the script from exiting automatically.

    ; This script will not exit automatically, even though it has nothing to do.
    ; However, you can use its tray icon to open the script in an editor, or to
    ; launch Window Spy or the Help file.
    Persistent
:::
