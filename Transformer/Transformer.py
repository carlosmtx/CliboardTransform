from TransformLoader.TransformerLoader import TransformerLoader
import re


class Transformer:
    def __init__(self, loader=TransformerLoader()):
        self.loader = loader
        self.transforms = loader.transforms

    def transform(self, str):
        final_str = str
        for transform in self.transforms:
            final_str = re.sub("%s" % transform.pattern, transform.transform, final_str)

        return final_str
