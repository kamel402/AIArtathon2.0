print('Loading needed modules. Please wait...')

import sys
import os
import json
import secrets
import copy

os.chdir('/content/tegridy-tools/tegridy-tools/')
import TMIDI
os.chdir('/content/')

from fuzzywuzzy import fuzz
from fuzzywuzzy import process
from itertools import islice, accumulate

from pprint import pprint

import tqdm.auto
from tqdm import auto
from midi2audio import FluidSynth
from IPython.display import display, Javascript, HTML, Audio

# only for plotting pianoroll
import pretty_midi
import librosa.display
import matplotlib.pyplot as plt

from google.colab import output, drive

def preparing():
    print('Creating Dataset dir...')
    if not os.path.exists('/content/Dataset'):
        os.makedirs('/content/Dataset')

    os.chdir('/content/')
    print('Loading complete. Enjoy! :)')

    # @title Download English Karaoke MIDI classification model
    % cd / content /
    !wget - -no - check - certificate - O
    Karaoke - English - Full.pickle
    "https://onedrive.live.com/download?cid=8A0D502FC99C608F&resid=8A0D502FC99C608F%2118485&authkey=ABXca9Cn2L-64UE"

    # @title Load and prep the model

    print('Loading the Karaoke model. Please wait...')
    data = TMIDI.Tegridy_Any_Pickle_File_Loader('/content/Karaoke-English-Full')

    print('Done!')
    print('Prepping data...')

    kar_ev_f = data[2]

    kar = []
    karaoke = []

    for k in auto.tqdm(kar_ev_f):
        k.sort(reverse=False, key=lambda x: x[1])
        for kk in k:

            if kk[0] == 'note' or kk[0] == 'text_event':
                kar.append(kk)

    kar_words = []
    for o in auto.tqdm(kar):
        if o[0] != 'note':
            kar_words.append(str(o[2]).lower())

    print('Done! Enjoy! :)')


def Generate_Music(lyrics=["hello"], words_lst=[]):
    preparing()
    # @title Generate Music from the lyrics below

    # @markdown NOTE: No symbols, special chars, commas, etc., please.

    # @markdown ProTip: Be as ambiguous and general as possible for best results as the current dictionary is too small for anything specific.

    randomize_words_matching = False  # @param {type:"boolean"}

    lyric1 = 'I have been going through some things (oh)'  # @param {type:"string"}
    lyric2 = 'I struggle with my inner man'  # @param {type:"string"}
    lyric3 = "I hustle, I'll do what I can to get this money"  # @param {type:"string"}
    lyric4 = 'Blaq Tuxedo'  # @param {type:"string"}

    lyric5 = 'Don Dada on the, Don Dada on the beat'  # @param {type:"string"}
    # lyric6 = 'I know you were right believing for so long' #@param {type:"string"}
    # lyric7 = 'I am all out of love what am I without you' #@param {type:"string"}
    # lyric8 = 'I cant be too late to say that I was so wrong' #@param {type:"string"}

    text = lyrics

    song = []

    print('=' * 100)

    print('Deep-Muse Text to Music Generator')
    print('Starting up...')

    print('=' * 100)

    for t in auto.tqdm(text):
        txt = t.lower().split(' ')

        kar_words_split = list(TMIDI.Tegridy_List_Slicer(kar_words, len(txt)))

        ratings = []

        for k in kar_words_split:
            ratings.append(fuzz.ratio(txt, k))

        if randomize_words_matching:

            try:
                ind = ratings.index(secrets.choice(
                    [max(ratings) - 5, max(ratings) - 4, max(ratings) - 3, max(ratings) - 2, max(ratings) - 1,
                     max(ratings)]))
            except:
                ind = ratings.index(max(ratings))

        else:
            ind = ratings.index(max(ratings))

        words_list = kar_words_split[ind]
        pos = ind * len(txt)

        print(words_list)

        words_lst += ' '.join(words_list) + chr(10)

        c = 0
        for i in range(len(kar)):
            if kar[i][0] != 'note':
                if c == pos:
                    idx = i
                    break

            if kar[i][0] != 'note':
                c += 1

        c = 0
        for i in range(idx, len(kar)):
            if kar[i][0] != 'note':
                if c == len(txt):
                    break

            if kar[i][0] == 'note':
                song.append(kar[i])

            if kar[i][0] != 'note':
                c += 1
                song.append(kar[i])

    so = [y for y in song if len(y) > 3]
    if so != []: sigs = TMIDI.Tegridy_MIDI_Signature(so, so)

    print('=' * 100)

    print(sigs[0])

    print('=' * 100)

    song1 = []
    p = song[0]
    p[1] = 0
    time = 0

    song.sort(reverse=False, key=lambda x: x[1])

    for i in range(len(song) - 1):

        ss = copy.deepcopy(song[i])
        if song[i][1] != p[1]:

            if abs(song[i][1] - p[1]) > 1000:
                time += 300
            else:
                time += abs(song[i][1] - p[1])

            ss[1] = time
            song1.append(ss)

            p = copy.deepcopy(song[i])
        else:

            ss[1] = time
            song1.append(ss)

            p = copy.deepcopy(song[i])

    pprint(words_lst, compact=True)
    print('=' * 100)
    return