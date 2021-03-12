from pathlib import Path

import pytest

from aiostore.base import AbstractStorage


@pytest.mark.asyncio
async def test_AbstractStorage_interface():
    stor = AbstractStorage()

    with pytest.raises(NotImplementedError):
        await stor.get(None)

    with pytest.raises(NotImplementedError):
        await stor.put(None, None)

    with pytest.raises(NotImplementedError):
        await stor.load(None)

    with pytest.raises(NotImplementedError):
        await stor.store(None, None)

    with pytest.raises(NotImplementedError):
        await stor.list(None)


def test_AbstractStorage_prefix_str():
    stor = AbstractStorage('prefix/')
    assert stor.prefix == Path('prefix/')


def test_AbstractStorage_prefix_path():
    stor = AbstractStorage(Path('prefix/'))
    assert stor.prefix == Path('prefix/')
