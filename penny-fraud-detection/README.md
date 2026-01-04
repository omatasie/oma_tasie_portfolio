# Project Penny: AI-Driven Security for Seniors

**Winner: Best Project @ USC MAIA Demo Day**

Recognised by a judging panel of engineers from Netflix and Google for its technical rigour, market viability, and impact on senior digital safety.

---

## Project Overview

Project Penny is an integrated hardware and software ecosystem designed to safeguard seniors from the 28.3 billion dollars lost annually to financial fraud. While traditional services are reactive, Penny is proactive—utilising a hybrid edge-to-cloud architecture to detect, signal, and alert caregivers of fraud in real-time.

By combining local audio capture with cloud-based machine learning, the system identifies predatory patterns during live communications, providing an essential safety net for both residents and facility staff.

---

## User Research and Validation

The project development was grounded in professional feedback from Lisa Muller, Activity Director at Hermitage Deep Run Senior Assisted Living. Key insights included:

* **Peak Vulnerability Windows:** Residents are most susceptible to scams between **5 PM and 6 PM** (post-dinner), requiring high-vigilance monitoring during these hours.
* **The Caregiver Gap:** Staff require a mobile-first solution, as their roles are highly interpersonal and they rarely access laptops during active shifts.
* **Dignity-First Intervention:** Families prefer that a "trusted adult" receive the risk alert rather than the senior, ensuring that interventions are handled calmly and with care.

---

## Technical Contributions

### 1. Audio Processing and Hardware Interface (voip_audio_capture.py)

As the Audio Preprocessing Engineer, I developed the real-time "ears" of the system and the physical feedback loop.

* **Signal Filtering:** Engineered a 4th-order Butterworth bandpass filter (300Hz–3400Hz) to isolate human speech and eliminate environmental noise.
* **Concurrency:** Implemented a multi-threaded Python pipeline using thread-safe queues to manage simultaneous audio capture, signal cleaning, and transcription.
* **Edge Speech-to-Text:** Integrated the VOSK model for local, privacy-preserving transcription, ensuring sensitive resident conversations remain on the device whenever possible.
* **Visual Status Signalling:** Mapped ML confidence scores to a physical GPIO-controlled LED stoplight system to provide seniors with instant, non-verbal safety cues.

### 2. Cloud Architecture and Scaling (Supabase)

To solve the scalability issues of high-cost hardware, I helped architect the transition from edge-heavy to cloud-efficient computation.

* **Cloud Offloading:** Integrated Supabase to handle the heavy lifting of ML inference and data storage. By moving computations to the cloud, we reduced the hardware requirement from an expensive Raspberry Pi to a cost-effective Bluetooth speaker.
* **System Logic:** Engineered the logic that pushes cloud-calculated risk scores back to the mobile interface, ensuring real-time synchronisation between the audio stream and the caregiver dashboard.

### 3. Mobile Experience (React Native and Expo Go)

I designed and developed the two primary screens of the caregiver application, focused on facility-wide monitoring.

* **Landing Screen:** Established a trustworthy visual brand and onboarding flow for nursing home staff.
* **Home Dashboard:** Built a dynamic risk-monitoring interface that visualises resident safety status. I implemented custom logic to categorise communications into Safe, Potential Threat, and Scam Detected based on model confidence scores.

---

## System Architecture: Edge-to-Cloud

The architecture prioritises low latency and data privacy through the following pipeline:

1. **Capture:** Raw audio is captured at the edge via Raspberry Pi 5 and segmented into one-minute processing chunks.
2. **Transcription:** Local STT via VOSK converts audio to text to minimise data transmission.
3. **Inference:** Text is processed by a DistilBERT classification model to generate a fraud confidence score.
4. **Action:** If a threat is detected, an asynchronous alert is pushed via Supabase to the React Native caregiver application, while local LEDs provide immediate visual feedback to the senior.

---

## Business and Market Strategy

| Metric | Detail |
| --- | --- |
| **Business Model** | B2B (Direct sales to nursing homes and care facilities) |
| **Revenue Model** | Hardware Installation (One-time) + Software Subscription (Monthly) |
| **Projected Margin** | Approximately 80% (190 USD profit per unit over 2 years) |
| **Total Addressable Market** | 243 million USD (US national distribution) |

---

## Future Directions

* **Multilingual Support:** Transitioning to DistilBERT Multilingual to support over 104 languages.
* **Family Portal:** Implementing an opt-in portal for families to receive weekly safety reports and secure messaging with staff.
* **Metadata Integration:** Incorporating call-time and location metadata to refine risk scoring during peak vulnerability hours identified in research.

---

*Created by Oma Tasie and Team at the USC Marshall AI Association.* **Because Every Penny Matters.**
