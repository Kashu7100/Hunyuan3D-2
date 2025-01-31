<div align="center">
  <a href=https://3d.hunyuan.tencent.com target="_blank"><img src=https://img.shields.io/badge/Official%20Site-333399.svg?logo=homepage height=22px></a>
  <a href=https://huggingface.co/spaces/tencent/Hunyuan3D-2  target="_blank"><img src=https://img.shields.io/badge/%F0%9F%A4%97%20Demo-276cb4.svg height=22px></a>
  <a href=https://huggingface.co/tencent/Hunyuan3D-2 target="_blank"><img src=https://img.shields.io/badge/%F0%9F%A4%97%20Models-d96902.svg height=22px></a>
  <a href=https://3d-models.hunyuan.tencent.com/ target="_blank"><img src= https://img.shields.io/badge/Page-bb8a2e.svg?logo=github height=22px></a>
  <a href=https://discord.gg/GuaWYwzKbX target="_blank"><img src= https://img.shields.io/badge/Discord-white.svg?logo=discord height=22px></a>
  <a href=https://arxiv.org/abs/2501.12202 target="_blank"><img src=https://img.shields.io/badge/Report-b5212f.svg?logo=arxiv height=22px></a>
  <a href=https://x.com/txhunyuan target="_blank"><img src=https://img.shields.io/badge/Hunyuan-black.svg?logo=x height=22px></a>
 <a href="#community-resources" target="_blank"><img src=https://img.shields.io/badge/Community-lavender.svg?logo=homeassistantcommunitystore height=22px></a>
</div>

[//]: # (  <a href=# target="_blank"><img src=https://img.shields.io/badge/Report-b5212f.svg?logo=arxiv height=22px></a>)

[//]: # (  <a href=# target="_blank"><img src= https://img.shields.io/badge/Colab-8f2628.svg?logo=googlecolab height=22px></a>)

[//]: # (  <a href="#"><img alt="PyPI - Downloads" src="https://img.shields.io/pypi/v/mulankit?logo=pypi"  height=22px></a>)


<p align="center">
  <img src="assets/images/system.jpg">
</p>

## ☯️ **Hunyuan3D 2.0**


Generation results of Hunyuan3D 2.0:
<p align="left">
  <img src="assets/images/e2e-2.gif"  height=250>
</p>

### Pretrained Models

It takes 11.5 GB VRAM for shape generation and 24.5 GB for shape and texture generation in total.

| Model                  | Date       | Params | Huggingface                                                                             |
|------------------------|------------|--------|-----------------------------------------------------------------------------------------| 
| Hunyuan3D-DiT-v2-0     | 2025-01-21 | 2.6B   | [Download](https://huggingface.co/tencent/Hunyuan3D-2)                                  |
| Hunyuan3D-Paint-v2-0   | 2025-01-21 | 1.3B   | [Download](https://huggingface.co/tencent/Hunyuan3D-2)                                  |
| Hunyuan3D-Delight-v2-0 | 2025-01-21 | 1.3B   | [Download](https://huggingface.co/tencent/Hunyuan3D-2/tree/main/hunyuan3d-delight-v2-0) | 

## 🤗 Get Started with Hunyuan3D 2.0

### Install Requirements

Please install Pytorch via the [official](https://pytorch.org/) site. Then install the other requirements via

```bash
conda create -n hunyuan python=3.10
conda activate hunyuan
git clone https://github.com/Kashu7100/Hunyuan3D-2.git
cd Hunyuan3D-2
pip install -r requirements.txt
# for texture
# need to have cuda (move to compute node)
cd hy3dgen/texgen/custom_rasterizer
python3 setup.py install
cd ../../..
cd hy3dgen/texgen/differentiable_renderer
python3 setup.py install
cd ../../..
```

### Usage
Please visit [minimal_demo.py](minimal_demo.py) for more (**text to 3D** and **image to 3D**).

```bash
python minimal_demo.py
```

### API Server

You could launch an API server locally, which you could post web request for Image/Text to 3D, Texturing existing mesh, and e.t.c.

```bash
python api_server.py --host 0.0.0.0 --port 8081
```

A demo post request for image to 3D without texture.
```bash
python sample_request.py
```

### Official Site

Don't forget to visit [Hunyuan3D](https://3d.hunyuan.tencent.com) for quick use, if you don't want to host yourself.


## 🔗 BibTeX

If you found this repository helpful, please cite our reports:

```bibtex
@misc{hunyuan3d22025tencent,
    title={Hunyuan3D 2.0: Scaling Diffusion Models for High Resolution Textured 3D Assets Generation},
    author={Tencent Hunyuan3D Team},
    year={2025},
    eprint={2501.12202},
    archivePrefix={arXiv},
    primaryClass={cs.CV}
}

@misc{yang2024hunyuan3d,
    title={Hunyuan3D 1.0: A Unified Framework for Text-to-3D and Image-to-3D Generation},
    author={Tencent Hunyuan3D Team},
    year={2024},
    eprint={2411.02293},
    archivePrefix={arXiv},
    primaryClass={cs.CV}
}
```

## Community Resources

Thanks for the contributions of community members, here we have these great extensions of Hunyuan3D 2.0:

- [ComfyUI-3D-Pack](https://github.com/MrForExample/ComfyUI-3D-Pack) 
- [ComfyUI-Hunyuan3DWrapper](https://github.com/kijai/ComfyUI-Hunyuan3DWrapper)
- [Hunyuan3D-2-for-windows](https://github.com/sdbds/Hunyuan3D-2-for-windows)
- [📦 A bundle for running on Windows | 整合包](https://github.com/YanWenKun/Hunyuan3D-2-WinPortable)
- [Hunyuan3D-2GP](https://github.com/deepbeepmeep/Hunyuan3D-2GP)


## Acknowledgements

We would like to thank the contributors to
the [DINOv2](https://github.com/facebookresearch/dinov2), [Stable Diffusion](https://github.com/Stability-AI/stablediffusion), [FLUX](https://github.com/black-forest-labs/flux), [diffusers](https://github.com/huggingface/diffusers), [HuggingFace](https://huggingface.co), [CraftsMan3D](https://github.com/wyysf-98/CraftsMan3D),
and [Michelangelo](https://github.com/NeuralCarver/Michelangelo/tree/main) repositories, for their open research and
exploration.
