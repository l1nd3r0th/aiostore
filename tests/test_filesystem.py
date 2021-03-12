from pathlib import Path
from unittest.mock import patch

import pytest

from aiostore.filesystem import FilesystemStorage


@pytest.mark.asyncio
@patch('aiostore.filesystem.aiofiles.open')
async def test_FilesystemStorage_get_text(mock_open):
    stor = FilesystemStorage(prefix='prefix/')
    await stor.get('path/file.txt')

    assert mock_open.call_args.args == (Path('prefix/path/file.txt'),)
    assert mock_open.call_args.kwargs == {'mode': 'r'}
    assert mock_open.return_value.__aenter__.return_value.read.call_count == 1


@pytest.mark.asyncio
@patch('aiostore.filesystem.aiofiles.open')
async def test_FilesystemStorage_get_bytes(mock_open):
    stor = FilesystemStorage(prefix='prefix/')
    await stor.get(Path('path/file.bin'), text=False)

    assert mock_open.call_args.args == (Path('prefix/path/file.bin'),)
    assert mock_open.call_args.kwargs == {'mode': 'rb'}
    assert mock_open.return_value.__aenter__.return_value.read.call_count == 1


@pytest.mark.asyncio
@patch('aiostore.filesystem.aiofiles.open')
async def test_FilesystemStorage_put_text(mock_open):
    stor = FilesystemStorage(prefix='prefix/')
    await stor.put('path/file.txt', 'test data')

    assert mock_open.call_args.args == (Path('prefix/path/file.txt'),)
    assert mock_open.call_args.kwargs == {'mode': 'w'}
    assert mock_open.return_value.__aenter__.return_value.write.call_count == 1


@pytest.mark.asyncio
@patch('aiostore.filesystem.aiofiles.open')
async def test_FilesystemStorage_put_bytes(mock_open):
    stor = FilesystemStorage(prefix='prefix/')
    await stor.put('path/file.bin', b'test\x00data')

    assert mock_open.call_args.args == (Path('prefix/path/file.bin'),)
    assert mock_open.call_args.kwargs == {'mode': 'wb'}
    assert mock_open.return_value.__aenter__.return_value.write.call_count == 1
