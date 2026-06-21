from pathlib import Path

import config
import prepare_data


def test_allowed_departments_are_unique():
    departments = prepare_data.ALLOWED_DEPARTMENTS

    assert len(departments) == 8
    assert len(departments) == len(set(departments))


def test_project_paths_are_relative_to_repository():
    root = Path(__file__).resolve().parents[1]

    assert config.BASE_DIR == root
    assert config.DATA_DIR == root / "data"
    assert config.IMAGE_DIR == root / "data" / "images"
    assert config.ARTIFACT_DIR == root / "artifacts"


def test_large_generated_outputs_are_ignored():
    ignore_text = (config.BASE_DIR / ".gitignore").read_text(
        encoding="utf-8"
    )

    for pattern in ["data/", "artifacts/", "*.pt", "*.onnx", "*.index"]:
        assert pattern in ignore_text
