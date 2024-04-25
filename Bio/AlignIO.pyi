from Bio.Align import MultipleSeqAlignment
from typing import Iterable, Literal, Optional, TextIO, Union

Handle = Union[str, TextIO]

AlignFormat = Union[Literal['fasta'], Literal['clustal']]

def write(alignments: Union[MultipleSeqAlignment, Iterable[MultipleSeqAlignment]], handle: Handle, format: AlignFormat) -> int: ...

def read(handle: Handle, format: str,  seq_count: Optional[int] = None) ->  MultipleSeqAlignment: ...