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
