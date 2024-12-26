def RecordingButtons1():
    global MController
    if input.button_is_pressed(Button.A):
        if MController == 0:
            MController = 1
            RecoringSystyms(list2)
    if input.button_is_pressed(Button.B):
        if MController == 0:
            PlayAudioSystyms(list2)
def StopRecording():
    AudioP = Music
def RecoringSystyms(Audio: List[any]):
    global Music
    record.start_recording(Music)
def RecordingButtons2():
    global MController
    if input.button_is_pressed(Button.A):
        if MController == 1:
            MController = 0
            StopRecording()
    if input.button_is_pressed(Button.B):
        if MController == 1:
            MController = 0
            StopRecording()
            PlayAudioSystyms(list2)
def PlayAudioSystyms(Audio2: List[any]):
    record.play_audio(Music)
list2: List[number] = []
MController = 0
MController = 0
Music = 0

def on_forever():
    if MController == 0:
        RecordingButtons1()
    if MController == 1:
        RecordingButtons2()
basic.forever(on_forever)
