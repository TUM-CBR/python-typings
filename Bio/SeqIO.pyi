from Bio.SeqRecord import SeqRecord
from typing import Iterator, Iterable, TextIO, Union

def write(
    sequences: Union[Iterable[SeqRecord], SeqRecord],
    handle: TextIO,
    format: str,
) -> int: ...

def parse(handle: TextIO, format: str) -> Iterator[SeqRecord]: ...

def read(handle: TextIO, format: str) -> SeqRecord: ...