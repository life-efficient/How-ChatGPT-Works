import imageio
from glob import glob

START_DIR = "raw_diagram_exports"

def find_gifs():
    gif_files = glob(f"{START_DIR}/*-*.png")
    print(gif_files)
    gif_names = set(["-".join(fp.split("/")[-1].split("-")[:-1]) for fp in gif_files])
    print(gif_names)
    for gif_name in gif_names:
        create_gif(gif_name)

def create_gif(gif_name):
    frames = glob(f"{START_DIR}/{gif_name}*")
    frames.sort()
    frames.reverse()
    frames.pop(0) # remove first file, which is the master component
    with imageio.get_writer(f'images/{gif_name}.gif', mode='I', duration=1.5) as writer:
        for filename in frames:
            image = imageio.imread(filename)
            writer.append_data(image)


if __name__ == "__main__":
    find_gifs()