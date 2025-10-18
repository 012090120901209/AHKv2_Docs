# HasProp

Returns a non-zero number if the specified value has a property by the
specified name.

``` Syntax
HasProp := HasProp(Value, Name)
```

## Parameters {#Parameters}

Value

:   Type: [Any](../Concepts.htm#values)

    Any value, of any type except ComObject.

Name

:   Type: [String](../Concepts.htm#strings)

    The property name to check for.

## Return Value {#Return_Value}

Type: [Integer (boolean)](../Concepts.htm#boolean)

This function returns 1 (true) if the value has a property by this name,
otherwise 0 (false).

## Remarks {#Remarks}

This function does not test for the presence of a \_\_Get or \_\_Set
[meta-function](../Objects.htm#Meta_Functions). If present, there is no
way to detect the exact set of properties that it may implement.

This function supports [primitive values](../Objects.htm#primitive).

## Related {#Related}

[Objects](../Objects.htm), [HasBase](HasBase.htm),
[HasMethod](HasMethod.htm)

## Examples {#Examples}

::: {#ExBasic .ex}
[](#ExBasic){.ex_number} Illustrates the use of this function.

    MsgBox HasProp({}, "x") ; 0
    MsgBox HasProp({x:1}, "x") ; 1
    MsgBox HasProp(0, "Base") ; 1
:::
