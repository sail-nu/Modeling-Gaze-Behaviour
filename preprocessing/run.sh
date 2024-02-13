#!/usr/bin/env bash
python3 bbox_reader.py && python3 gaze_script.py && python3 pupil_script.py && python3 csv_merge.py && python3 colision.py
