# OnError

Registers a [function](../Functions.htm) to be called automatically
whenever an unhandled error occurs.

``` Syntax
OnError Callback , AddRemove
```

## Parameters {#Parameters}

Callback

:   Type: [Function Object](../misc/Functor.htm)

    The function to call.

    The callback accepts two parameters and can be
    [defined](../Functions.htm#intro) as follows:

    ``` NoIndent
    MyCallback(Thrown, Mode) { ...
    ```

    Although the names you give the parameters do not matter, the
    following values are sequentially assigned to them:

    1.  The thrown value, usually an [Error object](Error.htm).
    2.  The error mode: Return, Exit, or ExitApp. For details, see the
        [table below](#Error_Modes).

    You can omit one or more parameters from the end of the callback\'s
    parameter list if the corresponding information is not needed, but
    in this case an asterisk must be specified as the final parameter,
    e.g. `MyCallback(Param1, *)`.

    The callback can return one of the following values (other values
    are reserved for future use and should be avoided):

    -   `0`, `""` or no Return: Allow error handling to proceed as
        normal.
    -   `1`: Suppress the default error dialog and any remaining error
        callbacks.
    -   `-1`: As above, but if *Mode* (the second parameter) contains
        the word Return, execution of the current thread is permitted to
        continue.

AddRemove

:   Type: [Integer](../Concepts.htm#numbers)

    If omitted, it defaults to 1. Otherwise, specify one of the
    following numbers:

    -   1 = Call the callback after any previously registered callbacks.
    -   -1 = Call the callback before any previously registered
        callbacks.
    -   0 = Do not call the callback.

## Error Modes {#Error_Modes}

  Mode      Description
  --------- -------------------------------------------------------------------------------------------------------------------------------
  Return    The thrown value is a continuable runtime error. The thread continues if the callback returns -1; otherwise the thread exits.
  Exit      The thrown value is a non-continuable runtime error or a value [thrown](Throw.htm) by the script. The thread will exit.
  ExitApp   The thrown value is a critical runtime error, such as corruption detected by DllCall. The program will exit.

## Remarks {#Remarks}

*Callback* is called only for errors or exceptions which would normally
cause an error message to be displayed. It cannot be called for a
load-time error, since OnError cannot be called until after the script
has loaded.

*Callback* is called on the current [thread](../misc/Threads.htm),
before it exits (that is, before the call stack unwinds).

## Related {#Related}

[Try](Try.htm), [Catch](Catch.htm), [Throw](Throw.htm),
[OnExit](OnExit.htm)

## Examples {#Examples}

::: {#ExBasic .ex}
[](#ExBasic){.ex_number} Logs errors caused by the script into a text
file instead of displaying them to the user.

    OnError LogError
    i := Integer("cause_error")

    LogError(exception, mode) {
        FileAppend "Error on line " exception.Line ": " exception.Message "`n"
            , "errorlog.txt"
        return true
    }
:::

::: {#ExAccumulator .ex}
[](#ExAccumulator){.ex_number} Use OnError to implement alternative
error handling methods. Caveat: OnError is ineffective while
[Try](Try.htm) is active.

    AccumulateErrors()
    {
        local ea := ErrorAccumulator()
        ea.Start()
        return ea
    }

    class ErrorAccumulator
    {
        Errors := []                        ; Array for accumulated errors.
        _cb := AccumulateError.Bind(this.Errors)
        Start() => OnError(this._cb, -1)    ; Register our cb before others.
        Stop() => OnError(this._cb, 0)      ; Unregister our cb.
        Last => this.Errors[-1]             ; Most recent error.
        Count => this.Errors.Length         ; Number of accumulated errors.
        __item[i] => this.Errors[i]         ; Shortcut for indexing.
        __delete() => this.Stop()           ; For tying to function scope.
    }

    ; This is the OnError callback. 'errors' is given a value via Bind().
    AccumulateError(errors, e, mode)
    {
        if mode != "Return" ; Not continuable.
            return
        if e.What = "" ; Expression defect or similar, not a built-in function.
            return
        try {
            ; Try to print the error to stdout.
            FileAppend Format("{1} ({2}) : ({3}) {4}`n", e.File, e.Line, e.What, e.Message), "*"
            if HasProp(e, "extra")
                FileAppend "     Specifically: " e.Extra "`n", "*"
        }
        errors.Push(e)
        return -1 ; Continue.
    }

    RearrangeWindows()
    {
        ; Start accumulating errors in 'err'.
        local err := AccumulateErrors()

        ; Do some things that might fail...
        MonitorGetWorkArea , &left, &top, &right, &bottom
        width := (right-left)//2, height := bottom-top
        WinMove left, top, width, height, A_ScriptFullPath
        WinMove left+width, top, width, height, "AutoHotkey v2 Help"

        ; Check if any errors occurred.
        if err.Count
            MsgBox err.Count " error(s); last error at line #" err.Last.Line
        else
            MsgBox "No errors"

        ; Stop is called automatically when the variable goes out of scope,
        ; since only we have a reference to the object.  This causes OnError
        ; to be called to unregister the callback.
        ;err.Stop()
    }

    ; Call the test function which suppresses and accumulates errors.
    RearrangeWindows()
    ; Call another function to show normal error behaviour is restored.
    WinMove 0, 0, 0, 0, "non-existent window"
:::
