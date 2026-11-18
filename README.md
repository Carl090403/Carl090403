# Hi, I'm Carlos

I'm a software developer in the Ottawa–Gatineau region, Canada. I build web apps and APIs.

I graduated from the University of Ottawa in Computer Engineering (Cum Laude) and I work in **English and French**.

**I'm looking for:**
- ** On-site, hybrid or Remote full-time roles**, junior to intermediate (backend, full-stack or data)
- **Freelance projects**: booking systems, internal tools, REST APIs, AI features, or moving messy data into a clean database

---

## What I work with

- **Backend:** Python (FastAPI, Pydantic), Java 17, Node.js, REST APIs, auth (Argon2id, JWT in HttpOnly cookies)
- **Frontend:** TypeScript, React, Next.js, Vite, Tailwind, TanStack Query, Zustand
- **Data:** PostgreSQL, SQLite, SQLAlchemy + Alembic, MongoDB, Firebase/Firestore, pandas, SQL ETL
- **Systems:** C11 + POSIX threads, C++, Raspberry Pi / GPIO, VHDL
- **How I ship:** tests first (pytest, JUnit, Vitest, Playwright), GitHub Actions CI, Docker Compose, Vercel / Render

---

## Projects I'd show you first

### [ChaseCart](https://github.com/Carl090403/Capstone01): autonomous shopping-cart robot (team capstone)
A robot that takes your shopping list and drives itself through a store to fetch each item, using LiDAR, wheel encoders and a live map. I worked on the React web app, the REST API and the migration from MongoDB to Firestore, and I helped debug and performance-test the robot. It took 200+ commits across a full year of teamwork.
React · Firestore · Raspberry Pi · ROS · ESP32 · [Live app](https://chasecart.onrender.com)

### [Rendez-vous](https://github.com/Carl090403/Rendez-vous): online booking for small businesses
Clients book a salon, tutor or clinic in under two minutes, without a phone call. Owners manage their services, hours and time off from a dashboard. Double bookings are blocked **by the database itself**: a PostgreSQL exclusion constraint returns 409 Conflict, so two people clicking at the same second can't both get the slot.
FastAPI · PostgreSQL · Next.js · TypeScript · Docker · Playwright end-to-end tests in CI
<!-- TODO: add the live demo link here -->

### [CreatorBooster](https://github.com/Carl090403/Creator-Booster): an AI SaaS I built and run
A live product for content creators: AI tools powered by Google Gemini, Firebase accounts, a credit system validated on the server (so users can't edit their own balance), and payment webhooks.
React · TypeScript · Gemini API · Firebase · Vercel serverless · [Try it](https://creator-booster.vercel.app)

### [Transfer Ledger Service](https://github.com/Carl090403/transfer-ledger-service) + [Java port](https://github.com/Carl090403/transfer-ledger-service-java)
A funds-transfer API that handles money correctly: integer cents, atomic transactions, idempotency keys (send the same request twice and you're charged once), and structured logs with request IDs. I then ported it to Java. Both versions pass the same shared contract file, and the project has 43 pytest tests and 28 JUnit tests.
Python · Java 17 · SQLite · CI

---

## Recently shipped

This list updates itself every day from my newest public repositories.

<!-- RECENT-PROJECTS:START -->
- **[Portfolio01](https://github.com/Carl090403/Portfolio01)**: Carlos Fadjebe Portfolio · `HTML` · [live](https://portfolio01-five-zeta.vercel.app) · Nov 2026
- **[transfer-ledger-service-java](https://github.com/Carl090403/transfer-ledger-service-java)**: Java 17 port of my transfer ledger API: same HTTP contract, same rules, 28 JUnit tests. · `Java` · Nov 2026
- **[rlc-seg-pipeline](https://github.com/Carl090403/rlc-seg-pipeline)**: Multi-threaded C11 pipeline: packet segmentation, reassembly and CRC-32 over a bounded MPMC queue. · `C` · Nov 2026
- **[transfer-ledger-service](https://github.com/Carl090403/transfer-ledger-service)**: Funds-transfer API in Python: integer cents, atomic SQLite transactions, idempotency keys, 43 tests. · `Python` · Nov 2026
- **[cx-survey](https://github.com/Carl090403/cx-survey)**: PHP 8.3 survey API: NPS and rating questions, queued AI sentiment analysis, aggregated reports. · `PHP` · Nov 2026
<!-- RECENT-PROJECTS:END -->

---

## What I'm working on now

- Deploying **Rendez-vous** and adding a live demo and screenshots
- Adding features to **CreatorBooster** based on what users actually ask for
- Getting deeper into Java backend work after finishing the ledger port

---

## Work with me

**Hiring for a remote role?** I'm on an open work permit in Canada, so I don't need sponsorship. My résumé is available on request.

**Need something built?** Send me two or three lines about the problem: what's slow, broken or missing. I'll reply with questions and a rough plan. <!-- TODO: say how fast you reply, e.g. "within 48 hours" -->

🌐 **https://portfolio01-carl090403s-projects.vercel.app/** 📧 **fadjebecarlos@gmail.com** · 💼 [LinkedIn](https://www.linkedin.com/in/carlos-fadjebe-7803852b3)

*Je travaille aussi en français, n'hésitez pas à m'écrire en français.*
