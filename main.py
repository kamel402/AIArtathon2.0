from deep_daze import deep_daze
import argparse
from deep_muse import deep_muse

parser = argparse.ArgumentParser(description='A test program.')

args = parser.parse_args()
def main():
    deep_daze(args.TEXT, args.NUM_LAYERS, args.SAVE_EVERY, args.IMAGE_WIDTH, args.SAVE_PROGRESS, args.LEARNING_RATE, args.ITERATIONS, args.START_IMAGE_PATH, args.weights_path, args.images_path, args.load_width)
    deep_muse.Generate_Music(args.lyrics, args.word_lst)

if __name__ == "__main__":
    parser.add_argument("TEXT")
    parser.add_argument("NUM_LAYERS")
    parser.add_argument("SAVE_EVERY")
    parser.add_argument("IMAGE_WIDTH")
    parser.add_argument("SAVE_PROGRESS")
    parser.add_argument("LEARNING_RATE")
    parser.add_argument("ITERATIONS")
    parser.add_argument("START_IMAGE_PATH")
    parser.add_argument("weights_path")
    parser.add_argument("images_path")
    parser.add_argument("load_width")
    parser.add_argument("lyrics")
    parser.add_argument("word_lst")
    args = parser.parse_args()

    main()