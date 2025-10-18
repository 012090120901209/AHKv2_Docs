# Enumerator Object

An enumerator is a type of [function object](../misc/Functor.htm) which
is called repeatedly to enumerate a sequence of values.

Enumerators exist primarily to support [For-loops](For.htm), and are not
usually called directly. The for-loop documentation details the process
by which an enumerator is called. The script may implement an enumerator
to control which values are assigned to the for-loop\'s variables on
each iteration of the loop.

Built-in enumerators are instances of the `Enumerator` class (which is
derived from [Func](Func.htm)), but any function object can potentially
be used with a for-loop.

## Table of Contents {#toc}

-   [Methods](#Methods):
    -   [Call](#Call): Retrieves the next item or items in an
        enumeration.
-   [Related](#Related)

## Methods {#Methods}

::: {#Call .methodShort}
### Call

Retrieves the next item or items in an enumeration.

``` Syntax
Boolean := Enum.Call(&OutputVar1 , &OutputVar2)
```

``` Syntax
Boolean := EnumFunction(&OutputVar1 , &OutputVar2)
```

#### Parameters {#Next_Parameters}

&OutputVar1, &OutputVar2

:   Type: [VarRef](../Concepts.htm#variable-references)

    One or more references to output variables for the enumerator to
    assign values.

#### Return Value {#Next_Return_Value}

Type: [Integer (boolean)](../Concepts.htm#boolean)

This method returns 1 (true) if successful or 0 (false) if there were no
items remaining.

#### Remarks {#Next_Remarks}

A simple function definition can be used to create an enumerator; in
that case, the Call method is implied.

When defining your own enumerator, the number of parameters should match
the number of variables expected to be passed to the for-loop (before
the \"in\" keyword). This is usually either 1 or 2, but a for-loop can
accept up to 19 variables. To allow the method to accept a varying
number of variables, declare [optional
parameters](../Functions.htm#optional).

An exception is thrown when the for-loop attempts to call the method if
there are more variables than parameters (too many parameters passed,
too few defined) or fewer variables than mandatory parameters.
:::

## Related {#Related}

[For-loop](For.htm), [OwnProps](Object.htm#OwnProps), [\_\_Enum
(Array)](Array.htm#__Enum), [\_\_Enum (Map)](Map.htm#__Enum)
