# Python Progress Timer

“Time – the one asset none of us are ever going to get more of.”
– Gary Vaynerchuk

We have all been in meeting and presentations and found it difficult to manage our time and get keep on time. The Python Progress bar is a very simple sample application that provides a visual guide to your audience to help show progress.

The sample application is implemented to be placed over top any window on the main display. As a result it can be included on top of an exiting presentation or live screen sharing session to track progress.

By being outside a presentation or slide you can switch between slides or across applications and still provide the visual vue on progress.

## Hotkeys

The application has the following hot keys defined
<ctrl>+<alt>+0 - Clear Timer
<ctrl>+<alt>+1 - <ctrl>+<alt>+9 Set Time from times.txt
<ctrl>+<shift>+1 - <ctrl>+<shift>+9 Set Time Extra time 1 - 5 mins

## Technical Details

Minimal sample application that uses Python [tkinker](https://docs.python.org/3/library/tkinter.html) module to implement a top of screen overlay.

## Getting Started

1. Ensure you have python >= 3.6 installed.

1. Install python requirements

```bash
pip install -r requirements.txt
```

1. Run sample

```bash
python timer.py
```

## Usage

The command line will ask how long to display timer. Options numeric value of 1-10 minutes or e to exit.

Press Control-C to exit application after exit
