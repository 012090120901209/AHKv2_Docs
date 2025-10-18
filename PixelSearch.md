# PixelSearch

Searches a region of the screen for a pixel of the specified color.

``` Syntax
PixelSearch &OutputVarX, &OutputVarY, X1, Y1, X2, Y2, ColorID , Variation
```

## Parameters {#Parameters}

&OutputVarX, &OutputVarY

:   Type: [VarRef](../Concepts.htm#variable-references)

    References to the output variables in which to store the X and Y
    coordinates of the first pixel that matches *ColorID* (if no match
    is found, the variables are made blank). Coordinates are relative to
    the active window\'s client area unless [CoordMode](CoordMode.htm)
    was used to change that.

X1, Y1

:   Type: [Integer](../Concepts.htm#numbers)

    The X and Y coordinates of the starting corner of the rectangle to
    search. Coordinates are relative to the active window\'s client area
    unless [CoordMode](CoordMode.htm) was used to change that.

X2, Y2

:   Type: [Integer](../Concepts.htm#numbers)

    The X and Y coordinates of the ending corner of the rectangle to
    search. Coordinates are relative to the active window\'s client area
    unless [CoordMode](CoordMode.htm) was used to change that.

ColorID

:   Type: [Integer](../Concepts.htm#numbers)

    The color ID to search for. This is typically expressed as a
    hexadecimal number in Red-Green-Blue (RGB) format. For example:
    `0x9d6346`. Color IDs can be determined using Window Spy (accessible
    from the tray menu) or via [PixelGetColor](PixelGetColor.htm).

Variation

:   Type: [Integer](../Concepts.htm#numbers)

    If omitted, it defaults to 0. Otherwise, specify a number between 0
    and 255 (inclusive) to indicate the allowed number of shades of
    variation in either direction for the intensity of the red, green,
    and blue components of the color. For example, if 2 is specified and
    *ColorID* is 0x444444, any color from 0x424242 to 0x464646 will be
    considered a match. This parameter is helpful if the color sought is
    not always exactly the same shade. If you specify 255 shades of
    variation, all colors will match.

## Return Value {#Return_Value}

Type: [Integer (boolean)](../Concepts.htm#boolean)

This function returns 1 (true) if the color was found in the specified
region, or 0 (false) if it was not found.

## Error Handling {#Error_Handling}

An [OSError](Error.htm#OSError) is thrown if there was a problem that
prevented the function from conducting the search.

## Remarks {#Remarks}

The region to be searched must be visible; in other words, it is not
possible to search a region of a window hidden behind another window. By
contrast, pixels beneath the mouse cursor can usually be detected. The
exception to this is game cursors, which in most cases will obstruct any
pixels beneath them.

Although color depths as low as 8-bit (256-color) are supported,
PixelSearch performs much better in 24-bit or 32-bit color.

The search starts at the coordinates specified by *X1* and *Y1* and
checks all pixels in the row from *X1* to *X2* for a match. If no match
is found there, the search continues toward *Y2*, row by row, until it
finds a matching pixel.

The search order depends on the order of the parameters. In other words,
if *X1* is greater than *X2*, the search will be conducted from right to
left, starting at column *X1*. Similarly, if *Y1* is greater than *Y2*,
the search will be conducted from bottom to top.

If the region to be searched is large and the search is repeated with
high frequency, it may consume a lot of CPU time. To alleviate this,
keep the size of the area to a minimum.

## Related {#Related}

[PixelGetColor](PixelGetColor.htm), [ImageSearch](ImageSearch.htm),
[CoordMode](CoordMode.htm), [MouseGetPos](MouseGetPos.htm)

## Examples {#Examples}

::: {#ExBasic .ex}
[](#ExBasic){.ex_number} Searches a region of the active window for a
pixel and stores in *Px* and *Py* the X and Y coordinates of the first
pixel that matches the specified color with 3 shades of variation.

    if PixelSearch(&Px, &Py, 200, 200, 300, 300, 0x9d6346, 3)
        MsgBox "A color within 3 shades of variation was found at X" Px " Y" Py
    else
        MsgBox "That color was not found in the specified region."
:::
