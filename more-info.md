# Overview

Providing some more information on why python progress bar created and why not use any of the many timers that are available.

In some of the online team meetings I have been involved we have been looking for ways experiment with timers to keep the meeting on track.

After an initial search I was unable to find a quick solution that met the following criteria:

- **Open Source** - Open source with source code available so can review and inspect the code being run and not need to install a compiled binary.

- **Cross Platform** - Be cross platform and able to run in Windows, MacOS and Linux environments.

- **Cross Application** Be able to sit on top of any application being shared as part of the meeting

- **Simple** Just perform timing related tasks and not an overall presentation system like [OBS Studio](https://obsproject.com/)

- **Configurable** Colors, position and text should be configurable and not hard coded

- **Accessible** Provide multiple methods of interaction via command line or via Hotkeys to quickly change progress bar state

- **Handle Extra Time** Allocated speaking times often go overtime. Provide a subtle way to allow for additional time but make people aware of extra time that is being used

- **Respond Quickly** Enable the person sharing the screen to quickly adjust the times so respond to changing time requirements

- **Extensible** Allow changes or additions to be quickly added based on feedback from meeting participants