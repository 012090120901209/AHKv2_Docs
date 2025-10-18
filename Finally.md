# Finally

Ensures that one or more [statements](../Concepts.htm#statement) are
always executed after a [Try](Try.htm) statement finishes.

``` Syntax
Finally Statement
```

``` {.Syntax style="line-height: 100%"}
Finally
{
    Statements
}
```

## Remarks {#Remarks}

Every use of *Finally* must belong to (be associated with) a
[Try](Try.htm) statement above it (after any optional [Catch](Catch.htm)
and/or [Else](Else.htm)). A *Finally* always belongs to the nearest
unclaimed *Try* statement above it unless a [block](Block.htm) is used
to change that behavior.

*Try* statements behave differently depending on whether *Catch* or
*Finally* is present. For more information, see [Try](Try.htm).

*Goto*, *Break*, *Continue* and *Return* cannot be used to exit a
*Finally* block, as that would require suppressing any control flow
statements within the *Try* block. For example, if *Try* uses
`return 42`, the value 42 is returned after the *Finally* block
executes. Attempts to jump out of a *Finally* block using one of these
statements are detected as errors at load time where possible, or at run
time otherwise.

*Finally* statements are not executed if the script is directly
terminated by any means, including the tray menu or
[ExitApp](ExitApp.htm).

The [One True Brace (OTB) style](Block.htm#otb) may optionally be used
with the *Finally* statement. For example:

    try {
        ...
    } finally {
        ...
    }

    try {
        ...
    } catch {
        ...
    } else {
        ...
    } finally {
        ...
    }

## Related {#Related}

[Try](Try.htm), [Catch](Catch.htm), [Else](Else.htm),
[Throw](Throw.htm), [Blocks](Block.htm)

## Examples {#Examples}

::: {#ExBasic .ex}
[](#ExBasic){.ex_number} Demonstrates the behavior of *Finally* in
detail.

    try
    {
        ToolTip "Working..."
        Example1()
    }
    catch as e
    {
        ; For more detail about the object that e contains, see Error.
        MsgBox(Type(e) " thrown!`n`nwhat: " e.what "`nfile: " e.file
            . "`nline: " e.line "`nmessage: " e.message "`nextra: " e.extra,, 16)
    }
    finally
    {
        ToolTip ; hide the tooltip
    }

    MsgBox "Done!"

    ; This function has a Finally block that acts as cleanup code
    Example1()
    {
        try
            Example2()
        finally
            MsgBox "This is always executed regardless of exceptions"
    }

    ; This function fails when the minutes are odd
    Example2()
    {
        if Mod(A_Min, 2)
            throw Error("That's odd...")
        MsgBox "Example2 did not fail"
    }
:::
