# Frequently Asked Questions (FAQ)

## Table of Contents {#toc}

**[General Troubleshooting](#general-troubleshooting)**

-   [What can I do if AutoHotkey won\'t install?](#install)
-   [How do I restore the right-click context menu options for .ahk
    files?](#rightclick)
-   [Why doesn\'t my script work on Windows *xxx* even though it worked
    on a previous version?](#vista)
-   [How do I work around problems caused by User Account Control
    (UAC)?](#uac)
-   [I can\'t edit my script via tray icon because it won\'t start due
    to an error. What should I do?](#DefaultScript)
-   [How can I find and fix errors in my code?](#Debug)
-   [Why is the Run function unable to launch my game or program?](#run)
-   [Why are the non-ASCII characters in my script displaying or sending
    incorrectly?](#nonascii)
-   [Why don\'t Hotstrings, Send, and Click work in certain
    games?](#games)
-   [How can performance be improved for games or at other times when
    the CPU is under heavy load?](#perf)
-   [My antivirus program flagged AutoHotkey or a compiled script as
    malware. Is it really a virus?](#Virus)

**[Common Tasks](#common-tasks)**

-   [Where can I find the official build, or older releases?](#Download)
-   [Can I run AHK from a USB drive?](#USB)
-   [How can the output of a command line operation be
    retrieved?](#output)
-   [How can a script close, pause, suspend or reload other
    script(s)?](#close)
-   [How can a repeating action be stopped without exiting the
    script?](#repeat)
-   [How can context sensitive help for AutoHotkey functions be used in
    any editor?](#help)
-   [How to detect when a web page is finished loading?](#load)
-   [How can dates and times be compared or manipulated?](#time)
-   [How can I send the current Date and/or Time?](#SendDate)
-   [How can I send text to a window which isn\'t active or isn\'t
    visible?](#ControlSend)
-   [How can Winamp be controlled even when it isn\'t active?](#winamp)
-   [How can MsgBox\'s button names be changed?](#msgbox)
-   [How can I change the default editor, which is accessible via
    context menu or tray icon?](#DefaultEditor)
-   [How can I save the contents of my GUI controls?](#GuiSubmit)
-   [Can I draw something with AHK?](#GDIPlus)
-   [How can I start an action when a window appears, closes or becomes
    \[in\]active?](#WinWaitAction)

**[Hotkeys, Hotstrings, and
Remapping](#hotkeys-hotstrings-and-remapping)**

-   [How do I put my hotkeys and hotstrings into effect automatically
    every time I start my PC?](#Startup)
-   [I\'m having trouble getting my mouse buttons working as hotkeys.
    Any advice?](#HotMouse)
-   [How can Tab and Space be defined as hotkeys?](#HotSymb)
-   [How can keys or mouse buttons be remapped so that they become
    different keys?](#Remap)
-   [How do I detect the double press of a key or button?](#DoublePress)
-   [How can a hotkey or hotstring be made exclusive to certain
    program(s)? In other words, I want a certain key to act as it
    normally does except when a specific window is active.](#HotContext)
-   [How can a prefix key be made to perform its native function rather
    than doing nothing?](#HotPrefix)
-   [How can the built-in Windows shortcut keys, such as Win+U (Utility
    Manager) and Win+R (Run), be changed or disabled?](#HotOverride)
-   [Can I use wildcards or regular expressions in
    Hotstrings?](#HotRegex)
-   [How can I use a hotkey that is not in my keyboard
    layout?](#SpecialKey)
-   [My keypad has a special 000 key. Is it possible to turn it into a
    hotkey?](#HotZero)

## General Troubleshooting

### What can I do if AutoHotkey won\'t install? {#install}

If AutoHotkey cannot be installed the normal way, see [How to Install
AutoHotkey](howto/Install.htm) for more help.

### How do I restore the right-click context menu options for .ahk files? {#rightclick}

Normally if AutoHotkey is installed, right-clicking an AutoHotkey script
(.ahk) file should give the following options:

-   Run script
-   Compile script (if Ahk2Exe is installed)
-   Edit script
-   Run as administrator
-   Run with UI access (if the
    [prerequisites](Program.htm#Installer_uiAccess) are met)

**Note:** On Windows 11, some of these options are usually relegated to
a submenu that can be accessed by selecting \"Show more options\".

Sometimes these options are overridden by settings in the current
user\'s profile, such as if *Open With* has been used to change the
default program for opening .ahk files. This can be fixed by deleting
the following registry key:

``` no-highlight
HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\FileExts\.ahk\UserChoice
```

This can be done by applying [this registry
patch](misc/remove-userchoice.reg){download="remove-userchoice.reg"} or
by running `UX\reset-assoc.ahk` from the AutoHotkey installation
directory.

It may also be necessary to repair the default registry values, either
by reinstalling AutoHotkey or by running `UX\install.ahk` from the
AutoHotkey installation directory.

### Why doesn\'t my script work on Windows *xxx* even though it worked on a previous version? {#vista}

There are many variations of this problem, such as:

-   I\'ve upgraded my computer/Windows and now my script won\'t work.
-   Hotkeys/hotstrings don\'t work when a program running as admin is
    active.
-   Some windows refuse to be automated (e.g. Device Manager ignores
    Send).

If you\'ve switched operating systems, it is likely that something else
has also changed and may be affecting your script. For instance, if
you\'ve got a new computer, it might have different drivers or other
software installed. If you\'ve also updated to a newer version of
AutoHotkey, find out which version you had before and then check the
[changelog](ChangeLog.htm) and [compatibility notes](Compat.htm).

Also refer to the following question:

### How do I work around problems caused by User Account Control (UAC)? {#uac}

By default, [User Account Control
(UAC)](https://en.wikipedia.org/wiki/User_Account_Control) protects
\"elevated\" programs (that is, programs which are running as admin)
from being automated by non-elevated programs, since that would allow
them to bypass security restrictions. Hotkeys are also blocked, so for
instance, a non-elevated program cannot spy on input intended for an
elevated program.

UAC may also prevent [SendPlay](lib/Send.htm#SendPlayDetail) and
[BlockInput](lib/BlockInput.htm) from working.

Common workarounds are as follows:

-   **Recommended:** [Run with UI
    access](Program.htm#Installer_uiAccess). This requires AutoHotkey to
    be installed under Program Files. There are several ways to do this,
    including:
    -   Right-click the script in Explorer and select *Run with UI
        access*.
    -   Use the *UIAccess* shell verb with Run, as in
        `Run '*UIAccess "Your script.ahk"'`.
    -   Use a [command line](Scripts.htm#cmd) such as
        `"AutoHotkey32_UIA.exe" "Your script.ahk"` (but include full
        paths where necessary).
    -   Set scripts to run with UI access by default, by checking the
        appropriate box in the [Launch
        Settings](Program.htm#launcher-config) GUI.
-   Run the script [as administrator](Variables.htm#IsAdmin). Note that
    this also causes any programs launched by the script to run as
    administrator, and may require the user to accept an approval prompt
    when launching the script.
-   Disable the local security policy \"Run all administrators in Admin
    Approval Mode\" (not recommended).
-   Disable UAC completely. This is not recommended, and is not feasible
    on Windows 8 or later.

### I can\'t edit my script via tray icon because it won\'t start due to an error. What should I do? {#DefaultScript}

You need to fix the error in your script before you can get your [tray
icon](Program.htm#tray-icon) back. This will require locating the script
and opening it in an editor by some other means than the tray icon.

If you are running an AutoHotkey executable file directly, the name of
the script depends on the executable. For example, if you are running
AutoHotkey32.exe, look for AutoHotkey32.ahk in the same directory. Note
that depending on your system settings the \".ahk\" part may be hidden,
but the file should have an icon like ![\[H\]](static/ahkfile16.png)

You can usually [edit a script file](Program.htm#edit) by right clicking
it and selecting *Edit Script*. If that doesn\'t work, you can open the
file in Notepad or another editor.

Normally, you should [create a script file](Program.htm#create)
(something.ahk) anywhere you like, and run that script file instead of
running AutoHotkey.

See also [Command Line Parameter \"Script
Filename\"](Scripts.htm#defaultfile) and [Portability of
AutoHotkey.exe](Program.htm#portability).

### How can I find and fix errors in my code? {#Debug}

For simple scripts, see [Debugging a Script](Scripts.htm#debug). To show
contents of a variable, use [MsgBox](lib/MsgBox.htm) or
[ToolTip](lib/ToolTip.htm). For complex scripts, see [Interactive
Debugging](Scripts.htm#idebug).

### Why is the [Run](lib/Run.htm) function unable to launch my game or program? {#run}

Some programs need to be started in their own directories (when in
doubt, it is usually best to do so). For example:

    Run A_ProgramFiles "\Some Application\App.exe", A_ProgramFiles "\Some Application"

If the program you are trying to start is in `A_WinDir "\System32"` and
you are using AutoHotkey 32-bit on a 64-bit system, the [File System
Redirector](https://learn.microsoft.com/windows/win32/winprog64/file-system-redirector)
may be interfering. To work around this, use `A_WinDir "\SysNative"`
instead; this is a virtual directory only visible to 32-bit programs
running on 64-bit systems.

### Why are the non-ASCII characters in my script displaying or sending incorrectly? {#nonascii}

Short answer: Save the script as UTF-8, preferably with BOM.

Non-ASCII characters are represented by different binary values
depending on the chosen encoding. In order for such characters to be
interpreted correctly, your text editor and AutoHotkey must be *on the
same codepage*, so to speak. AutoHotkey v2 defaults to UTF-8 for all
script files, although this can be overridden with the [/CP command line
switch](Scripts.htm#cp).

It is recommended to save the script as UTF-8 with BOM (byte order mark)
to ensure that editors (and maybe other applications) can determine with
certainty that the file is indeed UTF-8. Without BOM, the editor has to
guess the encoding of the file, which can sometimes be wrong.

To save as UTF-8 in Notepad, select *UTF-8* or *UTF-8 with BOM* from the
*Encoding* drop-down in the Save As dialog. Note that Notepad in Windows
10 v1903 and later defaults to *UTF-8* (without BOM).

To read other UTF-8 files which lack a byte order mark (BOM), use
[`FileEncoding`](lib/FileEncoding.htm)` "UTF-8-RAW"`, the `*P65001`
option with [FileRead](lib/FileRead.htm), or `"UTF-8-RAW"` for the third
parameter of [FileOpen](lib/FileOpen.htm). The `-RAW` suffix can be
omitted, but in that case any newly created files will have a BOM.

Note that INI files accessed with the standard INI functions do not
support UTF-8; they must be saved as ANSI or UTF-16.

### Why don\'t [Hotstrings](Hotstrings.htm), [Send](lib/Send.htm), and [Click](lib/Click.htm) work in certain games? {#games}

Not all games allow AHK to send keys and clicks or receive pixel colors.

But there are some alternatives, try all the solutions mentioned below.
If all these fail, it may not be possible for AHK to work with your
game. Sometimes games have a hack and cheat prevention measure, such as
GameGuard and Hackshield. If they do, there is a high chance that
AutoHotkey will not work with that game.

-   Use SendPlay via the [SendPlay](lib/Send.htm#SendPlay) function,
    [SendMode Play](lib/SendMode.htm#Play) and/or the [hotstring option
    SP](Hotstrings.htm#SP).

        SendPlay "abc"

        SendMode "Play"
        Send "abc"

        :SP:btw::by the way

        ; or

        #Hotstring SP
        ::btw::by the way

    **Deprecated:** SendPlay may have no effect at all on Windows 11 and
    later, or if [User Account Control
    (UAC)](https://en.wikipedia.org/wiki/User_Account_Control) is
    enabled, even if the script is running as an administrator.

-   Increase [SetKeyDelay](lib/SetKeyDelay.htm). For example:

        SetKeyDelay 0, 50
        SetKeyDelay 0, 50, "Play"

-   Try [ControlSend](lib/ControlSend.htm), which might work in cases
    where the other Send modes fail:

        ControlSend "abc",, GameTitle

-   Try the down and up event of a key with the various send methods:

        Send "{KEY Down}{KEY Up}"

-   Try the down and up event of a key with a [Sleep](lib/Sleep.htm)
    between them:

        Send "{KEY down}"
        Sleep 10 ; Try various milliseconds.
        Send "{KEY up}"

### How can performance be improved for games or at other times when the CPU is under heavy load? {#perf}

If a script\'s [Hotkeys](Hotkeys.htm), [Clicks](lib/Click.htm), or
[Sends](lib/Send.htm) are noticeably slower than normal while the CPU is
under heavy load, raising the script\'s process-priority may help. To do
this, include the following line near the top of the script:

    ProcessSetPriority "High"

### My antivirus program flagged AutoHotkey or a compiled script as malware. Is it really a virus? {#Virus}

Although it is certainly possible that the file has been infected, most
often these alerts are *false positives*, meaning that the antivirus
program is mistaken. One common suggestion is to upload the file to an
online service such as [virustotal](https://www.virustotal.com/) or
[Jotti](https://virusscan.jotti.org/) and see what other antivirus
programs have to say. If in doubt, you could send the file to the vendor
of your antivirus software for confirmation. This might also help us and
other AutoHotkey users, as the vendor may confirm it is a false positive
and fix their product to play nice with AutoHotkey.

False positives might be more common for compiled scripts which have
been compressed, such as with UPX (default for AutoHotkey 1.0 but not
1.1) or MPRESS (optional for AutoHotkey 1.1). As the default AutoHotkey
installation does not include a compressor, compiled scripts are not
compressed by default.

## Common Tasks

### Where can I find the official build, or older releases? {#Download}

See [download page of AutoHotkey](https://www.autohotkey.com/download/).

### Can I run AHK from a USB drive? {#USB}

See [Portability of AutoHotkey.exe](Program.htm#portability).

### How can the output of a command line operation be retrieved? {#output}

Testing shows that due to file caching, a temporary file can be very
fast for relatively small outputs. In fact, if the file is deleted
immediately after use, it often does not actually get written to disk.
For example:

    RunWait A_ComSpec ' /c dir > C:\My Temp File.txt'
    VarToContainContents := FileRead("C:\My Temp File.txt")
    FileDelete "C:\My Temp File.txt"

To avoid using a temporary file (especially if the output is large),
consider using the [Shell.Exec()](lib/Run.htm#ExStdOut) method as shown
in the examples for the [Run](lib/Run.htm) function.

### How can a script close, pause, suspend or reload other script(s)? {#close}

First, here is an example that closes another script:

    DetectHiddenWindows True  ; Allows a script's hidden main window to be detected.
    SetTitleMatchMode 2  ; Avoids the need to specify the full path of the file below.
    WinClose "ScriptFileName.ahk - AutoHotkey"  ; Update this to reflect the script's name (case-sensitive).

To [suspend](lib/Suspend.htm), [pause](lib/Pause.htm) or
[reload](lib/Reload.htm) another script, replace the last line above
with one of these:

    PostMessage 0x0111, 65305,,, "ScriptFileName.ahk - AutoHotkey"  ; Suspend.
    PostMessage 0x0111, 65306,,, "ScriptFileName.ahk - AutoHotkey"  ; Pause.
    PostMessage 0x0111, 65303,,, "ScriptFileName.ahk - AutoHotkey"  ; Reload.

### How can a repeating action be stopped without exiting the script? {#repeat}

To pause or resume the entire script at the press of a key, assign a
hotkey to the [Pause](lib/Pause.htm) function as in this example:

    ^!p::Pause  ; Press Ctrl+Alt+P to pause. Press it again to resume.

To stop an action that is repeating inside a [Loop](lib/Loop.htm),
consider the following working example, which is a hotkey that both
starts and stops its own repeating action. In other words, pressing the
hotkey once will start the loop. Pressing the same hotkey again will
stop it.

    #MaxThreadsPerHotkey 3
    #z::  ; Win+Z hotkey (change this hotkey to suit your preferences).
    {
        static KeepWinZRunning := false
        if KeepWinZRunning  ; This means an underlying thread is already running the loop below.
        {
            KeepWinZRunning := false  ; Signal that thread's loop to stop.
            return  ; End this thread so that the one underneath will resume and see the change made by the line above.
        }
        ; Otherwise:
        KeepWinZRunning := true
        Loop
        {
            ; The next four lines are the action you want to repeat (update them to suit your preferences):
            ToolTip "Press Win-Z again to stop this from flashing."
            Sleep 1000
            ToolTip
            Sleep 1000
            ; But leave the rest below unchanged.
            if not KeepWinZRunning  ; The user signaled the loop to stop by pressing Win-Z again.
                break  ; Break out of this loop.
        }
        KeepWinZRunning := false  ; Reset in preparation for the next press of this hotkey.
    }
    #MaxThreadsPerHotkey 1

### How can context sensitive help for AutoHotkey functions be used in any editor? {#help}

Rajat created [this script](scripts/index.htm#ContextSensitiveHelp).

### How to detect when a web page is finished loading? {#load}

With Internet Explorer, perhaps the most reliable method is to use
DllCall and COM as demonstrated at [this archived forum
thread](https://www.autohotkey.com/board/topic/17715-). On a related
note, the contents of the address bar and status bar can be retrieved as
demonstrated at [this archived forum
thread](https://www.autohotkey.com/board/topic/17714-).

**Older, less reliable method:** The technique in the following example
will work with MS Internet Explorer for most pages. A similar technique
might work in other browsers:

    Run "www.yahoo.com"
    MouseMove 0, 0  ; Prevents the status bar from showing a mouse-hover link instead of "Done".
    WinWait "Yahoo! - "
    WinActivate
    if StatusBarWait("Done", 30)
        MsgBox "The page is done loading."
    else
        MsgBox "The wait timed out or the window was closed."

### How can dates and times be compared or manipulated? {#time}

The [DateAdd](lib/DateAdd.htm) function can add or subtract a quantity
of days, hours, minutes, or seconds to a time-string that is in the
[YYYYMMDDHH24MISS](lib/FileSetTime.htm#YYYYMMDD) format. The following
example subtracts 7 days from the specified time:

    Result := DateAdd(VarContainingTimestamp, -7, "days")

To determine the amount of time between two dates or times, see
[DateDiff](lib/DateDiff.htm), which gives an example. Also, the built-in
variable [A_Now](Variables.htm#Now) contains the current local time.
Finally, there are several built-in [date/time
variables](Variables.htm#date), as well as the
[FormatTime](lib/FormatTime.htm) function to create a custom date/time
string.

### How can I send the current Date and/or Time? {#SendDate}

Use [FormatTime](lib/FormatTime.htm) or [built-in variables for date and
time](Variables.htm#date).

### How can I send text to a window which isn\'t active or isn\'t visible? {#ControlSend}

Use [ControlSend](lib/ControlSend.htm).

### How can Winamp be controlled even when it isn\'t active? {#winamp}

See [Automating Winamp](misc/Winamp.htm).

### How can [MsgBox](lib/MsgBox.htm)\'s button names be changed? {#msgbox}

Here is an [example](scripts/index.htm#MsgBoxButtonNames).

### How can I change the default editor, which is accessible via context menu or tray icon? {#DefaultEditor}

In the example section of [Edit](lib/Edit.htm) you will find a script
that allows you to change the default editor.

### How can I save the contents of my GUI controls? {#GuiSubmit}

Use [Gui.Submit](lib/Gui.htm#Submit). For Example:

    MyGui := Gui()
    MyGui.Add("Text",, "Enter some Text and press Submit:")
    MyGui.Add("Edit", "vMyEdit")
    MyGui.Add("Button",, "Submit").OnEvent("Click", Submit)
    MyGui.Show()

    Submit(*)
    {
        Saved := MyGui.Submit(false)
        MsgBox "Content of the edit control: " Saved.MyEdit
    }

### Can I draw something with AHK? {#GDIPlus}

See [GDI+ standard
library](https://www.autohotkey.com/boards/viewtopic.php?t=6517) by tic.
It\'s also possible with some rudimentary methods using Gui, but in a
limited way.

### How can I start an action when a window appears, closes or becomes \[in\]active? {#WinWaitAction}

Use [WinWait](lib/WinWait.htm), [WinWaitClose](lib/WinWaitClose.htm) or
[WinWait\[Not\]Active](lib/WinWaitActive.htm).

There are also user-created solutions such as
[OnWin.ahk](https://www.autohotkey.com/boards/viewtopic.php?f=6&t=6463)
and [\[How to\] Hook on to Shell to receive its
messages](https://www.autohotkey.com/board/topic/80644-how-to-hook-on-to-shell-to-receive-its-messages/)
on the archived forum.

## Hotkeys, Hotstrings, and Remapping

### How do I put my hotkeys and hotstrings into effect automatically every time I start my PC? {#Startup}

There are several ways to make a script (or any program) launch
automatically every time you start your PC. The easiest is to place a
shortcut to the script in the Startup folder:

1.  Find the script file, select it, and press [Ctrl]{.kbd}+[C]{.kbd}.
2.  Press [Win]{.kbd}+[R]{.kbd} to open the Run dialog, then enter
    `shell:startup` and click OK or [Enter]{.kbd}. This will open the
    Startup folder for the current user. To instead open the folder for
    all users, enter `shell:common startup` (however, in that case you
    must be an administrator to proceed).
3.  Right click inside the window, and click \"Paste Shortcut\". The
    shortcut to the script should now be in the Startup folder.

### I\'m having trouble getting my mouse buttons working as hotkeys. Any advice? {#HotMouse}

The left and right mouse buttons should be assignable normally (for
example, `#LButton::` is the [Win]{.kbd}+LeftButton hotkey). Similarly,
the middle button and the turning of the [mouse wheel](KeyList.htm)
should be assignable normally except on mice whose drivers directly
control those buttons.

The fourth button (XButton1) and the fifth button (XButton2) might be
assignable if your mouse driver allows their clicks to be
[seen](lib/KeyHistory.htm) by the system. If they cannot be seen \-- or
if your mouse has more than five buttons that you want to use \-- you
can try configuring the software that came with the mouse (sometimes
accessible in the Control Panel or Start Menu) to send a keystroke
whenever you press one of these buttons. Such a keystroke can then be
defined as a hotkey in a script. For example, if you configure the
fourth button to send [Ctrl]{.kbd}+[F1]{.kbd}, you can then indirectly
configure that button as a hotkey by using `^F1::` in a script.

If you have a five-button mouse whose fourth and fifth buttons cannot be
[seen](lib/KeyHistory.htm), you can try changing your mouse driver to
the default driver included with the OS. This assumes there is such a
driver for your particular mouse and that you can live without the
features provided by your mouse\'s custom software.

### How can Tab and Space be defined as hotkeys? {#HotSymb}

Use the names of the keys (Tab and Space) rather than their characters.
For example, `#Space` is [Win]{.kbd}+[Space]{.kbd} and `^!Tab` is
[Ctrl]{.kbd}+[Alt]{.kbd}+[Tab]{.kbd}.

### How can keys or mouse buttons be remapped so that they become different keys? {#Remap}

This is described on the [remapping](misc/Remap.htm) page.

### How do I detect the double press of a key or button? {#DoublePress}

Use [built-in variables for hotkeys](Variables.htm#h) as follows:

    ~Ctrl::
    {
        if (ThisHotkey = A_PriorHotkey && A_TimeSincePriorHotkey < 200)
            MsgBox "double-press"
    }

### How can a [hotkey](Hotkeys.htm) or [hotstring](Hotstrings.htm) be made exclusive to certain program(s)? In other words, I want a certain key to act as it normally does except when a specific window is active. {#HotContext}

The preferred method is [#HotIf](lib/_HotIf.htm). For example:

    #HotIf WinActive("ahk_class Notepad")
    ^a::MsgBox "You pressed Control-A while Notepad is active."

### How can a prefix key be made to perform its native function rather than doing nothing? {#HotPrefix}

Consider the following example, which makes Numpad0 into a prefix key:

    Numpad0 & Numpad1::MsgBox "You pressed Numpad1 while holding down Numpad0."

Now, to make Numpad0 send a real Numpad0 keystroke whenever it wasn\'t
used to launch a hotkey such as the above, add the following hotkey:

     $Numpad0::Send "{Numpad0}"

The \$ prefix is needed to prevent a warning dialog about an infinite
loop (since the hotkey \"sends itself\"). In addition, the above action
occurs at the time the key is **released**.

### How can the built-in Windows shortcut keys, such as Win+U (Utility Manager) and Win+R (Run), be changed or disabled? {#HotOverride}

Here are some [examples](misc/Override.htm).

### Can I use wildcards or regular expressions in Hotstrings? {#HotRegex}

Use the
[script](https://github.com/polyethene/AutoHotkey-Scripts/blob/master/Hotstrings.ahk)
by polyethene (examples are included).

### How can I use a hotkey that is not in my keyboard layout? {#SpecialKey}

See [Special Keys](KeyList.htm#SpecialKeys).

### My keypad has a special 000 key. Is it possible to turn it into a hotkey? {#HotZero}

You can. This [example script](scripts/index.htm#Numpad000) makes
[000]{.kbd} into an equals key. You can change the action by replacing
the `Send "="` line with line(s) of your choice.
