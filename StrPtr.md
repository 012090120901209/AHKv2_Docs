# StrPtr

Returns the current memory address of a string.

``` Syntax
Address := StrPtr(Value)
```

## Parameters {#Parameters}

Value

:   Type: [String](../Concepts.htm#strings)

## Return Value {#Return_Value}

Type: [Integer](../Concepts.htm#numbers)

This function returns the current memory address of *Value*.

## Remarks {#Remarks}

The lifetime of an address and which operations are valid to perform on
it depend on how *Value* was passed to this function. There are three
distinct cases, shown as example code below. In all cases, if the string
will [not]{.underline} be modified, the return value can be passed
*directly* to a [DllCall](DllCall.htm) function or
[SendMessage](SendMessage.htm).

    Ptr := StrPtr(MyVar)

If *Value* is a variable reference such as `MyVar` (and not a built-in
variable), the return value is the memory address of the variable\'s
internal string buffer.
[`VarSetStrCapacity`](VarSetStrCapacity.htm)`(&MyVar)` returns the size
of the buffer **in characters**, excluding the terminating null
character.

The address should be considered valid *only* until the variable is
freed or has been reassigned by means of any of the [assignment
operators](../Variables.htm#AssignOp) or by passing it to a built-in
function. The address of the contents of a function\'s
[local](../Functions.htm#Local) variable is not valid after the function
returns, as local variables are freed automatically.

The address can be stored in a [structure](DllCall.htm#struct) or
another variable, and passed indirectly to [DllCall](DllCall.htm) or
[SendMessage](SendMessage.htm) or used in other ways, for as long as it
remains valid as described above.

The script may change the value of the string indirectly by passing the
address to [NumPut](NumPut.htm), [DllCall](DllCall.htm) or
[SendMessage](SendMessage.htm). If the length of the string is changed
this way, the variable\'s internal length property must be updated by
calling [`VarSetStrCapacity`](VarSetStrCapacity.htm)`(&MyVar, -1)`.

    Ptr := StrPtr("literal string")

The address of a literal string is valid until the program exits. The
script should not attempt to modify the string. The address can be
stored in a [structure](DllCall.htm#struct) or another variable, and
passed indirectly to [DllCall](DllCall.htm) or
[SendMessage](SendMessage.htm) or used in other ways.

    SendMessage 0x000C, 0, StrPtr(A_ScriptName " changed this title"),, "A"

The address of a temporary string is valid only until evaluation of the
overall expression or function call statement is completed, after which
time it must not be used. For the example above, the address is valid
until SendMessage returns. All of the following yield temporary strings:

-   Concatenation.
-   Built-in variables such as
    [A_ScriptName](../Variables.htm#ScriptName).
-   Functions which return strings.
-   Accessing properties of an object, array elements or map elements.

If not explicitly covered above, it is safe to assume the string is
temporary.

## Related {#Related}

[VarSetStrCapacity](VarSetStrCapacity.htm), [DllCall](DllCall.htm),
[SendMessage](SendMessage.htm), [Buffer object](Buffer.htm),
[NumPut](NumPut.htm), [NumGet](NumGet.htm)
