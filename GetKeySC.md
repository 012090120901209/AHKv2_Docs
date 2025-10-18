# GetKeySC

Retrieves the scan code of a key.

``` Syntax
SC := GetKeySC(KeyName)
```

## Parameters {#Parameters}

KeyName

:   Type: [String](../Concepts.htm#strings)

    Any single character or one of the key names from the [key
    list](../KeyList.htm). Examples: B, 5, LWin, RControl, Alt, Enter,
    Escape.

    Alternatively, this can be an explicit virtual key code such as
    vkFF, an explicit scan code such as sc01D, or a combination of VK
    and SC (in that order) such as vk1Bsc001. Note that these codes must
    be in hexadecimal.

## Return Value {#Return_Value}

Type: [Integer](../Concepts.htm#numbers)

This function returns the scan code of the specified key, or 0 if the
key is invalid or has no scan code.

## Remarks {#Remarks}

Before using the scan code with a built-in function like
[Hotkey](Hotkey.htm) or [GetKeyState](GetKeyState.htm), it must first be
converted to hexadecimal format, such as by using
`Format("sc{:X}", sc_code)`. By contrast, external functions called via
[DllCall](DllCall.htm) typically use the numeric value directly.

If *KeyName* corresponds to a virtual key code or single character, the
function attempts to map the value to a scan code by calling certain
system functions which refer to the script\'s current keyboard layout.
This may differ from the keyboard layout of the active window.

If *KeyName* is an ASCII letter in the range A-Z and has no mapping
within the keyboard layout, the corresponding virtual key in the range
vk41-vk5A is used as a fallback. This virtual key is then mapped to a
scan code as described above.

Some keyboard layouts do not define a 1:1 mapping of virtual key codes
to scan codes. When multiple interpretations are possible, the
underlying system functions most likely choose one based on the order
defined in the keyboard layout, which is not always the most common or
logical choice.

## Related {#Related}

[GetKeyVK](GetKeyVK.htm), [GetKeyName](GetKeyName.htm),
[GetKeyState](GetKeyState.htm), [Key List](../KeyList.htm),
[Format](Format.htm)

## Examples {#Examples}

::: {#ExBasic .ex}
[](#ExBasic){.ex_number} Retrieves and reports the hexadecimal scan code
of the left [Ctrl]{.kbd}.

    sc_code := GetKeySC("LControl")
    MsgBox Format("sc{:X}", sc_code) ; Reports sc1D
:::
