# Monitor Functions

Functions for retrieving screen resolution and multi-monitor info. Click
on a function name for details.

  Function                                       Description
  ---------------------------------------------- ---------------------------------------------------------------------------------------------------------------
  [MonitorGet](MonitorGet.htm)                   Checks if the specified monitor exists and optionally retrieves its bounding coordinates.
  [MonitorGetCount](MonitorGetCount.htm)         Returns the total number of monitors.
  [MonitorGetName](MonitorGetName.htm)           Returns the operating system\'s name of the specified monitor.
  [MonitorGetPrimary](MonitorGetPrimary.htm)     Returns the number of the primary monitor.
  [MonitorGetWorkArea](MonitorGetWorkArea.htm)   Checks if the specified monitor exists and optionally retrieves the bounding coordinates of its working area.

## Remarks {#Remarks}

The built-in variables [A_ScreenWidth](../Variables.htm#Screen) and
[A_ScreenHeight](../Variables.htm#Screen) contain the dimensions of the
primary monitor, in pixels.

[SysGet](SysGet.htm) can be used to retrieve the bounding rectangle of
all display monitors. For example, this retrieves the width and height
of the virtual screen:

    MsgBox SysGet(78) " x " SysGet(79)

## Related {#Related}

[DllCall](DllCall.htm), [Win functions](Win.htm), [SysGet](SysGet.htm)

## Examples {#Examples}

::: {#ExLoopAll .ex}
[](#ExLoopAll){.ex_number} Displays info about each monitor.

    MonitorCount := MonitorGetCount()
    MonitorPrimary := MonitorGetPrimary()
    MsgBox "Monitor Count:`t" MonitorCount "`nPrimary Monitor:`t" MonitorPrimary
    Loop MonitorCount
    {
        MonitorGet A_Index, &L, &T, &R, &B
        MonitorGetWorkArea A_Index, &WL, &WT, &WR, &WB
        MsgBox
        (
            "Monitor:`t#" A_Index "
            Name:`t" MonitorGetName(A_Index) "
            Left:`t" L " (" WL " work)
            Top:`t" T " (" WT " work)
            Right:`t" R " (" WR " work)
            Bottom:`t" B " (" WB " work)"
        )
    }
:::
