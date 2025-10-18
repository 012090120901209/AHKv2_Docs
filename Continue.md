# Continue

Skips the rest of a [loop statement](../Language.htm#loop-statement)\'s
current iteration and begins a new one.

``` Syntax
Continue LoopLabel
```

## Parameters {#Parameters}

LoopLabel

:   If omitted or 1, this statement applies to the innermost loop in
    which it is enclosed. Otherwise, specify which loop this statement
    should apply to; either by [label name](../misc/Labels.htm) or
    numeric nesting level. If a [label](../misc/Labels.htm) is
    specified, it must point directly at a [loop
    statement](../Language.htm#loop-statement).

    *LoopLabel* must be a constant value - variables and expressions are
    not supported, with the exception of a single literal number or
    quoted string enclosed in parentheses. For example:
    `continue("outer")`

## Remarks {#Remarks}

Continue behaves the same as reaching the loop\'s closing brace:

1.  It increases [A_Index](../Variables.htm#Index) by 1.
2.  It skips the rest of the loop\'s body.
3.  The loop\'s condition (if it has one) is checked to see if it is
    satisfied. If so, a new iteration begins; otherwise the loop ends.

The use of [Break](Break.htm) and Continue are encouraged over
[Goto](Goto.htm) since they usually make scripts more readable and
maintainable.

## Related {#Related}

[Break](Break.htm), [Loop](Loop.htm), [Until](Until.htm),
[While-loop](While.htm), [For-loop](For.htm), [Blocks](Block.htm),
[Labels](../misc/Labels.htm)

## Examples {#Examples}

::: {#ExBasic .ex}
[](#ExBasic){.ex_number} Displays 5 message boxes, one for each number
between 6 and 10. Note that in the first 5 iterations of the loop, the
Continue statement causes the loop to start over before it reaches the
MsgBox line.

    Loop 10
    {
        if (A_Index <= 5)
            continue
        MsgBox A_Index
    }
:::

::: {#ExContinueOuter .ex}
[](#ExContinueOuter){.ex_number} Continues the outer loop from within a
nested loop.

    outer:
    Loop 3
    {
        x := A_Index
        Loop 3
        {
            if (x*A_Index = 4)
                continue outer  ; Equivalent to continue 2 or goto continue_outer.
            MsgBox x "," A_Index
        }
        continue_outer: ; For goto.
    }
:::
