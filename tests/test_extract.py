from pathlib import Path

import pytest

from src.extract import extract_csv


def test_extract_belfast():
    project_root = Path(__file__).resolve().parents[1]
    file_path = project_root / "data" / "parcelflow_belfast_2026-10-12.csv"

    records = extract_csv(file_path)

    assert len(records) == 320


def test_extract_manchester():
    project_root = Path(__file__).resolve().parents[1]
    file_path = project_root / "data" / "parcelflow_manchester_2026-10-12.csv"

    records = extract_csv(file_path)

    assert len(records) == 460


def test_extract_birmingham():
    project_root = Path(__file__).resolve().parents[1]
    file_path = project_root / "data" / "parcelflow_birmingham_2026-10-12.csv"

    records = extract_csv(file_path)

    assert len(records) == 570


def test_extract_structure():
    project_root = Path(__file__).resolve().parents[1]
    file_path = project_root / "data" / "parcelflow_belfast_2026-10-12.csv"
    
    records = extract_csv(file_path)

    assert isinstance(records[0], dict)
    assert 'shipment_id' in records[0]
    assert 'event_id' in records[0]


def test_extract_missing_file():
    project_root = Path(__file__).resolve().parents[1]
    file_path = project_root / "data" / "parcelflow_dublin_2022-01-02.csv"
            
    with pytest.raises(FileNotFoundError):
        extract_csv(file_path)