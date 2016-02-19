# coding=utf-8
from Transformer.TransformLoader.Transform.Transform import Transform


class TransformerLoader:
    def __init__(self):
        self.transforms = [
            Transform("a'", "á"),
            Transform("'a", "à"),
            Transform("a~", "ã")
        ]
