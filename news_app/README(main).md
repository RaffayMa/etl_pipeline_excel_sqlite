# 📰 News Project – Full Stack  - Main branch

## 📌 GitHub Workflow  

This project is organized into **two long-lived branches** to keep development clean and professional:  

- [🖥️ Frontend Branch](https://github.com/RaffayMa/News/tree/front-end/news-app)  
- [⚙️ Backend Branch](https://github.com/RaffayMa/News/tree/back-end/news_app)  

---

### 🔹 Repository Structure  
1. **`main`** – polished, production-ready code (final integrated project).  
2. **`news_front-end`** – active development of the frontend (UI & client-side logic).  
3. **`news_back-end`** – active development of the backend (API, automation, ETL).  

---

### 🔹 Development & Merge Process  

All code is pushed to the **frontend** or **backend** branch during development.  
Once the code is stable and ready to “ship”:  

1. Open a **Pull Request** on GitHub:  
   - `news_front-end` → `main` (frontend changes)  
   - `news_back-end` → `main` (backend changes)  

2. **Review & Test** the changes.  

3. **Merge into `main`** → keeping `main` clean as the combined **final product**.  

4. **Update Local Main**:  
   ```bash
   git checkout main
   git pull origin main

## 📽️ Project Goal

Build a news website, that fetches articles, headlines in a nutshell news from newsAPI.org

### Tech Stack 

**⚙️ Back-end**
Python, for API integration, organizes data and exposes it via REST API
**🔹 Steps**
1. Set up Flask API
2. Add error handling
3. Structure code for clarity
4. Test endpints
5. return JSON


**🖥️ Front-end**
Vanilla HTML,CSS & JS OR UI library like React, will fetch data from the backend and display in UI.
HTML, CSS & JS learning resource by Professor Jamie Mitchell at Trent university :
https://jamiemitchell.dev/cois2430/content/

1. Create app and build pages accordingly
2. fetch JSON from back-end
3. Style with Bootstrap or other resources

