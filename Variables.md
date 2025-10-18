# Variables and Expressions

## Table of Contents {#toc}

-   [Variables](#Intro)
-   [Expressions](#Expressions)
-   [Operators in Expressions](#Operators)
-   [Built-in Variables](#BuiltIn)
-   [Variable Capacity and Memory](#cap)

[]{#Variables}

## Variables {#Intro}

See [Variables](Concepts.htm#variables) for general explanation and
details about how variables work.

**Storing values in variables:** To store a string or number in a
variable, use the [colon-equal operator (:=)](#AssignOp) followed by a
number, quoted string or any other type of
[expression](Language.htm#expressions). For example:

    MyNumber := 123
    MyString := "This is a literal string."
    CopyOfVar := Var

A variable cannot be explicitly deleted, but its previous value can be
released by assigning a new value, such as an empty string:

    MyVar := ""

A variable can also be assigned a value indirectly, by [taking its
reference](#ref) and using a [double-deref](#deref) or passing it to a
function. For example:

    MouseGetPos &x, &y

Reading the value of a variable which has not been assigned a value is
considered an error. [IsSet](lib/IsSet.htm) can be used to detect this
condition.

**Retrieving the contents of variables:** To include the contents of a
variable in a string, use [concatenation](#concat) or
[Format](lib/Format.htm). For example:

    MsgBox "The value of Var is " . Var . "."
    MsgBox "The value in the variable named Var is " Var "."
    MsgBox Format("Var has the value {1}.", Var)

Sub-expressions can be combined with strings in the same way. For
example:

    MsgBox("The sum of X and Y is " . (X + Y))

**Comparing variables:** Please read the expressions section below for
important notes about the different kinds of comparisons.

## Expressions {#Expressions}

See [Expressions](Language.htm#expressions) for a structured overview
and further explanation.

Expressions are used to perform one or more operations upon a series of
variables, literal strings, and/or literal numbers.

Plain words in expressions are interpreted as variable names.
Consequently, literal strings must be enclosed in double quotes to
distinguish them from variables. For example:

    if (CurrentSetting > 100 or FoundColor != "Blue")
        MsgBox "The setting is too high or the wrong color is present."

In the example above, \"Blue\" appears in quotes because it is a literal
string. Single-quote marks (\') and double-quote marks (\") function
identically, except that a string enclosed in single-quote marks can
contain literal double-quote marks and vice versa. Therefore, to include
an *actual* quote mark inside a literal string,
[escape](misc/EscapeChar.htm) the quote mark or enclose the string in
the opposite type of quote mark. For example:

    MsgBox "She said, `"An apple a day.`""
    MsgBox 'She said, "An apple a day."'

**Empty strings:** To specify an empty string in an expression, use an
empty pair of quotes. For example, the statement `if (MyVar != "")`
would be true if *MyVar* is not blank.

**Storing the result of an expression:** To assign a result to a
variable, use the [colon-equal operator (:=)](#AssignOp). For example:

    NetPrice := Price * (1 - Discount/100)

**Boolean values:** When an expression is required to evaluate to true
or false (such as an IF-statement), a blank or zero result is considered
false and all other results are considered true. For example, the
statement `if ItemCount` would be false only if ItemCount is blank or 0.
Similarly, the expression `if not ItemCount` would yield the opposite
result.

Operators such as NOT/\>/=/\< automatically produce a true or false
value: they yield 1 for true and 0 for false. However, the AND/OR
operators always produce one of the input values. For example, in the
following expression, the variable *Done* is assigned 1 if A_Index is
greater than 5 or the value of *FoundIt* in all other cases:

    Done := A_Index > 5 or FoundIt

As hinted above, a variable can be used to hold a false value simply by
making it blank or assigning 0 to it. To take advantage of this, the
shorthand statement `if Done` can be used to check whether the variable
Done is true or false.

[]{#True}[]{#False}In an expression, the keywords *true* and *false*
resolve to 1 and 0. They can be used to make a script more readable as
in these examples:

    CaseSensitive := false
    ContinueSearch := true

**Integers and floating point:** Within an expression, numbers are
considered to be floating point if they contain a decimal point or
scientific notation; otherwise, they are integers. For most operators
\-- such as addition and multiplication \-- if either of the inputs is a
floating point number, the result will also be a floating point number.

Within expressions and non-expressions alike, integers may be written in
either hexadecimal or decimal format. Hexadecimal numbers all start with
the prefix 0x. For example, `Sleep 0xFF` is equivalent to `Sleep 255`.
Floating point numbers can optionally be written in scientific notation,
with or without a decimal point (e.g. `1e4` or `-2.1E-4`).

Within expressions, unquoted literal numbers such as `128`, `0x7F` and
`1.0` are converted to pure numbers before the script begins executing,
so converting the number to a string may produce a value different to
the original literal value. For example:

    MsgBox(0x7F)  ; Shows 128
    MsgBox(1.00)  ; Shows 1.0

## Operators in Expressions {#Operators}

See [Operators](Language.htm#operators) for general information about
operators.

Except where noted below, any blank value (empty string) or non-numeric
value involved in a math operation is **not** assumed to be zero.
Instead, a [TypeError](lib/Error.htm#TypeError) is thrown. If
[Try](lib/Try.htm) is not used, the unhandled exception causes an error
dialog by default.

### Expression Operators (in descending precedence order) {#operators}

+-----------------------------------+-----------------------------------+
| Operator                          | Description                       |
+===================================+===================================+
| %Expr%                            | **Dereference** or **name         |
|                                   | substitution**.                   |
|                                   |                                   |
|                                   | When *Expr* evaluates to a        |
|                                   | [VarRef](C                        |
|                                   | oncepts.htm#variable-references), |
|                                   | `%Expr%` accesses the             |
|                                   | corresponding variable. For       |
|                                   | example, `x := &y` takes a        |
|                                   | reference to *y* and assigns it   |
|                                   | to *x*, then `%x% := 1` assigns   |
|                                   | to the variable *y* and `%x%`     |
|                                   | reads its value.                  |
|                                   |                                   |
|                                   | Otherwise, the value of the       |
|                                   | sub-expression *Expr* is used as  |
|                                   | the name or partial name of a     |
|                                   | variable or property. This allows |
|                                   | the script to refer to a variable |
|                                   | or property whose name is         |
|                                   | determined by evaluating *Expr*,  |
|                                   | which is typically another        |
|                                   | variable. Variables cannot be     |
|                                   | created dynamically, but a        |
|                                   | variable can be assigned          |
|                                   | dynamically if it has been        |
|                                   | declared or referenced            |
|                                   | non-dynamically somewhere in the  |
|                                   | script.                           |
|                                   |                                   |
|                                   | **Note:** The                     |
|                                   | [result]{.underline} of the       |
|                                   | sub-expression *Expr* must be the |
|                                   | name or partial name of the       |
|                                   | variable or property to be        |
|                                   | accessed.                         |
|                                   |                                   |
|                                   | Percent signs cannot be used      |
|                                   | directly within *Expr* due to     |
|                                   | ambiguity, but can be nested      |
|                                   | within parentheses. Otherwise,    |
|                                   | *Expr* can be any expression.     |
|                                   |                                   |
|                                   | If there are any adjoining        |
|                                   | *%Expr%* sequences and partial    |
|                                   | [names](Concepts.htm#names)       |
|                                   | (without any spaces or other      |
|                                   | characters between them), they    |
|                                   | are combined to form a single     |
|                                   | name.                             |
|                                   |                                   |
|                                   | An [Error](lib/Error.htm) is      |
|                                   | typically thrown if the variable  |
|                                   | does not already exist, or if it  |
|                                   | is uninitialized and its value is |
|                                   | being read. The [or-maybe         |
|                                   | operator (??)](#or-maybe) can be  |
|                                   | used to avoid that case by        |
|                                   | providing a default value. For    |
|                                   | example: `%'novar'% ?? 42`.       |
|                                   |                                   |
|                                   | Although this is historically     |
|                                   | known as a \"double-deref\", this |
|                                   | term is inaccurate when *Expr*    |
|                                   | does not contain a variable       |
|                                   | (first deref), and also when the  |
|                                   | resulting variable is the target  |
|                                   | of an assignment, not being       |
|                                   | dereferenced (second deref).      |
+-----------------------------------+-----------------------------------+
| x.y\                              | **Member access**. Get or set a   |
| x.%z%                             | value or call a method of object  |
|                                   | *x*, where *y* is a literal name  |
|                                   | and *z* is an expression which    |
|                                   | evaluates to a name. See [object  |
|                                   | sy                                |
|                                   | ntax](Objects.htm#Usage_Objects). |
+-----------------------------------+-----------------------------------+
| *var***?**                        | **Maybe**. Permits the variable   |
|                                   | to be unset. This is valid only   |
|                                   | when passing a variable to an     |
|                                   | optional parameter, array element |
|                                   | or object literal; or on the      |
|                                   | right-hand side of a direct       |
|                                   | assignment. The question mark     |
|                                   | must be followed by one of the    |
|                                   | following symbols (ignoring       |
|                                   | whitespace):                      |
|                                   | `)]},:`{.no-highlight}. The       |
|                                   | variable may be passed            |
|                                   | conditionally via the [ternary    |
|                                   | operator](#ternary) or on the     |
|                                   | right-hand side of                |
|                                   | [AND](#and)/[OR](#or).            |
|                                   |                                   |
|                                   | The variable is typically an      |
|                                   | optional parameter, but can be    |
|                                   | any variable. For variables that  |
|                                   | are not function parameters, a    |
|                                   | [VarUnset                         |
|                                   | warning](lib/_Warn.htm#VarUnset)  |
|                                   | may still be shown at load-time   |
|                                   | if there are other references to  |
|                                   | the variable but no assignments.  |
|                                   |                                   |
|                                   | This operator is currently        |
|                                   | supported only for variables. To  |
|                                   | explicitly or conditionally omit  |
|                                   | a parameter in more general       |
|                                   | cases, use the `unset` keyword.   |
|                                   |                                   |
|                                   | See also: [unset (Optional        |
|                                   | Parameters)](Language.htm#unset)  |
+-----------------------------------+-----------------------------------+
| ++\                               | **Pre- and                        |
| \--                               | post-increment/decrement**. Adds  |
|                                   | or subtracts 1 from a variable.   |
|                                   | The operator may appear either    |
|                                   | before or after the variable\'s   |
|                                   | name. If it appears *before* the  |
|                                   | name, the operation is performed  |
|                                   | and its result is used by the     |
|                                   | next operation (the result is a   |
|                                   | variable reference in this case). |
|                                   | For example, `Var := ++X`         |
|                                   | increments X and then assigns its |
|                                   | value to *Var*. Conversely, if    |
|                                   | the operator appears *after* the  |
|                                   | variable\'s name, the result is   |
|                                   | the value of X prior to           |
|                                   | performing the operation. For     |
|                                   | example, `Var := X++` increments  |
|                                   | X but *Var* receives the value X  |
|                                   | had before it was incremented.    |
|                                   |                                   |
|                                   | These operators can also be used  |
|                                   | with a property of an object,     |
|                                   | such as `myArray.Length++` or     |
|                                   | `--myArray[i]`. In these cases,   |
|                                   | the result of the sub-expression  |
|                                   | is always a number, not a         |
|                                   | variable reference.               |
+-----------------------------------+-----------------------------------+
| \*\*                              | **Power**. Example usage:         |
|                                   | `Base**Exponent`. Both *Base* and |
|                                   | *Exponent* may contain a decimal  |
|                                   | point. If *Exponent* is negative, |
|                                   | the result will be formatted as a |
|                                   | floating point number even if     |
|                                   | *Base* and *Exponent* are both    |
|                                   | integers. Since \*\* is of higher |
|                                   | precedence than unary minus,      |
|                                   | `-2**2` is evaluated like         |
|                                   | `-(2**2)` and so yields -4. Thus, |
|                                   | to raise a literal negative       |
|                                   | number to a power, enclose it in  |
|                                   | parentheses such as `(-2)**2`.    |
|                                   |                                   |
|                                   | The power operator is             |
|                                   | right-associative. For example,   |
|                                   | `x ** y ** z` is evaluated as     |
|                                   | `x ** (y ** z)`.                  |
|                                   |                                   |
|                                   | **Note:** A negative *Base*       |
|                                   | combined with a fractional        |
|                                   | *Exponent* such as `(-2)**0.5` is |
|                                   | not supported; attempting it will |
|                                   | cause an exception to be thrown.  |
|                                   | But both `(-2)**2` and            |
|                                   | `(-2)**2.0` are supported. If     |
|                                   | both *Base* and *Exponent* are 0, |
|                                   | the result is undefined and an    |
|                                   | exception is thrown.              |
+-----------------------------------+-----------------------------------+
| \-\                               | **Unary minus (-):** Inverts the  |
| !\                                | sign of its operand.              |
| \~\                               |                                   |
| &                                 | **Unary plus (+):** `+N` is       |
|                                   | equivalent to `-(-N)`. This has   |
|                                   | no effect when applied to a pure  |
|                                   | number, but can be used to        |
|                                   | convert numeric strings to pure   |
|                                   | numbers.                          |
|                                   |                                   |
|                                   | **Logical-not (!):** If the       |
|                                   | operand is blank or 0, the result |
|                                   | of applying logical-not is 1,     |
|                                   | which means \"true\". Otherwise,  |
|                                   | the result is 0 (false). For      |
|                                   | example: `!x or !(y and z)`.      |
|                                   | Note: The word NOT is synonymous  |
|                                   | with **!** except that **!** has  |
|                                   | a higher precedence. Consecutive  |
|                                   | unary operators such as           |
|                                   | **`!!`**`Var` are allowed because |
|                                   | they are evaluated in             |
|                                   | right-to-left order.              |
|                                   |                                   |
|                                   | **Bitwise-not (\~):** This        |
|                                   | inverts each bit of its operand.  |
|                                   | As 64-bit signed integers are     |
|                                   | used, a positive input value will |
|                                   | always give a negative result and |
|                                   | vice versa. For example, `~0xf0f` |
|                                   | evaluates to -0xf10 (-3856),      |
|                                   | which is binary equivalent to     |
|                                   | 0xfffffffffffff0f0. If an         |
|                                   | unsigned 32-bit value is          |
|                                   | intended, the result can be       |
|                                   | truncated with                    |
|                                   | *`result`*` & 0xffffffff`. If the |
|                                   | operand is a floating point       |
|                                   | value, a                          |
|                                   | [Ty                               |
|                                   | peError](lib/Error.htm#TypeError) |
|                                   | is thrown.                        |
|                                   |                                   |
|                                   | **Reference (&):** Creates a      |
|                                   | VarRef, which is a value          |
|                                   | representing a reference to a     |
|                                   | variable. A VarRef can then be    |
|                                   | used to indirectly access the     |
|                                   | target variable. For example,     |
|                                   | `ref := &target` followed by      |
|                                   | `%ref% := 1` would assign the     |
|                                   | value 1 to *target*. The VarRef   |
|                                   | would typically be passed to a    |
|                                   | function, but could be stored in  |
|                                   | an array or property. See also:   |
|                                   | [Dereference](#deref),            |
|                                   | [ByRef](Functions.htm#ByRef).     |
|                                   |                                   |
|                                   | Taking a reference to a built-in  |
|                                   | variable such as                  |
|                                   | [                                 |
|                                   | A_Clipboard](lib/A_Clipboard.htm) |
|                                   | is currently not supported,       |
|                                   | except when being passed directly |
|                                   | to an *OutputVar* parameter of a  |
|                                   | built-in function.                |
+-----------------------------------+-----------------------------------+
| \*\                               | **Multiply (\*):** The result is  |
| /\                                | an integer if both inputs are     |
| //                                | integers; otherwise, it is a      |
|                                   | floating point number.            |
|                                   |                                   |
|                                   | **Other uses:** The asterisk (\*) |
|                                   | symbol is also used in [variadic  |
|                                   | function                          |
|                                   | ca                                |
|                                   | lls](Functions.htm#VariadicCall). |
|                                   |                                   |
|                                   | **True divide (/):** True         |
|                                   | division yields a floating point  |
|                                   | result even when both inputs are  |
|                                   | integers. For example, `3/2`      |
|                                   | yields 1.5 rather than 1, and     |
|                                   | `4/2` yields 2.0 rather than 2.   |
|                                   |                                   |
|                                   | **Integer divide (//):** The      |
|                                   | double-slash operator uses        |
|                                   | high-performance integer          |
|                                   | division. For example, `5//3` is  |
|                                   | 1 and `5//-3` is -1. If either of |
|                                   | the inputs is in floating point   |
|                                   | format, a                         |
|                                   | [Ty                               |
|                                   | peError](lib/Error.htm#TypeError) |
|                                   | is thrown. For modulo, see        |
|                                   | [Mod](lib/Math.htm#Mod).          |
|                                   |                                   |
|                                   | The [\*= and /=                   |
|                                   | operators](#AssignOp) are a       |
|                                   | shorthand way to multiply or      |
|                                   | divide the value in a variable by |
|                                   | another value. For example,       |
|                                   | `Var*=2` produces the same result |
|                                   | as `Var:=Var*2` (though the       |
|                                   | former performs better).          |
|                                   |                                   |
|                                   | Division by zero causes a         |
|                                   | [ZeroDivisionError]               |
|                                   | (lib/Error.htm#ZeroDivisionError) |
|                                   | to be thrown.                     |
+-----------------------------------+-----------------------------------+
| \+\                               | **Add (+)** and **subtract (-)**. |
| -                                 | On a related note, the [+= and -= |
|                                   | operators](#AssignOp) are a       |
|                                   | shorthand way to increment or     |
|                                   | decrement a variable. For         |
|                                   | example, `Var+=2` produces the    |
|                                   | same result as `Var:=Var+2`       |
|                                   | (though the former performs       |
|                                   | better). Similarly, a variable    |
|                                   | can be increased or decreased by  |
|                                   | 1 by using [Var++, Var\--, ++Var, |
|                                   | or \--Var](#IncDec).              |
|                                   |                                   |
|                                   | **Other uses:** If the + or -     |
|                                   | symbol is not preceded by a value |
|                                   | (or a sub-expression which yields |
|                                   | a value), it is interpreted as a  |
|                                   | [unary operator](#unary) instead. |
+-----------------------------------+-----------------------------------+
| \<\<\                             | **Bit shift left (\<\<)**.        |
| \>\>\                             | Example usage:                    |
| \>\>\>                            | `Value1 << Value2`. This is       |
|                                   | equivalent to multiplying         |
|                                   | *Value1* by \"2 to the *Value2*th |
|                                   | power\".                          |
|                                   |                                   |
|                                   | **Arithmetic bit shift right      |
|                                   | (\>\>)**. Example usage:          |
|                                   | `Value1 >> Value2`. This is       |
|                                   | equivalent to dividing *Value1*   |
|                                   | by \"2 to the *Value2*th power\"  |
|                                   | and rounding the result to the    |
|                                   | nearest integer leftward on the   |
|                                   | number line; for example, `-3>>1` |
|                                   | is -2.                            |
|                                   |                                   |
|                                   | **Logical bit shift right         |
|                                   | (\>\>\>)**. Example usage:        |
|                                   | `Value1 >>> Value2`. Unlike       |
|                                   | arithmetic bit shift right, this  |
|                                   | does not preserve the sign of the |
|                                   | number. For example, -1 has the   |
|                                   | same bit representation as the    |
|                                   | unsigned 64-bit integer           |
|                                   | 0xffffffffffffffff, therefore     |
|                                   | `-1 >>> 1` is 0x7fffffffffffffff. |
|                                   |                                   |
|                                   | The following applies to all      |
|                                   | three operators:                  |
|                                   |                                   |
|                                   | -   If either of the inputs is a  |
|                                   |     floating-point number, a      |
|                                   |     [Ty                           |
|                                   | peError](lib/Error.htm#TypeError) |
|                                   |     is thrown.                    |
|                                   | -   A 64-bit operation is         |
|                                   |     performed and the result is a |
|                                   |     64-bit signed integer.        |
|                                   | -   If *Value2* is less than 0 or |
|                                   |     greater than 63, an exception |
|                                   |     is thrown.                    |
+-----------------------------------+-----------------------------------+
| &\                                | **Bitwise-and (&)**,              |
| \^\                               | **bitwise-exclusive-or (\^)**,    |
| \|                                | and **bitwise-or (\|)**. Of the   |
|                                   | three, **&** has the highest      |
|                                   | precedence and **\|** has the     |
|                                   | lowest.                           |
|                                   |                                   |
|                                   | The following applies to all      |
|                                   | three operators:                  |
|                                   |                                   |
|                                   | -   If either of the inputs is a  |
|                                   |     floating-point number, a      |
|                                   |     [Ty                           |
|                                   | peError](lib/Error.htm#TypeError) |
|                                   |     is thrown.                    |
|                                   | -   A 64-bit operation is         |
|                                   |     performed and the result is a |
|                                   |     64-bit signed integer.        |
|                                   |                                   |
|                                   | Related: [Bitwise-not             |
|                                   | (\~)](#unary)                     |
+-----------------------------------+-----------------------------------+
| .                                 | **Concatenate**. A period (dot)   |
|                                   | with at least one space or tab on |
|                                   | each side is used to combine two  |
|                                   | items into a single string. You   |
|                                   | may also omit the period to       |
|                                   | achieve the same result (except   |
|                                   | where ambiguous such as           |
|                                   | `x `**`-`**`y`, or when the item  |
|                                   | on the right side has a leading   |
|                                   | ++ or \--). When the dot is       |
|                                   | omitted, there must be at least   |
|                                   | one space or tab between the      |
|                                   | items to be merged.               |
|                                   |                                   |
|                                   |     Var := "The color is          |
|                                   | " . FoundColor  ; Explicit concat |
|                                   |     Var := "The color             |
|                                   |  is " FoundColor    ; Auto-concat |
|                                   |                                   |
|                                   | Sub-expressions can also be       |
|                                   | concatenated. For example:        |
|                                   | `Var := "The net price is " `**`. |
|                                   | `**` Price * (1 - Discount/100)`. |
|                                   |                                   |
|                                   | A line that begins with a period  |
|                                   | (or any other operator) is        |
|                                   | automatically [appended           |
|                                   | to](Scripts.htm#continuation) the |
|                                   | line above it.                    |
|                                   |                                   |
|                                   | The entire                        |
|                                   | [length](lib/StrLen.htm) of each  |
|                                   | input is used, even if it         |
|                                   | includes binary zero. For         |
|                                   | example,                          |
|                                   | `Chr                              |
|                                   | (0x2010) Chr(0x0000) Chr(0x4030)` |
|                                   | produces the following string of  |
|                                   | bytes (due to UTF-16-LE           |
|                                   | encoding): 0x10, 0x20, 0, 0,      |
|                                   | 0x30, 0x40. The result has an     |
|                                   | additional null-terminator        |
|                                   | (binary zero) which is not        |
|                                   | included in the length.           |
|                                   |                                   |
|                                   | **Other uses:** If there is no    |
|                                   | space or tab to the right of a    |
|                                   | period (dot), it is interpreted   |
|                                   | as either a literal               |
|                                   | [floating-point number](#numbers) |
|                                   | or [member access](#objdot). For  |
|                                   | example, `1.1` and `(.5)` are     |
|                                   | numbers, `A_Args.Has(3)` is a     |
|                                   | method call and `A_Args.Length`   |
|                                   | is a property access.             |
+-----------------------------------+-----------------------------------+
| \~=                               | Shorthand for                     |
|                                   | [RegExMatch](lib/RegExMatch.htm). |
|                                   | For example, the result of        |
|                                   | `"abc123" ~= "\d"` is 4 (the      |
|                                   | position of the first numeric     |
|                                   | character).                       |
+-----------------------------------+-----------------------------------+
| \>   \<\                          | **Greater (\>)**, **less (\<)**,  |
| \>= \<=                           | **greater-or-equal (\>=)**, and   |
|                                   | **less-or-equal (\<=)**. The      |
|                                   | inputs are compared numerically.  |
|                                   | A                                 |
|                                   | [Ty                               |
|                                   | peError](lib/Error.htm#TypeError) |
|                                   | is thrown if either of the inputs |
|                                   | is not a number or a numeric      |
|                                   | string.                           |
+-----------------------------------+-----------------------------------+
| =\                                | **Case-insensitive equal (=) /    |
| ==\                               | not-equal (!=)** and              |
| !=\                               | **case-sensitive equal (==) /     |
| !==                               | not-equal (!==)**. The **==**     |
|                                   | operator behaves identically to   |
|                                   | **=** except when either of the   |
|                                   | inputs is not numeric (or both    |
|                                   | are strings), in which case       |
|                                   | **==** is always case-sensitive   |
|                                   | and **=** is always               |
|                                   | case-insensitive. The **!=** and  |
|                                   | **!==** behave identically to     |
|                                   | their counterparts without **!**, |
|                                   | except that the result is         |
|                                   | inverted.                         |
|                                   |                                   |
|                                   | The **==** and **!==** operators  |
|                                   | can be used to compare strings    |
|                                   | which contain binary zero. All    |
|                                   | other comparison operators except |
|                                   | **\~=** compare only up to the    |
|                                   | first binary zero.                |
|                                   |                                   |
|                                   | For case-insensitive comparisons, |
|                                   | only the ASCII letters A-Z are    |
|                                   | considered equivalent to their    |
|                                   | lowercase counterparts. To        |
|                                   | instead compare according to the  |
|                                   | rules of the current user\'s      |
|                                   | locale, use                       |
|                                   | [StrCompare](lib/StrCompare.htm)  |
|                                   | and specify \"Locale\" for the    |
|                                   | *CaseSense* parameter.            |
+-----------------------------------+-----------------------------------+
| IS\                               | *`Value`*` `**`is`**` `*`Class`*  |
| IN\                               | yields 1 (true) if *Value* is an  |
| CONTAINS                          | instance of *Class*, otherwise 0  |
|                                   | (false). *Class* must be an       |
|                                   | [Object](lib/Object.htm) with an  |
|                                   | own                               |
|                                   | [Pr                               |
|                                   | ototype](lib/Class.htm#Prototype) |
|                                   | property, but typically the       |
|                                   | property is defined implicitly by |
|                                   | a class definition. This          |
|                                   | operation is generally equivalent |
|                                   | to                                |
|                                   | `HasBase(`*`V                     |
|                                   | alue`*`, `*`Class`*`.Prototype)`. |
|                                   |                                   |
|                                   | **`in`{#in}** and                 |
|                                   | **`contains`{#contains}** are     |
|                                   | reserved for future use.          |
+-----------------------------------+-----------------------------------+
| NOT                               | **Logical-NOT**. Except for its   |
|                                   | lower precedence, this is the     |
|                                   | same as the **!** operator. For   |
|                                   | example, `not (x = 3 or y = 3)`   |
|                                   | is the same as                    |
|                                   | **`!`**`(x = 3 or y = 3)`.        |
+-----------------------------------+-----------------------------------+
| AND\                              | Both of these are                 |
| &&                                | **logical-AND**. For example:     |
|                                   | `x > 3 and x < 10`.               |
|                                   |                                   |
|                                   | In an expression where all        |
|                                   | operands are true, the            |
|                                   | [last]{.underline} operand is     |
|                                   | returned. Otherwise, the          |
|                                   | [first]{.underline} operand that  |
|                                   | is false is returned. In other    |
|                                   | words, the result is true only if |
|                                   | all operands are true. Boolean    |
|                                   | expressions are subject to        |
|                                   | [short-circuit                    |
|                                   | evalua                            |
|                                   | tion](Functions.htm#ShortCircuit) |
|                                   | (from left to right) to improve   |
|                                   | performance.                      |
|                                   |                                   |
|                                   | In the following example, all     |
|                                   | operands are true and will be     |
|                                   | evaluated:                        |
|                                   |                                   |
|                                   |     A := 1, B := {                |
|                                   | }, C := 20, D := true, E := "str" |
|                                   |     MsgBox(A && B &               |
|                                   | & C && D && E) ; Shows "str" (E). |
|                                   |                                   |
|                                   | In the following example, only    |
|                                   | the first two operands will be    |
|                                   | evaluated because B is false. The |
|                                   | rest is ignored, i.e. C is not    |
|                                   | incremented either:               |
|                                   |                                   |
|                                   |     A := 1, B := "                |
|                                   | ", C := 0, D := false, E := "str" |
|                                   |     MsgBox(A && B                 |
|                                   | && ++C && D && E) ; Shows "" (B). |
|                                   |                                   |
|                                   | A line that begins with `AND` or  |
|                                   | `&&` (or any other operator) is   |
|                                   | automatically [appended           |
|                                   | to](Scripts.htm#continuation) the |
|                                   | line above it.                    |
+-----------------------------------+-----------------------------------+
| OR\                               | Both of these are **logical-OR**. |
| \|\|                              | For example: `x <= 3 or x >= 10`. |
|                                   |                                   |
|                                   | In an expression where at least   |
|                                   | one operand is true, the          |
|                                   | [first]{.underline} operand that  |
|                                   | is true is returned. Otherwise,   |
|                                   | the [last]{.underline} operand    |
|                                   | that is false is returned. In     |
|                                   | other words, if at least one      |
|                                   | operand is true, the result is    |
|                                   | true. Boolean expressions are     |
|                                   | subject to [short-circuit         |
|                                   | evalua                            |
|                                   | tion](Functions.htm#ShortCircuit) |
|                                   | (from left to right) to improve   |
|                                   | performance.                      |
|                                   |                                   |
|                                   | In the following example, at      |
|                                   | least one operand is true. All    |
|                                   | operands up to D will be          |
|                                   | evaluated. E is ignored and will  |
|                                   | never be incremented:             |
|                                   |                                   |
|                                   |     A := "", B := f               |
|                                   | alse, C := 0, D := "str", E := 20 |
|                                   |     MsgBox(A || B ||              |
|                                   | C || D || ++E) ; Shows "str" (D). |
|                                   |                                   |
|                                   | In the following example, all     |
|                                   | operands are false and will be    |
|                                   | evaluated:                        |
|                                   |                                   |
|                                   |     A := "", B := false, C := 0   |
|                                   |     Msg                           |
|                                   | Box(A || B || C) ; Shows "0" (C). |
|                                   |                                   |
|                                   | A line that begins with `OR` or   |
|                                   | `||` (or any other operator) is   |
|                                   | automatically [appended           |
|                                   | to](Scripts.htm#continuation) the |
|                                   | line above it.                    |
+-----------------------------------+-----------------------------------+
| ??                                | **Or maybe**, otherwise known as  |
|                                   | the coalescing operator. If the   |
|                                   | left operand (which must be a     |
|                                   | variable) has a value, it becomes |
|                                   | the result and the right branch   |
|                                   | is skipped. Otherwise, the right  |
|                                   | operand becomes the result. In    |
|                                   | other words, `A ?? B` behaves     |
|                                   | like `A || B` ([logical-OR](#or)) |
|                                   | except that the condition is      |
|                                   | `IsSet(A)`.                       |
|                                   |                                   |
|                                   | This is typically used to provide |
|                                   | a default value when it is known  |
|                                   | that a variable or optional       |
|                                   | parameter might not already have  |
|                                   | a value. For example:             |
|                                   |                                   |
|                                   |                                   |
|                                   |   MsgBox MyVar ?? "Default value" |
|                                   |                                   |
|                                   | Since the variable is expected to |
|                                   | sometimes be                      |
|                                   | [uninitialized](Conce             |
|                                   | pts.htm#uninitialized-variables), |
|                                   | no error is thrown in that case.  |
|                                   | Unlike `IsSet(A) ? A : B`, a      |
|                                   | [VarUnset                         |
|                                   | warning](lib/_Warn.htm#VarUnset)  |
|                                   | may still be shown at load-time   |
|                                   | if there are other references to  |
|                                   | the variable but no assignments.  |
+-----------------------------------+-----------------------------------+
| ?:                                | **Ternary operator**. This        |
|                                   | operator is a shorthand           |
|                                   | replacement for the [if-else      |
|                                   | statement](lib/If.htm). It        |
|                                   | evaluates the condition on its    |
|                                   | left side to determine which of   |
|                                   | its two branches should become    |
|                                   | its final result. For example,    |
|                                   | `var := x>y ? 2 : 3` stores 2 in  |
|                                   | *Var* if x is greater than y;     |
|                                   | otherwise it stores 3. To enhance |
|                                   | performance, only the winning     |
|                                   | branch is evaluated (see          |
|                                   | [short-circuit                    |
|                                   | evaluati                          |
|                                   | on](Functions.htm#ShortCircuit)). |
|                                   |                                   |
|                                   | See also: [maybe                  |
|                                   | (*var*?)](#maybe), [or-maybe      |
|                                   | (??)](#or-maybe)                  |
|                                   |                                   |
|                                   | **Note:** When used at the        |
|                                   | beginning of a line, the ternary  |
|                                   | condition should usually be       |
|                                   | enclosed in parentheses to reduce |
|                                   | ambiguity with other types of     |
|                                   | statements. For details, see      |
|                                   | [Expression                       |
|                                   | Statements](Lan                   |
|                                   | guage.htm#expression-statements). |
+-----------------------------------+-----------------------------------+
| :=\                               | **Assign**. Performs an operation |
| +=\                               | on the contents of a variable and |
| -=\                               | stores the result back in the     |
| \*=\                              | same variable. The simplest       |
| /=\                               | assignment operator is            |
| //=\                              | colon-equal (:=), which stores    |
| .=\                               | the result of an expression in a  |
| \|=\                              | variable. For a description of    |
| &=\                               | what the other operators do, see  |
| \^=\                              | their related entries in this     |
| \>\>=\                            | table. For example, `Var //= 2`   |
| \<\<=\                            | performs [integer                 |
| \>\>\>=                           | division](#IntegerDivide) to      |
|                                   | divide *Var* by 2, then stores    |
|                                   | the result back in *Var*.         |
|                                   | Similarly, `Var `**`.=`**` "abc"` |
|                                   | is a shorthand way of writing     |
|                                   | `Var := Var `**`.`**` "abc"`.     |
|                                   |                                   |
|                                   | Unlike most other operators,      |
|                                   | assignments are evaluated from    |
|                                   | right to left. Consequently, a    |
|                                   | line such as `Var1 := Var2 := 0`  |
|                                   | first assigns 0 to *Var2* then    |
|                                   | assigns *Var2* to *Var1*.         |
|                                   |                                   |
|                                   | If an assignment is used as the   |
|                                   | input for some other operator,    |
|                                   | its value is the variable itself. |
|                                   | For example, the expression       |
|                                   | `(Var+=2) > 50` is true if the    |
|                                   | newly-increased value in *Var* is |
|                                   | greater than 50. It is also valid |
|                                   | to combine an assignment with the |
|                                   | [reference operator](#ref), as in |
|                                   | `&(Var := "initial value")`.      |
|                                   |                                   |
|                                   | The precedence of the assignment  |
|                                   | operators is automatically raised |
|                                   | when it would avoid a syntax      |
|                                   | error or provide more intuitive   |
|                                   | behavior. For example: `not x:=y` |
|                                   | is evaluated as `not (x:=y)`.     |
|                                   | Also,                             |
|                                   | `x==y && z:=1`{.no-highlight} is  |
|                                   | evaluated as                      |
|                                   | `x==y && (z:=1)`{.no-highlight},  |
|                                   | which                             |
|                                   | [short-circ                       |
|                                   | uits](Functions.htm#ShortCircuit) |
|                                   | when x doesn\'t equal y.          |
|                                   | Similarly, `++Var := X` is        |
|                                   | evaluated as `++(Var := X)`; and  |
|                                   | `Z>0 ? X:=2 : Y:=2` is evaluated  |
|                                   | as `Z>0 ? (X:=2) : (Y:=2)`.       |
|                                   |                                   |
|                                   | The target variable can be        |
|                                   | *un-set* by combining a direct    |
|                                   | assignment (`:=`) with the        |
|                                   | `unset` keyword or the [maybe     |
|                                   | (*var*?)](#maybe) operator. For   |
|                                   | example: `Var := unset`,          |
|                                   | `Var1 := (Var2?)`.                |
|                                   |                                   |
|                                   | An assignment can also target a   |
|                                   | property of an object, such as    |
|                                   | `myArray.Length += n` or          |
|                                   | `myArray[i] .= t`. When assigning |
|                                   | to a property, the result of the  |
|                                   | sub-expression is the value being |
|                                   | assigned, not a variable          |
|                                   | reference.                        |
+-----------------------------------+-----------------------------------+
| **() =\>** *expr*                 | **Fat arrow function**. Defines a |
|                                   | simple [function](Functions.htm)  |
|                                   | and returns a                     |
|                                   | [Func](lib/Func.htm) or           |
|                                   | [Closure](Functions.htm#closures) |
|                                   | object. Write the function\'s     |
|                                   | [parameter                        |
|                                   | list](Functions.htm#param)        |
|                                   | (optionally preceded by a         |
|                                   | function name) to the left of the |
|                                   | operator. When the function is    |
|                                   | called (via the returned          |
|                                   | reference), it evaluates the      |
|                                   | sub-expression *expr* and returns |
|                                   | the result.                       |
|                                   |                                   |
|                                   | The following two examples are    |
|                                   | equivalent:                       |
|                                   |                                   |
|                                   |     sumfn := Sum(a, b) => a + b   |
|                                   |                                   |
|                                   |     Sum(a, b) {                   |
|                                   |         return a + b              |
|                                   |     }                             |
|                                   |     sumfn := Sum                  |
|                                   |                                   |
|                                   | In both cases, the function is    |
|                                   | defined **unconditionally** at    |
|                                   | the moment the script launches,   |
|                                   | but the function reference is     |
|                                   | stored in *sumfn* only if and     |
|                                   | when the assignment is evaluated. |
|                                   |                                   |
|                                   | If the function name is omitted   |
|                                   | and the parameter list consists   |
|                                   | of only a single parameter name,  |
|                                   | the parentheses can be omitted.   |
|                                   | The example below defines an      |
|                                   | anonymous function with one       |
|                                   | parameter `a` and stores its      |
|                                   | reference in the variable         |
|                                   | `double`:                         |
|                                   |                                   |
|                                   |     double := a => a * 2          |
|                                   |                                   |
|                                   | Variable references in *expr* are |
|                                   | resolved in the same way as in    |
|                                   | the equivalent full function      |
|                                   | definition. For instance, *expr*  |
|                                   | may refer to an outer function\'s |
|                                   | local variables (as in any        |
|                                   | [nested                           |
|                                   | function](Functions.htm#nested)), |
|                                   | in which case a new               |
|                                   | [closure](Functions.htm#closures) |
|                                   | is created and returned each time |
|                                   | the fat arrow expression is       |
|                                   | evaluated. The function is always |
|                                   | [assume-l                         |
|                                   | ocal](Functions.htm#AssumeLocal), |
|                                   | since declarations cannot be      |
|                                   | used.                             |
|                                   |                                   |
|                                   | Specifying a name for the         |
|                                   | function allows it to be called   |
|                                   | recursively or by other nested    |
|                                   | functions without storing a       |
|                                   | reference to the                  |
|                                   | [closure](Functions.htm#closures) |
|                                   | within itself (thereby creating a |
|                                   | problematic [circular             |
|                                   | reference](O                      |
|                                   | bjects.htm#Circular_References)). |
|                                   | It can also be helpful for        |
|                                   | debugging, such as with           |
|                                   | [Func.Name](lib/Func.htm#Name) or |
|                                   | when displayed on the debugger\'s |
|                                   | call stack.                       |
|                                   |                                   |
|                                   | Fat arrow syntax can also be used |
|                                   | to define shorthand               |
|                                   | [properties](Objects.h            |
|                                   | tm#Custom_Classes_property_short) |
|                                   | and                               |
|                                   | [methods](Ob                      |
|                                   | jects.htm#Custom_Classes_method). |
+-----------------------------------+-----------------------------------+
| ,                                 | **Comma (multi-statement)**.      |
|                                   | Commas may be used to write       |
|                                   | multiple sub-expressions on a     |
|                                   | single line. This is most         |
|                                   | commonly used to group together   |
|                                   | multiple assignments or function  |
|                                   | calls. For example:               |
|                                   | `x:=1`**`,`**`                    |
|                                   | y+=2`**`,`**` ++index, MyFunc()`. |
|                                   | Such statements are executed in   |
|                                   | order from left to right.         |
|                                   |                                   |
|                                   | **Note:** A line that begins with |
|                                   | a comma (or any other operator)   |
|                                   | is automatically [appended        |
|                                   | to](Scripts.htm#continuation) the |
|                                   | line above it.                    |
|                                   |                                   |
|                                   | Comma is also used to delimit the |
|                                   | parameters of a function call or  |
|                                   | control flow statement. To        |
|                                   | include a multi-statement         |
|                                   | expression in a parameter list,   |
|                                   | enclose it in an extra set of     |
|                                   | parentheses. For example,         |
|                                   | `MyFn((x, y))` evaluates both x   |
|                                   | and y but passes y as the first   |
|                                   | and only parameter of MyFn.       |
+-----------------------------------+-----------------------------------+

The following types of sub-expressions override precedence/order of
evaluation:

+-----------------------------------+-----------------------------------+
| Expression                        | Description                       |
+===================================+===================================+
| **(***expression***)**            | Any sub-expression enclosed in    |
|                                   | parentheses. For example,         |
|                                   | `(3 + 2) * 2` forces `3 + 2` to   |
|                                   | be evaluated first.               |
|                                   |                                   |
|                                   | For a multi-statement expression, |
|                                   | the result of the                 |
|                                   | [last]{.underline} statement is   |
|                                   | returned. For example,            |
|                                   | `(a := 1, b := 2, c := 3)`        |
|                                   | returns 3.                        |
+-----------------------------------+-----------------------------------+
| Mod**()**\                        | **Function call**. There must be  |
| Round**()**\                      | no space between the function     |
| Abs**()**                         | name or expression and the open   |
|                                   | parenthesis which begins the      |
|                                   | parameter list. For details, see  |
|                                   | [Function                         |
|                                   | Cal                               |
|                                   | ls](Language.htm#function-calls). |
|                                   |                                   |
|                                   | *(expression)* is not necessarily |
|                                   | required to be enclosed in        |
|                                   | parentheses, but doing so may     |
|                                   | eliminate ambiguity. For example, |
|                                   | `(x.y)()` retrieves a function    |
|                                   | from a property and then calls it |
|                                   | with no parameters, whereas       |
|                                   | `x.y()` would implicitly pass `x` |
|                                   | as the first parameter.           |
+-----------------------------------+-----------------------------------+
| *(expression)***()**              |                                   |
+-----------------------------------+-----------------------------------+
| Fn(***Params*\***)                | [Variadic function                |
|                                   | c                                 |
|                                   | all](Functions.htm#VariadicCall). |
|                                   | *Params* is an enumerable object  |
|                                   | (an object with an                |
|                                   | [\_\_Enum](Objects.htm#__Enum)    |
|                                   | method), such as an               |
|                                   | [Array](lib/Array.htm) containing |
|                                   | parameter values.                 |
+-----------------------------------+-----------------------------------+
| **x\[y\]\                         | **Item access**. Get or set the   |
| \[a, b, c\]**                     | [\_\_Item](Objects.htm#__Item)    |
|                                   | property (or default property) of |
|                                   | object *x* with the parameter *y* |
|                                   | (or multiple parameters in place  |
|                                   | of *y*). This typically           |
|                                   | corresponds to an array element   |
|                                   | or item within a collection,      |
|                                   | where *y* is the item\'s index or |
|                                   | key. The item can be assigned a   |
|                                   | value by using any [assignment    |
|                                   | operator](#AssignOp) immediately  |
|                                   | after the closing bracket. For    |
|                                   | example, `x[y] := z`.             |
|                                   |                                   |
|                                   | **Array literal**. If the         |
|                                   | open-bracket is not preceded by a |
|                                   | value (or a sub-expression which  |
|                                   | yields a value), it is            |
|                                   | interpreted as the beginning of   |
|                                   | an array literal. For example,    |
|                                   | `[a, b, c]` is equivalent to      |
|                                   | `Array(a, b, c)` (a, b and c are  |
|                                   | variables).                       |
|                                   |                                   |
|                                   | See                               |
|                                   | [Arrays]                          |
|                                   | (Objects.htm#Usage_Simple_Arrays) |
|                                   | and                               |
|                                   | [Maps](Obje                       |
|                                   | cts.htm#Usage_Associative_Arrays) |
|                                   | for common usage.                 |
+-----------------------------------+-----------------------------------+
| **{a: b, c: d}**                  | **Object literal**. Create an     |
|                                   | [Object](lib/Object.htm). Each    |
|                                   | pair consists of a literal        |
|                                   | property name `a` and a property  |
|                                   | value expression `b`. For         |
|                                   | example, `x := {a: b}` is         |
|                                   | equivalent to                     |
|                                   | `x := Object(), x.a := b`.        |
|                                   | [Base](lib/Object.htm#Base) may   |
|                                   | be set within the object literal, |
|                                   | but all other properties are set  |
|                                   | as *own value properties*,        |
|                                   | potentially overriding properties |
|                                   | inherited from the base object.   |
|                                   |                                   |
|                                   | To use a dynamic property name,   |
|                                   | enclose the sub-expression in     |
|                                   | percent signs. For example:       |
|                                   | `{%nameVar%: valueVar}`.          |
+-----------------------------------+-----------------------------------+

## Built-in Variables {#BuiltIn}

The variables below are built into the program and can be referenced by
any script.

See [Built-in Variables](Concepts.htm#built-in-variables) for general
information.

### Table of Contents {#BuiltIn_TOC}

-   Special Characters: [A_Space](#Space), [A_Tab](#Tab)
-   Script Properties: [command line parameters](#Args),
    [A_WorkingDir](#WorkingDir), [A_ScriptDir](#ScriptDir),
    [A_ScriptName](#ScriptName), [(\...more\...)](#prop)
-   Date and Time: [A_YYYY](#YYYY), [A_MM](#MM), [A_DD](#DD),
    [A_Hour](#Hour), [A_Min](#Min), [A_Sec](#Sec),
    [(\...more\...)](#date)
-   Script Settings: [A_IsSuspended](#IsSuspended),
    [A_ListLines](#ListLines), [A_TitleMatchMode](#TitleMatchMode),
    [(\...more\...)](#settings)
-   User Idle Time: [A_TimeIdle](#TimeIdle),
    [A_TimeIdlePhysical](#TimeIdlePhysical),
    [A_TimeIdleKeyboard](#TimeIdleKeyboard),
    [A_TimeIdleMouse](#TimeIdleMouse)
-   Hotkeys, Hotstrings, and Custom Menu Items:
    [A_ThisHotkey](#ThisHotkey), [A_EndChar](#EndChar),
    [(\...more\...)](#h)
-   Operating System and User Info: [A_OSVersion](#OSVersion),
    [A_ScreenWidth](#Screen), [A_ScreenHeight](#Screen),
    [(\...more\...)](#os)
-   Misc: [A_Clipboard](#Clipboard), [A_Cursor](#Cursor),
    [A_EventInfo](#EventInfo), [(\...more\...)](#misc)
-   Loop: [A_Index](#Index), [(\...more\...)](#loop)

### Special Characters {#Special_Characters}

  Variable   Description
  ---------- ------------------------------------
  A_Space    Contains a single space character.
  A_Tab      Contains a single tab character.

### Script Properties {#prop}

+-----------------------------------+-----------------------------------+
| Variable                          | Description                       |
+===================================+===================================+
| A_Args                            | Contains an                       |
|                                   | [array]                           |
|                                   | (Objects.htm#Usage_Simple_Arrays) |
|                                   | of command line parameters. For   |
|                                   | details, see [Passing Command     |
|                                   | Line Parameters to a              |
|                                   | Script](Scripts.htm#cmd).         |
+-----------------------------------+-----------------------------------+
| A_WorkingDir                      | Can be used to get or set the     |
|                                   | script\'s current working         |
|                                   | directory, which is where files   |
|                                   | will be accessed by default. The  |
|                                   | final backslash is not included   |
|                                   | unless it is the root directory.  |
|                                   | Two examples: C:\\ and C:\\My     |
|                                   | Documents.                        |
|                                   |                                   |
|                                   | [SetW                             |
|                                   | orkingDir](lib/SetWorkingDir.htm) |
|                                   | can also be used to change the    |
|                                   | working directory.                |
|                                   |                                   |
|                                   | The script\'s working directory   |
|                                   | defaults to                       |
|                                   | [A_ScriptDir](#ScriptDir),        |
|                                   | regardless of how the script was  |
|                                   | launched.                         |
+-----------------------------------+-----------------------------------+
| A_InitialWorkingDir               | The script\'s initial working     |
|                                   | directory, which is determined by |
|                                   | how it was launched. For example, |
|                                   | if it was run via shortcut \--    |
|                                   | such as on the Start Menu \-- its |
|                                   | initial working directory is      |
|                                   | determined by the \"Start in\"    |
|                                   | field within the shortcut\'s      |
|                                   | properties.                       |
+-----------------------------------+-----------------------------------+
| A_ScriptDir                       | The full path of the directory    |
|                                   | where the current script is       |
|                                   | located. The final backslash is   |
|                                   | omitted (even for root            |
|                                   | directories).                     |
|                                   |                                   |
|                                   | If the script text is [read from  |
|                                   | stdin](Scripts.htm#stdin) rather  |
|                                   | than from file, this variable     |
|                                   | contains the [initial working     |
|                                   | directory](#InitialWorkingDir).   |
+-----------------------------------+-----------------------------------+
| A_ScriptName                      | Can be used to get or set the     |
|                                   | default title for                 |
|                                   | [MsgBox](lib/MsgBox.htm),         |
|                                   | [InputBox](lib/InputBox.htm),     |
|                                   | [FileSelect](lib/FileSelect.htm), |
|                                   | [DirSelect](lib/DirSelect.htm)    |
|                                   | and [Gui](lib/Gui.htm). If not    |
|                                   | set by the script, it defaults to |
|                                   | the file name of the current      |
|                                   | script, without its path, e.g.    |
|                                   | MyScript.ahk.                     |
|                                   |                                   |
|                                   | If the script text is [read from  |
|                                   | stdin](Scripts.htm#stdin) rather  |
|                                   | than from file, this variable     |
|                                   | contains an asterisk (\*).        |
|                                   |                                   |
|                                   | If the script is                  |
|                                   | [compiled](Scripts.htm#ahk2exe)   |
|                                   | or                                |
|                                   | [embedde                          |
|                                   | d](Program.htm#embedded-scripts), |
|                                   | this is the name of the current   |
|                                   | executable file.                  |
+-----------------------------------+-----------------------------------+
| A_ScriptFullPath                  | The full path of the current      |
|                                   | script, e.g. C:\\Scripts\\My      |
|                                   | Script.ahk                        |
|                                   |                                   |
|                                   | If the script text is [read from  |
|                                   | stdin](Scripts.htm#stdin) rather  |
|                                   | than from file, this variable     |
|                                   | contains an asterisk (\*).        |
|                                   |                                   |
|                                   | If the script is                  |
|                                   | [compiled](Scripts.htm#ahk2exe)   |
|                                   | or                                |
|                                   | [embedde                          |
|                                   | d](Program.htm#embedded-scripts), |
|                                   | this is the full path of the      |
|                                   | current executable file.          |
+-----------------------------------+-----------------------------------+
| A_ScriptHwnd                      | The unique ID (HWND/handle) of    |
|                                   | the script\'s hidden [main        |
|                                   | window](Program.htm#main-window). |
+-----------------------------------+-----------------------------------+
| A_LineNumber                      | The number of the currently       |
|                                   | executing line within the script  |
|                                   | (or one of its [#Include          |
|                                   | files](lib/_Include.htm)). This   |
|                                   | line number will match the one    |
|                                   | shown by                          |
|                                   | [ListLines](lib/ListLines.htm);   |
|                                   | it can be useful for error        |
|                                   | reporting such as this example:   |
|                                   | `Msg                              |
|                                   | Box "Could not write to log file  |
|                                   | (line number " A_LineNumber ")"`. |
|                                   |                                   |
|                                   | Since a [compiled                 |
|                                   | script](Scripts.htm#ahk2exe) has  |
|                                   | merged all its [#Include          |
|                                   | files](lib/_Include.htm) into one |
|                                   | big script, its line numbering    |
|                                   | may be different than when it is  |
|                                   | run in non-compiled mode.         |
+-----------------------------------+-----------------------------------+
| A_LineFile                        | The full path and name of the     |
|                                   | file to which                     |
|                                   | [A_LineNumber](#LineNumber)       |
|                                   | belongs. If the script was loaded |
|                                   | from an external file, this is    |
|                                   | the same as                       |
|                                   | [A                                |
|                                   | _ScriptFullPath](#ScriptFullPath) |
|                                   | unless the line belongs to one of |
|                                   | the script\'s [#Include           |
|                                   | files](lib/_Include.htm).         |
|                                   |                                   |
|                                   | If the script was                 |
|                                   | [compiled](Scripts.htm#ahk2exe)   |
|                                   | based on a [.bin                  |
|                                   | file](Scripts.htm#ahk2exe-base),  |
|                                   | this is the full path and name of |
|                                   | the current executable file, the  |
|                                   | same as                           |
|                                   | [A_                               |
|                                   | ScriptFullPath](#ScriptFullPath). |
|                                   |                                   |
|                                   | If the script is                  |
|                                   | [embedde                          |
|                                   | d](Program.htm#embedded-scripts), |
|                                   | A_LineFile contains an asterisk   |
|                                   | (\*) followed by the resource     |
|                                   | name; e.g. \*#1                   |
+-----------------------------------+-----------------------------------+
| A_ThisFunc                        | The name of the [user-defined     |
|                                   | function](Functions.htm) that is  |
|                                   | currently executing (blank if     |
|                                   | none); for example: MyFunction.   |
|                                   | See also: [Name property          |
|                                   | (Func)](lib/Func.htm#Name)        |
+-----------------------------------+-----------------------------------+
| A_AhkVersion                      | Contains the version of           |
|                                   | AutoHotkey that is running the    |
|                                   | script, such as 1.0.22. In the    |
|                                   | case of a [compiled               |
|                                   | script](Scripts.htm#ahk2exe), the |
|                                   | version that was originally used  |
|                                   | to compile it is reported. The    |
|                                   | formatting of the version number  |
|                                   | allows a script to check whether  |
|                                   | A_AhkVersion is greater than some |
|                                   | minimum version number with \> or |
|                                   | \>= as in this example:           |
|                                   | `i                                |
|                                   | f (A_AhkVersion >= "1.0.25.07")`. |
|                                   | See also:                         |
|                                   | [#Requires](lib/_Requires.htm)    |
|                                   | and                               |
|                                   | [VerCompare](lib/VerCompare.htm)  |
+-----------------------------------+-----------------------------------+
| A_AhkPath                         | For non-compiled or               |
|                                   | [embedd                           |
|                                   | ed](Program.htm#embedded-scripts) |
|                                   | scripts: The full path and name   |
|                                   | of the EXE file that is actually  |
|                                   | running the current script. For   |
|                                   | example: C:\\Program              |
|                                   | Files\\AutoHotkey\\AutoHotkey.exe |
|                                   |                                   |
|                                   | For [compiled                     |
|                                   | scripts](Scripts.htm#ahk2exe)     |
|                                   | based on a [.bin                  |
|                                   | file](Scripts.htm#ahk2exe-base),  |
|                                   | the value is determined by        |
|                                   | reading the installation          |
|                                   | directory from the registry and   |
|                                   | appending \"\\AutoHotkey.exe\".   |
|                                   | If AutoHotkey is not installed,   |
|                                   | the value is blank. The example   |
|                                   | below is equivalent:              |
|                                   |                                   |
|                                   |     I                             |
|                                   | nstallDir := RegRead("HKLM\SOFTWA |
|                                   | RE\AutoHotkey", "InstallDir", "") |
|                                   |     AhkPath := InstallDir ?       |
|                                   | InstallDir "\AutoHotkey.exe" : "" |
|                                   |                                   |
|                                   | For compiled scripts based on an  |
|                                   | .exe file, A_AhkPath contains the |
|                                   | full path of the compiled script. |
|                                   | This can be used in combination   |
|                                   | with                              |
|                                   | [                                 |
|                                   | /script](Scripts.htm#SlashScript) |
|                                   | to execute external scripts. To   |
|                                   | instead locate the installed copy |
|                                   | of AutoHotkey, read the registry  |
|                                   | as shown above.                   |
+-----------------------------------+-----------------------------------+
| A_IsCompiled                      | Contains 1 if the script is       |
|                                   | running as a [compiled            |
|                                   | EXE](Scripts.htm#ahk2exe) and 0   |
|                                   | (which is considered              |
|                                   | [false](#Boolean)) if it is not.  |
+-----------------------------------+-----------------------------------+

### Date and Time {#date}

+-----------------------------------+-----------------------------------+
| Variable                          | Description                       |
+===================================+===================================+
| A_YYYY                            | Current 4-digit year (e.g. 2004). |
|                                   | Synonymous with A_Year.           |
|                                   |                                   |
|                                   | **Note:** To retrieve a formatted |
|                                   | time or date appropriate for your |
|                                   | locale and language, use          |
|                                   | [`For                             |
|                                   | matTime`](lib/FormatTime.htm)`()` |
|                                   | (time and long date) or           |
|                                   | [`FormatTime`](li                 |
|                                   | b/FormatTime.htm)`(, "LongDate")` |
|                                   | (retrieves long-format date).     |
+-----------------------------------+-----------------------------------+
| A_MM                              | Current 2-digit month (01-12).    |
|                                   | Synonymous with A_Mon.            |
+-----------------------------------+-----------------------------------+
| A_DD                              | Current 2-digit day of the month  |
|                                   | (01-31). Synonymous with A_MDay.  |
+-----------------------------------+-----------------------------------+
| A_MMMM                            | Current month\'s full name in the |
|                                   | current user\'s language, e.g.    |
|                                   | July                              |
+-----------------------------------+-----------------------------------+
| A_MMM                             | Current month\'s abbreviation in  |
|                                   | the current user\'s language,     |
|                                   | e.g. Jul                          |
+-----------------------------------+-----------------------------------+
| A_DDDD                            | Current day of the week\'s full   |
|                                   | name in the current user\'s       |
|                                   | language, e.g. Sunday             |
+-----------------------------------+-----------------------------------+
| A_DDD                             | Current day of the week\'s        |
|                                   | abbreviation in the current       |
|                                   | user\'s language, e.g. Sun        |
+-----------------------------------+-----------------------------------+
| A_WDay                            | Current 1-digit day of the week   |
|                                   | (1-7). 1 is Sunday in all         |
|                                   | locales.                          |
+-----------------------------------+-----------------------------------+
| A_YDay                            | Current day of the year (1-366).  |
|                                   | The value is not zero-padded,     |
|                                   | e.g. 9 is retrieved, not 009. To  |
|                                   | retrieve a zero-padded value, use |
|                                   | the following:                    |
|                                   | [`FormatTime`](                   |
|                                   | lib/FormatTime.htm)`(, "YDay0")`. |
+-----------------------------------+-----------------------------------+
| A_YWeek                           | Current year and week number      |
|                                   | (e.g. 200453) according to ISO    |
|                                   | 8601. To separate the year from   |
|                                   | the week, use                     |
|                                   | `Year := `[`SubStr`]              |
|                                   | (lib/SubStr.htm)`(A_YWeek, 1, 4)` |
|                                   | and                               |
|                                   | `Week := `[`SubStr`               |
|                                   | ](lib/SubStr.htm)`(A_YWeek, -2)`. |
|                                   | Precise definition of A_YWeek: If |
|                                   | the week containing January 1st   |
|                                   | has four or more days in the new  |
|                                   | year, it is considered week 1.    |
|                                   | Otherwise, it is the last week of |
|                                   | the previous year, and the next   |
|                                   | week is week 1.                   |
+-----------------------------------+-----------------------------------+
| A_Hour                            | Current 2-digit hour (00-23) in   |
|                                   | 24-hour time (for example, 17 is  |
|                                   | 5pm). To retrieve 12-hour time as |
|                                   | well as an AM/PM indicator,       |
|                                   | follow this example:              |
|                                   | [`FormatTime`](lib/               |
|                                   | FormatTime.htm)`(, "h:mm:ss tt")` |
+-----------------------------------+-----------------------------------+
| A_Min                             | Current 2-digit minute (00-59).   |
+-----------------------------------+-----------------------------------+
| A_Sec                             | Current 2-digit second (00-59).   |
+-----------------------------------+-----------------------------------+
| A_MSec                            | Current 3-digit millisecond       |
|                                   | (000-999). To remove the leading  |
|                                   | zeros, follow this example:       |
|                                   | `Milliseconds := A_MSec + 0`.     |
+-----------------------------------+-----------------------------------+
| A_Now                             | The current local time in         |
|                                   | [YYYYMMDDHH24MI                   |
|                                   | SS](lib/FileSetTime.htm#YYYYMMDD) |
|                                   | format.                           |
|                                   |                                   |
|                                   | **Note:** Date and time math can  |
|                                   | be performed with                 |
|                                   | [DateAdd](lib/DateAdd.htm) and    |
|                                   | [DateDiff](lib/DateDiff.htm).     |
|                                   | Also,                             |
|                                   | [FormatTime](lib/FormatTime.htm)  |
|                                   | can format the date and/or time   |
|                                   | according to your locale or       |
|                                   | preferences.                      |
+-----------------------------------+-----------------------------------+
| A_NowUTC                          | The current Coordinated Universal |
|                                   | Time (UTC) in                     |
|                                   | [YYYYMMDDHH24MI                   |
|                                   | SS](lib/FileSetTime.htm#YYYYMMDD) |
|                                   | format. UTC is essentially the    |
|                                   | same as Greenwich Mean Time       |
|                                   | (GMT).                            |
+-----------------------------------+-----------------------------------+
| A_TickCount                       | The number of milliseconds that   |
|                                   | have elapsed since the system was |
|                                   | started, up to 49.7 days. By      |
|                                   | storing A_TickCount in a          |
|                                   | variable, elapsed time can later  |
|                                   | be measured by subtracting that   |
|                                   | variable from the latest          |
|                                   | A_TickCount value. For example:   |
|                                   |                                   |
|                                   |     StartTime := A_TickCount      |
|                                   |     Sleep 1000                    |
|                                   |     Elaps                         |
|                                   | edTime := A_TickCount - StartTime |
|                                   |     MsgBox ElapsedT               |
|                                   | ime " milliseconds have elapsed." |
|                                   |                                   |
|                                   | If you need more precision than   |
|                                   | A_TickCount\'s 10 ms, use         |
|                                   | [QueryPerformanceC                |
|                                   | ounter()](lib/DllCall.htm#ExQPC). |
+-----------------------------------+-----------------------------------+

### Script Settings {#settings}

+-----------------------------------+-----------------------------------+
| Variable                          | Description                       |
+===================================+===================================+
| A_IsSuspended                     | Contains 1 if the script is       |
|                                   | [suspended](lib/Suspend.htm),     |
|                                   | otherwise 0.                      |
+-----------------------------------+-----------------------------------+
| A_IsPaused                        | Contains 1 if the                 |
|                                   | [thread](misc/Threads.htm)        |
|                                   | immediately underneath the        |
|                                   | current thread is                 |
|                                   | [paused](lib/Pause.htm),          |
|                                   | otherwise 0.                      |
+-----------------------------------+-----------------------------------+
| A_IsCritical                      | Contains 0 if                     |
|                                   | [Critical](lib/Critical.htm) is   |
|                                   | off for the [current              |
|                                   | thread](misc/Threads.htm).        |
|                                   | Otherwise it contains an integer  |
|                                   | greater than zero, namely the     |
|                                   | [message-check                    |
|                                   | int                               |
|                                   | erval](lib/Critical.htm#Interval) |
|                                   | being used by Critical. The       |
|                                   | current state of Critical can be  |
|                                   | saved and restored via            |
|                                   | `Old_IsCritical := A_IsCritical`  |
|                                   | followed later by                 |
|                                   | `Critical Old_IsCritical`.        |
+-----------------------------------+-----------------------------------+
| A_ListLines                       | Can be used to get or set whether |
|                                   | to log lines. Possible values are |
|                                   | 0 (disabled) and 1 (enabled). For |
|                                   | details, see                      |
|                                   | [ListLines](lib/ListLines.htm).   |
+-----------------------------------+-----------------------------------+
| A_TitleMatchMode                  | Can be used to get or set the     |
|                                   | title match mode. Possible values |
|                                   | are 1, 2, 3, and RegEx. For       |
|                                   | details, see                      |
|                                   | [SetTitleMatch                    |
|                                   | Mode](lib/SetTitleMatchMode.htm). |
+-----------------------------------+-----------------------------------+
| A_TitleMatchModeSpeed             | Can be used to get or set the     |
|                                   | title match speed. Possible       |
|                                   | values are Fast and Slow. For     |
|                                   | details, see                      |
|                                   | [SetTitleMatch                    |
|                                   | Mode](lib/SetTitleMatchMode.htm). |
+-----------------------------------+-----------------------------------+
| A_DetectHiddenWindows             | Can be used to get or set whether |
|                                   | to detect hidden windows.         |
|                                   | Possible values are 0 (disabled)  |
|                                   | and 1 (enabled). For details, see |
|                                   | [DetectHiddenWindo                |
|                                   | ws](lib/DetectHiddenWindows.htm). |
+-----------------------------------+-----------------------------------+
| A_DetectHiddenText                | Can be used to get or set whether |
|                                   | to detect hidden text in a        |
|                                   | window. Possible values are 0     |
|                                   | (disabled) and 1 (enabled). For   |
|                                   | details, see                      |
|                                   | [DetectHidde                      |
|                                   | nText](lib/DetectHiddenText.htm). |
+-----------------------------------+-----------------------------------+
| A_FileEncoding                    | Can be used to get or set the     |
|                                   | default encoding for various      |
|                                   | built-in functions. For details,  |
|                                   | see                               |
|                                   | [Fil                              |
|                                   | eEncoding](lib/FileEncoding.htm). |
+-----------------------------------+-----------------------------------+
| A_SendMode                        | Can be used to get or set the     |
|                                   | send mode. Possible values are    |
|                                   | Event, Input, Play, and           |
|                                   | InputThenPlay. For details, see   |
|                                   | [SendMode](lib/SendMode.htm).     |
+-----------------------------------+-----------------------------------+
| A_SendLevel                       | Can be used to get or set the     |
|                                   | send level, an integer from 0 to  |
|                                   | 100. For details, see             |
|                                   | [SendLevel](lib/SendLevel.htm).   |
+-----------------------------------+-----------------------------------+
| A_StoreCapsLockMode               | Can be used to get or set whether |
|                                   | to restore the state of           |
|                                   | [CapsLock]{.kbd} after a          |
|                                   | [Send](lib/Send.htm). Possible    |
|                                   | values are 0 (disabled) and 1     |
|                                   | (enabled). For details, see       |
|                                   | [SetStoreCapsLockMod              |
|                                   | e](lib/SetStoreCapsLockMode.htm). |
+-----------------------------------+-----------------------------------+
| A_KeyDelay\                       | Can be used to get or set the     |
| A_KeyDuration                     | delay or duration for keystrokes, |
|                                   | in milliseconds. For details, see |
|                                   | [S                                |
|                                   | etKeyDelay](lib/SetKeyDelay.htm). |
+-----------------------------------+-----------------------------------+
| A_KeyDelayPlay\                   | Can be used to get or set the     |
| A_KeyDurationPlay                 | delay or duration for keystrokes  |
|                                   | sent via                          |
|                                   | [SendP                            |
|                                   | lay](lib/Send.htm#SendPlayDetail) |
|                                   | mode, in milliseconds. For        |
|                                   | details, see                      |
|                                   | [S                                |
|                                   | etKeyDelay](lib/SetKeyDelay.htm). |
+-----------------------------------+-----------------------------------+
| A_WinDelay                        | Can be used to get or set the     |
|                                   | delay for windowing functions, in |
|                                   | milliseconds. For details, see    |
|                                   | [S                                |
|                                   | etWinDelay](lib/SetWinDelay.htm). |
+-----------------------------------+-----------------------------------+
| A_ControlDelay                    | Can be used to get or set the     |
|                                   | delay for control-modifying       |
|                                   | functions, in milliseconds. For   |
|                                   | details, see                      |
|                                   | [SetContro                        |
|                                   | lDelay](lib/SetControlDelay.htm). |
+-----------------------------------+-----------------------------------+
| A_MenuMaskKey                     | Controls which key is used to     |
|                                   | mask Win or Alt keyup events. For |
|                                   | details, see                      |
|                                   | [A_Men                            |
|                                   | uMaskKey](lib/A_MenuMaskKey.htm). |
+-----------------------------------+-----------------------------------+
| A_MouseDelay\                     | Can be used to get or set the     |
| A_MouseDelayPlay                  | mouse delay, in milliseconds.     |
|                                   | A_MouseDelay is for the           |
|                                   | traditional SendEvent mode,       |
|                                   | whereas A_MouseDelayPlay is for   |
|                                   | [SendPl                           |
|                                   | ay](lib/Send.htm#SendPlayDetail). |
|                                   | For details, see                  |
|                                   | [SetMo                            |
|                                   | useDelay](lib/SetMouseDelay.htm). |
+-----------------------------------+-----------------------------------+
| A_DefaultMouseSpeed               | Can be used to get or set the     |
|                                   | default mouse speed, an integer   |
|                                   | from 0 (fastest) to 100           |
|                                   | (slowest). For details, see       |
|                                   | [SetDefaultMouseSpee              |
|                                   | d](lib/SetDefaultMouseSpeed.htm). |
+-----------------------------------+-----------------------------------+
| A_CoordModeToolTip\               | Can be used to get or set the     |
| A_CoordModePixel\                 | area to which coordinates are to  |
| A_CoordModeMouse\                 | be relative. Possible values are  |
| A_CoordModeCaret\                 | Screen, Window, and Client. For   |
| A_CoordModeMenu                   | details, see                      |
|                                   | [CoordMode](lib/CoordMode.htm).   |
+-----------------------------------+-----------------------------------+
| A_RegView                         | Can be used to get or set the     |
|                                   | registry view. Possible values    |
|                                   | are 32, 64 and Default. For       |
|                                   | details, see                      |
|                                   | [SetRegView](lib/SetRegView.htm). |
+-----------------------------------+-----------------------------------+
| A_TrayMenu                        | Returns a [Menu                   |
|                                   | object](lib/Menu.htm) which can   |
|                                   | be used to modify or display the  |
|                                   | tray menu.                        |
+-----------------------------------+-----------------------------------+
| A_AllowMainWindow                 | Can be used to get or set whether |
|                                   | the script\'s [main               |
|                                   | window](Program.htm#main-window)  |
|                                   | is allowed to be opened via the   |
|                                   | [tray                             |
|                                   | icon](Program.htm#tray-icon).     |
|                                   | Possible values are 0 (forbidden) |
|                                   | and 1 (allowed).                  |
|                                   |                                   |
|                                   | If the script is neither          |
|                                   | [compiled](Scripts.htm#ahk2exe)   |
|                                   | nor                               |
|                                   | [embedde                          |
|                                   | d](Program.htm#embedded-scripts), |
|                                   | this variable defaults to 1,      |
|                                   | otherwise this variable defaults  |
|                                   | to 0 but can be overridden by     |
|                                   | assigning it a value. Setting it  |
|                                   | to 1 also restores the \"Open\"   |
|                                   | menu item to the tray menu and    |
|                                   | enables the items in the main     |
|                                   | window\'s View menu such as       |
|                                   | \"Lines most recently executed\", |
|                                   | which allows viewing of the       |
|                                   | script\'s source code and other   |
|                                   | info.                             |
|                                   |                                   |
|                                   | The following functions are       |
|                                   | always able to show the main      |
|                                   | window and select the             |
|                                   | corresponding View options when   |
|                                   | they are encountered in the       |
|                                   | script at runtime:                |
|                                   | [ListLines](lib/ListLines.htm),   |
|                                   | [ListVars](lib/ListVars.htm),     |
|                                   | [L                                |
|                                   | istHotkeys](lib/ListHotkeys.htm), |
|                                   | and                               |
|                                   | [KeyHistory](lib/KeyHistory.htm). |
|                                   |                                   |
|                                   | Setting it to 1 does not prevent  |
|                                   | the main window from being shown  |
|                                   | by [WinShow](lib/WinShow.htm) or  |
|                                   | inspected by                      |
|                                   | [Contro                           |
|                                   | lGetText](lib/ControlGetText.htm) |
|                                   | or similar methods, but it does   |
|                                   | prevent the script\'s source code |
|                                   | and other info from being exposed |
|                                   | via the main window, except when  |
|                                   | one of the functions listed above |
|                                   | is called by the script.          |
+-----------------------------------+-----------------------------------+
| A_IconHidden                      | Can be used to get or set whether |
|                                   | to hide the [tray                 |
|                                   | icon](Program.htm#tray-icon).     |
|                                   | Possible values are 0 (visible)   |
|                                   | and 1 (hidden). For details, see  |
|                                   | [#                                |
|                                   | NoTrayIcon](lib/_NoTrayIcon.htm). |
+-----------------------------------+-----------------------------------+
| A_IconTip                         | Can be used to get or set the     |
|                                   | [tray                             |
|                                   | icon](Program.htm#tray-icon)\'s   |
|                                   | tooltip text, which is displayed  |
|                                   | when the mouse hovers over it. If |
|                                   | blank, the script\'s name is used |
|                                   | instead.                          |
|                                   |                                   |
|                                   | To create a multi-line tooltip,   |
|                                   | use the linefeed character (\`n)  |
|                                   | in between each line, e.g.        |
|                                   | `` "Line1`nLine2" ``. Only the    |
|                                   | first 127 characters are          |
|                                   | displayed, and the text is        |
|                                   | truncated at the first tab        |
|                                   | character, if present.            |
|                                   |                                   |
|                                   | On Windows 10 and earlier, to     |
|                                   | display tooltip text containing   |
|                                   | ampersands (&), escape each       |
|                                   | ampersand with two additional     |
|                                   | ampersands. For example,          |
|                                   | assigning `"A &&& B"` would       |
|                                   | display \"A & B\" in the tooltip. |
+-----------------------------------+-----------------------------------+
| A_IconFile                        | Blank unless a custom [tray       |
|                                   | icon](Program.htm#tray-icon) has  |
|                                   | been specified via                |
|                                   | [                                 |
|                                   | TraySetIcon](lib/TraySetIcon.htm) |
|                                   | \-- in which case it is the full  |
|                                   | path and name of the icon\'s      |
|                                   | file.                             |
+-----------------------------------+-----------------------------------+
| A_IconNumber                      | Blank if A_IconFile is blank.     |
|                                   | Otherwise, it\'s the number of    |
|                                   | the icon in A_IconFile (typically |
|                                   | 1).                               |
+-----------------------------------+-----------------------------------+

### User Idle Time {#User_Idle_Time}

+-----------------------------------+-----------------------------------+
| Variable                          | Description                       |
+===================================+===================================+
| A_TimeIdle                        | The number of milliseconds that   |
|                                   | have elapsed since the system     |
|                                   | last received keyboard, mouse, or |
|                                   | other input. This is useful for   |
|                                   | determining whether the user is   |
|                                   | away. Physical input from the     |
|                                   | user as well as artificial input  |
|                                   | generated by **any** program or   |
|                                   | script (such as the               |
|                                   | [Send](lib/Send.htm) or           |
|                                   | [MouseMove](lib/MouseMove.htm)    |
|                                   | functions) will reset this value  |
|                                   | back to zero. Since this value    |
|                                   | tends to increase by increments   |
|                                   | of 10, do not check whether it is |
|                                   | equal to another value. Instead,  |
|                                   | check whether it is greater or    |
|                                   | less than another value. For      |
|                                   | example:                          |
|                                   |                                   |
|                                   |     if A_TimeIdle > 600000        |
|                                   |         MsgBox "                  |
|                                   | Last activity was 10 minutes ago" |
+-----------------------------------+-----------------------------------+
| A_TimeIdlePhysical                | Similar to above but ignores      |
|                                   | artificial keystrokes and/or      |
|                                   | mouse clicks whenever the         |
|                                   | corresponding hook                |
|                                   | ([ke                              |
|                                   | yboard](lib/InstallKeybdHook.htm) |
|                                   | or                                |
|                                   | [                                 |
|                                   | mouse](lib/InstallMouseHook.htm)) |
|                                   | is installed; that is, it         |
|                                   | responds only to physical events. |
|                                   | (This prevents simulated          |
|                                   | keystrokes and mouse clicks from  |
|                                   | falsely indicating that a user is |
|                                   | present.) If neither hook is      |
|                                   | installed, this variable is       |
|                                   | equivalent to A_TimeIdle. If only |
|                                   | one hook is installed, only its   |
|                                   | type of physical input affects    |
|                                   | A_TimeIdlePhysical (the           |
|                                   | other/non-installed hook\'s       |
|                                   | input, both physical and          |
|                                   | artificial, has no effect).       |
+-----------------------------------+-----------------------------------+
| A_TimeIdleKeyboard                | If the [keyboard                  |
|                                   | hook](lib/InstallKeybdHook.htm)   |
|                                   | is installed, this is the number  |
|                                   | of milliseconds that have elapsed |
|                                   | since the system last received    |
|                                   | physical keyboard input.          |
|                                   | Otherwise, this variable is       |
|                                   | equivalent to A_TimeIdle.         |
+-----------------------------------+-----------------------------------+
| A_TimeIdleMouse                   | If the [mouse                     |
|                                   | hook](lib/InstallMouseHook.htm)   |
|                                   | is installed, this is the number  |
|                                   | of milliseconds that have elapsed |
|                                   | since the system last received    |
|                                   | physical mouse input. Otherwise,  |
|                                   | this variable is equivalent to    |
|                                   | A_TimeIdle.                       |
+-----------------------------------+-----------------------------------+

### Hotkeys, Hotstrings, and Custom Menu Items {#h}

+-----------------------------------+-----------------------------------+
| Variable                          | Description                       |
+===================================+===================================+
| A_ThisHotkey                      | The most recently executed        |
|                                   | [hotkey](Hotkeys.htm) or          |
|                                   | [non-auto-replace                 |
|                                   | hotstring](Hotstrings.htm) (blank |
|                                   | if none), e.g. #z. This value     |
|                                   | will change if the [current       |
|                                   | thread](misc/Threads.htm) is      |
|                                   | interrupted by another hotkey or  |
|                                   | hotstring, so it is generally     |
|                                   | better to use the parameter       |
|                                   | [Th                               |
|                                   | isHotkey](Hotkeys.htm#ThisHotkey) |
|                                   | when available.                   |
|                                   |                                   |
|                                   | When a hotkey is first created    |
|                                   | \-- either by the [Hotkey         |
|                                   | function](lib/Hotkey.htm) or the  |
|                                   | [double-colon                     |
|                                   | syntax](Hotkeys.htm) in the       |
|                                   | script \-- its key name and the   |
|                                   | ordering of its modifier symbols  |
|                                   | becomes the permanent name of     |
|                                   | that hotkey, shared by all        |
|                                   | [                                 |
|                                   | variants](lib/_HotIf.htm#variant) |
|                                   | of the hotkey.                    |
|                                   |                                   |
|                                   | When a hotstring is first created |
|                                   | \-- either by the [Hotstring      |
|                                   | function](lib/Hotstring.htm) or a |
|                                   | [double-colon                     |
|                                   | label](Hotstrings.htm) in the     |
|                                   | script \-- its trigger string and |
|                                   | sequence of option characters     |
|                                   | becomes the permanent name of     |
|                                   | that hotstring.                   |
+-----------------------------------+-----------------------------------+
| A_PriorHotkey                     | Same as above except for the      |
|                                   | previous hotkey. It will be blank |
|                                   | if none.                          |
+-----------------------------------+-----------------------------------+
| A_PriorKey                        | The name of the last key which    |
|                                   | was pressed prior to the most     |
|                                   | recent key-press or key-release,  |
|                                   | or blank if no applicable         |
|                                   | key-press can be found in the key |
|                                   | history. All input generated by   |
|                                   | AutoHotkey scripts is excluded.   |
|                                   | For this variable to be of use,   |
|                                   | the                               |
|                                   | [ke                               |
|                                   | yboard](lib/InstallKeybdHook.htm) |
|                                   | or [mouse                         |
|                                   | hook](lib/InstallMouseHook.htm)   |
|                                   | must be installed and [key        |
|                                   | history](lib/KeyHistory.htm) must |
|                                   | be enabled.                       |
+-----------------------------------+-----------------------------------+
| A_TimeSinceThisHotkey             | The number of milliseconds that   |
|                                   | have elapsed since A_ThisHotkey   |
|                                   | was pressed. It will be blank     |
|                                   | whenever A_ThisHotkey is blank.   |
+-----------------------------------+-----------------------------------+
| A_TimeSincePriorHotkey            | The number of milliseconds that   |
|                                   | have elapsed since A_PriorHotkey  |
|                                   | was pressed. It will be blank     |
|                                   | whenever A_PriorHotkey is blank.  |
+-----------------------------------+-----------------------------------+
| A_EndChar                         | The [ending                       |
|                                   | ch                                |
|                                   | aracter](Hotstrings.htm#EndChars) |
|                                   | that was pressed by the user to   |
|                                   | trigger the most recent           |
|                                   | [non-auto-replace                 |
|                                   | hotstring](Hotstrings.htm). If no |
|                                   | ending character was required     |
|                                   | (due to the [\*                   |
|                                   | o                                 |
|                                   | ption](Hotstrings.htm#Asterisk)), |
|                                   | this variable will be blank.      |
+-----------------------------------+-----------------------------------+
| A_MaxHotkeysPerInterval           | Can be used to get or set the     |
|                                   | maximum number of hotkeys that    |
|                                   | can be pressed within the         |
|                                   | interval defined by               |
|                                   | A_HotkeyInterval without          |
|                                   | triggering a warning dialog. For  |
|                                   | details, see                      |
|                                   | [A_MaxHotkeysPerInterval](        |
|                                   | lib/A_MaxHotkeysPerInterval.htm). |
+-----------------------------------+-----------------------------------+
| A_HotkeyInterval                  | Can be used to get or set the     |
|                                   | length of the interval used by    |
|                                   | [A_MaxHotkeysPerInterval](        |
|                                   | lib/A_MaxHotkeysPerInterval.htm), |
|                                   | in milliseconds.                  |
+-----------------------------------+-----------------------------------+
| A_HotkeyModifierTimeout           | Can be used to get or set the     |
|                                   | timeout affecting the behavior of |
|                                   | [Send](lib/Send.htm) with         |
|                                   | [hotkey](Hotkeys.htm) modifiers   |
|                                   | [Ctrl]{.kbd}, [Alt]{.kbd},        |
|                                   | [Win]{.kbd}, and [Shift]{.kbd}.   |
|                                   | For details, see                  |
|                                   | [A_HotkeyModifierTimeout](        |
|                                   | lib/A_HotkeyModifierTimeout.htm). |
+-----------------------------------+-----------------------------------+

### Operating System and User Info {#os}

+-----------------------------------+-----------------------------------+
| Variable                          | Description                       |
+===================================+===================================+
| A_ComSpec                         | Contains the same string as the   |
|                                   | ComSpec environment variable,     |
|                                   | which is usually the full path to |
|                                   | the command prompt executable     |
|                                   | (cmd.exe). Often used with        |
|                                   | [Run/RunWait](lib/Run.htm). For   |
|                                   | example:                          |
|                                   |                                   |
|                                   | ``` {.NoIndent .no-highlight}     |
|                                   | C:\Windows\system32\cmd.exe       |
|                                   | ```                               |
+-----------------------------------+-----------------------------------+
| A_Temp                            | The full path and name of the     |
|                                   | folder designated to hold         |
|                                   | temporary files. It is retrieved  |
|                                   | from one of the following         |
|                                   | locations (in order): 1) the      |
|                                   | [environment                      |
|                                   | variables](Co                     |
|                                   | ncepts.htm#environment-variables) |
|                                   | TMP, TEMP, or USERPROFILE; 2) the |
|                                   | Windows directory. For example:   |
|                                   |                                   |
|                                   | ``` {.NoIndent .no-highlight}     |
|                                   | C:\Us                             |
|                                   | ers\<UserName>\AppData\Local\Temp |
|                                   | ```                               |
+-----------------------------------+-----------------------------------+
| A_OSVersion                       | The version number of the         |
|                                   | operating system, in the format   |
|                                   | \"*major*.*minor*.*build*\". For  |
|                                   | example, Windows 7 SP1 is         |
|                                   | 6.1.7601.                         |
|                                   |                                   |
|                                   | Applying compatibility settings   |
|                                   | in the AutoHotkey executable or   |
|                                   | compiled script\'s properties     |
|                                   | causes the OS to report a         |
|                                   | different version number, which   |
|                                   | is reflected by A_OSVersion.      |
+-----------------------------------+-----------------------------------+
| A_Is64bitOS                       | Contains 1 (true) if the OS is    |
|                                   | 64-bit or 0 (false) if it is      |
|                                   | 32-bit.                           |
+-----------------------------------+-----------------------------------+
| A_PtrSize                         | Contains the size of a pointer,   |
|                                   | in bytes. This is either 4        |
|                                   | (32-bit) or 8 (64-bit), depending |
|                                   | on what type of executable (EXE)  |
|                                   | is running the script.            |
+-----------------------------------+-----------------------------------+
| A_Language                        | The system\'s default language,   |
|                                   | which is one of [these 4-digit    |
|                                   | codes](misc/Languages.htm).       |
+-----------------------------------+-----------------------------------+
| A_ComputerName                    | The name of the computer as seen  |
|                                   | on the network.                   |
+-----------------------------------+-----------------------------------+
| A_UserName                        | The logon name of the user who    |
|                                   | launched this script.             |
+-----------------------------------+-----------------------------------+
| A_WinDir                          | The Windows directory. For        |
|                                   | example: `C:\Windows`             |
+-----------------------------------+-----------------------------------+
| A_ProgramFiles                    | The Program Files directory (e.g. |
|                                   | `C:\Program Files` or             |
|                                   | `C:\Program Files (x86)`). This   |
|                                   | is usually the same as the        |
|                                   | *ProgramFiles* [environment       |
|                                   | variable](Con                     |
|                                   | cepts.htm#environment-variables). |
|                                   |                                   |
|                                   | On [64-bit systems](#Is64bitOS)   |
|                                   | (and not 32-bit systems), the     |
|                                   | following applies:                |
|                                   |                                   |
|                                   | -   If the executable (EXE) that  |
|                                   |     is running the script is      |
|                                   |     32-bit, A_ProgramFiles        |
|                                   |     returns the path of the       |
|                                   |     \"Program Files (x86)\"       |
|                                   |     directory.                    |
|                                   | -   For 32-bit processes, the     |
|                                   |     *ProgramW6432* environment    |
|                                   |     variable contains the path of |
|                                   |     the 64-bit Program Files      |
|                                   |     directory. On Windows 7 and   |
|                                   |     later, it is also set for     |
|                                   |     64-bit processes.             |
|                                   | -   The *ProgramFiles(x86)*       |
|                                   |     environment variable contains |
|                                   |     the path of the 32-bit        |
|                                   |     Program Files directory.      |
+-----------------------------------+-----------------------------------+
| A_AppData                         | The full path and name of the     |
|                                   | folder containing the current     |
|                                   | user\'s application-specific      |
|                                   | data. For example:                |
|                                   |                                   |
|                                   | ``` {.NoIndent .no-highlight}     |
|                                   | C:                                |
|                                   | \Users\<UserName>\AppData\Roaming |
|                                   | ```                               |
+-----------------------------------+-----------------------------------+
| A_AppDataCommon                   | The full path and name of the     |
|                                   | folder containing the all-users   |
|                                   | application-specific data. For    |
|                                   | example:                          |
|                                   |                                   |
|                                   | ``` {.NoIndent .no-highlight}     |
|                                   | C:\ProgramData                    |
|                                   | ```                               |
+-----------------------------------+-----------------------------------+
| A_Desktop                         | The full path and name of the     |
|                                   | folder containing the current     |
|                                   | user\'s desktop files. For        |
|                                   | example:                          |
|                                   |                                   |
|                                   | ``` {.NoIndent .no-highlight}     |
|                                   | C:\Users\<UserName>\Desktop       |
|                                   | ```                               |
+-----------------------------------+-----------------------------------+
| A_DesktopCommon                   | The full path and name of the     |
|                                   | folder containing the all-users   |
|                                   | desktop files. For example:       |
|                                   |                                   |
|                                   | ``` {.NoIndent .no-highlight}     |
|                                   | C:\Users\Public\Desktop           |
|                                   | ```                               |
+-----------------------------------+-----------------------------------+
| A_StartMenu                       | The full path and name of the     |
|                                   | current user\'s Start Menu        |
|                                   | folder. For example:              |
|                                   |                                   |
|                                   | ``` {.NoIndent .no-highlight}     |
|                                   | C:\Users\<UserName>\AppData\Roa   |
|                                   | ming\Microsoft\Windows\Start Menu |
|                                   | ```                               |
+-----------------------------------+-----------------------------------+
| A_StartMenuCommon                 | The full path and name of the     |
|                                   | all-users Start Menu folder. For  |
|                                   | example:                          |
|                                   |                                   |
|                                   | ``` {.NoIndent .no-highlight}     |
|                                   | C:\Program                        |
|                                   | Data\Microsoft\Windows\Start Menu |
|                                   | ```                               |
+-----------------------------------+-----------------------------------+
| A_Programs                        | The full path and name of the     |
|                                   | Programs folder in the current    |
|                                   | user\'s Start Menu. For example:  |
|                                   |                                   |
|                                   | ``` {.NoIndent .no-highlight}     |
|                                   | C:\User                           |
|                                   | s\<UserName>\AppData\Roaming\Micr |
|                                   | osoft\Windows\Start Menu\Programs |
|                                   | ```                               |
+-----------------------------------+-----------------------------------+
| A_ProgramsCommon                  | The full path and name of the     |
|                                   | Programs folder in the all-users  |
|                                   | Start Menu. For example:          |
|                                   |                                   |
|                                   | ``` {.NoIndent .no-highlight}     |
|                                   | C:\ProgramData\Micr               |
|                                   | osoft\Windows\Start Menu\Programs |
|                                   | ```                               |
+-----------------------------------+-----------------------------------+
| A_Startup                         | The full path and name of the     |
|                                   | Startup folder in the current     |
|                                   | user\'s Start Menu. For example:  |
|                                   |                                   |
|                                   | ``` {.NoIndent .no-highlight}     |
|                                   | C:\Users\<UserN                   |
|                                   | ame>\AppData\Roaming\Microsoft\Wi |
|                                   | ndows\Start Menu\Programs\Startup |
|                                   | ```                               |
+-----------------------------------+-----------------------------------+
| A_StartupCommon                   | The full path and name of the     |
|                                   | Startup folder in the all-users   |
|                                   | Start Menu. For example:          |
|                                   |                                   |
|                                   | ``` {.NoIndent .no-highlight}     |
|                                   | C:\ProgramData\Microsoft\Wi       |
|                                   | ndows\Start Menu\Programs\Startup |
|                                   | ```                               |
+-----------------------------------+-----------------------------------+
| A_MyDocuments                     | The full path and name of the     |
|                                   | current user\'s \"My Documents\"  |
|                                   | folder. Unlike most of the        |
|                                   | similar variables, if the folder  |
|                                   | is the root of a drive, the final |
|                                   | backslash is not included (e.g.   |
|                                   | it would contain `M:` rather than |
|                                   | `M:\`). For example:              |
|                                   |                                   |
|                                   | ``` {.NoIndent .no-highlight}     |
|                                   | C:\Users\<UserName>\Documents     |
|                                   | ```                               |
+-----------------------------------+-----------------------------------+
| A_IsAdmin                         | Contains 1 if the current user    |
|                                   | has admin rights, otherwise 0.    |
|                                   |                                   |
|                                   | To have the script restart itself |
|                                   | as admin (or show a prompt to the |
|                                   | user requesting admin), use [Run  |
|                                   | \*RunAs](lib/Run.htm#RunAs).      |
|                                   | However, note that running the    |
|                                   | script as admin causes all        |
|                                   | programs launched by the script   |
|                                   | to also run as admin. For a       |
|                                   | possible alternative, see [the    |
|                                   | FAQ](FAQ.htm#uac).                |
+-----------------------------------+-----------------------------------+
| A_ScreenWidth\                    | The width and height of the       |
| A_ScreenHeight                    | primary monitor, in pixels (e.g.  |
|                                   | 1024 and 768).                    |
|                                   |                                   |
|                                   | To discover the dimensions of     |
|                                   | other monitors in a multi-monitor |
|                                   | system, use                       |
|                                   | [SysGet](lib/SysGet.htm).         |
|                                   |                                   |
|                                   | To instead discover the width and |
|                                   | height of the entire desktop      |
|                                   | (even if it spans multiple        |
|                                   | monitors), use the following      |
|                                   | example:                          |
|                                   |                                   |
|                                   |     VirtualWidth := SysGet(78)    |
|                                   |     VirtualHeight := SysGet(79)   |
|                                   |                                   |
|                                   | In addition, use                  |
|                                   | [SysGet](lib/SysGet.htm) to       |
|                                   | discover the work area of a       |
|                                   | monitor, which can be smaller     |
|                                   | than the monitor\'s total area    |
|                                   | because the taskbar and other     |
|                                   | registered desktop toolbars are   |
|                                   | excluded.                         |
+-----------------------------------+-----------------------------------+
| A_ScreenDPI                       | Number of pixels per logical inch |
|                                   | along the screen width. In a      |
|                                   | system with multiple display      |
|                                   | monitors, this value is the same  |
|                                   | for all monitors. On most systems |
|                                   | this is 96; it depends on the     |
|                                   | system\'s text size (DPI)         |
|                                   | setting. See also the GUI\'s      |
|                                   | [-DPIScale](lib/Gui.htm#DPIScale) |
|                                   | option.                           |
+-----------------------------------+-----------------------------------+

### Misc. {#misc}

+-----------------------------------+-----------------------------------+
| Variable                          | Description                       |
+===================================+===================================+
| A_Clipboard                       | Can be used to get or set the     |
|                                   | contents of the OS\'s clipboard.  |
|                                   | For details, see                  |
|                                   | [A                                |
|                                   | _Clipboard](lib/A_Clipboard.htm). |
+-----------------------------------+-----------------------------------+
| A_Cursor                          | The type of mouse cursor          |
|                                   | currently being displayed. It     |
|                                   | will be one of the following      |
|                                   | words: AppStarting, Arrow, Cross, |
|                                   | Help, IBeam, Icon, No, Size,      |
|                                   | SizeAll, SizeNESW, SizeNS,        |
|                                   | SizeNWSE, SizeWE, UpArrow, Wait,  |
|                                   | Unknown. The acronyms used with   |
|                                   | the size-type cursors are compass |
|                                   | directions, e.g. NESW =           |
|                                   | NorthEast+SouthWest. The          |
|                                   | hand-shaped cursors (pointing and |
|                                   | grabbing) are classified as       |
|                                   | Unknown.                          |
+-----------------------------------+-----------------------------------+
| A_EventInfo                       | Contains additional information   |
|                                   | about the following events:       |
|                                   |                                   |
|                                   | -   [Mouse wheel                  |
|                                   |     hotkeys](Hotkeys.htm#Wheel)   |
|                                   |     (WheelDown/Up/Left/Right)     |
|                                   | -                                 |
|                                   |    [OnMessage](lib/OnMessage.htm) |
|                                   | -   [Regular Expression           |
|                                   |                                   |
|                                   |  Callouts](misc/RegExCallout.htm) |
|                                   |                                   |
|                                   | Note: Unlike variables such as    |
|                                   | A_ThisHotkey, each                |
|                                   | [thread](misc/Threads.htm)        |
|                                   | retains its own value for         |
|                                   | A_EventInfo. Therefore, if a      |
|                                   | thread is interrupted by another, |
|                                   | upon being resumed it will still  |
|                                   | see its original/correct values   |
|                                   | in these variables.               |
|                                   |                                   |
|                                   | A_EventInfo can also be set by    |
|                                   | the script, but can only accept   |
|                                   | unsigned integers within the      |
|                                   | range available to pointers       |
|                                   | (32-bit or 64-bit depending on    |
|                                   | the version of AutoHotkey).       |
+-----------------------------------+-----------------------------------+
| A_LastError                       | This is usually the result from   |
|                                   | the OS\'s GetLastError() function |
|                                   | after the script calls certain    |
|                                   | functions, including              |
|                                   | [DllCall](lib/DllCall.htm),       |
|                                   | [Run/RunWait](lib/Run.htm),       |
|                                   | File/Ini/Reg functions (where     |
|                                   | documented) and possibly others.  |
|                                   | A_LastError is a number between 0 |
|                                   | and 4294967295 (always formatted  |
|                                   | as decimal, not hexadecimal).     |
|                                   | Zero (0) means success, but any   |
|                                   | other number means the call       |
|                                   | failed. Each number corresponds   |
|                                   | to a specific error condition.    |
|                                   | See                               |
|                                   | [OSError](lib/Error.htm#OSError)  |
|                                   | for how to get the localized      |
|                                   | error description text, or search |
|                                   | [www.microso                      |
|                                   | ft.com](http://www.microsoft.com) |
|                                   | for \"system error codes\" to get |
|                                   | a list. A_LastError is a          |
|                                   | per-thread setting; that is,      |
|                                   | interruptions by other            |
|                                   | [threads](misc/Threads.htm)       |
|                                   | cannot change it.                 |
|                                   |                                   |
|                                   | Assigning a value to A_LastError  |
|                                   | also causes the OS\'s             |
|                                   | SetLastError() function to be     |
|                                   | called.                           |
+-----------------------------------+-----------------------------------+
| True\                             | Contain 1 and 0. They can be used |
| False                             | to make a script more readable.   |
|                                   | For details, see [Boolean         |
|                                   | Values](Concepts.htm#boolean).    |
|                                   |                                   |
|                                   | These are actually                |
|                                   | [k                                |
|                                   | eywords](Language.htm#constants), |
|                                   | not variables.                    |
+-----------------------------------+-----------------------------------+

### Loop

  Variable               Description
  ---------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  A_Index                Can be used to get or set the number of the current loop iteration (a 64-bit integer). It contains 1 the first time the loop\'s body is executed. For the second time, it contains 2; and so on. If an inner loop is enclosed by an outer loop, the inner loop takes precedence. A_Index works inside [all types of loops](Language.htm#loop-statement), but contains 0 outside of a loop. For counted loops such as [Loop](lib/Loop.htm), changing A_Index affects the number of iterations that will be performed.
  A_LoopFileName, etc.   This and other related variables are valid only inside a [file loop](lib/LoopFiles.htm).
  A_LoopRegName, etc.    This and other related variables are valid only inside a [registry loop](lib/LoopReg.htm).
  A_LoopReadLine         See [file-reading loop](lib/LoopRead.htm).
  A_LoopField            See [parsing loop](lib/LoopParse.htm).

## Variable Capacity and Memory {#cap}

-   When a variable is given a new string longer than its current
    contents, additional system memory is allocated automatically.
-   The memory occupied by a large variable can be freed by setting it
    equal to nothing, e.g. `var := ""`.
-   There is no limit to how many variables a script may create. The
    program is designed to support at least several million variables
    without a significant drop in performance.
-   Functions and expressions that accept numeric inputs generally
    support 15 digits of precision for floating point values. For
    integers, 64-bit signed values are supported, which range from
    -9223372036854775808 (-0x8000000000000000) to 9223372036854775807
    (0x7FFFFFFFFFFFFFFF). Any integer constants outside this range wrap
    around. Similarly, arithmetic operations on integers wrap around
    upon overflow (e.g. 0x7FFFFFFFFFFFFFFF + 1 = -0x8000000000000000).
