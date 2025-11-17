/*
    AutoHotkey v2 Example: SoundBeep
    Documentation: SoundBeep.md
    Category: Sound Functions

    This example demonstrates practical usage of SoundBeep.
    Modify and experiment to learn!
*/


; Simple beep
SoundBeep

; Custom frequency and duration
SoundBeep 1000, 500  ; 1000Hz for 500ms

; Beep pattern
Loop 3 {
    SoundBeep 500, 200
    Sleep 200
}


/*
    For complete documentation, see: SoundBeep.md
    AutoHotkey v2 Documentation: https://www.autohotkey.com/docs/v2/
*/
