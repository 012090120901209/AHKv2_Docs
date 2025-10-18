# RegCreateKey

Creates a registry key without writing a value.

``` Syntax
RegCreateKey KeyName
```

## Parameters {#Parameters}

KeyName

:   Type: [String](../Concepts.htm#strings)

    The full name of the registry key, e.g.
    `"HKLM\Software\SomeApplication"`.

    This must start with HKEY_LOCAL_MACHINE (or HKLM), HKEY_USERS (or
    HKU), HKEY_CURRENT_USER (or HKCU), HKEY_CLASSES_ROOT (or HKCR), or
    HKEY_CURRENT_CONFIG (or HKCC).

    To access a [remote registry](LoopReg.htm#remote), prepend the
    computer name and a backslash, e.g. `"\\workstation01\HKLM"`.

    *KeyName* can be omitted only if a [registry loop](LoopReg.htm) is
    running, in which case it defaults to the key of the current loop
    item (even if the key has been deleted during the loop). If the item
    is a subkey, the full name of that subkey is used by default.

## Error Handling {#Error_Handling}

An [OSError](Error.htm#OSError) is thrown on failure.

[A_LastError](../Variables.htm#LastError) is set to the result of the
operating system\'s GetLastError() function.

## Remarks {#Remarks}

If *KeyName* specifies an existing registry key, RegCreateKey verifies
that the script has write access to the key, but makes no changes.
Otherwise, RegCreateKey attempts to create the key (along with its
ancestors, if necessary).

For details about how to access the registry of a remote computer, see
the remarks in [registry loop](LoopReg.htm#remote).

To create subkeys in the 64-bit sections of the registry in a 32-bit
script or vice versa, use [SetRegView](SetRegView.htm).

## Related {#Related}

[RegDelete](RegDelete.htm), [RegDeleteKey](RegDeleteKey.htm),
[RegRead](RegRead.htm), [RegWrite](RegWrite.htm), [registry
loop](LoopReg.htm), [SetRegView](SetRegView.htm)

## Examples {#Examples}

::: {#ExBasic .ex}
[](#ExBasic){.ex_number} Creates an empty registry key. If Notepad++ is
installed, this has the effect of adding it to the \"open with\" menu
for .ahk files.

    RegCreateKey "HKCU\Software\Classes\.ahk\OpenWithList\notepad++.exe"
:::
