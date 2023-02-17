import imageio
import os
from glob import glob

START_DIR = "figma_diagram_exports"
OUTPUT_DIR = "generated_gifs"


def find_gifs(start_dir="frames"):
    gif_files = glob(f"./{start_dir}/*-*.png")
    # print(gif_files)
    gif_names = set(["-".join(fp.split("/")[-1].split("-")[:-1])
                    for fp in gif_files])
    print(gif_names)
    for gif_name in gif_names:
        create_gif(gif_name, start_dir)


def create_gif(gif_name, start_dir):
    frames = glob(f"./{start_dir}/{gif_name}*")
    frames.sort(key=lambda x: int(x.split("-")[-1].split(".")[0]))
    frames.reverse()
    frames.pop(0)  # remove first file, which is the master component
    gif_name = f'{gif_name}.gif'
    print("Creating:", gif_name)
    # if gif_name in os.listdir(OUTPUT_DIR):
    #     print("Skipping:", gif_name)
    #     return
    gif_name = f'{OUTPUT_DIR}/{gif_name}'
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR, exist_ok=True)
    with imageio.get_writer(gif_name, mode='I', fps=10) as writer:
        for filename in frames:
            image = imageio.imread(filename)
            writer.append_data(image)
    print("Generated:", gif_name)


if __name__ == "__main__":
    find_gifs(START_DIR)
