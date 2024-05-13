from Bio.SeqRecord import SeqRecord
from typing import Iterable, TextIO, Union

def write(
    sequences: Union[Iterable[SeqRecord], SeqRecord],
    handle: TextIO,
    format: str,
) -> int: ...

def parse(handle: TextIO, format: str) -> Iterable[SeqRecord]: ...