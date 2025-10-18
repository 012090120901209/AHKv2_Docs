# CaretGetPos

Retrieves the current position of the caret (text insertion point).

``` Syntax
CaretFound := CaretGetPos(&OutputVarX, &OutputVarY)
```

## Parameters {#Parameters}

&OutputVarX, &OutputVarY

:   Type: [VarRef](../Concepts.htm#variable-references)

    If omitted, the corresponding value will not be stored. Otherwise,
    specify references to the output variables in which to store the X
    and Y coordinates. The retrieved coordinates are relative to the
    active window\'s client area unless overridden by using
    [CoordMode](CoordMode.htm) or
    [A_CoordModeCaret](../Variables.htm#CoordMode).

## Return Value {#Return_Value}

Type: [Integer (boolean)](../Concepts.htm#boolean)

If there is no active window or the caret position cannot be determined,
the function returns 0 (false) and the output variables are made blank.
The function returns 1 (true) if the system returned a caret position,
but this does not necessarily mean a caret is visible.

## Remarks {#Remarks}

Any of the output variables may be omitted if the corresponding
information is not needed.

Note that some windows (e.g. certain versions of MS Word) report the
same caret position regardless of its actual position.

## Related {#Related}

[CoordMode](CoordMode.htm),
[A_CoordModeCaret](../Variables.htm#CoordMode)

## Examples {#Examples}

::: {#ExWatchCaret .ex}
[](#ExWatchCaret){.ex_number} Allows the user to move the caret around
to see its current position displayed in an auto-update tooltip.

    SetTimer WatchCaret, 100
    WatchCaret() {
        if CaretGetPos(&x, &y)
            ToolTip "X" x " Y" y, x, y - 20
        else
            ToolTip "No caret"
    }
:::
