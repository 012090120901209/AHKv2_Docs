# HasBase

Returns a non-zero number if the specified value is derived from the
specified base object.

``` Syntax
HasBase := HasBase(Value, BaseObj)
```

## Parameters {#Parameters}

Value

:   Any value, of any type.

BaseObj

:   Type: [Object](../Concepts.htm#objects)

    The potential base object to test.

## Return Value {#Return_Value}

Type: [Integer (boolean)](../Concepts.htm#boolean)

This function returns 1 (true) if *BaseObj* is in *Value*\'s chain of
base objects, otherwise 0 (false).

## Remarks {#Remarks}

The following code is roughly equivalent to this function:

    MyHasBase(Value, BaseObj) {
        b := Value
        while b := ObjGetBase(b)
            if b = BaseObj
                return true
        return false
    }

For example, `HasBase(Obj, Array.Prototype)` is true if *Obj* is an
instance of [Array](Array.htm) or any derived class. This the same check
performed by `Obj is Array`; however, instances can be based on other
instances, whereas `is` requires a [Class](Class.htm).

HasBase accepts both objects and [primitive
values](../Objects.htm#primitive). For example, `HasBase(1, 0.base)`
returns true.

## Related {#Related}

[Objects](../Objects.htm), [Obj.Base](Object.htm#Base),
[ObjGetBase](Any.htm#GetBase), [HasMethod](HasMethod.htm),
[HasProp](HasProp.htm)

## Examples {#Examples}

::: {#ExBasic .ex}
[](#ExBasic){.ex_number} Illustrates the use of this function.

    thebase := {key: "value"}
    derived := {base: thebase}
    MsgBox HasBase(thebase, derived) ; 0
    MsgBox HasBase(derived, thebase) ; 1
:::
