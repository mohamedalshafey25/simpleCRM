Simple CRM Frontend — User Guide

Welcome! This guide helps a first-time user run and use the frontend for the Simple CRM demo.

Prerequisites
- Node.js (LTS) and npm installed on your machine.
- Backend API running at http://127.0.0.1:8000 (FastAPI server started from the repository root: `uvicorn app.main:app --reload`).

Start the frontend
1. Open a terminal and change to the frontend folder:

   ```powershell
   cd "c:\Users\A store\simple-crm\frontend"
   ```

2. Install dependencies (only once or after package.json changes):

   ```powershell
   npm install
   ```

   If `npm audit` reports vulnerabilities, run `npm audit fix`. If `npm install` fails because of registry/version mismatch, delete `package-lock.json` and run `npm install` again.

3. Start the dev server:

   ```powershell
   npm run dev
   ```

4. Open your browser at http://localhost:3000/ (Vite will show the local URL in the terminal output).

Using the app
- Customers list: The left panel shows the customers list. Click the "Load Customers" button to fetch the latest customers from the backend.
- Create customer: Fill name and email on the right panel and click "Create". While the request is in progress the Create button is disabled and reads "Creating...".
- Success / error messages: Notifications appear at the top-right. Success messages disappear quickly; error messages remain longer so you can read them.
- Optimistic UI: When you create a customer, the UI shows the new customer immediately (optimistic update). If the server rejects the creation, the optimistic entry is removed and an error notification is shown.

Troubleshooting
- If customers do not load, check the browser DevTools console for network errors. Ensure the backend is running at http://127.0.0.1:8000 and CORS is allowed for http://localhost:3000.
- If `npm install` fails because of unavailable package versions (ETARGET), try changing problematic dependency versions in `frontend/package.json` or regenerate the lockfile:

  ```powershell
  Remove-Item package-lock.json
  npm cache clean --force
  npm install
  ```

- If you see deprecation warnings from Vite about the CJS API, they are informational and do not block normal development.

Next steps
- Add form-level validation rules or server-side error display if your backend returns field-level errors.
- Commit the generated `package-lock.json` after you finish local installs to lock dependency versions for collaborators.

If you want, I can help automate any of the troubleshooting steps or adjust the UI behaviour further.
