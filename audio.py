
import numpy as np
import simpleaudio as sa

FREQUENCY = 440
SAMPLES = 44100
TIME = 3
TIMESPAN = np.linspace(0, TIME, TIME * SAMPLES, endpoint=False)


def create_note(frequency: float, timespan: np.ndarray, volume: float) -> np.ndarray:
    """
    WIP
    """
    # Create a sin wave with the correct frequency:
    note = np.sin(frequency * timespan * 2 * np.pi)
    # Scale the amplitude depending on the volume:
    audio = note * (2 ** volume - 1) / np.max(np.abs(note))
    # Convert to the correct type:
    return audio.astype(np.int16)


notes = [
    create_note(261, TIMESPAN, 10),
    create_note(329, TIMESPAN, 10),
    create_note(391, TIMESPAN, 10),
    create_note(523, TIMESPAN, 10),
]

audio = sum(notes)

play_obj = sa.play_buffer(audio, 1, 2, SAMPLES)

play_obj.wait_done()
