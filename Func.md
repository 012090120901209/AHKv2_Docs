# Func Object

``` NoIndent
class Func extends Object
```

Represents a user-defined or built-in function and provides an interface
to call it, bind parameters to it, and retrieve information about it or
its parameters.

For information about other objects which can be called like functions,
see [Function Objects](../misc/Functor.htm).

The `Closure` class extends `Func` but does not define any new
properties.

For each built-in function or function definition within the script,
there is a corresponding read-only variable containing a Func object.
This variable is directly used to call the function, but its value can
also be read to retrieve the function itself, as a value. For example:

    InspectFn StrLen
    InspectFn InspectFn

    InspectFn(fn)
    {
        ; Display information about the passed function.
        MsgBox fn.Name "() is " (fn.IsBuiltIn ? "built-in." : "user-defined.")
    }

\"FuncObj\" is used below as a placeholder for any Func object, as
\"Func\" is the class itself.

In addition to the methods and property inherited from
[Object](Object.htm), Func objects have the following predefined methods
and properties.

## Table of Contents {#toc}

-   [Methods](#Methods):
    -   [Call](#Call): Calls the function.
    -   [Bind](#Bind): Binds parameters to the function.
    -   [IsByRef](#IsByRef): Determines whether a parameter is ByRef.
    -   [IsOptional](#IsOptional): Determines whether a parameter is
        optional.
-   [Properties](#Properties):
    -   [Name](#Name): Returns the function\'s name.
    -   [IsBuiltIn](#IsBuiltIn): Returns 1 (true) if the function is
        built-in, otherwise 0 (false).
    -   [IsVariadic](#IsVariadic): Returns 1 (true) if the function is
        variadic, otherwise 0 (false).
    -   [MinParams](#MinParams): Returns the number of required
        parameters.
    -   [MaxParams](#MaxParams): Returns the number of formally-declared
        parameters for a user-defined function or maximum parameters for
        a built-in function.

## Methods {#Methods}

::: {#Call .methodShort}
### Call

Calls the function.

``` Syntax
FuncObj(Param1, Param2, ...)
FuncObj.Call(Param1, Param2, ...)
```

#### Parameters {#Call_Parameters}

Param1, Param2, \...

:   Parameters and return value are defined by the function.

#### Remarks {#Call_Remarks}

The \"Call\" method is implied when calling a value, so need not be
explicitly specified.
:::

::: {#Bind .methodShort}
### Bind

Binds parameters to the function.

``` Syntax
BoundFunc := FuncObj.Bind(Param1, Param2, ...)
```

#### Parameters {#Bind_Parameters}

Param1, Param2, \...

:   Any number of parameters.

#### Return Value {#Bind_Return_Value}

Type: [Object](../Concepts.htm#objects)

This method returns a [BoundFunc object](../misc/Functor.htm#BoundFunc).
:::

::: {#IsByRef .methodShort}
### IsByRef

Determines whether a parameter is ByRef.

``` Syntax
Boolean := FuncObj.IsByRef(ParamIndex)
```

#### Parameters {#IsByRef_Parameters}

ParamIndex

:   Type: [Integer](../Concepts.htm#numbers)

    If omitted, *Boolean* indicates whether the function has any ByRef
    parameters. Otherwise, specify the one-based index of a parameter.

#### Return Value {#IsByRef_Return_Value}

Type: [Integer (boolean)](../Concepts.htm#boolean)

This method returns 1 (true) if the parameter is ByRef, otherwise 0
(false). If *ParamIndex* is invalid, an exception is thrown.
:::

::: {#IsOptional .methodShort}
### IsOptional

Determines whether a parameter is optional.

``` Syntax
Boolean := FuncObj.IsOptional(ParamIndex)
```

#### Parameters {#IsOptional_Parameters}

ParamIndex

:   Type: [Integer](../Concepts.htm#numbers)

    If omitted, *Boolean* indicates whether the function has any
    optional parameters. Otherwise, specify the one-based index of a
    parameter.

#### Return Value {#IsOptional_Return_Value}

Type: [Integer (boolean)](../Concepts.htm#boolean)

This method returns 1 (true) if the parameter is optional, otherwise 0
(false). If *ParamIndex* is invalid, an exception is thrown.

#### Remarks {#IsOptional_Remarks}

Parameters do not need to be formally declared if the function is
variadic. Built-in functions are supported.
:::

## Properties {#Properties}

::: {#Name .methodShort}
### Name

Returns the function\'s name.

``` Syntax
FunctionName := FuncObj.Name
```
:::

::: {#IsBuiltIn .methodShort}
### IsBuiltIn

Returns 1 (true) if the function is
[built-in](../Functions.htm#BuiltIn), otherwise 0 (false).

``` Syntax
Boolean := FuncObj.IsBuiltIn
```
:::

::: {#IsVariadic .methodShort}
### IsVariadic

Returns 1 (true) if the function is
[variadic](../Functions.htm#Variadic), otherwise 0 (false).

``` Syntax
Boolean := FuncObj.IsVariadic
```
:::

::: {#MinParams .methodShort}
### MinParams

Returns the number of required parameters.

``` Syntax
ParamCount := FuncObj.MinParams
```
:::

::: {#MaxParams .methodShort}
### MaxParams

Returns the number of formally-declared parameters for a user-defined
function or maximum parameters for a built-in function.

``` Syntax
ParamCount := FuncObj.MaxParams
```

If the function is [variadic](../Functions.htm#Variadic), *ParamCount*
indicates the maximum number of parameters which can be accepted by the
function without overflowing into the \"variadic\*\" parameter.
:::
