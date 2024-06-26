from abc import ABC
from typing import Any, Dict, Iterator, Optional, Union

class SequenceDataAbstractBaseClass(ABC):
    ...

class _SeqAbstractBaseClass(ABC):
    ...

class Seq:
    _data: Union[bytes, SequenceDataAbstractBaseClass]

    def __init__(
        self,
        data: Union[
            str,
            bytes,
            bytearray,
            _SeqAbstractBaseClass,
            SequenceDataAbstractBaseClass,
            Dict[Any, Any],
            None,
        ],
        length: Optional[int] = None,
    ) -> None: ...

    def replace(
        self,
        old: Union[str, _SeqAbstractBaseClass],
        new: Union[str, _SeqAbstractBaseClass]
    ) -> 'Seq':...

    def __iter__(self) -> Iterator[str]: ...

    def __getitem__(self, index: int) -> str: ...

class MutableSeq:
    ...