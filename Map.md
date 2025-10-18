# Map Object

``` NoIndent
class Map extends Object
```

A **Map** object associates or *maps* one set of values, called *keys*,
to another set of values. A key and the value it is mapped to are known
as a key-value pair. A map can contain any number of key-value pairs,
but each key must be unique.

A key may be any [Integer](../Concepts.htm#numbers),
[object](../Objects.htm) reference or null-terminated
[String](../Concepts.htm#strings). Comparison of string keys is
case-sensitive, while objects are compared by reference/address.
[Float](../Concepts.htm#numbers) keys are automatically converted to
String.

The simplest use of a map is to retrieve or set a key-value pair via the
implicit [\_\_Item](#__Item) property, by simply writing the key between
brackets following the map object. For example:

    clrs := Map()
    clrs["Red"] := "ff0000"
    clrs["Green"] := "00ff00"
    clrs["Blue"] := "0000ff"
    for clr in Array("Blue", "Green")
        MsgBox clrs[clr]

\"MapObj\" is used below as a placeholder for any Map object, as \"Map\"
is the class itself.

In addition to the methods and property inherited from
[Object](Object.htm), Map objects have the following predefined methods
and properties.

## Table of Contents {#toc}

-   [Static Methods](#StaticMethods):
    -   [Call](#Call): Creates a Map and sets items.
-   [Methods](#Methods):
    -   [Clear](#Clear): Removes all key-value pairs from a map.
    -   [Clone](#Clone): Returns a shallow copy of a map.
    -   [Delete](#Delete): Removes a key-value pair from a map.
    -   [Get](#Get): Returns the value associated with a key, or a
        default value.
    -   [Has](#Has): Returns true if the specified key has an associated
        value within a map.
    -   [Set](#Set): Sets zero or more items.
    -   [\_\_Enum](#__Enum): Enumerates key-value pairs.
    -   [\_\_New](#__New): Sets items. Equivalent to Set.
-   [Properties](#Properties):
    -   [Count](#Count): Retrieves the number of key-value pairs present
        in a map.
    -   [Capacity](#Capacity): Retrieves or sets the current capacity of
        a map.
    -   [CaseSense](#CaseSense): Retrieves or sets a map\'s case
        sensitivity setting.
    -   [Default](#Default): Defines the default value returned when a
        key is not found.
    -   [\_\_Item](#__Item): Retrieves or sets the value of a key-value
        pair.

## Static Methods {#StaticMethods}

::: {#Call .methodShort}
### Call

Creates a Map and sets items.

``` Syntax
MapObj := Map(Key1, Value1, Key2, Value2, ...)
MapObj := Map.Call(Key1, Value1, Key2, Value2, ...)
```

This is equivalent to setting each item with `MapObj[Key] := Value`,
except that [\_\_Item](#__Item) is not called and [Capacity](#Capacity)
is automatically adjusted to avoid expanding multiple times during a
single call.

Parameters are defined by [\_\_New](#__New).
:::

## Methods {#Methods}

::: {#Clear .methodShort}
### Clear

Removes all key-value pairs from a map.

``` Syntax
MapObj.Clear()
```
:::

::: {#Clone .methodShort}
### Clone

Returns a shallow copy of a map.

``` Syntax
Clone := MapObj.Clone()
```

All key-value pairs are copied to the new map. Object *references* are
copied (like with a normal assignment), not the objects themselves.

Own properties, own methods and base are copied as per
[Obj.Clone](Object.htm#Clone).
:::

::: {#Delete .methodShort}
### Delete

Removes a key-value pair from a map.

``` Syntax
RemovedValue := MapObj.Delete(Key)
```

#### Parameters {#Delete_Parameters}

Key

:   Type: [Integer](../Concepts.htm#numbers),
    [Object](../Concepts.htm#objects) or
    [String](../Concepts.htm#strings)

    Any single key. If the map does not contain this key, an
    [UnsetItemError](Error.htm#UnsetError) is thrown.

#### Return Value {#Delete_Return_Value}

Type: [Any](../Concepts.htm#values)

This method returns the removed value.
:::

::: {#Get .methodShort}
### Get

Returns the value associated with a key, or a default value.

``` Syntax
Value := MapObj.Get(Key , Default)
```

This method does the following:

-   Return the value associated with *Key*, if found.
-   Return the value of the *Default* parameter, if specified.
-   Return the value of `MapObj.Default`, if defined.
-   Throw an [UnsetItemError](Error.htm#UnsetError).

When *Default* is omitted, this is equivalent to `MapObj[Key]`, except
that [\_\_Item](#__Item) is not called.
:::

::: {#Has .methodShort}
### Has

Returns true if the specified key has an associated value within a map,
otherwise false.

``` Syntax
MapObj.Has(Key)
```
:::

::: {#Set .methodShort}
### Set

Sets zero or more items.

``` Syntax
MapObj.Set(Key, Value, Key2, Value2, ...)
```

This is equivalent to setting each item with `MapObj[Key] := Value`,
except that [\_\_Item](#__Item) is not called and [Capacity](#Capacity)
is automatically adjusted to avoid expanding multiple times during a
single call.

#### Return Value {#Set_Return_Value}

Type: [Object](../Concepts.htm#objects)

This method returns the Map.
:::

::: {#__Enum .methodShort}
### \_\_Enum

Enumerates key-value pairs.

``` Syntax
For Key , Value in MapObj
```

Returns a new [enumerator](Enumerator.htm). This method is typically not
called directly. Instead, the map object is passed directly to a
[for-loop](For.htm), which calls \_\_Enum once and then calls the
enumerator once for each iteration of the loop. Each call to the
enumerator returns the next key and/or value. The for-loop\'s variables
correspond to the enumerator\'s parameters, which are:

Key

:   Type: [Integer](../Concepts.htm#numbers),
    [Object](../Concepts.htm#objects) or
    [String](../Concepts.htm#strings)

    The key.

Value

:   Type: [Any](../Concepts.htm#values)

    The value.
:::

::: {#__New .methodShort}
### \_\_New

Sets items. Equivalent to [Set](#Set).

``` Syntax
MapObj.__New(Key, Value, Key2, Value2, ...)
```

This method exists to support [Call](#Call), and is not intended to be
called directly. See [Construction and
Destruction](../Objects.htm#Custom_NewDelete).
:::

## Properties {#Properties}

::: {#Count .methodShort}
### Count

Retrieves the number of key-value pairs present in a map.

``` Syntax
Count := MapObj.Count
```
:::

::: {#Capacity .methodShort}
### Capacity

Retrieves or sets the current capacity of a map.

``` Syntax
MaxItems := MapObj.Capacity
```

``` Syntax
MapObj.Capacity := MaxItems
```

*MaxItems* is an [integer](../Concepts.htm#numbers) representing the
maximum number of key-value pairs the map should be able to contain
before it must be automatically expanded. If setting a value less than
the current number of key-value pairs, that number is used instead, and
any unused space is freed.
:::

::: {#CaseSense .methodShort}
### CaseSense

Retrieves or sets a map\'s case sensitivity setting.

``` Syntax
CurrentSetting := MapObj.CaseSense
```

``` Syntax
MapObj.CaseSense := NewSetting
```

*CurrentSetting* is *NewSetting* if assigned, otherwise On by default
(but note that this property only retrieves the string variant of the
current setting).

*NewSetting* is one of the following [strings](../Concepts.htm#strings)
or [integers (boolean)](../Concepts.htm#boolean):

**On** or **1** (true): Key lookups are case-sensitive. This is the
default setting.

**Off** or **0** (false): Key lookups are not case-sensitive, i.e. the
letters A-Z are considered identical to their lowercase counterparts.

**Locale:** Key lookups are not case-sensitive according to the rules of
the current user\'s locale. For example, most English and Western
European locales treat not only the letters A-Z as identical to their
lowercase counterparts, but also non-ASCII letters like Ä and Ü as
identical to theirs. *Locale* is 1 to 8 times slower than *Off*
depending on the nature of the strings being compared.

Attempting to assign to this property causes an exception to be thrown
if the Map is not empty.
:::

::: {#Default .methodShort}
### Default

Defines the default value returned when a key is not found.

``` Syntax
MapObj.Default := Value
```

This property actually doesn\'t exist by default, but can be defined by
the script. If defined, its value is returned by [\_\_Item](#__Item) or
[Get](#Get) if the requested item cannot be found, instead of throwing
an [UnsetItemError](Error.htm#UnsetError). It can be implemented by any
of the normal means, including a [dynamic
property](Object.htm#DefineProp) or
[meta-function](../Objects.htm#Meta_Functions), but determining which
key was queried would require overriding [\_\_Item](#__Item) or
[Get](#Get) instead.
:::

::: {#__Item .methodShort}
### \_\_Item

Retrieves or sets the value of a key-value pair.

``` Syntax
Value := MapObj[Key]
Value := MapObj.__Item[Key]
```

``` Syntax
MapObj[Key] := Value
MapObj.__Item[Key] := Value
```

When retrieving a value, *Key* must be a unique value previously
associated with another value. An [UnsetItemError](Error.htm#UnsetError)
is thrown if *Key* has no associated value within the map, unless a
[Default](#Default) property is defined, in which case its value is
returned.

When assigning a value, *Key* can be any value to associate with
*Value*; in other words, the *key* used to later access *Value*.
[Float](../Concepts.htm#numbers) keys are automatically converted to
String.

The property name \_\_Item is typically omitted, as shown above, but is
used when overriding the property.
:::
