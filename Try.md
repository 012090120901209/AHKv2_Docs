# Try

Guards one or more [statements](../Concepts.htm#statement) against
runtime errors and values thrown by the [Throw](Throw.htm) statement.

``` Syntax
Try Statement
```

``` {.Syntax style="line-height: 100%"}
Try
{
    Statements
}
```

## Remarks {#Remarks}

The *Try* statement is usually followed by a [block](Block.htm) (one or
more [statements](../Concepts.htm#statement) enclosed in braces). If
only a single statement is to be executed, it can be placed on the same
line as *Try* or on the next line, and the braces can be omitted. To
specify code that executes only when *Try* catches an error, use one or
more [Catch](Catch.htm) statements.

If *Try* is used without *Catch* or *Finally*, it is equivalent to
having `catch Error` with an empty block.

A value can be thrown by the [Throw](Throw.htm) statement or by the
program when a runtime error occurs. When a value is thrown from within
a *Try* block or a function called by one, the following occurs:

-   If there is a [Catch](Catch.htm) statement which matches the class
    of the thrown value, execution is transferred into it.
-   If there is no matching *Catch* statement but there is a
    [Finally](Finally.htm) statement, it is executed, but once it
    finishes the value is automatically thrown again.
-   If there is no matching *Catch* statement or *Finally* statement,
    the value is automatically thrown again (unless there is no *Catch*
    or *Finally* at all, as noted above).

The last *Catch* can optionally be followed by [*Else*](Else.htm). If
the *Try* statement completes without an exception being thrown (and
without control being transferred elsewhere by *Return*, *Break* or
similar), the *Else* statement is executed. Exceptions thrown by the
*Else* statement are not handled by its associated *Try* statement, but
may be handled by an enclosing *Try* statement. *Finally* can also be
present, but must be placed after *Else*, and is always executed last.

The [One True Brace (OTB) style](Block.htm#otb) may optionally be used
with the *Try* statement. For example:

    try {
        ...
    } catch Error as err {
        ...
    } else {
        ...
    } finally {
        ...
    }

## Related {#Related}

[Throw](Throw.htm), [Catch](Catch.htm), [Else](Else.htm),
[Finally](Finally.htm), [Blocks](Block.htm), [OnError](OnError.htm)

## Examples {#Examples}

::: {#ex_basic .ex}
[](#ex_basic){.ex_number} Demonstrates the basic concept of *Try-Catch*
and *Throw*.

    try  ; Attempts to execute code.
    {
        HelloWorld
        MakeToast
    }
    catch as e  ; Handles the first error thrown by the block above.
    {
        MsgBox "An error was thrown!`nSpecifically: " e.Message
        Exit
    }

    HelloWorld()  ; Always succeeds.
    {
        MsgBox "Hello, world!"
    }

    MakeToast()  ; Always fails.
    {
        ; Jump immediately to the try block's error handler:
        throw Error(A_ThisFunc " is not implemented, sorry")
    }
:::

::: {#ex_el .ex}
[](#ex_el){.ex_number} Demonstrates basic error handling of built-in
functions.

    try
    {
        ; The following tries to back up certain types of files:
        FileCopy A_MyDocuments "\*.txt", "D:\Backup\Text documents"
        FileCopy A_MyDocuments "\*.doc", "D:\Backup\Text documents"
        FileCopy A_MyDocuments "\*.jpg", "D:\Backup\Photos"
    }
    catch
    {
        MsgBox "There was a problem while backing the files up!",, "IconX"
        ExitApp 1
    }
    else
    {
        MsgBox "Backup successful."
        ExitApp 0
    }
:::

::: {#ex_com .ex}
[](#ex_com){.ex_number} Demonstrates the use of *Try-Catch* dealing with
COM errors. For details about the COM object used below, see [Using the
ScriptControl (Microsoft
Docs)](https://learn.microsoft.com/previous-versions/visualstudio/visual-studio-6.0/aa227633(v=vs.60)).

    try
    {
        obj := ComObject("ScriptControl")
        obj.ExecuteStatement('MsgBox "This is embedded VBScript"')  ; This line produces an Error.
        obj.InvalidMethod()  ; This line would produce a MethodError.
    }
    catch MemberError  ; Covers MethodError and PropertyError.
    {
        MsgBox "We tried to invoke a member that doesn't exist."
    }
    catch as e
    {
        ; For more detail about the object that e contains, see Error Object.
        MsgBox("Exception thrown!`n`nwhat: " e.what "`nfile: " e.file 
            . "`nline: " e.line "`nmessage: " e.message "`nextra: " e.extra,, 16) 
    }
:::

::: {#ex_nesting .ex}
[](#ex_nesting){.ex_number} Demonstrates nesting *Try-Catch* statements.

    try Example1 ; Any single statement can be on the same line with Try.
    catch Number as e
        MsgBox "Example1() threw " e

    Example1()
    {
        try Example2
        catch Number as e
        {
            if (e = 1)
                throw ; Rethrow the caught value to our caller.
            else
                MsgBox "Example2() threw " e
        }
    }

    Example2()
    {
        throw Random(1, 2)
    }
:::
