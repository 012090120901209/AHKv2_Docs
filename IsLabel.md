# IsLabel

Returns a non-zero number if the specified label exists in the current
scope.

``` Syntax
Boolean := IsLabel(LabelName)
```

## Parameters {#Parameters}

LabelName

:   Type: [String](../Concepts.htm#strings)

    The name of a [label](../misc/Labels.htm). The trailing colon should
    not be included.

## Return Value {#Return_Value}

Type: [Integer (boolean)](../Concepts.htm#boolean)

This function returns 1 (true) if the specified label exists within the
current scope, otherwise 0 (false).

## Remarks {#Remarks}

This function is useful to avoid runtime errors when specifying a
dynamic label for [Goto](Goto.htm).

When called from inside a function, only that function\'s labels are
searched. Global labels are not valid targets for a local goto.

## Related {#Related}

[Labels](../misc/Labels.htm)

## Examples {#Examples}

::: {#ExBasic .ex}
[](#ExBasic){.ex_number} Reports \"Target label exists\" because the
label does exist.

    if IsLabel("Label")
        MsgBox "Target label exists"
    else
        MsgBox "Target label doesn't exist"

    Label:
    return
:::
