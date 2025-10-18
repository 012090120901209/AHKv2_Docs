# IsSet / IsSetRef

Returns a non-zero number if the specified variable has been assigned a
value.

``` Syntax
Boolean := IsSet(Var)
Boolean := IsSetRef(&Ref)
```

## Parameters {#Parameters}

Var

:   Type: [Variable](../Concepts.htm#variables)

    A direct variable reference. For example: `IsSet(MyVar)`.

&Ref

:   Type: [VarRef](../Concepts.htm#variable-references)

    An indirect reference to the variable. This would usually not be
    passed directly, as in `IsSetRef(&MyVar)`, but indirectly, such as
    to check a parameter *containing* a VarRef prior to
    [dereferencing](../Variables.htm#deref) it.

## Return Value {#Return_Value}

Type: [Integer (boolean)](../Concepts.htm#boolean)

This function returns 1 (true) if *Var* or the variable represented by
*Ref* has been assigned a value, otherwise 0 (false).

## Remarks {#Remarks}

Use IsSet to check a variable directly, as in `IsSet(MyGlobalVar)`.

Use IsSetRef to check a [VarRef](../Concepts.htm#variable-references),
which would typically be contained by a variable, as in the example
below.

A variable which has not been assigned a value is also known as an
[uninitialized variable](../Concepts.htm#uninitialized-variables).
Attempting to read an uninitialized variable causes an exception to be
thrown. IsSet can be used to avoid this, such as for initializing a
global or static variable on first use.

**Note:** [Static initializers](../Functions.htm#InitStatic) such as
`static my_static_array := []` are evaluated only once, the first time
they are reached during execution, so typically do not require the use
of IsSet.

Although IsSet uses the same syntax as a function call, it may be
considered more of an operator than a function. The keyword *IsSet* is
reserved for the use shown here and cannot be redefined as a variable or
function. IsSet cannot be called indirectly because any attempt to pass
an uninitialized variable would cause an error to be thrown.

IsSetRef can also be used to check a specific variable, by using it with
the [reference operator](../Variables.htm#ref). When using it this way,
be aware of the need to [declare the variable](../Functions.htm#Global)
first if it is global. For example, the `&` in `IsSetRef(&MyVar)` would
cause *MyVar* to resolve to a local variable by default, if used within
an assume-local function which lacks the declaration `global MyVar`.

## Related {#Related}

[ByRef parameters](../Functions.htm#ByRef)

## Examples {#Examples}

::: {#ExBasic .ex}
[](#ExBasic){.ex_number} Shows different uses for IsSet and IsSetRef.

    Loop 2
        if !IsSet(MyVar)  ; Is this the first "use" of MyVar?
            MyVar := A_Index  ; Initialize on first "use".
    MsgBox Function1(&MyVar)
    MsgBox Function2(&MyVar)

    Function1(&Param)  ; ByRef parameter.
    {
        if IsSet(Param)  ; Pass Param itself, which is an alias for MyVar.
            return Param  ; ByRef parameters are automatically dereferenced.
        else
            return "unset"
    }

    Function2(Param)
    {
        if IsSetRef(Param)  ; Pass the VarRef contained by Param.
            return %Param%  ; Explicitly dereference Param.
        else
            return "unset"
    }
:::
