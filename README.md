# random_episode
Tiny Python-based app for generating random episode number of TV series. Based on Kivy Framework

## Python
On first launch program takes a number of seasons and episodes and stores them in memory.
When it generates random season-episode pair, program marks them as **watched**. So it will generate only **unwatched** episodes.
When list of available episodes ends it`s suggested to reset marked list or input new TV series data.

## Kivy
There are Kivy Framework files in repo. They can be used to build Android (and also iOS, not tested) application via Buildozer.
One test APK is included.
