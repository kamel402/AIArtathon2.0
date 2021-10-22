import torch
from tqdm.notebook import trange
from IPython.display import Image, display
from deep_daze.deep_daze import Imagine
from tqdm.notebook import trange
from IPython.display import Image, display


def deep_daze(TEXT, NUM_LAYERS, SAVE_EVERY, IMAGE_WIDTH, SAVE_PROGRESS=True, LEARNING_RATE=1e-5, ITERATIONS=1021, START_IMAGE_PATH='', weights_path='', images_path='', load_width=False):
    model = Imagine(
        text=TEXT,
        num_layers=NUM_LAYERS,
        save_every=SAVE_EVERY,
        image_width=IMAGE_WIDTH,
        lr=LEARNING_RATE,
        iterations=ITERATIONS,
        save_progress=SAVE_PROGRESS
    )
    model.textpath = images_path + "/image"
    for epoch in trange(20, desc='epochs'):
        for i in trange(ITERATIONS, desc='iteration'):
            model.train_step(epoch, i)

            if i % model.save_every != 0:
                continue
            filename = '/content/drive/MyDrive/artathon/journey/first/images/image'
            image = Image(f'/{filename}.jpg')
            print(image)
            display(image)
            torch.save(model.state_dict(), weights_path + f'/epoch_{epoch}')
    return