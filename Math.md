# Math Functions

Functions for performing various mathematical operations such as
rounding, exponentiation, squaring, etc.

## Table of Contents {#toc}

-   [General Math](#General):
    -   [Abs](#Abs): Returns the absolute value of a number.
    -   [Ceil](#Ceil): Returns a number rounded up to the nearest
        integer.
    -   [Exp](#Exp): Returns the result of raising e to the *N*th power.
    -   [Floor](#Floor): Returns a number rounded down to the nearest
        integer.
    -   [Log](#Log): Returns the logarithm (base 10) of a number.
    -   [Ln](#Ln): Returns the natural logarithm (base e) of a number.
    -   [Max](#Max): Returns the highest number from a set of numbers.
    -   [Min](#Min): Returns the lowest number from a set of numbers.
    -   [Mod](#Mod): Modulo. Returns the remainder of a division.
    -   [Round](#Round): Returns a number rounded to *N* decimal places.
    -   [Sqrt](#Sqrt): Returns the square root of a number.
-   [Trigonometry](#Trigonometry):
    -   [Sin](#Sin): Returns the trigonometric sine of a number.
    -   [Cos](#Cos): Returns the trigonometric cosine of a number.
    -   [Tan](#Tan): Returns the trigonometric tangent of a number.
    -   [ASin](#ASin): Returns the arcsine of a number in radians.
    -   [ACos](#ACos): Returns the arccosine of a number in radians.
    -   [ATan](#ATan): Returns the arctangent of a number in radians.
-   [Error-handling](#Errors)

## General Math {#General}

### Abs {#Abs}

Returns the absolute value of the specified number.

``` Syntax
Value := Abs(Number)
```

The return value is the same type as *Number* (integer or floating
point).

``` NoIndent
MsgBox Abs(-1.2) ; Returns 1.2
```

### Ceil {#Ceil}

Returns the specified number rounded up to the nearest integer (without
any .00 suffix).

``` Syntax
Value := Ceil(Number)
```

``` NoIndent
MsgBox Ceil(1.2)  ; Returns 2
MsgBox Ceil(-1.2) ; Returns -1
```

### Exp {#Exp}

Returns the result of raising e (which is approximately
2.71828182845905) to the *N*th power.

``` Syntax
Value := Exp(N)
```

*N* may be negative and may contain a decimal point. To raise numbers
other than e to a power, use the [\*\* operator](../Variables.htm#pow).

``` NoIndent
MsgBox Exp(1.2) ; Returns 3.320117
```

### Floor {#Floor}

Returns the specified number rounded down to the nearest integer
(without any .00 suffix).

``` Syntax
Value := Floor(Number)
```

``` NoIndent
MsgBox Floor(1.2)  ; Returns 1
MsgBox Floor(-1.2) ; Returns -2
```

### Log {#Log}

Returns the logarithm (base 10) of the specified number.

``` Syntax
Value := Log(Number)
```

The result is a floating-point number. If *Number* is negative, a
[ValueError](Error.htm#ValueError) is thrown.

``` NoIndent
MsgBox Log(1.2) ; Returns 0.079181
```

### Ln {#Ln}

Returns the natural logarithm (base e) of the specified number.

``` Syntax
Value := Ln(Number)
```

The result is a floating-point number. If *Number* is negative, a
[ValueError](Error.htm#ValueError) is thrown.

``` NoIndent
MsgBox Ln(1.2) ; Returns 0.182322
```

### Max {#Max}

Returns the highest number from a set of numbers.

``` Syntax
Number := Max(Number1 , Number2, ...)
```

``` NoIndent
MsgBox Max(2.11, -2, 0) ; Returns 2.11
```

You can also specify a [variadic parameter](../Functions.htm#Variadic)
to pass an [array](Array.htm) of numbers. For example:

``` NoIndent
Numbers := [1, 2, 3, 4]
MsgBox Max(Numbers*) ; Returns 4
```

### Min {#Min}

Returns the lowest number from a set of numbers.

``` Syntax
Number := Min(Number1 , Number2, ...)
```

``` NoIndent
MsgBox Min(2.11, -2, 0) ; Returns -2
```

You can also specify a [variadic parameter](../Functions.htm#Variadic)
to pass an [array](Array.htm) of numbers. For example:

``` NoIndent
Numbers := [1, 2, 3, 4]
MsgBox Min(Numbers*) ; Returns 1
```

### Mod {#Mod}

Modulo. Returns the remainder of a number (dividend) divided by another
number (divisor).

``` Syntax
Value := Mod(Dividend, Divisor)
```

The sign of the result is always the same as the sign of the first
parameter. If either input is a floating point number, the result is
also a floating point number. If the second parameter is zero, a
[ZeroDivisionError](Error.htm#ZeroDivisionError) is thrown.

``` NoIndent
MsgBox Mod(7.5, 2) ; Returns 1.5 (2 x 3 + 1.5)
```

### Round {#Round}

Returns the specified number rounded to *N* decimal places.

``` Syntax
Value := Round(Number , N)
```

If *N* is omitted or 0, *Number* is rounded to the nearest integer:

``` NoIndent
MsgBox Round(3.14)    ; Returns 3
```

If *N* is positive, *Number* is rounded to *N* decimal places:

``` NoIndent
MsgBox Round(3.14, 1) ; Returns 3.1
```

If *N* is negative, *Number* is rounded by *N* digits to the left of the
decimal point:

``` NoIndent
MsgBox Round(345, -1) ; Returns 350
MsgBox Round(345, -2) ; Returns 300
```

The result is an integer if *N* is omitted or less than 1. Otherwise,
the result is a numeric string with exactly *N* decimal places. If a
pure number is needed, simply perform another math operation on Round\'s
return value; for example: `Round(3.333, 1)+0`.

### Sqrt {#Sqrt}

Returns the square root of the specified number.

``` Syntax
Value := Sqrt(Number)
```

The result is a floating-point number. If *Number* is negative, a
[ValueError](Error.htm#ValueError) is thrown.

``` NoIndent
MsgBox Sqrt(16) ; Returns 4
```

## Trigonometry {#Trigonometry}

**Note:** To convert a radians value to degrees, multiply it by 180/pi
(approximately 57.29578). To convert a degrees value to radians,
multiply it by pi/180 (approximately 0.01745329252). The value of pi
(approximately 3.141592653589793) is 4 times the arctangent of 1.

### Sin {#Sin}

Returns the trigonometric sine of the specified number.

``` Syntax
Value := Sin(Number)
```

*Number* must be expressed in radians.

``` NoIndent
MsgBox Sin(1.2) ; Returns 0.932039
```

### Cos {#Cos}

Returns the trigonometric cosine of the specified number.

``` Syntax
Value := Cos(Number)
```

*Number* must be expressed in radians.

``` NoIndent
MsgBox Cos(1.2) ; Returns 0.362358
```

### Tan {#Tan}

Returns the trigonometric tangent of the specified number.

``` Syntax
Value := Tan(Number)
```

*Number* must be expressed in radians.

``` NoIndent
MsgBox Tan(1.2) ; Returns 2.572152
```

### ASin {#ASin}

Returns the arcsine (the number whose sine is the specified number) in
radians.

``` Syntax
Value := ASin(Number)
```

If *Number* is less than -1 or greater than 1, a
[ValueError](Error.htm#ValueError) is thrown.

``` NoIndent
MsgBox ASin(0.2) ; Returns 0.201358
```

### ACos {#ACos}

Returns the arccosine (the number whose cosine is the specified number)
in radians.

``` Syntax
Value := ACos(Number)
```

If *Number* is less than -1 or greater than 1, a
[ValueError](Error.htm#ValueError) is thrown.

``` NoIndent
MsgBox ACos(0.2) ; Returns 1.369438
```

### ATan {#ATan}

Returns the arctangent (the number whose tangent is the specified
number) in radians.

``` Syntax
Value := ATan(Number)
```

``` NoIndent
MsgBox ATan(1.2) ; Returns 0.876058
```

## Error-Handling {#Errors}

These functions throw an exception if any incoming parameters are
non-numeric or an invalid operation (such as divide by zero) is
attempted.
