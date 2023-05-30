import torch

import modules.scripts as scripts
import gradio as gr

from modules.script_callbacks import CFGDenoisedParams, on_cfg_denoised

from modules.processing import StableDiffusionProcessing


class Script(scripts.Script):
    def __init__(self):
        super().__init__()
        return 

    def title(self):
        return "Perp-Neg"

    def show(self, is_img2img):
        return scripts.AlwaysVisible

    def ui(self, is_img2img):
        with gr.Group():
            with gr.Accordion("Perp-Neg", open=False):
                with gr.Row():
                    enable = gr.Checkbox(value=False, label="Enable")
        return (enable, )

    def get_perpneg(self, x, y, u):
        assert x.shape == y.shape == u.shape
        xu = x - u
        yu = y - u
        # webui側uncondが引かれてしまうので、あらかじめuncondを足しておく
        return xu - ((torch.mul(xu, yu).sum())/(torch.norm(yu)**2)) * yu + u

    def denoised_callback(self, params: CFGDenoisedParams):
        if self.enable:
            # params.x: [main_prompt, sub_prompt1, sub_prompt2, ...] * batch_size + [uncond] * batch_size
            x_cond = params.x[:-self.batch_size]
            x_uncond = params.x[-self.batch_size:]
            num_prompt = x_cond.shape[0] // self.batch_size
            for i in range(1, num_prompt):
                x_cond[i::num_prompt] = \
                    self.get_perpneg(x_cond[i::num_prompt], x_cond[0::num_prompt], x_uncond)
            params.x = torch.cat([x_cond, x_uncond], dim=0)

    def process(
        self,
        p: StableDiffusionProcessing,
        enable: bool
    ):

        self.enable = enable
        self.batch_size = p.batch_size
        if not self.enable:
            return

        if not hasattr(self, 'callbacks_added'):
            on_cfg_denoised(self.denoised_callback)
            self.callbacks_added = True
        return
