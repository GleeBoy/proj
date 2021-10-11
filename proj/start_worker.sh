#!/bin/bash
nohup celery -A proj worker -n hotplay_default_worker -c 3 -Q hotplay_sh_default_queue -l info &