# EnvGet

Retrieves the value of the specified [environment
variable](../Concepts.htm#environment-variables).

``` Syntax
Value := EnvGet(EnvVar)
```

## Parameters {#Parameters}

EnvVar

:   Type: [String](../Concepts.htm#strings)

    The name of the environment variable, e.g. `"Path"`.

## Return Value {#Return_Value}

Type: [String](../Concepts.htm#strings)

This function returns *EnvVar*\'s value. If *EnvVar* has an empty value
or does not exist, an empty string is returned.

## Remarks {#Remarks}

The operating system limits each environment variable to 32 KB of text.

This function exists because [normal script variables](../Variables.htm)
are not stored in the environment. This is because performance would be
worse and also because the OS limits environment variables to 32 KB.

## Related {#Related}

[EnvSet](EnvSet.htm), [Run / RunWait](Run.htm)

## Examples {#Examples}

::: {#ExBasic .ex}
[](#ExBasic){.ex_number} Retrieves the value of an environment variable
and stores it in `LogonServer`{.variable}.

    LogonServer := EnvGet("LogonServer")
:::

::: {#ExProgramFiles .ex}
[](#ExProgramFiles){.ex_number} Retrieves and reports the path of the
\"Program Files\" directory. See [RegRead example
#2](RegRead.htm#ExProgramFiles) for an alternative method.

    ProgramFilesDir := EnvGet(A_Is64bitOS ? "ProgramW6432" : "ProgramFiles")
    MsgBox "Program files are in: " ProgramFilesDir
:::

::: {#ExLocalAppData .ex}
[](#ExLocalAppData){.ex_number} Retrieves and reports the path of the
current user\'s Local AppData directory.

    LocalAppData := EnvGet("LocalAppData")
    MsgBox A_UserName "'s Local directory is located at: " LocalAppData
:::
