# Loop (normal)

Performs one or more [statements](../Concepts.htm#statement) repeatedly:
either the specified number of times or until [Break](Break.htm) is
encountered.

``` Syntax
Loop Count
```

## Parameters {#Parameters}

Count

:   Type: [Integer](../Concepts.htm#numbers)

    If omitted, the loop continues indefinitely until a
    [Break](Break.htm) or [Return](Return.htm) is encountered.
    Otherwise, specify how many times (iterations) to perform the loop.
    However, an explicit blank value or number less than 1 causes the
    loop to be skipped entirely.

    *Count* is evaluated only once, right before the loop begins. For
    instance, if *Count* is an expression with side-effects such as
    function calls or assignments, the side-effects occur only once.

    If *Count* is enclosed in parentheses, a space or tab is not
    required. For example: `Loop(2)`

## Remarks {#Remarks}

The loop statement is usually followed by a [block](Block.htm), which is
a collection of statements that form the *body* of the loop. However, a
loop with only a single statement does not require a block (an \"if\"
and its \"else\" count as a single statement for this purpose).

A common use of this statement is an infinite loop that uses the
[Break](Break.htm) statement somewhere in the loop\'s *body* to
determine when to stop the loop.

The use of [Break](Break.htm) and [Continue](Continue.htm) inside a loop
are encouraged as alternatives to [Goto](Goto.htm), since they generally
make a script more understandable and maintainable. One can also create
a \"While\" or \"Do\...While/Until\" loop by making the first or last
statement of the loop\'s *body* an IF statement that conditionally
issues the [Break](Break.htm) statement, but the use of
[While](While.htm) or [Loop\...Until](Until.htm) is usually preferred.

The built-in variable **A_Index** contains the number of the current
loop iteration. It contains 1 the first time the loop\'s *body* is
executed. For the second time, it contains 2; and so on. If an inner
loop is enclosed by an outer loop, the inner loop takes precedence.
A_Index works inside all types of loops, including [file
loops](LoopFiles.htm) and [registry loops](LoopReg.htm); but A_Index
contains 0 outside of a loop.

A_Index can be assigned any integer value by the script. If *Count* is
specified, changing A_Index affects the number of iterations that will
be performed. For example, `A_Index := 3` would make the loop statement
act as though it is on the third iteration (A_Index will be 4 on the
next iteration), while `A_Index--` would prevent the current iteration
from being counted toward the total.

The loop may optionally be followed by an [Else](Else.htm) statement,
which is executed if *Count* is zero.

The [One True Brace (OTB) style](Block.htm#otb) may optionally be used.
For example:

    Loop {
        ...
    }
    Loop RepeatCount {
        ...
    }

Specialized loops: Loops can be used to automatically retrieve files,
folders, or registry items (one at a time). See [file
loop](LoopFiles.htm) and [registry loop](LoopReg.htm) for details. In
addition, [file-reading loops](LoopRead.htm) can operate on the entire
contents of a file, one line at a time. Finally, [parsing
loops](LoopParse.htm) can operate on the individual fields contained
inside a delimited string.

## Related {#Related}

[Until](Until.htm), [While-loop](While.htm), [For-loop](For.htm),
[Files-and-folders loop](LoopFiles.htm), [Registry loop](LoopReg.htm),
[File-reading loop](LoopRead.htm), [Parsing loop](LoopParse.htm),
[Break](Break.htm), [Continue](Continue.htm), [Blocks](Block.htm),
[Else](Else.htm)

## Examples {#Examples}

::: {#ExBasic .ex}
[](#ExBasic){.ex_number} Creates a loop with 3 iterations.

    Loop 3
    {
        MsgBox "Iteration number is " A_Index  ; A_Index will be 1, 2, then 3
        Sleep 100
    }
:::

::: {#ExBreakContinue .ex}
[](#ExBreakContinue){.ex_number} Creates an infinite loop, but it will
be terminated after the 25th iteration.

    Loop
    {
        if (A_Index > 25)
            break  ; Terminate the loop
        if (A_Index < 20)
            continue ; Skip the below and start a new iteration
        MsgBox "A_Index = " A_Index ; This will display only the numbers 20 through 25
    }
:::
