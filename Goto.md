# Goto

Jumps to the specified label and continues execution.

``` Syntax
Goto Label
Goto("Label")
```

## Parameters {#Parameters}

Label

:   Type: [String](../Concepts.htm#strings)

    The name of the [label](../misc/Labels.htm) to which to jump.

## Remarks {#Remarks}

*Label* can be a variable or expression only if parentheses are used.
For example, `Goto MyLabel` and `Goto("MyLabel")` both jump to
`MyLabel:`.

Performance is slightly reduced when using a dynamic label (that is, a
variable or expression which returns a label name) because the target
label must be \"looked up\" each time rather than only once when the
script is first loaded. An error dialog will be displayed if the label
does not exist. To avoid this, call [IsLabel()](IsLabel.htm) beforehand.
For example:

    if IsLabel(VarContainingLabelName)
        Goto(VarContainingLabelName)

The use of Goto is discouraged because it generally makes scripts less
readable and harder to maintain. Consider using [Else](Else.htm),
[Blocks](Block.htm), [Break](Break.htm), and [Continue](Continue.htm) as
substitutes for Goto.

## Related {#Related}

[Return](Return.htm), [IsLabel](IsLabel.htm), [Else](Else.htm),
[Blocks](Block.htm), [Break](Break.htm), [Continue](Continue.htm)

## Examples {#Examples}

::: {#ExBasic .ex}
[](#ExBasic){.ex_number} Jumps to the label named \"MyLabel\" and
continues execution.

    Goto MyLabel
    ; ...
    MyLabel:
    Sleep 100
    ; ...
:::
