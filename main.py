#!/usr/bin/env python3
import sys;import os;_, file, *ts=sys.argv;os.execlp('ffmpeg', 'ffmpreg', *[i for j, t in enumerate(ts) for i in ['-ss', t, '-frames:v', '1', f'output{j}.png']], '-i', file)
