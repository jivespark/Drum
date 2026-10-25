import board
import audiobusio
import audiocore
import audiomixer
import time
import touchio

touch_pins=(
    board.IO1, board.IO2, board.IO3, board.IO4, board.IO5, board.IO6, board.IO7, board.IO8,
)
pads=[touchio.TouchIn(pin) for pin in touch_pins]

audio=audiobusio.I2SOut(
    bit_clock=board.IO44,
    word_select=board.IO43,
    data=board.IO9,
)

mixer=audiomixer.Mixer(
    voice_count=8,
    sample_rate=22050,
    channel_count=1,
    bits_per_sample=16,
    samples_signed=True,
    buffer_size=4096,
)

audio.play(mixer)

files=[
    "/sounds/kick.wav", "/sounds/snare.wav", "/sounds/high.wav", "/sounds/floor.wav", "/sounds/closed.wav", "/sounds/open.wav", "/sounds/crash.wav", "/sounds/ride.wav",
]
samples=[audiocore.WaveFile(open(path, "rb")) for path in files]

was_touched=[False]*len(pads)
while True:
    for i, pad in enumerate(pads):
        touched=pad.value
        if touched and not was_touched[i]:
            mixer.voice[i].play(samples[i], loop=False)
        was_touched[i]=touched
    time.sleep(0.01)