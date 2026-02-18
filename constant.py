import pathlib
from pathlib import Path

BASE_DIR: Path = pathlib.Path(__file__).parent
INITIAL_DATA_DIR_LESSON_16: Path = BASE_DIR / "lessons" / "Lesson_16" / "initial_data"
INITIAL_DATA_XMLS_LESSON_16: Path = INITIAL_DATA_DIR_LESSON_16 / "xmls"
INITIAL_DATA_JSONS_LESSON_16: Path = INITIAL_DATA_DIR_LESSON_16 / "jsons"
INITIAL_DATA_CSVS_LESSON_16: Path = INITIAL_DATA_DIR_LESSON_16 / "csvs"
