# Until

Applies a condition to the continuation of a Loop or For-loop.

``` Syntax
Loop {
    ...
} Until Expression
```

## Parameters {#Parameters}

Expression

:   Any valid [expression](../Variables.htm#Expressions).

## Remarks {#Remarks}

The space or tab after `Until` is optional if the expression is enclosed
in parentheses, as in `until(expression)`.

The expression is evaluated once after each iteration, and is evaluated
even if [Continue](Continue.htm) was used. If the expression evaluates
to false (which is an empty string or the number 0), the loop continues;
otherwise, the loop is broken and execution continues at the line
following *Until*.

Loop Until is shorthand for the following:

    Loop {
        ...
        if (Expression)
            break
    }

However, Loop Until is often easier to understand and unlike the above,
can be used with a single-line action. For example:

    Loop
        x *= 2
    Until x > y

*Until* can be used with any Loop or For. For example:

    Loop Read, A_ScriptFullPath
        lines .= A_LoopReadLine . "`n"
    Until A_Index=5  ; Read the first five lines.
    MsgBox lines

If [A_Index](../Variables.htm#Index) is used in *Expression*, it
contains the index of the iteration which has just finished.

## Related {#Related}

[Loop](Loop.htm), [While-loop](While.htm), [For-loop](For.htm),
[Break](Break.htm), [Continue](Continue.htm), [Blocks](Block.htm),
[Files-and-folders loop](LoopFiles.htm), [Registry loop](LoopReg.htm),
[File-reading loop](LoopRead.htm), [Parsing loop](LoopParse.htm),
[If](If.htm)
