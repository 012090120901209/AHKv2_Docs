# Buffer Object

``` NoIndent
class Buffer extends Object
```

Encapsulates a block of memory for use with advanced techniques such as
DllCall, structures, StrPut and raw file I/O.

Buffer objects are typically created by calling [Buffer()](#Call), but
can also be returned by [FileRead](FileRead.htm) with the \"RAW\"
option.

    BufferObj := Buffer(ByteCount)

[ClipboardAll](ClipboardAll.htm) returns a sub-type of Buffer, also
named ClipboardAll.

    class ClipboardAll extends Buffer

\"BufferObj\" is used below as a placeholder for any Buffer object, as
\"Buffer\" is the class itself.

In addition to the methods and property inherited from
[Object](Object.htm), Buffer objects have the following predefined
properties.

## Table of Contents {#toc}

-   [Buffer-like Objects](#like)
-   [Static Methods](#StaticMethods):
    -   [Call](#Call): Creates a new Buffer object.
-   [Methods](#Methods):
    -   [\_\_New](#__New): Allocates or reallocates the buffer and
        optionally fills it.
-   [Properties](#Properties):
    -   [Ptr](#Ptr): Retrieves the buffer\'s current memory address.
    -   [Size](#Size): Retrieves or sets the buffer\'s size, in bytes.
-   [Related](#Related)
-   [Examples](#Examples)

## Buffer-like Objects {#like}

Some built-in functions accept a Buffer object in place of an address -
see the [Related](#Related) section for links. These functions also
accept any other object which has [Ptr](#Ptr) and [Size](#Size)
properties, but are optimized for the native Buffer object.

In most cases, passing a Buffer object is safer than passing an address,
as the function can read the [buffer size](#Size) to ensure that it does
not attempt to access any memory location outside of the buffer. One
exception is that [DllCall](DllCall.htm) calls functions outside of the
program; in those cases, it may be necessary to explicitly pass the
[buffer size](#Size) to the function.

## Static Methods {#StaticMethods}

::: {#Call .methodShort}
### Call

Creates a new Buffer object.

``` Syntax
BufferObj := Buffer(ByteCount, FillByte)
BufferObj := Buffer.Call(ByteCount, FillByte)
```

#### Parameters {#Call_Parameters}

ByteCount

:   Type: [Integer](../Concepts.htm#numbers)

    The number of bytes to allocate. Corresponds to
    [Buffer.Size](#Size).

    If omitted, the Buffer is created with a null (zero) [Ptr](#Ptr) and
    zero [Size](#Size).

FillByte

:   Type: [Integer](../Concepts.htm#numbers)

    Specify a number between 0 and 255 to set each byte in the buffer to
    that number.

    This should generally be omitted in cases where the buffer will be
    written into without first being read, as it has a time-cost
    proportionate to the number of bytes. If omitted, the memory of the
    buffer is not initialized; the value of each byte is arbitrary.

#### Return Value {#Call_Return_Value}

Type: [Object](../Concepts.htm#objects)

This method or function returns a Buffer object.

#### Remarks {#Call_Remarks}

A [MemoryError](Error.htm#MemoryError) is thrown if the memory could not
be allocated, such as if *ByteCount* is unexpectedly large or the system
is low on virtual memory.

Parameters are defined by [\_\_New](#__New).
:::

## Methods {#Methods}

::: {#__New .methodShort}
### \_\_New

Allocates or reallocates the buffer and optionally fills it.

``` Syntax
BufferObj.__New(ByteCount, FillByte)
```

This method exists to support [Call](#Call), and is not usually called
directly. See [Construction and
Destruction](../Objects.htm#Custom_NewDelete).

Specify *ByteCount* to allocate, reallocate or free the buffer. This is
equivalent to assigning [Size](#Size).

Specify *FillByte* to fill the buffer with the given numeric byte value,
overwriting any existing content.

If both parameters are omitted, this method has no effect.
:::

## Properties {#Properties}

::: {#Ptr .methodShort}
### Ptr

Retrieves the buffer\'s current memory address.

``` Syntax
CurrentPtr := BufferObj.Ptr
```

*CurrentPtr* is an [integer](../Concepts.htm#numbers) representing the
buffer\'s current memory address. This address becomes invalid when the
buffer is freed or reallocated. Invalid addresses must not be used. The
buffer is not freed until the Buffer object\'s [reference
count](../Objects.htm#Reference_Counting) reaches zero, but it is
reallocated when its [Size](#Size) is changed.
:::

::: {#Size .methodShort}
### Size

Retrieves or sets the buffer\'s size, in bytes.

``` Syntax
CurrentByteCount := BufferObj.Size
```

``` Syntax
BufferObj.Size := NewByteCount
```

*CurrentByteCount* and *NewByteCount* are an
[integer](../Concepts.htm#numbers) representing the buffer\'s size, in
bytes. The buffer\'s address typically changes whenever its size is
changed. If the size is decreased, the data within the buffer is
truncated, but the remaining bytes are preserved. If the size is
increased, all data is preserved and the values of any new bytes are
arbitrary (they are not initialized, for performance reasons).

A [MemoryError](Error.htm#MemoryError) is thrown if the memory could not
be allocated, such as if *NewByteCount* is unexpectedly large or the
system is low on virtual memory.

*CurrentByteCount* is always the exact value it was given either by
[\_\_New](#__New) or by a previous assignment.
:::

## Related {#Related}

[DllCall](DllCall.htm), [NumPut](NumPut.htm), [NumGet](NumGet.htm),
[StrPut](StrPut.htm), [StrGet](StrGet.htm),
[File.RawRead](File.htm#RawRead), [File.RawWrite](File.htm#RawWrite),
[ClipboardAll](ClipboardAll.htm)

## Examples {#Examples}

::: {#ExString .ex}
[](#ExString){.ex_number} Uses a Buffer to receive a string from an
external function via [DllCall](DllCall.htm).

    max_chars := 11

    ; Allocate a buffer for use with the Unicode version of wsprintf.
    bufW := Buffer(max_chars*2)

    ; Print a UTF-16 string into the buffer with wsprintfW().
    DllCall("wsprintfW", "Ptr", bufW, "Str", "0x%08x", "UInt", 4919, "CDecl")

    ; Retrieve the string from bufW and show it.
    MsgBox StrGet(bufW, "UTF-16")  ; Or just StrGet(bufW).

    ; Allocate a buffer for use with the ANSI version of wsprintf.
    bufA := Buffer(max_chars)

    ; Print an ANSI string into the buffer with wsprintfA().
    DllCall("wsprintfA", "Ptr", bufA, "AStr", "0x%08x", "UInt", 4919, "CDecl")

    ; Retrieve the string from bufA (converted to the native format), and show it.
    MsgBox StrGet(bufA, "CP0")
:::
