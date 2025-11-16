# Cloud-Ink: Interactive Virtual Smart Board

Cloud-Ink turns a simple webcam into a gesture-controlled virtual smart board.

Users can:

- ✍️ **Write** on a digital board using hand gestures  
- 🧽 **Erase** drawn content  
- ✋ **Move / inspect** existing strokes  
- 🧼 **Clear** the entire board with a full-hand gesture  
- 🌐 Send gesture events to a **local FastAPI server** for logging and future UI / AI features  

---

## Current Components (Engine Only)

> Right now this repo only tracks dependencies and documentation.  
> All engine code is still local while we finish refactoring.

### 1. Gesture Board

- OpenCV + MediaPipe based drawing surface  
- Detects finger states (write / erase / move / clean)  
- Renders to a black board window in real time  

### 2. Hand Detector

- Wrapper around MediaPipe Hands  
- Provides:
  - Landmark coordinates in pixel space  
  - Handedness (Left / Right)  
  - Utility functions like `fingersUp()` and distance between points  

### 3. Event Client

- Lightweight HTTP client using `requests`  
- Sends gesture events to a local API:

```text
POST /gesture/event
{
  "gesture": "<write|erase|move|clean>",
  "x": <int>,
  "y": <int>,
  "state": "<current_state>"
}
