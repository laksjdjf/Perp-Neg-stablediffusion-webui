# Perp-Neg-stablediffusion-webui
（実験中）
[Perp-Neg](https://github.com/Perp-Neg/Perp-Neg-stablediffusion)のwebui拡張です。インストールしてでてくるアコーディオン開いてenableにチェックを押すと起動します。

以下のようにプロンプトを指定して、ネガティブプロンプトの欄を空欄にしてください。
```
<main_prompt>
AND <negative_prompt> :-1.0
```

Perp-Neg自体は3D画像の生成のための手法ですが、この拡張はその実装をする予定はありません。
# CITIATION
```
@article{armandpour2023re,
  title={Re-imagine the Negative Prompt Algorithm: Transform 2D Diffusion into 3D, alleviate Janus problem and Beyond},
  author={Armandpour, Mohammadreza and Sadeghian, Ali and Zheng, Huangjie and Sadeghian, Amir and Zhou, Mingyuan},
  journal={arXiv preprint arXiv:2304.04968},
  year={2023}
}
```
