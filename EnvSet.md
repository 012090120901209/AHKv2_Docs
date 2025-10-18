# EnvSet

Writes a value to the specified [environment
variable](../Concepts.htm#environment-variables).

``` Syntax
EnvSet EnvVar , Value
```

## Parameters {#Parameters}

EnvVar

:   Type: [String](../Concepts.htm#strings)

    The name of the environment variable, e.g. `"Path"`.

Value

:   Type: [String](../Concepts.htm#strings)

    If omitted, the environment variable will be deleted. Otherwise,
    specify the value to write.

## Error Handling {#Error_Handling}

An [OSError](Error.htm#OSError) is thrown on failure.

## Remarks {#Remarks}

The operating system limits each environment variable to 32 KB of text.

An environment variable created or changed with this function will be
accessible only to programs the script launches via [Run](Run.htm) or
[RunWait](Run.htm). See [environment
variables](../Concepts.htm#environment-variables) for more details.

This function exists because [normal script variables](../Variables.htm)
are not stored in the environment. This is because performance would be
worse and also because the OS limits environment variables to 32 KB.

## Related {#Related}

[EnvGet](EnvGet.htm), [Run / RunWait](Run.htm)

## Examples {#Examples}

::: {#ExBasic .ex}
[](#ExBasic){.ex_number} Writes some text to an environment variable.

    EnvSet "AutGUI", "Some text to put in the environment variable."
:::
