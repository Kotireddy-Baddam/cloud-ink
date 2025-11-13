# ☁️ Cloud-Ink: Interactive Virtual Smart Board

**Cloud-Ink** transforms a simple webcam into a gesture-controlled virtual smart board.
Users can write, erase, move objects, and interact with an assistive communication tile board —
all **without touching the screen**.

Designed for classrooms, accessibility support, and touch-free interaction.

---

# 📌 Latest Weekly Update (Nov 10 – Nov 17)

### **Goal:**

Build and validate the **gesture → tile → intent → speech** pipeline.

### **This Week’s Targets**

* Finalize mapping for **6–10 tiles** (Water, Help, Pain, etc.)
* Connect gesture engine output into backend `/video_feed`.
* Integrate AWS **Bedrock** (intent → sentence).
* Add **TTS** using AWS **Polly** or a local engine.
* UI should show:
  **Write → Select Tile → Generate Sentence → Speak Output**
* Prepare a short end-to-end demo video.

---

# 🧠 Core System Components

### **1. Virtual Board System**

* Real-time drawing surface controlled by fingertip.
* Supports: **write, erase, move, clear**.
* Fully local with OpenCV processing.

### **2. Gesture Recognition Engine**

* **YOLOv2** detects hand region.
* **VGGNet** identifies fingertip and gesture type.
* Outputs:

  * fingertip coordinates
  * gesture label (write/erase/move/clear)

### **3. Assistive Tiles**

* Tile panel for communication.
* When the user holds their fingertip on a tile:
  → tile is selected
  → intent is generated

### **4. AI Response Layer (Cloud + Local Hybrid)**

* Input: Tile intent (e.g., “thirsty”).
* AWS **Bedrock LLM** (planned):
  Converts intent → full polite sentence.
* AWS **Polly** or local TTS:
  Converts sentence → spoken audio.

### **5. Hybrid Architecture**

* **Local**: camera, gesture engine, board, tiles
* **Cloud**: only AI text and speech
* Reduces latency and protects privacy

---

# ⚙️ Tech Stack

### **Languages & Libraries**

* Python 3.11
* OpenCV
* NumPy
* PyTorch (YOLOv2 / VGGNet)

### **Backend**

* Flask or FastAPI
* Local API endpoints:
  `/video_feed`, `/tiles`, `/select_tile`, `/health`

### **Frontend**

* HTML / JS
* Streamlit or web-based UI
* Figma design reference

### **Cloud Services (Planned)**

* AWS ECS (deployment)
* AWS S3 (session logs / assets)
* AWS Bedrock (intent → sentence)
* AWS Polly (speech output)
* CloudWatch (monitoring)

### **DevOps**

* Docker
* GitHub Actions (CI/CD)

---

# 👥 Team Roles (Updated)

| Name                       | Role             | Responsibilities                                                                        |
| -------------------------- | ---------------- | --------------------------------------------------------------------------------------- |
| **Kotireddy Baddam**       | Cloud Engineer   | Cloud integration (Bedrock, Polly), backend API, deployment workflow, architecture.     |
| **Trishal Varma Mudunuri** | Full Stack Dev   | UI building, frontend-backend wiring, tile selection interface, Figma → implementation. |
| **Sujith Reddy Yanamala**  | System Developer | YOLOv2 + VGGNet detection pipeline, gesture mapping, fingertip tracking stability.      |
| **Mohammad Abdul Basith**  | Support / QA     | Tile mapping, testing endpoints, documentation, verifying interaction flow.             |

---

# 🚀 Vision

> **“Write in the air. Speak with gestures.
> Cloud-Ink brings touch-free interaction and accessibility into everyday digital spaces.”**

---

