# ☁️ Cloud-Ink: Interactive Virtual Smart Board

**Cloud-Ink** turns a simple webcam into a gesture-controlled smart board that understands hand movement, voice, and intent — all without touching the screen.  
It’s designed for both **interactive classrooms** and **assistive communication**, where users can write, erase, or point to tiles like “Help,” “Water,” or “Pain,” and hear their intent spoken aloud.

---

## 🎯 Weekly Goal (Nov 10 – Nov 17)

Focus: Build and validate the **gesture → tile → intent → speech** pipeline.

**Tasks**
1. Finalize mapping for 6–10 gesture-controlled tiles.  
2. Integrate AWS **Bedrock** for intent-to-sentence generation.  
3. Add **text-to-speech** with AWS **Polly** or local TTS.  
4. Demonstrate full flow:  
   *Write → select tile → generate polite sentence → speech output.*  
5. Record a short demo video showing complete interaction.

---

## 🧠 Core Components

| Component | Description |
|------------|-------------|
| **Virtual Board System** | Real-time hand tracking via webcam using OpenCV. |
| **Gesture Recognition Engine** | YOLOv2 + VGGNet models for fingertip and gesture classification. |
| **Interactive Tiles** | Accessible UI section with customizable communication tiles. |
| **AI Response Layer** | AWS Bedrock LLM + Polly for text generation and speech. |
| **Hybrid Architecture** | Runs locally for speed, uses cloud only for AI text and speech. |

---

## ⚙️ Tech Stack

**Languages & Libs:** Python 3.11, OpenCV, NumPy, PyTorch, TensorFlow  
**Frameworks:** Flask / Streamlit, Docker  
**Cloud Services:** AWS ECS, S3, Bedrock, Polly, CloudWatch  
**CI/CD:** GitHub Actions

---

## 🚀 Vision

> *“Write in the air. Speak with gestures. Cloud-Ink brings touch-free interaction and accessibility into everyday digital spaces.”*

---

## 👥 Team Roles

| Name | Role | Key Responsibilities |
|------|------|-----------------------|
| **Kotireddy Baddam** | Cloud Engineer | Cloud setup, AWS Bedrock + Polly integration, deployment. |
| **Trishal Varma Mudunuri** | Full Stack Developer | UI & frontend integration with backend gesture logic. |
| **Sujith Reddy Yanamala** | System Developer | Hand/fingertip detection using OpenCV + YOLO pipeline. |
| **Mohammad Abdul Basith** | Support Engineer | Testing, debugging, documentation, and quality control. |

---

