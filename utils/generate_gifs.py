import imageio
from glob import glob

def find_gifs():
    gif_files = glob(f"raw_diagram_exports/*-*.png")
    print(gif_files)
    gif_names = set(["-".join(fp.split("/")[-1].split("-")[:-1]) for fp in gif_files])
    print(gif_names)
    for gif_name in gif_names:
        create_gif(gif_name)

def create_gif(gif_name):
    frames = glob(f"raw_diagram_exports/{gif_name}*")
    with imageio.get_writer(f'images/{gif_name}.gif', mode='I', duration=1.5) as writer:
        for filename in frames:
            image = imageio.imread(filename)
            writer.append_data(image)


if __name__ == "__main__":
    find_gifs()