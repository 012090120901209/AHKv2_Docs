# Array Object

``` NoIndent
class Array extends Object
```

An **Array** object contains a list or sequence of values.

Values are addressed by their position within the array (known as an
*array index*), where position 1 is the first element.

Arrays are often created by enclosing a list of values in brackets. For
example:

    veg := ["Asparagus", "Broccoli", "Cucumber"]
    Loop veg.Length
        MsgBox veg[A_Index]

A negative index can be used to address elements in reverse, so -1 is
the last element, -2 is the second last element, and so on.

Attempting to use an array index which is out of bounds (such as zero,
or if its absolute value is greater than the [Length](#Length) of the
array) is considered an error and will cause an
[IndexError](Error.htm#IndexError) to be thrown. The best way to add new
elements to the array is to call [InsertAt](#InsertAt) or [Push](#Push).
For example:

    users := Array()
    users.Push(A_UserName)
    MsgBox users[1]

An array can also be extended by assigning a larger value to
[Length](#Length). This changes which indices are valid, but [Has](#Has)
will show that the new elements have no value. Elements without a value
are typically used for [variadic calls](../Functions.htm#VariadicCall)
or by [variadic functions](../Functions.htm#Variadic), but can be used
for any purpose.

\"ArrayObj\" is used below as a placeholder for any Array object, as
\"Array\" is the class itself.

In addition to the methods and property inherited from
[Object](Object.htm), Array objects have the following predefined
methods and properties.

## Table of Contents {#toc}

-   [Static Methods](#StaticMethods):
    -   [Call](#Call): Creates a new Array containing the specified
        values.
-   [Methods](#Methods):
    -   [Clone](#Clone): Returns a shallow copy of an array.
    -   [Delete](#Delete): Removes the value of an array element,
        leaving the index without a value.
    -   [Get](#Get): Returns the value at a given index, or a default
        value.
    -   [Has](#Has): Returns a non-zero number if the index is valid and
        there is a value at that position.
    -   [InsertAt](#InsertAt): Inserts one or more values at a given
        position.
    -   [Pop](#Pop): Removes and returns the last array element.
    -   [Push](#Push): Appends values to the end of an array.
    -   [RemoveAt](#RemoveAt): Removes items from an array.
    -   [\_\_New](#__New): Appends items. Equivalent to Push.
    -   [\_\_Enum](#__Enum): Enumerates array elements.
-   [Properties](#Properties):
    -   [Length](#Length): Retrieves or sets the length of an array.
    -   [Capacity](#Capacity): Retrieves or sets the current capacity of
        an array.
    -   [Default](#Default): Defines the default value returned when an
        element with no value is requested.
    -   [\_\_Item](#__Item): Retrieves or sets the value of an array
        element.

## Static Methods {#StaticMethods}

::: {#Call .methodShort}
### Call

Creates a new Array containing the specified values.

``` Syntax
ArrayObj := Array(Value, Value2, ..., ValueN)
ArrayObj := Array.Call(Value, Value2, ..., ValueN)
```

Parameters are defined by [\_\_New](#__New).
:::

## Methods {#Methods}

::: {#Clone .methodShort}
### Clone

Returns a shallow copy of an array.

``` Syntax
Clone := ArrayObj.Clone()
```

All array elements are copied to the new array. Object *references* are
copied (like with a normal assignment), not the objects themselves.

Own properties, own methods and base are copied as per
[Obj.Clone](Object.htm#Clone).
:::

::: {#Delete .methodShort}
### Delete

Removes the value of an array element, leaving the index without a
value.

``` Syntax
RemovedValue := ArrayObj.Delete(Index)
```

#### Parameters {#Delete_Parameters}

Index

:   Type: [Integer](../Concepts.htm#numbers)

    A valid array index.

#### Return Value {#Delete_Return_Value}

Type: [Any](../Concepts.htm#values)

This method returns the removed value (blank if none).

#### Remarks {#Delete_Remarks}

This method does not affect the [Length](#Length) of the array.

A [ValueError](Error.htm#ValueError) is thrown if *Index* is out of
range.
:::

::: {#Get .methodShort}
### Get

Returns the value at a given index, or a default value.

``` Syntax
Value := ArrayObj.Get(Index , Default)
```

This method does the following:

-   Throw an [IndexError](Error.htm#IndexError) if *Index* is zero or
    out of range.
-   Return the value at *Index*, if there is one (see [Has](#Has)).
-   Return the value of the *Default* parameter, if specified.
-   Return the value of `ArrayObj.Default`, if defined.
-   Throw an [UnsetItemError](Error.htm#UnsetError).

When *Default* is omitted, this is equivalent to `ArrayObj[Index]`,
except that [\_\_Item](#__Item) is not called.
:::

::: {#Has .methodShort}
### Has

Returns a non-zero number if the index is valid and there is a value at
that position.

``` Syntax
HasIndex := ArrayObj.Has(Index)
```
:::

::: {#InsertAt .methodShort}
### InsertAt

Inserts one or more values at a given position.

``` Syntax
ArrayObj.InsertAt(Index, Value1 , Value2, ... ValueN)
```

#### Parameters {#InsertAt_Parameters}

Index

:   Type: [Integer](../Concepts.htm#numbers)

    The position to insert *Value1* at. Subsequent values are inserted
    at Index+1, Index+2, etc. Specifying an index of 0 is the same as
    specifying [Length](#Length) + 1.

Value1 \...

:   Type: [Any](../Concepts.htm#values)

    One or more values to insert. To insert an array of values, pass
    [`theArray*`](../Functions.htm#VariadicCall) as the last parameter.

#### Remarks {#InsertAt_Remarks}

InsertAt is the counterpart of [RemoveAt](#RemoveAt).

Any items previously at or to the right of *Index* are shifted to the
right. Missing parameters are also inserted, but without a value. For
example:

    x := []
    x.InsertAt(1, "A", "B") ; =>  ["A", "B"]
    x.InsertAt(2, "C")      ; =>  ["A", "C", "B"]

    ; Missing elements are preserved:
    x := ["A", , "C"]
    x.InsertAt(2, "B")      ; =>  ["A", "B",    , "C"]

    x := ["C"]
    x.InsertAt(1, , "B")    ; =>  [   , "B", "C"]

A [ValueError](Error.htm#ValueError) is thrown if *Index* is less than
`-ArrayObj.Length` or greater than `ArrayObj.Length + 1`. For example,
with an array of 3 items, *Index* must be between -3 and 4, inclusive.
:::

::: {#Pop .methodShort}
### Pop

Removes and returns the last array element.

``` Syntax
RemovedValue := ArrayObj.Pop()
```

All of the following are equivalent:

    RemovedValue := ArrayObj.Pop()
    RemovedValue := ArrayObj.RemoveAt(ArrayObj.Length)
    RemovedValue := ArrayObj.RemoveAt(-1)

If the array is empty ([Length](#Length) is 0), an [Error](Error.htm) is
thrown.
:::

::: {#Push .methodShort}
### Push

Appends values to the end of an array.

``` Syntax
ArrayObj.Push(Value, Value2, ..., ValueN)
```

#### Parameters {#Push_Parameters}

Value \...

:   Type: [Any](../Concepts.htm#values)

    One or more values to insert. To insert an array of values, pass
    [`theArray*`](../Functions.htm#VariadicCall) as the last parameter.
:::

::: {#RemoveAt .methodShort}
### RemoveAt

Removes items from an array.

``` Syntax
RemovedValue := ArrayObj.RemoveAt(Index)
ArrayObj.RemoveAt(Index, Length)
```

#### Parameters {#RemoveAt_Parameters}

Index

:   Type: [Integer](../Concepts.htm#numbers)

    The index of the value or values to remove.

Length

:   Type: [Integer](../Concepts.htm#numbers)

    If omitted, one item is removed. Otherwise, specify the length of
    the range of values to remove.

#### Return Value {#RemoveAt_Return_Value}

Type: [Any](../Concepts.htm#values)

If *Length* is omitted, the removed value is returned (blank if none).
Otherwise there is no return value.

#### Remarks {#RemoveAt_Remarks}

RemoveAt is the counterpart of [InsertAt](#InsertAt).

A [ValueError](Error.htm#ValueError) is thrown if the range indicated by
*Index* and *Length* is not entirely within the array\'s current bounds.

The remaining items to the right of *Pos* are shifted to the left by
*Length* (or 1 if omitted). For example:

    x := ["A", "B"]
    MsgBox x.RemoveAt(1)  ; A
    MsgBox x[1]           ; B

    x := ["A", , "C"]
    MsgBox x.RemoveAt(1, 2)  ; 1
    MsgBox x[1]              ; C
:::

::: {#__New .methodShort}
### \_\_New

Appends items. Equivalent to [Push](#Push).

``` Syntax
ArrayObj.__New(Value, Value2, ..., ValueN)
```

This method exists to support [Call](#Call), and is not intended to be
called directly. See [Construction and
Destruction](../Objects.htm#Custom_NewDelete).
:::

::: {#__Enum .methodShort}
### \_\_Enum

Enumerates array elements.

``` Syntax
For Value in ArrayObj
```

``` Syntax
For Index, Value in ArrayObj
```

Returns a new [enumerator](Enumerator.htm). This method is typically not
called directly. Instead, the array object is passed directly to a
[for-loop](For.htm), which calls \_\_Enum once and then calls the
enumerator once for each iteration of the loop. Each call to the
enumerator returns the next array element. The for-loop\'s variables
correspond to the enumerator\'s parameters, which are:

Index

:   Type: [Integer](../Concepts.htm#numbers)

    The array index, typically the same as
    [A_Index](../Variables.htm#Index). This is present only in the
    two-parameter mode.

Value

:   Type: [Any](../Concepts.htm#values)

    The value (if there is no value, *Value* becomes
    [uninitialized](../Concepts.htm#uninitialized-variables)).
:::

## Properties {#Properties}

::: {#Length .methodShort}
### Length

Retrieves or sets the length of an array.

``` Syntax
Length := ArrayObj.Length
```

``` Syntax
ArrayObj.Length := Length
```

The length includes elements which have no value. Increasing the length
changes which indices are considered valid, but the new elements have no
value (as indicated by [Has](#Has)). Decreasing the length truncates the
array.

    MsgBox ["A", "B", "C"].Length  ;  3
    MsgBox ["A",    , "C"].Length  ;  3
:::

::: {#Capacity .methodShort}
### Capacity

Retrieves or sets the current capacity of an array.

``` Syntax
MaxItems := ArrayObj.Capacity
```

``` Syntax
ArrayObj.Capacity := MaxItems
```

*MaxItems* is an [integer](../Concepts.htm#numbers) representing the
maximum number of elements the array should be able to contain before it
must be automatically expanded. If setting a value less than
[Length](#Length), elements are removed.
:::

::: {#Default .methodShort}
### Default

Defines the default value returned when an element with no value is
requested.

``` Syntax
ArrayObj.Default := Value
```

This property actually doesn\'t exist by default, but can be defined by
the script. If defined, its value is returned by [\_\_Item](#__Item) or
[Get](#Get) if the requested element has no value, instead of throwing
an [UnsetItemError](Error.htm#UnsetError). It can be implemented by any
of the normal means, including a [dynamic
property](Object.htm#DefineProp) or
[meta-function](../Objects.htm#Meta_Functions), but determining which
key was queried would require overriding [\_\_Item](#__Item) or
[Get](#Get) instead.

Setting a default value does not prevent an error from being thrown when
the index is out of range.
:::

::: {#__Item .methodShort}
### \_\_Item

Retrieves or sets the value of an array element.

``` Syntax
Value := ArrayObj[Index]
Value := ArrayObj.__Item[Index]
```

``` Syntax
ArrayObj[Index] := Value
ArrayObj.__Item[Index] := Value
```

*Index* is an [integer](../Concepts.htm#numbers) representing a valid
array index; that is, an integer with absolute value between 1 and
[Length](#Length) (inclusive). A negative index can be used to address
elements in reverse, so that -1 is the last element, -2 is the second
last element, and so on. Attempting to use an index which is out of
bounds (such as zero, or if its absolute value is greater than the
[Length](#Length) of the array) is considered an error and will cause an
[IndexError](Error.htm#IndexError) to be thrown.

The property name \_\_Item is typically omitted, as shown above, but is
used when overriding the property.
:::
