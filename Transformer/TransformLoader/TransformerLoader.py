# coding=utf-8
from Transformer.TransformLoader.Transform.Transform import Transform


class TransformerLoader:
    def __init__(self):
        self.transforms = [

            Transform("a`", "à"),
            Transform("A`", "À"),

            Transform("a'", "á"),
            Transform("A'", "Á"),

            Transform("a~", "ã"),
            Transform("A~", "Ã"),

            Transform("e'", "é"),
            Transform("E'", "É"),

            Transform("e~", "ẽ"),
            Transform("E~", "Ẽ"),

            Transform("e\^", "ê"),
            Transform("E\^", "Ê"),

            Transform("i'", "í"),
            Transform("I'", "Í"),

            Transform("o'", "ó"),
            Transform("O'", "Ó"),

            Transform("o~", "õ"),
            Transform("O~", "Õ"),

            Transform("u'", "ú"),
            Transform("U'", "Ú"),

            Transform("c~", "ç"),
            Transform("C~", "Ç"),

        ]
