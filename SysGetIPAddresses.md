# SysGetIPAddresses

Returns an array of the system\'s IPv4 addresses.

``` Syntax
Addresses := SysGetIPAddresses()
```

## Parameters {#Parameters}

This function has no parameters.

## Return Value {#Return_Value}

Type: [Array](Array.htm)

This function returns an array, where each element is an IPv4 address
string such as \"192.168.0.1\".

## Remarks {#Remarks}

Currently only IPv4 is supported.

This function returns only the IP addresses of the computer\'s network
adapters. If the computer is connected to the Internet through a router,
this will not include the computer\'s public (Internet) IP address. To
determine the computer\'s public IP address, use an external web API.
For example:

    whr := ComObject("WinHttp.WinHttpRequest.5.1")
    whr.Open("GET", "https://api.ipify.org")
    whr.Send()
    MsgBox "Public IP address: " whr.ResponseText

## Related {#Related}

[A_ComputerName](../Variables.htm#ComputerName)

## Examples {#Examples}

::: {#ExBasic .ex}
[](#ExBasic){.ex_number} Retrieves and reports the system\'s IPv4
addresses.

    addresses := SysGetIPAddresses()
    msg := "IP addresses:`n"
    for n, address in addresses
        msg .= address "`n"
    MsgBox msg
:::
