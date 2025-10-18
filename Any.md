# Any

`Any` is the class at the root of AutoHotkey\'s type hierarchy. All
other types are a sub-type of Any.

`Any.Prototype` defines methods and properties that are applicable to
all values and objects (currently excluding [ComValue](ComValue.htm) and
derived types) unless overridden. The prototype object itself is
natively an [Object](Object.htm), but has no `base` and therefore does
not identify as an instance of Object.

## Table of Contents {#toc}

-   [Methods](#Methods):
    -   [GetMethod](#GetMethod): Retrieves the implementation function
        of a method.
    -   [HasBase](#HasBase): Returns true if the specified base object
        is in the value\'s chain of base objects.
    -   [HasMethod](#HasMethod): Returns true if the value has a method
        by this name.
    -   [HasProp](#HasProp): Returns true if the value has a property by
        this name.
-   [Properties](#Properties):
    -   [Base](#Base): Retrieves the value\'s base object.
-   [Functions](#Functions):
    -   [ObjGetBase](#GetBase): Returns the value\'s base object.

## Methods {#Methods}

::: {#GetMethod .methodShort}
### GetMethod

Retrieves the implementation function of a method.

``` Syntax
Value.GetMethod(Name, ParamCount)
```

This method is exactly equivalent to
`GetMethod(Value, Name, ParamCount)`, unless overridden.
:::

::: {#HasBase .methodShort}
### HasBase

Returns true if the specified [base object](../Objects.htm#delegation)
is in the value\'s chain of base objects, otherwise false.

``` Syntax
Value.HasBase(BaseObj)
```

This method is exactly equivalent to `HasBase(Value, BaseObj)`, unless
overridden.
:::

::: {#HasMethod .methodShort}
### HasMethod

Returns true if the value has a method by this name, otherwise false.

``` Syntax
Value.HasMethod(Name, ParamCount)
```

This method is exactly equivalent to
`HasMethod(Value, Name, ParamCount)`, unless overridden.
:::

::: {#HasProp .methodShort}
### HasProp

Returns true if the value has a property by this name, otherwise false.

``` Syntax
Value.HasProp(Name)
```

This method is exactly equivalent to `HasProp(Value, Name)`, unless
overridden.
:::

## Properties {#Properties}

::: {#Base .methodShort}
### Base

Retrieves the value\'s [base object](../Objects.htm#delegation).

``` Syntax
BaseObj := Value.Base
```

For [primitive values](../Objects.htm#primitive), the return value is
the pre-defined prototype object corresponding to `Type(Value)`.

See also: [ObjGetBase](#GetBase), [ObjSetBase](Object.htm#SetBase),
[Obj.Base](Object.htm#Base)
:::

## Functions {#Functions}

### ObjGetBase {#GetBase}

Returns the value\'s [base object](../Objects.htm#delegation).

``` Syntax
BaseObj := ObjGetBase(Value)
```

No [meta-functions](../Objects.htm#Meta_Functions) or [property
functions](../Objects.htm#Custom_Classes_property) are called.
Overriding the [Base](#Base) property does not affect the behaviour of
this function.

If there is no base, the return value is an empty string. Only the Any
prototype itself has no base.

See also: [Base](#Base), [ObjSetBase](Object.htm#SetBase),
[Obj.Base](Object.htm#Base)
