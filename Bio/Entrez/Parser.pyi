from typing import Union

class IntegerElement(int): ...

class StringElement(str): ...

class DictionaryElement(dict[Union[str, StringElement], 'EntrezElement']): ...

class ListElement(list['EntrezElement']): ...

class NoneElement: ...

EntrezElement = Union[IntegerElement, StringElement, DictionaryElement, ListElement, NoneElement]