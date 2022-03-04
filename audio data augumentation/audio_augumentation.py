import librosa
import soundfile as sf
import os
from pydub import AudioSegment
import numpy as np


def augument_audio(orig_file_name):
    """
    """
    slow_down=[0.25,0.3,0.5,0.6,0.75]
    speeds=[1.25,1.8,1.5,1.75,2]
    pitches=[3,5,6,8,9]
    noise_file_dir='./noises'
    noise_files=[os.path.join(noise_file_dir,file) for file in os.listdir(noise_file_dir)]
    selected_speeds=np.random.choice(slow_down,2)+np.random.choice(speeds,2)
    selected_pitches=np.random.choice(pitches,2)
    selected_noises=np.random.choice(noise_files,4)
    filelist=list()
    #load file
    data,sr=librosa.load(orig_file_name)
    #speed change
    for speed in selected_speeds:
        new_filename=os.path.splitext(orig_file_name)[0]+f"_speed_{str(speed)}X.wav"
        data_speed=librosa.effects.time_stretch(data,rate=speed)
        sf.write(new_filename,data_speed,sr) 
        filelist.append(new_filename)
    #pitch shift
    for pitch in selected_pitches:
        new_filename=os.path.splitext(orig_file_name)[0]+f"_pitch_{str(pitch)}.wav"
        data_pitch=librosa.effects.time_stretch(data,rate=speed)
        sf.write(new_filename,data_pitch,sr) 
        filelist.append(new_filename)
#     addition of noise
    for i,noise in enumerate(selected_noises):
        sound1 = AudioSegment.from_file(noise_files[1])
        sound2 = AudioSegment.from_file(orig_file_name)
        duration=sound2.duration_seconds
        sound1= sound1[0:duration*1000]
        combined = sound2.overlay(sound1)
        new_filepath=os.path.splitext(orig_file_name)[0]+f"_noise_{str(i)}.wav"
        combined.export(new_filepath, format='wav')
        filelist.append(new_filepath)
    #return list of all generated files
    return filelist


if __name__ =='__main__':
    test_file='./samples/sample1_marathi_2.wav'
    augument_audio(test_file)
