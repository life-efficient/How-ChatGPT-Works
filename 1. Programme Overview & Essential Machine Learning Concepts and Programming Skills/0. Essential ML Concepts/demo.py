# %%
import torch
import plotly.express as px
from plotly.subplots import make_subplots
import numpy as np
import sys
sys.path.append('../..')
from utils.generate_gifs import find_gifs  # noqa


def generate_params():
    def reset_params():
        w = torch.tensor(0).float().unsqueeze(0)
        w = w.unsqueeze(0)
        b = torch.tensor(0).float().unsqueeze(0)
        return w, b

    thetas = torch.linspace(0, 2*np.pi, 100)
    w, b = reset_params()
    for theta in thetas:
        w = torch.ones_like(w) * torch.sin(theta)
        yield w, b

    w, b = reset_params()
    for theta in thetas:
        b = torch.ones_like(b) * torch.sin(theta)
        b *= 5
        yield w, b

    for theta in thetas:
        w = torch.ones_like(w) * torch.sin(theta)
        b = torch.ones_like(b) * torch.sin(theta)
        b *= 5
        yield w, b


class LinearModel(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(1, 1)

    def forward(self, x):
        return self.linear(x)


def visualise():
    """
    Use this function to visualise the model's predictions for different yielded parameters using plotly express

    Shows a figure with two 2d subplots side by side, one for the predictions and one for the parameters.

    The paramameters are on a graph where the x-axis is the bias and the y-axis is the weight.

    For each set of parameters, images of both graphs are saved to the current directory
    The range for each figure is fixed to [-10, 10] for the x-axis and [-10, 10] for the y-axis
    The range for the parameters is also fixed to [-10, 10] for the x-axis and [-10, 10] for the y-axis
    The figures are square
    The 
    """
    model = LinearModel()
    inputs = np.linspace(-10, 10)
    inputs = torch.tensor(inputs).float().unsqueeze(1)

    for idx, params in enumerate(generate_params()):
        # print('Params: ', params)
        w, b = params
        # print(model.linear.weight.shape)
        # print(w.shape)
        model.linear.weight = torch.nn.Parameter(w)
        # print(model.linear.weight.shape)
        model.linear.bias = torch.nn.Parameter(b)
        # print(inputs.shape)
        predictions = model(inputs)
        predictions = predictions.squeeze().detach().numpy()
        fig = make_subplots(rows=1, cols=2, specs=[
                            [{"type": "scatter"}, {"type": "scatter"}]])
        fig.add_trace(px.line(x=inputs.squeeze().numpy(),
                      y=predictions).data[0], row=1, col=1)

        b = b.squeeze().detach().numpy()
        w = w.squeeze().detach().numpy()
        fig.add_trace(px.scatter(x=[b], y=[w]).data[0], row=1, col=2)

        fig.update_xaxes(range=[-10, 10], row=1, col=1)
        fig.update_yaxes(range=[-10, 10], row=1, col=1)
        fig.update_xaxes(title_text="Input", row=1, col=1)
        fig.update_yaxes(title_text="Prediction", row=1, col=1)

        fig.update_xaxes(range=[-10, 10], row=1, col=2)
        fig.update_yaxes(range=[-10, 10], row=1, col=2)
        fig.update_xaxes(title_text="Bias", row=1, col=2)
        fig.update_yaxes(title_text="Weight", row=1, col=2)

        fig.update_layout(title_text=f"b: {b}, w: {w}")

        fig.update_layout(width=1000, height=500)

        # fig = px.line(x=inputs.squeeze().numpy(), y=predictions)
        # fig.update_xaxes(range=[-10, 10])
        # fig.update_yaxes(range=[-10, 10])
        # fig.update_layout(width=500, height=500)
        # fig.show()
        # fig = px.scatter(x=b, y=w)
        # fig.show()

        fig.write_image(f"output/prediction-{idx}.png")
        # fig.write_image(f"output/params-{idx}.png")
        if idx > 100:
            break


if __name__ == "__main__":
    visualise()
    find_gifs("output")

# %%
