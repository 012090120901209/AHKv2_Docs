# Alphabetical Function Index

Click on a function name for details. Entries in [large font]{.larger}
are the most commonly used.

Go to entries starting with: [E](#E),   [I](#I),   [M](#M),   [S](#S),  
[W](#W),   [\#](#hash)

+-----------------------------------+-----------------------------------+
| Name                              | Description                       |
+===================================+===================================+
| [{ \... } (Block)](Block.htm)     | Blocks are one or more            |
|                                   | [state                            |
|                                   | ments](../Concepts.htm#statement) |
|                                   | enclosed in braces. Typically     |
|                                   | used with [function               |
|                                   | defi                              |
|                                   | nitions](../Functions.htm#define) |
|                                   | and [control flow                 |
|                                   | statement                         |
|                                   | s](../Language.htm#control-flow). |
+-----------------------------------+-----------------------------------+
| [{ \... } /                       | Creates an [Object](Object.htm)   |
| Obje                              | from a list of property name and  |
| ct](../Objects.htm#Usage_Objects) | value pairs.                      |
+-----------------------------------+-----------------------------------+
| [\[ \... \] /                     | Creates an [Array](Array.htm)     |
| Array](..                         | from a sequence of parameter      |
| /Objects.htm#Usage_Simple_Arrays) | values.                           |
+-----------------------------------+-----------------------------------+
| [Abs](Math.htm#Abs)               | Returns the absolute value of the |
|                                   | specified number.                 |
+-----------------------------------+-----------------------------------+
| [ASin](Math.htm#ASin)             | Returns the arcsine (the number   |
|                                   | whose sine is the specified       |
|                                   | number) in radians.               |
+-----------------------------------+-----------------------------------+
| [ACos](Math.htm#ACos)             | Returns the arccosine (the number |
|                                   | whose cosine is the specified     |
|                                   | number) in radians.               |
+-----------------------------------+-----------------------------------+
| [ATan](Math.htm#ATan)             | Returns the arctangent (the       |
|                                   | number whose tangent is the       |
|                                   | specified number) in radians.     |
+-----------------------------------+-----------------------------------+
| [BlockInput](BlockInput.htm)      | Disables or enables the user\'s   |
|                                   | ability to interact with the      |
|                                   | computer via keyboard and mouse.  |
+-----------------------------------+-----------------------------------+
| [Break](Break.htm)                | Exits (terminates) any type of    |
|                                   | [loop                             |
|                                   | statement]                        |
|                                   | (../Language.htm#loop-statement). |
+-----------------------------------+-----------------------------------+
| [Buffer](Buffer.htm#Call)         | Creates a Buffer, which           |
|                                   | encapsulates a block of memory    |
|                                   | for use with other functions.     |
+-----------------------------------+-----------------------------------+
| [Ca                               | Creates a machine-code address    |
| llbackCreate](CallbackCreate.htm) | that when called, redirects the   |
|                                   | call to a                         |
|                                   | [function](../Functions.htm) in   |
|                                   | the script.                       |
+-----------------------------------+-----------------------------------+
| [CallbackFree]                    | Deletes a callback and releases   |
| (CallbackCreate.htm#CallbackFree) | its reference to the function     |
|                                   | object.                           |
+-----------------------------------+-----------------------------------+
| [CaretGetPos](CaretGetPos.htm)    | Retrieves the current position of |
|                                   | the caret (text insertion point). |
+-----------------------------------+-----------------------------------+
| [Catch](Catch.htm)                | Specifies one or more             |
|                                   | [state                            |
|                                   | ments](../Concepts.htm#statement) |
|                                   | to execute if a value or error is |
|                                   | thrown during execution of a      |
|                                   | [Try](Try.htm) statement.         |
+-----------------------------------+-----------------------------------+
| [Ceil](Math.htm#Ceil)             | Returns the specified number      |
|                                   | rounded up to the nearest integer |
|                                   | (without any .00 suffix).         |
+-----------------------------------+-----------------------------------+
| [Chr](Chr.htm)                    | Returns the string (usually a     |
|                                   | single character) corresponding   |
|                                   | to the character code indicated   |
|                                   | by the specified number.          |
+-----------------------------------+-----------------------------------+
| [Click](Click.htm)                | Clicks a mouse button at the      |
|                                   | specified coordinates. It can     |
|                                   | also hold down a mouse button,    |
|                                   | turn the mouse wheel, or move the |
|                                   | mouse.                            |
+-----------------------------------+-----------------------------------+
| [ClipboardAll](ClipboardAll.htm)  | Creates an object containing      |
|                                   | everything on the clipboard (such |
|                                   | as pictures and formatting).      |
+-----------------------------------+-----------------------------------+
| [ClipWait](ClipWait.htm)          | Waits until the                   |
|                                   | [clipboard](A_Clipboard.htm)      |
|                                   | contains data.                    |
+-----------------------------------+-----------------------------------+
| [ComCall](ComCall.htm)            | Calls a native COM interface      |
|                                   | method by index.                  |
+-----------------------------------+-----------------------------------+
| [ComObjActive](ComObjActive.htm)  | Retrieves a registered COM        |
|                                   | object.                           |
+-----------------------------------+-----------------------------------+
| [ComObjArray](ComObjArray.htm)    | Creates a SafeArray for use with  |
|                                   | COM.                              |
+-----------------------------------+-----------------------------------+
| [                                 | Connects a COM object\'s event    |
| ComObjConnect](ComObjConnect.htm) | source to the script, enabling    |
|                                   | events to be handled.             |
+-----------------------------------+-----------------------------------+
| [ComObject](ComObject.htm)        | Creates a COM object.             |
+-----------------------------------+-----------------------------------+
| [ComObjFlags](ComObjFlags.htm)    | Retrieves or changes flags which  |
|                                   | control a COM wrapper object\'s   |
|                                   | behaviour.                        |
+-----------------------------------+-----------------------------------+
| [                                 | Wraps a raw                       |
| ComObjFromPtr](ComObjFromPtr.htm) | [IDispatch](https                 |
|                                   | ://learn.microsoft.com/windows/wi |
|                                   | n32/api/oaidl/nn-oaidl-idispatch) |
|                                   | pointer (COM object) for use by   |
|                                   | the script.                       |
+-----------------------------------+-----------------------------------+
| [ComObjGet](ComObjGet.htm)        | Returns a reference to an object  |
|                                   | provided by a COM component.      |
+-----------------------------------+-----------------------------------+
| [ComObjQuery](ComObjQuery.htm)    | Queries a COM object for an       |
|                                   | interface or service.             |
+-----------------------------------+-----------------------------------+
| [ComObjType](ComObjType.htm)      | Retrieves type information from a |
|                                   | COM object.                       |
+-----------------------------------+-----------------------------------+
| [ComObjValue](ComObjValue.htm)    | Retrieves the value or pointer    |
|                                   | stored in a COM wrapper object.   |
+-----------------------------------+-----------------------------------+
| [ComValue](ComValue.htm)          | Wraps a value, SafeArray or COM   |
|                                   | object for use by the script or   |
|                                   | for passing to a COM method.      |
+-----------------------------------+-----------------------------------+
| [Continue](Continue.htm)          | Skips the rest of a [loop         |
|                                   | statement](.                      |
|                                   | ./Language.htm#loop-statement)\'s |
|                                   | current iteration and begins a    |
|                                   | new one.                          |
+-----------------------------------+-----------------------------------+
| [Co                               | Adds the specified string as a    |
| ntrolAddItem](ControlAddItem.htm) | new entry at the bottom of a      |
|                                   | ListBox or ComboBox.              |
+-----------------------------------+-----------------------------------+
| [ControlCho                       | Sets the selection in a ListBox,  |
| oseIndex](ControlChooseIndex.htm) | ComboBox or Tab control to be the |
|                                   | Nth item.                         |
+-----------------------------------+-----------------------------------+
| [ControlChoos                     | Sets the selection in a ListBox   |
| eString](ControlChooseString.htm) | or ComboBox to be the first entry |
|                                   | whose leading part matches the    |
|                                   | specified string.                 |
+-----------------------------------+-----------------------------------+
| [ControlClick](ControlClick.htm)  | Sends a mouse button or mouse     |
|                                   | wheel event to a control.         |
+-----------------------------------+-----------------------------------+
| [ControlD                         | Deletes the specified entry       |
| eleteItem](ControlDeleteItem.htm) | number from a ListBox or          |
|                                   | ComboBox.                         |
+-----------------------------------+-----------------------------------+
| [Cont                             | Returns the entry number of a     |
| rolFindItem](ControlFindItem.htm) | ListBox or ComboBox that is a     |
|                                   | complete match for the specified  |
|                                   | string.                           |
+-----------------------------------+-----------------------------------+
| [ControlFocus](ControlFocus.htm)  | Sets input focus to a given       |
|                                   | control on a window.              |
+-----------------------------------+-----------------------------------+
| [ControlG                         | Returns a non-zero value if the   |
| etChecked](ControlGetChecked.htm) | checkbox or radio button is       |
|                                   | checked.                          |
+-----------------------------------+-----------------------------------+
| [Contro                           | Returns the name of the currently |
| lGetChoice](ControlGetChoice.htm) | selected entry in a ListBox or    |
|                                   | ComboBox.                         |
+-----------------------------------+-----------------------------------+
| [ControlG                         | Returns the ClassNN (class name   |
| etClassNN](ControlGetClassNN.htm) | and sequence number) of the       |
|                                   | specified control.                |
+-----------------------------------+-----------------------------------+
| [ControlG                         | Returns a non-zero value if the   |
| etEnabled](ControlGetEnabled.htm) | specified control is enabled.     |
+-----------------------------------+-----------------------------------+
| [Cont                             | Retrieves which control of the    |
| rolGetFocus](ControlGetFocus.htm) | target window has keyboard focus, |
|                                   | if any.                           |
+-----------------------------------+-----------------------------------+
| [Co                               | Returns the unique ID number of   |
| ntrolGetHwnd](ControlGetHwnd.htm) | the specified control.            |
+-----------------------------------+-----------------------------------+
| [Cont                             | Returns the index of the          |
| rolGetIndex](ControlGetIndex.htm) | currently selected entry or tab   |
|                                   | in a ListBox, ComboBox or Tab     |
|                                   | control.                          |
+-----------------------------------+-----------------------------------+
| [Cont                             | Returns an array of items/rows    |
| rolGetItems](ControlGetItems.htm) | from a ListBox, ComboBox, or      |
|                                   | DropDownList.                     |
+-----------------------------------+-----------------------------------+
| [                                 | Retrieves the position and size   |
| ControlGetPos](ControlGetPos.htm) | of a control.                     |
+-----------------------------------+-----------------------------------+
| [ControlGetStyle\                 | Returns an integer representing   |
| Contro                            | the style or extended style of    |
| lGetExStyle](ControlGetStyle.htm) | the specified control.            |
+-----------------------------------+-----------------------------------+
| [Co                               | Retrieves text from a control.    |
| ntrolGetText](ControlGetText.htm) |                                   |
+-----------------------------------+-----------------------------------+
| [ControlG                         | Returns a non-zero value if the   |
| etVisible](ControlGetVisible.htm) | specified control is visible.     |
+-----------------------------------+-----------------------------------+
| [ControlHide](ControlHide.htm)    | Hides the specified control.      |
+-----------------------------------+-----------------------------------+
| [ControlHideD                     | Hides the drop-down list of a     |
| ropDown](ControlHideDropDown.htm) | ComboBox control.                 |
+-----------------------------------+-----------------------------------+
| [ControlMove](ControlMove.htm)    | Moves or resizes a control.       |
+-----------------------------------+-----------------------------------+
| [ControlSend\                     | Sends simulated keystrokes or     |
| ControlSendText](ControlSend.htm) | text to a window or control.      |
+-----------------------------------+-----------------------------------+
| [ControlS                         | Turns on (checks) or turns off    |
| etChecked](ControlSetChecked.htm) | (unchecks) a checkbox or radio    |
|                                   | button.                           |
+-----------------------------------+-----------------------------------+
| [ControlS                         | Enables or disables the specified |
| etEnabled](ControlSetEnabled.htm) | control.                          |
+-----------------------------------+-----------------------------------+
| [ControlSetStyle\                 | Changes the style or extended     |
| Contro                            | style of the specified control,   |
| lSetExStyle](ControlSetStyle.htm) | respectively.                     |
+-----------------------------------+-----------------------------------+
| [Co                               | Changes the text of a control.    |
| ntrolSetText](ControlSetText.htm) |                                   |
+-----------------------------------+-----------------------------------+
| [ControlShow](ControlShow.htm)    | Shows the specified control if it |
|                                   | was previously hidden.            |
+-----------------------------------+-----------------------------------+
| [ControlShowD                     | Shows the drop-down list of a     |
| ropDown](ControlShowDropDown.htm) | ComboBox control.                 |
+-----------------------------------+-----------------------------------+
| [CoordMode](CoordMode.htm)        | Sets coordinate mode for various  |
|                                   | built-in functions to be relative |
|                                   | to either the active window or    |
|                                   | the screen.                       |
+-----------------------------------+-----------------------------------+
| [Cos](Math.htm#Cos)               | Returns the trigonometric cosine  |
|                                   | of the specified number.          |
+-----------------------------------+-----------------------------------+
| [Critical](Critical.htm)          | Prevents the [current             |
|                                   | thread](../misc/Threads.htm) from |
|                                   | being interrupted by other        |
|                                   | threads, or enables it to be      |
|                                   | interrupted.                      |
+-----------------------------------+-----------------------------------+
| [DateAdd](DateAdd.htm)            | Adds or subtracts time from a     |
|                                   | [dat                              |
|                                   | e-time](FileSetTime.htm#YYYYMMDD) |
|                                   | value.                            |
+-----------------------------------+-----------------------------------+
| [DateDiff](DateDiff.htm)          | Compares two                      |
|                                   | [dat                              |
|                                   | e-time](FileSetTime.htm#YYYYMMDD) |
|                                   | values and returns the            |
|                                   | difference.                       |
+-----------------------------------+-----------------------------------+
| [Detect                           | Determines whether invisible text |
| HiddenText](DetectHiddenText.htm) | in a window is \"seen\" for the   |
|                                   | purpose of finding the window.    |
|                                   | This affects windowing functions  |
|                                   | such as [WinExist](WinExist.htm)  |
|                                   | and                               |
|                                   | [WinActivate](WinActivate.htm).   |
+-----------------------------------+-----------------------------------+
| [DetectHidden                     | Determines whether invisible      |
| Windows](DetectHiddenWindows.htm) | windows are \"seen\" by the       |
|                                   | script.                           |
+-----------------------------------+-----------------------------------+
| [DirCopy](DirCopy.htm)            | Copies a folder along with all    |
|                                   | its sub-folders and files         |
|                                   | (similar to xcopy) or the entire  |
|                                   | contents of an archive file such  |
|                                   | as ZIP.                           |
+-----------------------------------+-----------------------------------+
| [DirCreate](DirCreate.htm)        | Creates a folder.                 |
+-----------------------------------+-----------------------------------+
| [DirDelete](DirDelete.htm)        | Deletes a folder.                 |
+-----------------------------------+-----------------------------------+
| [DirExist](DirExist.htm)          | Checks for the existence of a     |
|                                   | folder and returns its            |
|                                   | attributes.                       |
+-----------------------------------+-----------------------------------+
| [DirMove](DirMove.htm)            | Moves a folder along with all its |
|                                   | sub-folders and files. It can     |
|                                   | also rename a folder.             |
+-----------------------------------+-----------------------------------+
| [DirSelect](DirSelect.htm)        | Displays a standard dialog that   |
|                                   | allows the user to select a       |
|                                   | folder.                           |
+-----------------------------------+-----------------------------------+
| [DllCall](DllCall.htm)            | Calls a function inside a DLL,    |
|                                   | such as a standard Windows API    |
|                                   | function.                         |
+-----------------------------------+-----------------------------------+
| [Download](Download.htm)          | Downloads a file from the         |
|                                   | Internet.                         |
+-----------------------------------+-----------------------------------+
| [DriveEject](DriveEject.htm)      | Ejects the tray of the specified  |
|                                   | CD/DVD drive, or ejects a         |
|                                   | removable drive.                  |
+-----------------------------------+-----------------------------------+
| [DriveG                           | Returns the total capacity of the |
| etCapacity](DriveGetCapacity.htm) | drive which contains the          |
|                                   | specified path, in megabytes.     |
+-----------------------------------+-----------------------------------+
| [DriveGetFi                       | Returns the type of the specified |
| leSystem](DriveGetFileSystem.htm) | drive\'s file system.             |
+-----------------------------------+-----------------------------------+
| [                                 | Returns the volume label of the   |
| DriveGetLabel](DriveGetLabel.htm) | specified drive.                  |
+-----------------------------------+-----------------------------------+
| [DriveGetList](DriveGetList.htm)  | Returns a string of letters, one  |
|                                   | character for each drive letter   |
|                                   | in the system.                    |
+-----------------------------------+-----------------------------------+
| [Dr                               | Returns the volume serial number  |
| iveGetSerial](DriveGetSerial.htm) | of the specified drive.           |
+-----------------------------------+-----------------------------------+
| [DriveGet                         | Returns the free disk space of    |
| SpaceFree](DriveGetSpaceFree.htm) | the drive which contains the      |
|                                   | specified path, in megabytes.     |
+-----------------------------------+-----------------------------------+
| [Dr                               | Returns the status of the drive   |
| iveGetStatus](DriveGetStatus.htm) | which contains the specified      |
|                                   | path.                             |
+-----------------------------------+-----------------------------------+
| [DriveG                           | Returns the media status of the   |
| etStatusCD](DriveGetStatusCD.htm) | specified CD/DVD drive.           |
+-----------------------------------+-----------------------------------+
| [DriveGetType](DriveGetType.htm)  | Returns the type of the drive     |
|                                   | which contains the specified      |
|                                   | path.                             |
+-----------------------------------+-----------------------------------+
| [DriveLock](DriveLock.htm)        | Prevents the eject feature of the |
|                                   | specified drive from working.     |
+-----------------------------------+-----------------------------------+
| [DriveRetract](DriveEject.htm)    | Retracts the tray of the          |
|                                   | specified CD/DVD drive.           |
+-----------------------------------+-----------------------------------+
| [                                 | Changes the volume label of the   |
| DriveSetLabel](DriveSetLabel.htm) | specified drive.                  |
+-----------------------------------+-----------------------------------+
| [DriveUnlock](DriveUnlock.htm)    | Restores the eject feature of the |
|                                   | specified drive.                  |
+-----------------------------------+-----------------------------------+
| [Edit](Edit.htm)                  | Opens the current script for      |
|                                   | editing in the default editor.    |
+-----------------------------------+-----------------------------------+
| [EditGetC                         | Returns the column number in an   |
| urrentCol](EditGetCurrentCol.htm) | Edit control where the caret      |
|                                   | (text insertion point) resides.   |
+-----------------------------------+-----------------------------------+
| [EditGetCur                       | Returns the line number in an     |
| rentLine](EditGetCurrentLine.htm) | Edit control where the caret      |
|                                   | (text insert point) resides.      |
+-----------------------------------+-----------------------------------+
| [EditGetLine](EditGetLine.htm)    | Returns the text of the specified |
|                                   | line in an Edit control.          |
+-----------------------------------+-----------------------------------+
| [EditGe                           | Returns the number of lines in an |
| tLineCount](EditGetLineCount.htm) | Edit control.                     |
+-----------------------------------+-----------------------------------+
| [EditGetSelec                     | Returns the selected text in an   |
| tedText](EditGetSelectedText.htm) | Edit control.                     |
+-----------------------------------+-----------------------------------+
| [EditPaste](EditPaste.htm)        | Pastes the specified string at    |
|                                   | the caret (text insertion point)  |
|                                   | in an Edit control.               |
+-----------------------------------+-----------------------------------+
| [Else](Else.htm)                  | Specifies one or more             |
|                                   | [state                            |
|                                   | ments](../Concepts.htm#statement) |
|                                   | to execute if the associated      |
|                                   | statement\'s body did not         |
|                                   | execute.                          |
+-----------------------------------+-----------------------------------+
| [EnvGet](EnvGet.htm)              | Retrieves the value of the        |
|                                   | specified [environment            |
|                                   | variable](../Con                  |
|                                   | cepts.htm#environment-variables). |
+-----------------------------------+-----------------------------------+
| [EnvSet](EnvSet.htm)              | Writes a value to the specified   |
|                                   | [environment                      |
|                                   | variable](../Con                  |
|                                   | cepts.htm#environment-variables). |
+-----------------------------------+-----------------------------------+
| [Exit](Exit.htm)                  | Exits the [current                |
|                                   | thread](../misc/Threads.htm).     |
+-----------------------------------+-----------------------------------+
| [ExitApp](ExitApp.htm)            | Terminates the script.            |
+-----------------------------------+-----------------------------------+
| [Exp](Math.htm#Exp)               | Returns the result of raising e   |
|                                   | (which is approximately           |
|                                   | 2.71828182845905) to the *N*th    |
|                                   | power.                            |
+-----------------------------------+-----------------------------------+
| [FileAppend](FileAppend.htm)      | Writes text or binary data to the |
|                                   | end of a file (first creating the |
|                                   | file, if necessary).              |
+-----------------------------------+-----------------------------------+
| [FileCopy](FileCopy.htm)          | Copies one or more files.         |
+-----------------------------------+-----------------------------------+
| [FileCreate                       | Creates a shortcut (.lnk) file.   |
| Shortcut](FileCreateShortcut.htm) |                                   |
+-----------------------------------+-----------------------------------+
| [FileDelete](FileDelete.htm)      | Deletes one or more files         |
|                                   | permanently.                      |
+-----------------------------------+-----------------------------------+
| [FileEncoding](FileEncoding.htm)  | Sets the default encoding for     |
|                                   | [FileRead](FileRead.htm), [Loop   |
|                                   | Read](LoopRead.htm),              |
|                                   | [FileAppend](FileAppend.htm), and |
|                                   | [FileOpen](FileOpen.htm).         |
+-----------------------------------+-----------------------------------+
| [FileExist](FileExist.htm)        | Checks for the existence of a     |
|                                   | file or folder and returns its    |
|                                   | attributes.                       |
+-----------------------------------+-----------------------------------+
| [FileInstall](FileInstall.htm)    | Includes the specified file       |
|                                   | inside the [compiled              |
|                                   | version](../Scripts.htm#ahk2exe)  |
|                                   | of the script.                    |
+-----------------------------------+-----------------------------------+
| [                                 | Reports whether a file or folder  |
| FileGetAttrib](FileGetAttrib.htm) | is read-only, hidden, etc.        |
+-----------------------------------+-----------------------------------+
| [File                             | Retrieves information about a     |
| GetShortcut](FileGetShortcut.htm) | shortcut (.lnk) file, such as its |
|                                   | target file.                      |
+-----------------------------------+-----------------------------------+
| [FileGetSize](FileGetSize.htm)    | Retrieves the size of a file.     |
+-----------------------------------+-----------------------------------+
| [FileGetTime](FileGetTime.htm)    | Retrieves the datetime stamp of a |
|                                   | file or folder.                   |
+-----------------------------------+-----------------------------------+
| [Fi                               | Retrieves the version of a file.  |
| leGetVersion](FileGetVersion.htm) |                                   |
+-----------------------------------+-----------------------------------+
| [FileMove](FileMove.htm)          | Moves or renames one or more      |
|                                   | files.                            |
+-----------------------------------+-----------------------------------+
| [FileOpen](FileOpen.htm)          | Opens a file to read specific     |
|                                   | content from it and/or to write   |
|                                   | new content into it.              |
+-----------------------------------+-----------------------------------+
| [FileRead](FileRead.htm)          | Retrieves the contents of a file. |
+-----------------------------------+-----------------------------------+
| [FileRecycle](FileRecycle.htm)    | Sends a file or directory to the  |
|                                   | recycle bin if possible, or       |
|                                   | permanently deletes it.           |
+-----------------------------------+-----------------------------------+
| [FileRe                           | Empties the recycle bin.          |
| cycleEmpty](FileRecycleEmpty.htm) |                                   |
+-----------------------------------+-----------------------------------+
| [FileSelect](FileSelect.htm)      | Displays a standard dialog that   |
|                                   | allows the user to open or save   |
|                                   | file(s).                          |
+-----------------------------------+-----------------------------------+
| [                                 | Changes the attributes of one or  |
| FileSetAttrib](FileSetAttrib.htm) | more files or folders. Wildcards  |
|                                   | are supported.                    |
+-----------------------------------+-----------------------------------+
| [FileSetTime](FileSetTime.htm)    | Changes the datetime stamp of one |
|                                   | or more files or folders.         |
|                                   | Wildcards are supported.          |
+-----------------------------------+-----------------------------------+
| [Finally](Finally.htm)            | Ensures that one or more          |
|                                   | [state                            |
|                                   | ments](../Concepts.htm#statement) |
|                                   | are always executed after a       |
|                                   | [Try](Try.htm) statement          |
|                                   | finishes.                         |
+-----------------------------------+-----------------------------------+
| [Float](Float.htm)                | Converts a numeric string or      |
|                                   | integer value to a floating-point |
|                                   | number.                           |
+-----------------------------------+-----------------------------------+
| [Floor](Math.htm#Floor)           | Returns the specified number      |
|                                   | rounded down to the nearest       |
|                                   | integer (without any .00 suffix). |
+-----------------------------------+-----------------------------------+
| [For](For.htm)                    | Repeats one or more               |
|                                   | [state                            |
|                                   | ments](../Concepts.htm#statement) |
|                                   | once for each key-value pair in   |
|                                   | an object.                        |
+-----------------------------------+-----------------------------------+
| [Format](Format.htm)              | Formats a variable number of      |
|                                   | input values according to a       |
|                                   | format string.                    |
+-----------------------------------+-----------------------------------+
| [FormatTime](FormatTime.htm)      | Transforms a                      |
|                                   | [YYYYMMDDHH                       |
|                                   | 24MISS](FileSetTime.htm#YYYYMMDD) |
|                                   | timestamp into the specified      |
|                                   | date/time format.                 |
+-----------------------------------+-----------------------------------+
| [GetKeyName](GetKeyName.htm)      | Retrieves the name/text of a key. |
+-----------------------------------+-----------------------------------+
| [GetKeyVK](GetKeyVK.htm)          | Retrieves the virtual key code of |
|                                   | a key.                            |
+-----------------------------------+-----------------------------------+
| [GetKeySC](GetKeySC.htm)          | Retrieves the scan code of a key. |
+-----------------------------------+-----------------------------------+
| [GetKeyState](GetKeyState.htm)    | Returns 1 (true) or 0 (false)     |
|                                   | depending on whether the          |
|                                   | specified keyboard key or         |
|                                   | mouse/controller button is down   |
|                                   | or up. Also retrieves controller  |
|                                   | status.                           |
+-----------------------------------+-----------------------------------+
| [GetMethod](GetMethod.htm)        | Retrieves the implementation      |
|                                   | function of a method.             |
+-----------------------------------+-----------------------------------+
| [Goto](Goto.htm)                  | Jumps to the specified label and  |
|                                   | continues execution.              |
+-----------------------------------+-----------------------------------+
| [                                 | Activates the next window in a    |
| GroupActivate](GroupActivate.htm) | window group that was defined     |
|                                   | with [GroupAdd](GroupAdd.htm).    |
+-----------------------------------+-----------------------------------+
| [GroupAdd](GroupAdd.htm)          | Adds a window specification to a  |
|                                   | window group, creating the group  |
|                                   | if necessary.                     |
+-----------------------------------+-----------------------------------+
| [GroupClose](GroupClose.htm)      | Closes the active window if it    |
|                                   | was just activated by             |
|                                   | [                                 |
|                                   | GroupActivate](GroupActivate.htm) |
|                                   | or                                |
|                                   | [Group                            |
|                                   | Deactivate](GroupDeactivate.htm). |
|                                   | It then activates the next window |
|                                   | in the series. It can also close  |
|                                   | all windows in a group.           |
+-----------------------------------+-----------------------------------+
| [Grou                             | Similar to                        |
| pDeactivate](GroupDeactivate.htm) | [                                 |
|                                   | GroupActivate](GroupActivate.htm) |
|                                   | except activates the next window  |
|                                   | [not]{.underline} in the group.   |
+-----------------------------------+-----------------------------------+
| [Gui()](Gui.htm#Call)             | Creates and returns a new [Gui    |
|                                   | object](Gui.htm). This can be     |
|                                   | used to define a custom window,   |
|                                   | or graphical user interface       |
|                                   | (GUI), to display information or  |
|                                   | accept user input.                |
+-----------------------------------+-----------------------------------+
| [GuiC                             | Retrieves the [GuiControl         |
| trlFromHwnd](GuiCtrlFromHwnd.htm) | object](GuiControl.htm) of a GUI  |
|                                   | control associated with the       |
|                                   | specified window handle.          |
+-----------------------------------+-----------------------------------+
| [GuiFromHwnd](GuiFromHwnd.htm)    | Retrieves the [Gui                |
|                                   | object](Gui.htm) of a GUI window  |
|                                   | associated with the specified     |
|                                   | window handle.                    |
+-----------------------------------+-----------------------------------+
| [HasBase](HasBase.htm)            | Returns a non-zero number if the  |
|                                   | specified value is derived from   |
|                                   | the specified base object.        |
+-----------------------------------+-----------------------------------+
| [HasMethod](HasMethod.htm)        | Returns a non-zero number if the  |
|                                   | specified value has a method by   |
|                                   | the specified name.               |
+-----------------------------------+-----------------------------------+
| [HasProp](HasProp.htm)            | Returns a non-zero number if the  |
|                                   | specified value has a property by |
|                                   | the specified name.               |
+-----------------------------------+-----------------------------------+
| [HotIf / HotIfWin\...](HotIf.htm) | Specifies the criteria for        |
|                                   | subsequently created or modified  |
|                                   | [hotkey                           |
|                                   | variants](Hotkey.htm#variant) and |
|                                   | [hotstring                        |
|                                   | variants](Hotstring.htm#variant). |
+-----------------------------------+-----------------------------------+
| [Hotkey](Hotkey.htm)              | Creates, modifies, enables, or    |
|                                   | disables a hotkey while the       |
|                                   | script is running.                |
+-----------------------------------+-----------------------------------+
| [Hotstring](Hotstring.htm)        | Creates, modifies, enables, or    |
|                                   | disables a hotstring while the    |
|                                   | script is running.                |
+-----------------------------------+-----------------------------------+
| [If](If.htm)                      | Specifies one or more             |
|                                   | [state                            |
|                                   | ments](../Concepts.htm#statement) |
|                                   | to execute if an                  |
|                                   | [expressi                         |
|                                   | on](../Variables.htm#Expressions) |
|                                   | evaluates to true.                |
+-----------------------------------+-----------------------------------+
| [IL                               | The means by which icons are      |
| _Create](ListView.htm#IL_Create)\ | added to a                        |
| [IL_Add](ListView.htm#IL_Add)\    | [ListView](ListView.htm) or       |
| [IL_                              | [TreeView](TreeView.htm) control. |
| Destroy](ListView.htm#IL_Destroy) |                                   |
+-----------------------------------+-----------------------------------+
| [ImageSearch](ImageSearch.htm)    | Searches a region of the screen   |
|                                   | for an image.                     |
+-----------------------------------+-----------------------------------+
| [IniDelete](IniDelete.htm)        | Deletes a value from a standard   |
|                                   | format .ini file.                 |
+-----------------------------------+-----------------------------------+
| [IniRead](IniRead.htm)            | Reads a value, section or list of |
|                                   | section names from a standard     |
|                                   | format .ini file.                 |
+-----------------------------------+-----------------------------------+
| [IniWrite](IniWrite.htm)          | Writes a value or section to a    |
|                                   | standard format .ini file.        |
+-----------------------------------+-----------------------------------+
| [InputBox](InputBox.htm)          | Displays an input box to ask the  |
|                                   | user to enter a string.           |
+-----------------------------------+-----------------------------------+
| [InputHook](InputHook.htm)        | Creates an object which can be    |
|                                   | used to collect or intercept      |
|                                   | keyboard input.                   |
+-----------------------------------+-----------------------------------+
| [Instal                           | Installs or uninstalls the        |
| lKeybdHook](InstallKeybdHook.htm) | keyboard hook.                    |
+-----------------------------------+-----------------------------------+
| [Instal                           | Installs or uninstalls the mouse  |
| lMouseHook](InstallMouseHook.htm) | hook.                             |
+-----------------------------------+-----------------------------------+
| [InStr](InStr.htm)                | Searches for a given *occurrence* |
|                                   | of a string, from the left or the |
|                                   | right.                            |
+-----------------------------------+-----------------------------------+
| [Integer](Integer.htm)            | Converts a numeric string or      |
|                                   | floating-point value to an        |
|                                   | integer.                          |
+-----------------------------------+-----------------------------------+
| [IsLabel](IsLabel.htm)            | Returns a non-zero number if the  |
|                                   | specified label exists in the     |
|                                   | current scope.                    |
+-----------------------------------+-----------------------------------+
| [IsObject](IsObject.htm)          | Returns a non-zero number if the  |
|                                   | specified value is an object.     |
+-----------------------------------+-----------------------------------+
| [IsSet / IsSetRef](IsSet.htm)     | Returns a non-zero number if the  |
|                                   | specified variable has been       |
|                                   | assigned a value.                 |
+-----------------------------------+-----------------------------------+
| [KeyHistory](KeyHistory.htm)      | Displays script info and a        |
|                                   | history of the most recent        |
|                                   | keystrokes and mouse clicks.      |
+-----------------------------------+-----------------------------------+
| [KeyWait](KeyWait.htm)            | Waits for a key or                |
|                                   | mouse/controller button to be     |
|                                   | released or pressed down.         |
+-----------------------------------+-----------------------------------+
| [ListHotkeys](ListHotkeys.htm)    | Displays the hotkeys in use by    |
|                                   | the current script, whether their |
|                                   | subroutines are currently         |
|                                   | running, and whether or not they  |
|                                   | use the                           |
|                                   | [keyboard](InstallKeybdHook.htm)  |
|                                   | or [mouse](InstallMouseHook.htm)  |
|                                   | hook.                             |
+-----------------------------------+-----------------------------------+
| [ListLines](ListLines.htm)        | Enables or disables line logging  |
|                                   | or displays the script lines most |
|                                   | recently executed.                |
+-----------------------------------+-----------------------------------+
| [ListVars](ListVars.htm)          | Displays the script\'s            |
|                                   | [variables](../Variables.htm):    |
|                                   | their names and current contents. |
+-----------------------------------+-----------------------------------+
| [ListViewGe                       | Returns a list of items/rows from |
| tContent](ListViewGetContent.htm) | a ListView.                       |
+-----------------------------------+-----------------------------------+
| [LoadPicture](LoadPicture.htm)    | Loads a picture from file and     |
|                                   | returns a bitmap or icon handle.  |
+-----------------------------------+-----------------------------------+
| [Log](Math.htm#Log)               | Returns the logarithm (base 10)   |
|                                   | of the specified number.          |
+-----------------------------------+-----------------------------------+
| [Ln](Math.htm#Ln)                 | Returns the natural logarithm     |
|                                   | (base e) of the specified number. |
+-----------------------------------+-----------------------------------+
| [Loop (normal)](Loop.htm)         | Performs one or more              |
|                                   | [state                            |
|                                   | ments](../Concepts.htm#statement) |
|                                   | repeatedly: either the specified  |
|                                   | number of times or until          |
|                                   | [Break](Break.htm) is             |
|                                   | encountered.                      |
+-----------------------------------+-----------------------------------+
| [Loop Files](LoopFiles.htm)       | Retrieves the specified files or  |
|                                   | folders, one at a time.           |
+-----------------------------------+-----------------------------------+
| [Loop Parse](LoopParse.htm)       | Retrieves substrings (fields)     |
|                                   | from a string, one at a time.     |
+-----------------------------------+-----------------------------------+
| [Loop Read](LoopRead.htm)         | Retrieves the lines in a text     |
|                                   | file, one at a time.              |
+-----------------------------------+-----------------------------------+
| [Loop Reg](LoopReg.htm)           | Retrieves the contents of the     |
|                                   | specified registry subkey, one    |
|                                   | item at a time.                   |
+-----------------------------------+-----------------------------------+
| [Map](../Obje                     | Creates a [Map](Map.htm) from a   |
| cts.htm#Usage_Associative_Arrays) | list of key-value pairs.          |
+-----------------------------------+-----------------------------------+
| [Max](Math.htm#Max)               | Returns the highest number from a |
|                                   | set of numbers.                   |
+-----------------------------------+-----------------------------------+
| [MenuBar()](Menu.htm#Call)        | Creates a [MenuBar                |
|                                   | object](Menu.htm), which can be   |
|                                   | used to define a [GUI menu        |
|                                   | bar](Gui.htm#MenuBar).            |
+-----------------------------------+-----------------------------------+
| [Menu()](Menu.htm#Call)           | Creates a [Menu                   |
|                                   | object](Menu.htm), which can be   |
|                                   | used to create and display a      |
|                                   | menu.                             |
+-----------------------------------+-----------------------------------+
| [Me                               | Retrieves the [Menu or MenuBar    |
| nuFromHandle](MenuFromHandle.htm) | object](Menu.htm) corresponding   |
|                                   | to a Win32 menu handle.           |
+-----------------------------------+-----------------------------------+
| [MenuSelect](MenuSelect.htm)      | Invokes a menu item from the menu |
|                                   | bar of the specified window.      |
+-----------------------------------+-----------------------------------+
| [Min](Math.htm#Min)               | Returns the lowest number from a  |
|                                   | set of numbers.                   |
+-----------------------------------+-----------------------------------+
| [Mod](Math.htm#Mod)               | Modulo. Returns the remainder of  |
|                                   | a number (dividend) divided by    |
|                                   | another number (divisor).         |
+-----------------------------------+-----------------------------------+
| [MonitorGet](MonitorGet.htm)      | Checks if the specified monitor   |
|                                   | exists and optionally retrieves   |
|                                   | its bounding coordinates.         |
+-----------------------------------+-----------------------------------+
| [Moni                             | Returns the total number of       |
| torGetCount](MonitorGetCount.htm) | monitors.                         |
+-----------------------------------+-----------------------------------+
| [Mo                               | Returns the operating system\'s   |
| nitorGetName](MonitorGetName.htm) | name of the specified monitor.    |
+-----------------------------------+-----------------------------------+
| [MonitorG                         | Returns the number of the primary |
| etPrimary](MonitorGetPrimary.htm) | monitor.                          |
+-----------------------------------+-----------------------------------+
| [MonitorGet                       | Checks if the specified monitor   |
| WorkArea](MonitorGetWorkArea.htm) | exists and optionally retrieves   |
|                                   | the bounding coordinates of its   |
|                                   | working area.                     |
+-----------------------------------+-----------------------------------+
| [MouseClick](MouseClick.htm)      | Clicks or holds down a mouse      |
|                                   | button, or turns the mouse wheel. |
|                                   | Note: The [Click](Click.htm)      |
|                                   | function is generally more        |
|                                   | flexible and easier to use.       |
+-----------------------------------+-----------------------------------+
| [Mo                               | Clicks and holds the specified    |
| useClickDrag](MouseClickDrag.htm) | mouse button, moves the mouse to  |
|                                   | the destination coordinates, then |
|                                   | releases the button.              |
+-----------------------------------+-----------------------------------+
| [MouseGetPos](MouseGetPos.htm)    | Retrieves the current position of |
|                                   | the mouse cursor, and optionally  |
|                                   | which window and control it is    |
|                                   | hovering over.                    |
+-----------------------------------+-----------------------------------+
| [MouseMove](MouseMove.htm)        | Moves the mouse cursor.           |
+-----------------------------------+-----------------------------------+
| [MsgBox](MsgBox.htm)              | Displays the specified text in a  |
|                                   | small window containing one or    |
|                                   | more buttons (such as Yes and     |
|                                   | No).                              |
+-----------------------------------+-----------------------------------+
| [Number](Number.htm)              | Converts a numeric string to a    |
|                                   | pure integer or floating-point    |
|                                   | number.                           |
+-----------------------------------+-----------------------------------+
| [NumGet](NumGet.htm)              | Returns the binary number stored  |
|                                   | at the specified address+offset.  |
+-----------------------------------+-----------------------------------+
| [NumPut](NumPut.htm)              | Stores one or more numbers in     |
|                                   | binary format at the specified    |
|                                   | address+offset.                   |
+-----------------------------------+-----------------------------------+
| [ObjAddRef /                      | Increments or decrements an       |
| ObjRelease](ObjAddRef.htm)        | object\'s [reference              |
|                                   | count](..                         |
|                                   | /Objects.htm#Reference_Counting). |
+-----------------------------------+-----------------------------------+
| [                                 | Creates a [BoundFunc              |
| ObjBindMethod](ObjBindMethod.htm) | objec                             |
|                                   | t](../misc/Functor.htm#BoundFunc) |
|                                   | which calls a method of a given   |
|                                   | object.                           |
+-----------------------------------+-----------------------------------+
| [ObjHa                            | These functions are equivalent to |
| sOwnProp](Object.htm#HasOwnProp)\ | built-in methods of the           |
| [O                                | [Object](Object.htm) type. It is  |
| bjOwnProps](Object.htm#OwnProps)\ | usually recommended to use the    |
|                                   | corresponding method instead.     |
+-----------------------------------+-----------------------------------+
| [ObjGetBase](Any.htm#GetBase)     | Retrieves an object\'s [base      |
|                                   | ob                                |
|                                   | ject](../Objects.htm#delegation). |
+-----------------------------------+-----------------------------------+
| [ObjGet                           | Returns the current capacity of   |
| Capacity](Object.htm#GetCapacity) | the object\'s internal array of   |
|                                   | properties.                       |
+-----------------------------------+-----------------------------------+
| [ObjOwnPr                         | Returns the number of properties  |
| opCount](Object.htm#OwnPropCount) | owned by an object.               |
+-----------------------------------+-----------------------------------+
| [ObjSetBase](Object.htm#SetBase)  | Sets an object\'s [base           |
|                                   | ob                                |
|                                   | ject](../Objects.htm#delegation). |
+-----------------------------------+-----------------------------------+
| [ObjSet                           | Sets the current capacity of the  |
| Capacity](Object.htm#SetCapacity) | object\'s internal array of own   |
|                                   | properties.                       |
+-----------------------------------+-----------------------------------+
| [OnClipbo                         | Registers a                       |
| ardChange](OnClipboardChange.htm) | [function](../Functions.htm) to   |
|                                   | be called automatically whenever  |
|                                   | the clipboard\'s content changes. |
+-----------------------------------+-----------------------------------+
| [OnError](OnError.htm)            | Registers a                       |
|                                   | [function](../Functions.htm) to   |
|                                   | be called automatically whenever  |
|                                   | an unhandled error occurs.        |
+-----------------------------------+-----------------------------------+
| [OnExit](OnExit.htm)              | Registers a                       |
|                                   | [function](../Functions.htm) to   |
|                                   | be called automatically whenever  |
|                                   | the script exits.                 |
+-----------------------------------+-----------------------------------+
| [OnMessage](OnMessage.htm)        | Registers a                       |
|                                   | [function](../Functions.htm) to   |
|                                   | be called automatically whenever  |
|                                   | the script receives the specified |
|                                   | message.                          |
+-----------------------------------+-----------------------------------+
| [Ord](Ord.htm)                    | Returns the ordinal value         |
|                                   | (numeric character code) of the   |
|                                   | first character in the specified  |
|                                   | string.                           |
+-----------------------------------+-----------------------------------+
| [OutputDebug](OutputDebug.htm)    | Sends a string to the debugger    |
|                                   | (if any) for display.             |
+-----------------------------------+-----------------------------------+
| [Pause](Pause.htm)                | Pauses the script\'s [current     |
|                                   | thread](../misc/Threads.htm) or   |
|                                   | sets the pause state of the       |
|                                   | underlying thread.                |
+-----------------------------------+-----------------------------------+
| [Persistent](Persistent.htm)      | Prevents the script from exiting  |
|                                   | automatically when its last       |
|                                   | thread completes, allowing it to  |
|                                   | stay running in an idle state.    |
+-----------------------------------+-----------------------------------+
| [                                 | Retrieves the color of the pixel  |
| PixelGetColor](PixelGetColor.htm) | at the specified X and Y          |
|                                   | coordinates.                      |
+-----------------------------------+-----------------------------------+
| [PixelSearch](PixelSearch.htm)    | Searches a region of the screen   |
|                                   | for a pixel of the specified      |
|                                   | color.                            |
+-----------------------------------+-----------------------------------+
| [PostMessage](PostMessage.htm)    | Places a message in the message   |
|                                   | queue of a window or control.     |
+-----------------------------------+-----------------------------------+
| [ProcessClose](ProcessClose.htm)  | Forces the first matching process |
|                                   | to close.                         |
+-----------------------------------+-----------------------------------+
| [ProcessExist](ProcessExist.htm)  | Checks if the specified process   |
|                                   | exists.                           |
+-----------------------------------+-----------------------------------+
| [Pr                               | Returns the name of the specified |
| ocessGetName](ProcessGetName.htm) | process.                          |
+-----------------------------------+-----------------------------------+
| [Proces                           | Returns the process ID (PID) of   |
| sGetParent](ProcessGetParent.htm) | the process which created the     |
|                                   | specified process.                |
+-----------------------------------+-----------------------------------+
| [Pr                               | Returns the path of the specified |
| ocessGetPath](ProcessGetName.htm) | process.                          |
+-----------------------------------+-----------------------------------+
| [ProcessSet                       | Changes the priority level of the |
| Priority](ProcessSetPriority.htm) | first matching process.           |
+-----------------------------------+-----------------------------------+
| [ProcessWait](ProcessWait.htm)    | Waits for the specified process   |
|                                   | to exist.                         |
+-----------------------------------+-----------------------------------+
| [Proces                           | Waits for all matching processes  |
| sWaitClose](ProcessWaitClose.htm) | to close.                         |
+-----------------------------------+-----------------------------------+
| [Random](Random.htm)              | Generates a pseudo-random number. |
+-----------------------------------+-----------------------------------+
| [RegExMatch](RegExMatch.htm)      | Determines whether a string       |
|                                   | contains a pattern (regular       |
|                                   | expression).                      |
+-----------------------------------+-----------------------------------+
| [RegExReplace](RegExReplace.htm)  | Replaces occurrences of a pattern |
|                                   | (regular expression) inside a     |
|                                   | string.                           |
+-----------------------------------+-----------------------------------+
| [RegCreateKey](RegCreateKey.htm)  | Creates a registry key without    |
|                                   | writing a value.                  |
+-----------------------------------+-----------------------------------+
| [RegDelete](RegDelete.htm)        | Deletes a value from the          |
|                                   | registry.                         |
+-----------------------------------+-----------------------------------+
| [RegDeleteKey](RegDeleteKey.htm)  | Deletes a subkey from the         |
|                                   | registry.                         |
+-----------------------------------+-----------------------------------+
| [RegRead](RegRead.htm)            | Reads a value from the registry.  |
+-----------------------------------+-----------------------------------+
| [RegWrite](RegWrite.htm)          | Writes a value to the registry.   |
+-----------------------------------+-----------------------------------+
| [Reload](Reload.htm)              | Replaces the currently running    |
|                                   | instance of the script with a new |
|                                   | one.                              |
+-----------------------------------+-----------------------------------+
| [Return](Return.htm)              | Returns from a function to which  |
|                                   | execution had previously jumped   |
|                                   | via                               |
|                                   | [                                 |
|                                   | function-call](../Functions.htm), |
|                                   | [Hotkey](../Hotkeys.htm)          |
|                                   | activation, or other means.       |
+-----------------------------------+-----------------------------------+
| [Round](Math.htm#Round)           | Returns the specified number      |
|                                   | rounded to *N* decimal places.    |
+-----------------------------------+-----------------------------------+
| [Run](Run.htm)                    | Runs an external program.         |
+-----------------------------------+-----------------------------------+
| [RunAs](RunAs.htm)                | Specifies a set of user           |
|                                   | credentials to use for all        |
|                                   | subsequent [Run](Run.htm) and     |
|                                   | [RunWait](Run.htm) functions.     |
+-----------------------------------+-----------------------------------+
| [RunWait](Run.htm)                | Runs an external program and      |
|                                   | waits until it finishes.          |
+-----------------------------------+-----------------------------------+
| [Send](Send.htm) /                | Sends simulated keystrokes and    |
| [SendText](Send.htm#SendText) /   | mouse clicks to the               |
| [SendInput](Send.htm#SendInput) / | [active](WinActivate.htm) window. |
| [SendPlay](Send.htm#SendPlay) /   |                                   |
| [SendEvent](Send.htm#SendEvent)   |                                   |
+-----------------------------------+-----------------------------------+
| [SendLevel](SendLevel.htm)        | Controls which artificial         |
|                                   | keyboard and mouse events are     |
|                                   | ignored by hotkeys and            |
|                                   | hotstrings.                       |
+-----------------------------------+-----------------------------------+
| [SendMessage](SendMessage.htm)    | Sends a message to a window or    |
|                                   | control and waits for             |
|                                   | acknowledgement.                  |
+-----------------------------------+-----------------------------------+
| [SendMode](SendMode.htm)          | Makes [Send](Send.htm) synonymous |
|                                   | with SendEvent or SendPlay rather |
|                                   | than the default (SendInput).     |
|                                   | Also makes Click and              |
|                                   | MouseMove/Click/Drag use the      |
|                                   | specified method.                 |
+-----------------------------------+-----------------------------------+
| [SetCapsLockStat                  | Sets the state of                 |
| e](SetNumScrollCapsLockState.htm) | [CapsLock]{.kbd}. Can also force  |
|                                   | the key to stay on or off.        |
+-----------------------------------+-----------------------------------+
| [SetC                             | Sets the delay that will occur    |
| ontrolDelay](SetControlDelay.htm) | after each control-modifying      |
|                                   | function.                         |
+-----------------------------------+-----------------------------------+
| [SetDefaultMous                   | Sets the mouse speed that will be |
| eSpeed](SetDefaultMouseSpeed.htm) | used if unspecified in            |
|                                   | [Click](Click.htm),               |
|                                   | [MouseMove](MouseMove.htm),       |
|                                   | [MouseClick](MouseClick.htm), and |
|                                   | [Mou                              |
|                                   | seClickDrag](MouseClickDrag.htm). |
+-----------------------------------+-----------------------------------+
| [SetKeyDelay](SetKeyDelay.htm)    | Sets the delay that will occur    |
|                                   | after each keystroke sent by      |
|                                   | [Send](Send.htm) or               |
|                                   | [ControlSend](ControlSend.htm).   |
+-----------------------------------+-----------------------------------+
| [                                 | Sets the delay that will occur    |
| SetMouseDelay](SetMouseDelay.htm) | after each mouse movement or      |
|                                   | click.                            |
+-----------------------------------+-----------------------------------+
| [SetNumLockStat                   | Sets the state of                 |
| e](SetNumScrollCapsLockState.htm) | [NumLock]{.kbd}. Can also force   |
|                                   | the key to stay on or off.        |
+-----------------------------------+-----------------------------------+
| [SetScrollLockStat                | Sets the state of                 |
| e](SetNumScrollCapsLockState.htm) | [ScrollLock]{.kbd}. Can also      |
|                                   | force the key to stay on or off.  |
+-----------------------------------+-----------------------------------+
| [SetRegView](SetRegView.htm)      | Sets the registry view used by    |
|                                   | [RegRead](RegRead.htm),           |
|                                   | [RegWrite](RegWrite.htm),         |
|                                   | [RegDelete](RegDelete.htm),       |
|                                   | [RegDeleteKey](RegDeleteKey.htm)  |
|                                   | and [Loop Reg](LoopReg.htm),      |
|                                   | allowing them in a 32-bit script  |
|                                   | to access the 64-bit registry     |
|                                   | view and vice versa.              |
+-----------------------------------+-----------------------------------+
| [SetStoreCapsLo                   | Whether to restore the state of   |
| ckMode](SetStoreCapsLockMode.htm) | [CapsLock]{.kbd} after a          |
|                                   | [Send](Send.htm).                 |
+-----------------------------------+-----------------------------------+
| [SetTimer](SetTimer.htm)          | Causes a function to be called    |
|                                   | automatically and repeatedly at a |
|                                   | specified time interval.          |
+-----------------------------------+-----------------------------------+
| [SetTitle                         | Sets the matching behavior of the |
| MatchMode](SetTitleMatchMode.htm) | [*WinTitle*                       |
|                                   | parameter](../misc/WinTitle.htm)  |
|                                   | in built-in functions such as     |
|                                   | [WinWait](WinWait.htm).           |
+-----------------------------------+-----------------------------------+
| [SetWinDelay](SetWinDelay.htm)    | Sets the delay that will occur    |
|                                   | after each windowing function,    |
|                                   | such as                           |
|                                   | [WinActivate](WinActivate.htm).   |
+-----------------------------------+-----------------------------------+
| [                                 | Changes the script\'s current     |
| SetWorkingDir](SetWorkingDir.htm) | working directory.                |
+-----------------------------------+-----------------------------------+
| [Shutdown](Shutdown.htm)          | Shuts down, restarts, or logs off |
|                                   | the system.                       |
+-----------------------------------+-----------------------------------+
| [Sin](Math.htm#Sin)               | Returns the trigonometric sine of |
|                                   | the specified number.             |
+-----------------------------------+-----------------------------------+
| [Sleep](Sleep.htm)                | Waits the specified amount of     |
|                                   | time before continuing.           |
+-----------------------------------+-----------------------------------+
| [Sort](Sort.htm)                  | Arranges a variable\'s contents   |
|                                   | in alphabetical, numerical, or    |
|                                   | random order (optionally removing |
|                                   | duplicates).                      |
+-----------------------------------+-----------------------------------+
| [SoundBeep](SoundBeep.htm)        | Emits a tone from the PC speaker. |
+-----------------------------------+-----------------------------------+
| [SoundGet                         | Retrieves a native COM interface  |
| Interface](SoundGetInterface.htm) | of a sound device or component.   |
+-----------------------------------+-----------------------------------+
| [SoundGetMute](SoundGetMute.htm)  | Retrieves a mute setting of a     |
|                                   | sound device.                     |
+-----------------------------------+-----------------------------------+
| [SoundGetName](SoundGetName.htm)  | Retrieves the name of a sound     |
|                                   | device or component.              |
+-----------------------------------+-----------------------------------+
| [So                               | Retrieves a volume setting of a   |
| undGetVolume](SoundGetVolume.htm) | sound device.                     |
+-----------------------------------+-----------------------------------+
| [SoundPlay](SoundPlay.htm)        | Plays a sound, video, or other    |
|                                   | supported file type.              |
+-----------------------------------+-----------------------------------+
| [SoundSetMute](SoundSetMute.htm)  | Changes a mute setting of a sound |
|                                   | device.                           |
+-----------------------------------+-----------------------------------+
| [So                               | Changes a volume setting of a     |
| undSetVolume](SoundSetVolume.htm) | sound device.                     |
+-----------------------------------+-----------------------------------+
| [SplitPath](SplitPath.htm)        | Separates a file name or URL into |
|                                   | its name, directory, extension,   |
|                                   | and drive.                        |
+-----------------------------------+-----------------------------------+
| [Sqrt](Math.htm#Sqrt)             | Returns the square root of the    |
|                                   | specified number.                 |
+-----------------------------------+-----------------------------------+
| [Status                           | Retrieves the text from a         |
| BarGetText](StatusBarGetText.htm) | standard status bar control.      |
+-----------------------------------+-----------------------------------+
| [                                 | Waits until a window\'s status    |
| StatusBarWait](StatusBarWait.htm) | bar contains the specified        |
|                                   | string.                           |
+-----------------------------------+-----------------------------------+
| [StrCompare](StrCompare.htm)      | Compares two strings              |
|                                   | alphabetically.                   |
+-----------------------------------+-----------------------------------+
| [StrGet](StrGet.htm)              | Copies a string from a memory     |
|                                   | address or buffer, optionally     |
|                                   | converting it from a given code   |
|                                   | page.                             |
+-----------------------------------+-----------------------------------+
| [String](String.htm)              | Converts a value to a string.     |
+-----------------------------------+-----------------------------------+
| [StrLen](StrLen.htm)              | Retrieves the count of how many   |
|                                   | characters are in a string.       |
+-----------------------------------+-----------------------------------+
| [StrLower](StrLower.htm)          | Converts a string to lowercase.   |
+-----------------------------------+-----------------------------------+
| [StrPtr](StrPtr.htm)              | Returns the current memory        |
|                                   | address of a string.              |
+-----------------------------------+-----------------------------------+
| [StrPut](StrPut.htm)              | Copies a string to a memory       |
|                                   | address or buffer, optionally     |
|                                   | converting it to a given code     |
|                                   | page.                             |
+-----------------------------------+-----------------------------------+
| [StrReplace](StrReplace.htm)      | Replaces the specified substring  |
|                                   | with a new string.                |
+-----------------------------------+-----------------------------------+
| [StrSplit](StrSplit.htm)          | Separates a string into an array  |
|                                   | of substrings using the specified |
|                                   | delimiters.                       |
+-----------------------------------+-----------------------------------+
| [StrTitle](StrLower.htm)          | Converts a string to title case.  |
+-----------------------------------+-----------------------------------+
| [StrUpper](StrLower.htm)          | Converts a string to uppercase.   |
+-----------------------------------+-----------------------------------+
| [SubStr](SubStr.htm)              | Retrieves one or more characters  |
|                                   | from the specified position in a  |
|                                   | string.                           |
+-----------------------------------+-----------------------------------+
| [Suspend](Suspend.htm)            | Disables or enables all or        |
|                                   | selected                          |
|                                   | [hotkeys](../Hotkeys.htm) and     |
|                                   | [hotstrings](../Hotstrings.htm).  |
+-----------------------------------+-----------------------------------+
| [Switch](Switch.htm)              | Compares a value with multiple    |
|                                   | cases and executes the            |
|                                   | [state                            |
|                                   | ments](../Concepts.htm#statement) |
|                                   | of the first match.               |
+-----------------------------------+-----------------------------------+
| [SysGet](SysGet.htm)              | Retrieves dimensions of system    |
|                                   | objects, and other system         |
|                                   | properties.                       |
+-----------------------------------+-----------------------------------+
| [SysGetIP                         | Returns an array of the system\'s |
| Addresses](SysGetIPAddresses.htm) | IPv4 addresses.                   |
+-----------------------------------+-----------------------------------+
| [Tan](Math.htm#Tan)               | Returns the trigonometric tangent |
|                                   | of the specified number.          |
+-----------------------------------+-----------------------------------+
| [Thread](Thread.htm)              | Sets the priority or              |
|                                   | interruptibility of               |
|                                   | [threads](../misc/Threads.htm).   |
|                                   | It can also temporarily disable   |
|                                   | all [timers](SetTimer.htm).       |
+-----------------------------------+-----------------------------------+
| [Throw](Throw.htm)                | Signals the occurrence of an      |
|                                   | error. This signal can be caught  |
|                                   | by a                              |
|                                   | [Try](Try.htm)-[Catch](Catch.htm) |
|                                   | statement.                        |
+-----------------------------------+-----------------------------------+
| [ToolTip](ToolTip.htm)            | Shows an always-on-top window     |
|                                   | anywhere on the screen.           |
+-----------------------------------+-----------------------------------+
| [TraySetIcon](TraySetIcon.htm)    | Changes the script\'s [tray       |
|                                   | icon](../Program.htm#tray-icon)   |
|                                   | (which is also used by            |
|                                   | [GUI](Gui.htm) and dialog         |
|                                   | windows).                         |
+-----------------------------------+-----------------------------------+
| [TrayTip](TrayTip.htm)            | Shows a balloon message window    |
|                                   | or, on Windows 10 and later, a    |
|                                   | toast notification near the [tray |
|                                   | icon](../Program.htm#tray-icon).  |
+-----------------------------------+-----------------------------------+
| [Trim / LTrim / RTrim](Trim.htm)  | Trims characters from the         |
|                                   | beginning and/or end of a string. |
+-----------------------------------+-----------------------------------+
| [Try](Try.htm)                    | Guards one or more                |
|                                   | [state                            |
|                                   | ments](../Concepts.htm#statement) |
|                                   | against runtime errors and values |
|                                   | thrown by the [Throw](Throw.htm)  |
|                                   | statement.                        |
+-----------------------------------+-----------------------------------+
| [Type](Type.htm)                  | Returns the class name of a       |
|                                   | value.                            |
+-----------------------------------+-----------------------------------+
| [Until](Until.htm)                | Applies a condition to the        |
|                                   | continuation of a Loop or         |
|                                   | For-loop.                         |
+-----------------------------------+-----------------------------------+
| [VarSetSt                         | Enlarges a variable\'s holding    |
| rCapacity](VarSetStrCapacity.htm) | capacity or frees its memory.     |
|                                   | This is not normally needed, but  |
|                                   | may be used with                  |
|                                   | [DllCall](DllCall.htm) or         |
|                                   | [SendMessage](SendMessage.htm) or |
|                                   | to optimize repeated              |
|                                   | concatenation.                    |
+-----------------------------------+-----------------------------------+
| [VerCompare](VerCompare.htm)      | Compares two version strings.     |
+-----------------------------------+-----------------------------------+
| [While-loop](While.htm)           | Performs one or more              |
|                                   | [state                            |
|                                   | ments](../Concepts.htm#statement) |
|                                   | repeatedly until the specified    |
|                                   | [expressi                         |
|                                   | on](../Variables.htm#Expressions) |
|                                   | evaluates to false.               |
+-----------------------------------+-----------------------------------+
| [WinActivate](WinActivate.htm)    | Activates the specified window.   |
+-----------------------------------+-----------------------------------+
| [WinActiv                         | Same as                           |
| ateBottom](WinActivateBottom.htm) | [WinActivate](WinActivate.htm)    |
|                                   | except that it activates the      |
|                                   | bottommost matching window rather |
|                                   | than the topmost.                 |
+-----------------------------------+-----------------------------------+
| [WinActive](WinActive.htm)        | Checks if the specified window is |
|                                   | active and returns its unique ID  |
|                                   | (HWND).                           |
+-----------------------------------+-----------------------------------+
| [WinClose](WinClose.htm)          | Closes the specified window.      |
+-----------------------------------+-----------------------------------+
| [WinExist](WinExist.htm)          | Checks if the specified window    |
|                                   | exists and returns the unique ID  |
|                                   | (HWND) of the first matching      |
|                                   | window.                           |
+-----------------------------------+-----------------------------------+
| [WinGetClass](WinGetClass.htm)    | Retrieves the specified window\'s |
|                                   | class name.                       |
+-----------------------------------+-----------------------------------+
| [WinG                             | Retrieves the position and size   |
| etClientPos](WinGetClientPos.htm) | of the specified window\'s client |
|                                   | area.                             |
+-----------------------------------+-----------------------------------+
| [Wi                               | Returns an array of names         |
| nGetControls](WinGetControls.htm) | (ClassNNs) for all controls in    |
|                                   | the specified window.             |
+-----------------------------------+-----------------------------------+
| [WinGetCont                       | Returns an array of unique ID     |
| rolsHwnd](WinGetControlsHwnd.htm) | numbers (HWNDs) for all controls  |
|                                   | in the specified window.          |
+-----------------------------------+-----------------------------------+
| [WinGetCount](WinGetCount.htm)    | Returns the number of existing    |
|                                   | windows that match the specified  |
|                                   | criteria.                         |
+-----------------------------------+-----------------------------------+
| [WinGetID](WinGetID.htm)          | Returns the unique ID number      |
|                                   | (HWND) of the specified window.   |
+-----------------------------------+-----------------------------------+
| [WinGetIDLast](WinGetIDLast.htm)  | Returns the unique ID number      |
|                                   | (HWND) of the last/bottommost     |
|                                   | window if there is more than one  |
|                                   | match.                            |
+-----------------------------------+-----------------------------------+
| [WinGetList](WinGetList.htm)      | Returns an array of unique ID     |
|                                   | numbers (HWNDs) for all existing  |
|                                   | windows that match the specified  |
|                                   | criteria.                         |
+-----------------------------------+-----------------------------------+
| [WinGetMinMax](WinGetMinMax.htm)  | Returns a non-zero number if the  |
|                                   | specified window is maximized or  |
|                                   | minimized.                        |
+-----------------------------------+-----------------------------------+
| [WinGetPID](WinGetPID.htm)        | Returns the Process ID number     |
|                                   | (PID) of the specified window.    |
+-----------------------------------+-----------------------------------+
| [WinGetPos](WinGetPos.htm)        | Retrieves the position and size   |
|                                   | of the specified window.          |
+-----------------------------------+-----------------------------------+
| [WinGetPr                         | Returns the name of the process   |
| ocessName](WinGetProcessName.htm) | that owns the specified window.   |
+-----------------------------------+-----------------------------------+
| [WinGetPr                         | Returns the full path and name of |
| ocessPath](WinGetProcessPath.htm) | the process that owns the         |
|                                   | specified window.                 |
+-----------------------------------+-----------------------------------+
| [WinGetStyle\                     | Returns the style or extended     |
| WinGetExStyle](WinGetStyle.htm)   | style (respectively) of the       |
|                                   | specified window.                 |
+-----------------------------------+-----------------------------------+
| [WinGetText](WinGetText.htm)      | Retrieves the text from the       |
|                                   | specified window.                 |
+-----------------------------------+-----------------------------------+
| [WinGetTitle](WinGetTitle.htm)    | Retrieves the title of the        |
|                                   | specified window.                 |
+-----------------------------------+-----------------------------------+
| [WinGet                           | Returns the color that is marked  |
| TransColor](WinGetTransColor.htm) | transparent in the specified      |
|                                   | window.                           |
+-----------------------------------+-----------------------------------+
| [WinGetTr                         | Returns the degree of             |
| ansparent](WinGetTransparent.htm) | transparency of the specified     |
|                                   | window.                           |
+-----------------------------------+-----------------------------------+
| [WinHide](WinHide.htm)            | Hides the specified window.       |
+-----------------------------------+-----------------------------------+
| [WinKill](WinKill.htm)            | Forces the specified window to    |
|                                   | close.                            |
+-----------------------------------+-----------------------------------+
| [WinMaximize](WinMaximize.htm)    | Enlarges the specified window to  |
|                                   | its maximum size.                 |
+-----------------------------------+-----------------------------------+
| [WinMinimize](WinMinimize.htm)    | Collapses the specified window    |
|                                   | into a button on the task bar.    |
+-----------------------------------+-----------------------------------+
| [WinMinimizeAll /                 | Minimizes or unminimizes all      |
| WinMin                            | windows.                          |
| imizeAllUndo](WinMinimizeAll.htm) |                                   |
+-----------------------------------+-----------------------------------+
| [WinMove](WinMove.htm)            | Changes the position and/or size  |
|                                   | of the specified window.          |
+-----------------------------------+-----------------------------------+
| [                                 | Sends the specified window to the |
| WinMoveBottom](WinMoveBottom.htm) | bottom of stack; that is, beneath |
|                                   | all other windows.                |
+-----------------------------------+-----------------------------------+
| [WinMoveTop](WinMoveTop.htm)      | Brings the specified window to    |
|                                   | the top of the stack without      |
|                                   | explicitly activating it.         |
+-----------------------------------+-----------------------------------+
| [WinRedraw](WinRedraw.htm)        | Redraws the specified window.     |
+-----------------------------------+-----------------------------------+
| [WinRestore](WinRestore.htm)      | Unminimizes or unmaximizes the    |
|                                   | specified window if it is         |
|                                   | minimized or maximized.           |
+-----------------------------------+-----------------------------------+
| [WinSetAl                         | Makes the specified window stay   |
| waysOnTop](WinSetAlwaysOnTop.htm) | on top of all other windows       |
|                                   | (except other always-on-top       |
|                                   | windows).                         |
+-----------------------------------+-----------------------------------+
| [                                 | Enables or disables the specified |
| WinSetEnabled](WinSetEnabled.htm) | window.                           |
+-----------------------------------+-----------------------------------+
| [WinSetRegion](WinSetRegion.htm)  | Changes the shape of the          |
|                                   | specified window to be the        |
|                                   | specified rectangle, ellipse, or  |
|                                   | polygon.                          |
+-----------------------------------+-----------------------------------+
| [WinSetStyle\                     | Changes the style or extended     |
| WinSetExStyle](WinSetStyle.htm)   | style of the specified window,    |
|                                   | respectively.                     |
+-----------------------------------+-----------------------------------+
| [WinSetTitle](WinSetTitle.htm)    | Changes the title of the          |
|                                   | specified window.                 |
+-----------------------------------+-----------------------------------+
| [WinSet                           | Makes all pixels of the chosen    |
| TransColor](WinSetTransColor.htm) | color invisible inside the        |
|                                   | specified window.                 |
+-----------------------------------+-----------------------------------+
| [WinSetTr                         | Makes the specified window        |
| ansparent](WinSetTransparent.htm) | semi-transparent.                 |
+-----------------------------------+-----------------------------------+
| [WinShow](WinShow.htm)            | Unhides the specified window.     |
+-----------------------------------+-----------------------------------+
| [WinWait](WinWait.htm)            | Waits until the specified window  |
|                                   | exists.                           |
+-----------------------------------+-----------------------------------+
| [WinWaitActive /                  | Waits until the specified window  |
| Win                               | is active or not active.          |
| WaitNotActive](WinWaitActive.htm) |                                   |
+-----------------------------------+-----------------------------------+
| [WinWaitClose](WinWaitClose.htm)  | Waits until no matching windows   |
|                                   | can be found.                     |
+-----------------------------------+-----------------------------------+
| [#Clipboa                         | Changes how long the script keeps |
| rdTimeout](_ClipboardTimeout.htm) | trying to access the clipboard    |
|                                   | when the first attempt fails.     |
+-----------------------------------+-----------------------------------+
| [#DllLoad](_DllLoad.htm)          | [Loads](DllCall.htm#load) a DLL   |
|                                   | or EXE file before the script     |
|                                   | starts executing.                 |
+-----------------------------------+-----------------------------------+
| [#ErrorStdOut](_ErrorStdOut.htm)  | Sends any syntax error that       |
|                                   | prevents a script from launching  |
|                                   | to the standard error stream      |
|                                   | (stderr) rather than displaying a |
|                                   | dialog.                           |
+-----------------------------------+-----------------------------------+
| [#Hotstring](_Hotstring.htm)      | Changes                           |
|                                   | [hotstring](../Hotstrings.htm)    |
|                                   | options or ending characters.     |
+-----------------------------------+-----------------------------------+
| [#HotIf](_HotIf.htm)              | Creates context-sensitive         |
|                                   | [hotkeys](../Hotkeys.htm) and     |
|                                   | [hotstrings](../Hotstrings.htm).  |
|                                   | They perform a different action   |
|                                   | (or none at all) depending on any |
|                                   | condition (an                     |
|                                   | [expressio                        |
|                                   | n](../Language.htm#expressions)). |
+-----------------------------------+-----------------------------------+
| [                                 | Sets the maximum time that may be |
| #HotIfTimeout](_HotIfTimeout.htm) | spent evaluating a single         |
|                                   | [#HotIf](_HotIf.htm) expression.  |
+-----------------------------------+-----------------------------------+
| [#Include /                       | Causes the script to behave as    |
| #IncludeAgain](_Include.htm)      | though the specified file\'s      |
|                                   | contents are present at this      |
|                                   | exact position.                   |
+-----------------------------------+-----------------------------------+
| [#InputLevel](_InputLevel.htm)    | Controls which artificial         |
|                                   | keyboard and mouse events are     |
|                                   | ignored by hotkeys and            |
|                                   | hotstrings.                       |
+-----------------------------------+-----------------------------------+
| [#MaxThreads](_MaxThreads.htm)    | Sets the maximum number of        |
|                                   | simultaneous                      |
|                                   | [threads](../misc/Threads.htm).   |
+-----------------------------------+-----------------------------------+
| [#MaxThre                         | Causes some or all                |
| adsBuffer](_MaxThreadsBuffer.htm) | [hotkeys](../Hotkeys.htm) to      |
|                                   | buffer rather than ignore         |
|                                   | keypresses when their             |
|                                   | [#MaxThreadsPer                   |
|                                   | Hotkey](_MaxThreadsPerHotkey.htm) |
|                                   | limit has been reached.           |
+-----------------------------------+-----------------------------------+
| [#MaxThreadsPer                   | Sets the maximum number of        |
| Hotkey](_MaxThreadsPerHotkey.htm) | simultaneous                      |
|                                   | [threads](../misc/Threads.htm)    |
|                                   | per [hotkey](../Hotkeys.htm) or   |
|                                   | [hotstring](../Hotstrings.htm).   |
+-----------------------------------+-----------------------------------+
| [#NoTrayIcon](_NoTrayIcon.htm)    | Disables the showing of a [tray   |
|                                   | icon](../Program.htm#tray-icon).  |
+-----------------------------------+-----------------------------------+
| [#Requires](_Requires.htm)        | Displays an error and quits if a  |
|                                   | version requirement is not met.   |
+-----------------------------------+-----------------------------------+
| [#Sin                             | Determines whether a script is    |
| gleInstance](_SingleInstance.htm) | allowed to run again when it is   |
|                                   | already running.                  |
+-----------------------------------+-----------------------------------+
| [#S                               | Exempts subsequent                |
| uspendExempt](_SuspendExempt.htm) | [hotkeys](../Hotkeys.htm) and     |
|                                   | [hotstrings](../Hotstrings.htm)   |
|                                   | from [suspension](Suspend.htm).   |
+-----------------------------------+-----------------------------------+
| [#UseHook](_UseHook.htm)          | Forces the use of the hook to     |
|                                   | implement all or some keyboard    |
|                                   | [hotkeys](../Hotkeys.htm).        |
+-----------------------------------+-----------------------------------+
| [#Warn](_Warn.htm)                | Enables or disables warnings for  |
|                                   | specific conditions which may     |
|                                   | indicate an error, such as a typo |
|                                   | or missing \"global\"             |
|                                   | declaration.                      |
+-----------------------------------+-----------------------------------+
| [#WinActi                         | Skips the gentle method of        |
| vateForce](_WinActivateForce.htm) | activating a window and goes      |
|                                   | straight to the forceful method.  |
+-----------------------------------+-----------------------------------+
