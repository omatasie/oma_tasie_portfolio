# Project Penny: AI-Powered Financial Fraud Detection for Senior Protection

**Winner: Best Project @ USC MAIA Demo Day**

Recognised by a judging panel of engineers from Netflix and Google for technical rigour, market viability, and impact on senior digital safety.

---

## Project Overview

* **Organisation:** Marshall AI Association (MAIA) - Finance Department, USC
* **Project Duration:** Fall 2025
* **Key Roles:** Audio Processing Engineer & iOS Frontend Developer
* **Technologies:** Raspberry Pi 5, Python, React Native, Expo Go, DistilBERT, Supabase

## Problem Statement

Approximately 28.3 billion dollars is stolen annually from Americans over age 60 via financial fraud. Seniors in nursing homes are primary targets for sophisticated phone and email scams that exploit cognitive vulnerabilities and social isolation.

## The Solution

Penny is a comprehensive hardware-software ecosystem that detects and alerts caregivers of fraud in real-time through:

* **Hardware:** A Raspberry Pi-powered device (prototype) transitioning to a Bluetooth-integrated unit for scalability.
* **Mobile App:** An iOS application for nursing home staff with real-time push notifications.
* **Interface:** GPIO stoplight indicators (Red/Yellow/Green) for immediate visual feedback and an ElevenLabs-powered voice agent.
* **Intelligence:** A DistilBERT AI model for high-accuracy threat classification.

---

## System Architecture

### Hardware Components

* **Development Prototype:** Raspberry Pi 5, AI Hat+, USB microphone/speakers, and GPIO LEDs. Encased in an accessible form factor.
* **Scalable Production Model:** Bluetooth speaker with integrated lights. Reduced per-unit hardware cost from 297 dollars to 17 dollars by offloading compute to the cloud via Supabase.

### Software Stack

* **Backend:** Python for signal processing, VOSK for local Speech-to-Text (STT), and DistilBERT for classification.
* **Frontend:** React Native, Expo Go, and Node.js.
* **Cloud:** Supabase for data storage and remote ML inference.

---

## Technical Contributions

### 1. Audio Processing Pipeline (voip_audio_capture.py)

I implemented the comprehensive audio capture and preprocessing system to ensure high-fidelity data for ML inference.

**Core Engineering:**

* **Input Modes:** Supported live microphone capture, VOIP streams, and WAV file validation.
* **Signal Processing:** Implemented threshold-based noise gates and 300-3400 Hz bandpass filters optimised for human voice using scipy.
* **Performance:** Architected a producer-consumer threading pattern with thread-safe queues to maintain <20ms latency for real-time processing.
* **Privacy-First STT:** Integrated VOSK for offline transcription to ensure resident privacy, with a Google Speech API fallback.

### 2. iOS Mobile Application (HomeScreen.tsx, LandingScreen.tsx)

I co-developed the caregiver-facing interface focused on high-speed monitoring and triage.

**Key Features:**

* **Real-Time Alert Feed:** Colour-coded risk levels (High: #FF6B6B, Medium: #FFA94D, Low: #516166).
* **Facility Dashboard:** Overview of 42 residents per facility, including active alerts and weekly summaries.
* **UX Design:** Optimised for highly mobile staff who require "quick-glance" information architecture.

---

## AI/ML Classification System

### DistilBERT Fraud Detection

* **Confidence Levels:** 0-50% (Safe), 50-75% (Potential Threat), 75-100% (Confirmed Scam).
* **Multi-Modal Analysis:** Processes call transcriptions, email content (via IMAP), and metadata.
* **Metadata Weighting:** Classification is weighted by situational signals, such as the 5 PM to 6 PM peak vulnerability window identified in research.

---

## Business Model and Market Analysis

* **Model:** B2B (Nursing homes and assisted living facilities).
* **Unit Economics:** 40 dollars hardware + 100 dollars annual subscription.
* **Margin:** Approximately 90% (220 dollars profit per customer over 2 years).
* **TAM:** 243 million dollars (U.S. nursing home market).

### Competitive Advantage

| Feature | Penny | Aura / LifeLock | Alexa |
| --- | --- | --- | --- |
| **Real-Time Voice Alerts** | Yes | No | No |
| **Physical Light Indicators** | Yes | No | Yes |
| **Real-Time Call Classification** | Yes | No | No |
| **Caregiver Alert System (B2B)** | Yes | No | No |

---

## Market Validation

**Primary Research:** Lisa W. Mullen (Activity Director, Hermitage Deep Run Senior Assisted Living).

* **Finding:** Caregivers are highly mobile and rarely use laptops; an iOS app is essential.
* **Finding:** Families prefer alerts to go to staff ("trusted adults") rather than residents to prevent senior panic.
* **Finding:** Scams peak post-dinner (5 PM to 6 PM), validating our metadata-assisted detection.

---

## Technical Challenges and Solutions

* **Resource Constraints:** Optimised Python threading and used model quantisation to run DistilBERT on Raspberry Pi 5.
* **Audio Variability:** Developed adaptive preprocessing to handle poor VOIP connections and background noise.
* **Sensitivity Balance:** Implemented a three-tier risk system and adversarial debiasing to mitigate alarm fatigue.

---

*Developed by Oma Tasie-Amadi and Team @ USC Marshall AI Association.* **Because Every Penny Matters.**
