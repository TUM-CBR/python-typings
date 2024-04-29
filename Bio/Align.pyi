import numpy as np
from numpy.typing import NDArray
from typing import Dict, Iterator, Sequence

from Bio.SeqRecord import SeqRecord

class Alignment:
    @property
    def inverse_indices(self) -> Sequence[NDArray[np.int64]]: ...

    @property
    def indices(self) -> NDArray[np.int64]: ...

    @property
    def frequencies(self) -> Dict[str, NDArray[np.int64]]: ...

class MultipleSeqAlignment:

    def __iter__(self) -> Iterator[SeqRecord]: ...

    @property
    def alignment(self) -> Alignment: ...

    def __getitem__(self, index: int) -> SeqRecord: ...

    def get_alignment_length(self) -> int: ...

    def __len__(self) -> int: ...