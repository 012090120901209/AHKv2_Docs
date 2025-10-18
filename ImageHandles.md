# Image Handles

To use an icon or bitmap handle in place of an image filename, use the
following syntax:

``` Syntax
HBITMAP:BitmapHandle
HICON:IconHandle
```

Replace *BitmapHandle* or *IconHandle* with the actual handle value. For
example, `"hicon:" handle`, where *handle* is a variable containing an
icon handle.

The following things support this syntax:

-   [Gui.AddPicture](../lib/GuiControls.htm#Picture) (and
    [GuiControl.Value](../lib/GuiControl.htm#Value) when setting a
    Picture control\'s content).
-   [IL_Add](../lib/ListView.htm#IL_Add)
-   [LoadPicture](../lib/LoadPicture.htm)
-   [SB.SetIcon](../lib/GuiControls.htm#SB_SetIcon)
-   [ImageSearch](../lib/ImageSearch.htm)
-   [TraySetIcon](../lib/TraySetIcon.htm) or
    [Menu.SetIcon](../lib/Menu.htm#SetIcon)

A bitmap or icon handle is a numeric value which identifies a bitmap or
icon in memory. The majority of scripts never need to deal with handles,
as in most cases AutoHotkey takes care of loading the image from file
and freeing it when it is no longer needed. The syntax shown above is
intended for use when the script obtains an icon or bitmap handle from
another source, such as by sending the WM_GETICON message to a window.
It can also be used in combination with
[LoadPicture](../lib/LoadPicture.htm) to avoid loading an image from
file multiple times.

By default, AutoHotkey treats the handle as though it loaded the image
from file - for example, a bitmap used on a Picture control is deleted
when the GUI is destroyed, and an image will generally be deleted
immediately if it needs to be resized. To avoid this, put an asterisk
between the colon and handle. For example: `"hbitmap:*" handle`. With
the exception of ImageSearch, this forces the function to take a copy of
the image.

## Examples {#Examples}

::: {#ExHICON .ex}
[](#ExHICON){.ex_number} Shows a menu of the first *n* files matching a
pattern, and their icons.

    pattern := A_ScriptDir "\*"
    n := 15

    ; Create a menu.
    Fmenu := Menu()

    ; Allocate memory for a SHFILEINFOW struct.
    fileinfo := Buffer(fisize := A_PtrSize + 688)

    Loop Files, pattern, "FD"
    {
        ; Add a menu item for each file.
        Fmenu.Add(A_LoopFileName, (*) => "") ; Do nothing.
        
        ; Get the file's icon.
        if DllCall("shell32\SHGetFileInfoW", "WStr", A_LoopFileFullPath
            , "UInt", 0, "Ptr", fileinfo, "UInt", fisize, "UInt", 0x100)
        {
            hicon := NumGet(fileinfo, 0, "Ptr")
            ; Set the menu item's icon.
            Fmenu.SetIcon(A_Index "&", "HICON:" hicon)
            ; Because we used ":" and not ":*", the icon will be automatically
            ; freed when the program exits or if the menu or item is deleted.
        }
    }
    until A_Index = n
    Fmenu.Show()
:::

See also [LoadPicture example #1](../lib/LoadPicture.htm#ExSlideShow).
