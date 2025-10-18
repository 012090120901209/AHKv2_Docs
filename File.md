# File Object

``` NoIndent
class File extends Object
```

Provides an interface for file input/output, such as reading or writing
text or retrieving its length. [FileOpen](FileOpen.htm) returns an
object of this type.

\"FileObj\" is used below as a placeholder for any File object, as
\"File\" is the class itself.

In addition to the methods and property inherited from
[Object](Object.htm), File objects have the following predefined methods
and properties.

## Table of Contents {#toc}

-   [Methods](#Methods):
    -   [Read](#Read): Reads a string of characters from the file and
        advances the file pointer.
    -   [Write](#Write): Writes a string of characters to the file and
        advances the file pointer.
    -   [ReadLine](#ReadLine): Reads a line of text from the file and
        advances the file pointer.
    -   [WriteLine](#WriteLine): Writes a line of text to the file and
        advances the file pointer.
    -   [Read*NumType*](#ReadNum): Reads a number from the file and
        advances the file pointer.
    -   [Write*NumType*](#WriteNum): Writes a number to the file and
        advances the file pointer.
    -   [RawRead](#RawRead): Reads raw binary data from the file into
        memory and advances the file pointer.
    -   [RawWrite](#RawWrite): Writes raw binary data to the file and
        advances the file pointer.
    -   [Seek](#Seek): Moves the file pointer.
    -   [Close](#Close): Closes the file, flushes any data in the cache
        to disk and releases the share locks.
-   [Properties](#Properties):
    -   [Pos](#Pos): Retrieves or sets the position of the file pointer.
    -   [Length](#Length): Retrieves or sets the size of the file.
    -   [AtEOF](#AtEOF): Retrieves a non-zero number if the file pointer
        has reached the end of the file.
    -   [Encoding](#Encoding): Retrieves or sets the text encoding used
        by this file object.
    -   [Handle](#Handle): Retrieves a system file handle, intended for
        use with DllCall.

## Methods {#Methods}

::: {#Read .methodShort}
### Read

Reads a string of characters from the file and advances the file
pointer.

``` Syntax
String := FileObj.Read(Characters)
```

#### Parameters {#Read_Parameters}

Characters

:   Type: [Integer](../Concepts.htm#numbers)

    If omitted, the rest of the file is read and returned as one string.
    Otherwise, specify the maximum number of characters to read. If the
    File object was created from a handle to a non-seeking device such
    as a console buffer or pipe, omitting this parameter may cause the
    method to fail or return only what data is currently available.

#### Return Value {#Read_Return_Value}

Type: [String](../Concepts.htm#strings)

This method returns the string of characters that were read.
:::

::: {#Write .methodShort}
### Write

Writes a string of characters to the file and advances the file pointer.

``` Syntax
BytesWritten := FileObj.Write(String)
```

#### Parameters {#Write_Parameters}

String

:   Type: [String](../Concepts.htm#strings)

    The string to write.

#### Return Value {#Write_Return_Value}

Type: [Integer](../Concepts.htm#numbers)

This method returns the number of bytes (not characters) that were
written.
:::

::: {#ReadLine .methodShort}
### ReadLine

Reads a line of text from the file and advances the file pointer.

``` Syntax
TextLine := FileObj.ReadLine()
```

#### Return Value {#ReadLine_Return_Value}

Type: [String](../Concepts.htm#strings)

This method returns a line of text, excluding the line ending.

#### Remarks {#ReadLine_Remarks}

Lines up to 65,534 characters long can be read. If the length of a line
exceeds this, the remainder of the line is returned by subsequent calls
to this method.
:::

::: {#WriteLine .methodShort}
### WriteLine

Writes a line of text to the file and advances the file pointer.

``` Syntax
BytesWritten := FileObj.WriteLine(String)
```

#### Parameters {#WriteLine_Parameters}

String

:   Type: [String](../Concepts.htm#strings)

    If blank or omitted, an empty line will be written. Otherwise,
    specify the string to write, which is always followed by `` `n `` or
    `` `r`n ``, depending on the EOL flags used to open the file.

#### Return Value {#WriteLine_Return_Value}

Type: [Integer](../Concepts.htm#numbers)

This method returns the number of bytes (not characters) that were
written.
:::

::: {#ReadNum .methodShort}
### Read*NumType*

Reads a number from the file and advances the file pointer.

``` Syntax
Num := FileObj.ReadNumType()
```

*NumType* is either UInt, Int, Int64, Short, UShort, Char, UChar,
Double, or Float. These type names have the same meanings as with
[DllCall](DllCall.htm#types).

#### Return Value {#ReadNum_Return_Value}

Type: [Integer](../Concepts.htm#numbers),
[Float](../Concepts.htm#numbers) or [String
(empty)](../Concepts.htm#nothing)

On success, this method returns a number. On failure, it returns an
empty string.

#### Remarks {#ReadNum_Remarks}

If the number of bytes read is non-zero but less than the size of
*NumType*, the missing bytes are assumed to be zero.
:::

::: {#WriteNum .methodShort}
### Write*NumType*

Writes a number to the file and advances the file pointer.

``` Syntax
BytesWritten := FileObj.WriteNumType(Num)
```

*NumType* is either UInt, Int, Int64, Short, UShort, Char, UChar,
Double, or Float. These type names have the same meanings as with
[DllCall](DllCall.htm#types).

#### Parameters {#WriteNum_Parameters}

Num

:   Type: [Integer](../Concepts.htm#numbers) or
    [Float](../Concepts.htm#numbers)

    The number to write.

#### Return Value {#WriteNum_Return_Value}

Type: [Integer](../Concepts.htm#numbers)

This method returns the number of bytes that were written. For example,
`FileObj.WriteUInt(42)` returns 4 if successful.
:::

::: {#RawRead .methodShort}
### RawRead

Reads raw binary data from the file into memory and advances the file
pointer.

``` Syntax
BytesRead := FileObj.RawRead(Buffer , Bytes)
```

#### Parameters {#RawRead_Parameters}

Buffer

:   Type: [Object](../Concepts.htm#objects) or
    [Integer](../Concepts.htm#numbers)

    The [Buffer](Buffer.htm)-like object or memory address which will
    receive the data.

    Reading into a [Buffer](Buffer.htm) is recommended. If *Bytes* is
    omitted, it defaults to the size of the buffer. An exception is
    thrown if *Bytes* exceeds the size of the buffer.

    If a memory address is passed, *Bytes* must also be specified.

Bytes

:   Type: [Integer](../Concepts.htm#numbers)

    The maximum number of bytes to read. This is optional when *Buffer*
    is an object; otherwise, it is required.

#### Return Value {#RawRead_Return_Value}

Type: [Integer](../Concepts.htm#numbers)

This method returns the number of bytes that were read.
:::

::: {#RawWrite .methodShort}
### RawWrite

Writes raw binary data to the file and advances the file pointer.

``` Syntax
BytesWritten := FileObj.RawWrite(Data , Bytes)
```

#### Parameters {#RawWrite_Parameters}

Data

:   Type: [Object](../Concepts.htm#objects),
    [String](../Concepts.htm#strings) or
    [Integer](../Concepts.htm#numbers)

    A [Buffer](Buffer.htm)-like object or string containing binary data,
    or a memory address. If an object or string is specified, *Bytes* is
    optional and defaults to the size of the buffer or string.
    Otherwise, *Bytes* must also be specified.

Bytes

:   Type: [Integer](../Concepts.htm#numbers)

    The number of bytes to write. This is optional when *Data* is an
    object or string; otherwise, it is required.

#### Return Value {#RawWrite_Return_Value}

Type: [Integer](../Concepts.htm#numbers)

This method returns the number of bytes that were written.
:::

::: {#Seek .methodShort}
### Seek

Moves the file pointer.

``` Syntax
IsMoved := FileObj.Seek(Distance , Origin)
```

#### Parameters {#Seek_Parameters}

Distance

:   Type: [Integer](../Concepts.htm#numbers)

    Distance to move, in bytes. Lower values are closer to the beginning
    of the file.

Origin

:   Type: [Integer](../Concepts.htm#numbers)

    If omitted, it defaults to 2 when *Distance* is negative and 0
    otherwise. Otherwise, specify one of the following numbers to
    indicate the starting point for the file pointer move:

    -   0 (SEEK_SET): Beginning of the file. *Distance* must be zero or
        greater.
    -   1 (SEEK_CUR): Current position of the file pointer.
    -   2 (SEEK_END): End of the file. *Distance* should usually be
        negative.

#### Return Value {#Seek_Return_Value}

Type: [Integer (boolean)](../Concepts.htm#boolean)

On success, this method returns 1 (true). On failure, it returns 0
(false).

#### Remarks {#Seek_Remarks}

This method is equivalent to `FileObj.Pos := Distance`, if *Distance* is
not negative and *Origin* is omitted or 0 (SEEK_SET).
:::

::: {#Close .methodShort}
### Close

Closes the file, flushes any data in the cache to disk and releases the
share locks.

``` Syntax
FileObj.Close()
```

Although the file is closed automatically when the object is freed, it
is recommended to close the file as soon as possible.
:::

## Properties {#Properties}

::: {#Pos .methodShort}
### Pos

Retrieves or sets the position of the file pointer.

``` Syntax
CurrentPos := FileObj.Pos
```

``` Syntax
FileObj.Pos := NewPos
```

*CurrentPos* and *NewPos* are a byte offset from the beginning of the
file, where 0 is the first byte. When data is written to or read from
the file, the file pointer automatically moves to the next byte after
that data.

This property is equivalent to `FileObj.Seek(NewPos)`.
:::

::: {#Length .methodShort}
### Length

Retrieves or sets the size of the file.

``` Syntax
CurrentSize := FileObj.Length
```

``` Syntax
FileObj.Length := NewSize
```

*CurrentSize* and *NewSize* are the size of the file, in bytes.

This property should be used only with an actual file. If the File
object was created from a handle to a pipe, it may return the amount of
data currently available in the pipe\'s internal buffer, but this
behaviour is not guaranteed.
:::

::: {#AtEOF .methodShort}
### AtEOF

Retrieves a non-zero number if the file pointer has reached the end of
the file, otherwise zero.

``` Syntax
IsAtEOF := FileObj.AtEOF
```

This property should be used only with an actual file. If the File
object was created from a handle to a non-seeking device such as a
console buffer or pipe, the returned value may not be meaningful, as
such devices do not logically have an \"end of file\".
:::

::: {#Encoding .methodShort}
### Encoding

Retrieves or sets the text encoding used by this file object.

``` Syntax
CurrentEncoding := FileObj.Encoding
```

``` Syntax
FileObj.Encoding := NewEncoding
```

*NewEncoding* may be a numeric code page identifier (see [Microsoft
Docs](https://learn.microsoft.com/windows/win32/intl/code-page-identifiers))
or one of the following strings.

*CurrentEncoding* is one of the following strings:

-   `UTF-8`{.no-highlight}: Unicode UTF-8, equivalent to CP65001.
-   `UTF-16`{.no-highlight}: Unicode UTF-16 with little endian byte
    order, equivalent to CP1200.
-   `CP`*`nnn`*: a code page with numeric identifier *nnn*.

*CurrentEncoding* is never a value with the `-RAW` suffix, regardless of
how the file was opened or whether it contains a byte order mark (BOM).
Setting *NewEncoding* never causes a BOM to be added or removed, as the
BOM is normally written to the file when it is first created.

Setting *NewEncoding* to `UTF-8-RAW`{.no-highlight} or
`UTF-16-RAW`{.no-highlight} is valid, but the `-RAW` suffix is ignored.
This only applies to `FileObj.Encoding`, not [FileOpen](FileOpen.htm).
:::

::: {#Handle .methodShort}
### Handle

Returns a system file handle, intended for use with
[DllCall](DllCall.htm). See
[CreateFile](https://learn.microsoft.com/windows/win32/api/fileapi/nf-fileapi-createfilea).

``` Syntax
Handle := FileObj.Handle
```

File objects internally buffer reads or writes. If data has been written
into the object\'s internal buffer, it is committed to disk before the
handle is returned. If the buffer contains data read from file, it is
discarded and the actual file pointer is reset to the logical position
indicated by the [Pos](#Pos) property.
:::
