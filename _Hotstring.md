# #Hotstring

Changes [hotstring](../Hotstrings.htm) options or ending characters.

``` Syntax
#Hotstring NoMouse
#Hotstring EndChars NewChars
#Hotstring NewOptions
```

## Parameters {#Parameters}

NoMouse

:   Type: [String](../Concepts.htm#strings)

    Prevents mouse clicks from resetting the hotstring recognizer as
    described [here](../Hotstrings.htm#NoMouse). As a side-effect, this
    also prevents the [mouse hook](InstallMouseHook.htm) from being
    required by hotstrings (though it will still be installed if the
    script requires it for other purposes, such as mouse hotkeys). The
    presence of `#Hotstring NoMouse` anywhere in the script affects all
    hotstrings, not just those physically beneath it.

EndChars NewChars

:   Type: [String](../Concepts.htm#strings)

    Specify the word EndChars followed by a single space and then the
    new ending characters. For example:

        #Hotstring EndChars -()[]{}':;"/\,.?!`n`s`t

    Since the new ending characters are in effect globally for the
    entire script \-- regardless of where the EndChars directive appears
    \-- there is no need to specify EndChars more than once.

    The maximum number of ending characters is 100. Characters beyond
    this length are ignored.

    To make tab or space an ending character, include \`t or \`s in the
    list.

NewOptions

:   Type: [String](../Concepts.htm#strings)

    Specify new options as described in [Hotstring
    Options](../Hotstrings.htm#Options). For example:
    `#Hotstring r s k0 c0`.

    Unlike *EndChars* above, the #Hotstring directive is positional when
    used this way. In other words, entire sections of hotstrings can
    have different default options as in this example:

        ::btw::by the way

        #Hotstring r c  ; All the below hotstrings will use "send raw" and will be case-sensitive by default.
        ::al::airline
        ::CEO::Chief Executive Officer

        #Hotstring c0  ; Make all hotstrings below this point case-insensitive.

## Remarks {#Remarks}

Like other directives, #Hotstring cannot be executed conditionally.

## Related {#Related}

[Hotstrings](../Hotstrings.htm)

The [Hotstring](Hotstring.htm) function can be used to change hotstring
options while the script is running.
