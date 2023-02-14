"""Init method where main routes are."""
import logging
from pathlib import Path

ROOT = Path(__file__).parents[1]
RESULTS_FOLDER = ROOT / "results"
MODEL_PATH = ROOT / "models" / "speedy"

log = logging.getLogger(__name__)
