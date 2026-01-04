# 🛡️ Project Penny: AI-Driven Security for Seniors

**Winner: Best Project @ USC MAIA Demo Day** *Recognised by a judging panel of engineers from Netflix and Google for its technical rigour, empathetic design, and real-world scalability.*

---

## 📌 Executive Summary

**Penny** is a comprehensive hardware and software ecosystem designed to protect seniors from the **$28.3 billion** lost annually to financial fraud. While traditional services are reactive, Penny is proactive—utilising a hybrid edge-to-cloud architecture to detect, signal, and alert caregivers of fraud in real-time.

## 👥 Problem Space & User Research

Through interviews with **Lisa Muller** (Activity Director at Hermitage Deep Run Senior Assisted Living), our team identified three critical pillars for the project:

1. **The "Sundown" Window:** Residents are most susceptible to scams between **5:00 PM and 6:00 PM**, requiring a system that is most vigilant during high-risk hours.
2. **Trust-Based Alerts:** Families and residents prefer that "trusted adults" (caregivers) receive notifications to prevent senior panic during a call.
3. **Mobile-First Care:** Caregivers are highly mobile; they require an **iOS-first solution** to monitor residents while on the move.

---

## 🛠️ My Technical Contributions

### 1. Audio Processing & Edge Logic (`voip_audio_capture.py`)

As the **Audio Preprocessing Engineer**, I architected the "Real-Time Ears" of the system.

* **Signal Processing:** Implemented a 4th-order **Butterworth bandpass filter** (300Hz–3400Hz) to isolate human speech and eliminate background noise.
* **Concurrency:** Engineered a multi-threaded pipeline using `queue.Queue` to handle simultaneous audio capture, signal cleaning, and transcription.
* **Edge STT:** Integrated the **VOSK model** for local, privacy-preserving Speech-to-Text, ensuring sensitive resident data remains on the device.
* **Visual Feedback:** Mapped ML confidence scores to **GPIO-controlled LED stoplights** on the physical device to provide seniors with instant, non-verbal safety cues.

### 2. UI/UX & Mobile Development (`React Native`)

I designed and developed the **Penny Caregiver App**, focusing on a professional yet approachable aesthetic.

* **Branding & Onboarding:** Created the `LandingScreen` using a "Piggybank" visual metaphor (Soft Pinks and Shield Accents) to reduce technology anxiety.
* **Risk Visualisation:** Developed the `HomeScreen` dashboard featuring a **Dynamic Risk Signal** system. I used custom utility logic to map complex ML confidence scores into a simple "Red/Orange/Green" status for staff.
* **Facility Management:** Built a scalable stats-tracking card that monitors total residents protected and resolved threats, providing nursing home directors with clear "peace of mind" metrics.

### 3. Cloud Infrastructure & Scaling Strategy

To ensure the system remained cost-effective, I led the architecture transition to the cloud:

* **Supabase Integration:** Offloaded intensive ML inference from the Raspberry Pi 5 to **Supabase** for cloud compute and data storage.
* **Hardware Optimisation:** This hybrid approach reduced the per-unit hardware cost from $300 to roughly $40, making Penny a viable B2B solution for large-scale facilities.

---

## 🏗️ Technical Stack

* **Languages:** Python (Signal Processing), TypeScript (Frontend).
* **ML Models:** DistilBERT (Classification), VOSK (STT), Adversarial Debiasing.
* **Hardware:** Raspberry Pi 5, AI Hat+, GPIO Stoplight LEDs, USB Microphone.
* **Frontend:** React Native, Expo Go.
* **Backend:** Node.js, Supabase (Cloud Compute & Storage).

---

## 📈 Market & Business Logic

* **B2B Model:** Sold directly to assisted living facilities as a "Hardware-as-a-Service" (HaaS).
* **Revenue:** Projected **$190 profit per customer (~80% margin)** based on a monthly subscription model.
* **Market Opportunity:** Targeting a Total Addressable Market (TAM) of **$243M** within the US national senior care network.


---

*Developed by Oma Tasie & Team @ USC Marshall AI Association.* **"Because Every Penny Matters."**

---
