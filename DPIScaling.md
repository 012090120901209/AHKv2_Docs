# DPI Scaling

DPI scaling is a function performed either by the operating system or by
the application, to increase the visual size of content proportionate to
the \"dots per inch\" setting of the display. Generally it allows
content to appear at the same physical size on systems with different
display resolutions, or to at least be usable on very high-resolution
displays. Sometimes a user may increase the DPI setting just to make
content larger and more comfortable to read.

[A_ScreenDPI](../Variables.htm#ScreenDPI) returns the DPI setting of the
primary screen.

There are two types of DPI scaling that relate to AutoHotkey: Gui DPI
Scaling and OS DPI Scaling.

## Gui DPI Scaling {#Gui_DPI_Scaling}

Automatic scaling is performed by the Gui and GuiControl
methods/properties by default, so that GUI scripts with hard-coded
positions, sizes and margins will tend to scale as appropriate on high
DPI screens. If this interferes with the script, or if the script will
do its own scaling, the automatic scaling can be disabled. For more
details, see the [-DPIScale](../lib/Gui.htm#DPIScale) option.

## OS DPI Scaling {#OS_DPI_Scaling}

For applications which are not DPI-aware, the operating system
automatically scales coordinates passed to and returned from certain
system functions. This type of scaling affects AutoHotkey only on
systems with multiple screens where not all screens have the same DPI
setting.

### Per-Monitor DPI Awareness {#Per-Monitor_DPI_Awareness}

On Windows 8.1 and later, secondary screens can have different DPI
settings, and \"per-monitor DPI-aware\" applications are expected to
scale their windows according to the DPI of whichever screen they are
currently on, adapting dynamically when the window moves between
screens.

For applications which are not per-monitor DPI-aware, the system
performs bitmap scaling to allow windows to change sizes when they move
between screens, and hides this from the application by reporting
coordinates and sizes scaled to the global DPI setting that the
application expects to have. For instance, on an 11 inch 4K screen, a
GUI designed to display at 96 dpi (100 %) would be almost impossible to
use, whereas upscaling it by 200 % would make it usable.

AutoHotkey is not designed to perform per-monitor scaling, and therefore
has not been marked as per-monitor DPI-aware. This is a boon, for
instance, when moving a GUI window between a large external screen with
100 % DPI and a smaller screen with 200 % DPI. However, automatic
scaling does have negative implications.

In order of the system\'s automatic scaling to work, system functions
such as
[MoveWindow](https://learn.microsoft.com/windows/win32/api/winuser/nf-winuser-movewindow)
and
[GetWindowRect](https://learn.microsoft.com/windows/win32/api/winuser/nf-winuser-getwindowrect)
automatically scale the coordinates that they accept or return. When
AutoHotkey uses these functions to work with external windows, this
often produces unexpected results if the coordinates are not on the
primary screen. To add further confusion, some functions scale
coordinates based on which screen the script\'s last active window was
displayed on.

## Workarounds {#Workarounds}

On Windows 10 version 1607 and later, the
[SetThreadDpiAwarenessContext](https://learn.microsoft.com/windows/win32/api/winuser/nf-winuser-setthreaddpiawarenesscontext)
system function can be used to change the program\'s DPI awareness
setting at runtime. For instance, enabling per-monitor DPI awareness
disables the scaling performed by the system, so built-in functions such
as [WinMove](../lib/WinMove.htm) and [WinGetPos](../lib/WinGetPos.htm)
will accept or return coordinates in pixels, untouched by DPI scaling.
However, if a GUI is sized for a screen with 100 % DPI and then moved to
a screen with 200 % DPI, it will not adjust automatically, and may be
very hard to use.

To enable per-monitor DPI awareness, call the following function prior
to using functions that are normally affected by DPI scaling:

    DllCall("SetThreadDpiAwarenessContext", "ptr", -3, "ptr")

On Windows 10 version 1703 and later, -3 can be replaced with -4 to
enable the \"Per Monitor v2\" mode. This enables scaling of dialogs,
menus, tooltips and some other things. However, it also causes the
non-client area (title bar) to scale, which may cause the window\'s
client area to be too small unless the script is designed to adjust for
it (such as by responding to the [WM_DPICHANGED
message](https://learn.microsoft.com/windows/win32/hidpi/wm-dpichanged)).
This can be avoided by setting the context to -3 before creating the
GUI, but -4 before creating any tooltips, menus or dialogs.

The thread\'s DPI awareness may temporarily change while the user is
moving one of the script\'s windows, or while the script is displaying a
dialog. Therefore, it is safest to set the DPI awareness immediately
before using any functions which rely on it.

### Compiled Scripts {#Compiled_Scripts}

Per-monitor DPI awareness can be enabled process-wide by changing the
content of the `<dpiAware>` element of the compiled script\'s manifest
resource from `true` (the default set in the base AutoHotkey executable
file) to `true/pm`.
