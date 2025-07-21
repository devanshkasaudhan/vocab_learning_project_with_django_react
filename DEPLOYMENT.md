# 🚀 Deployment Instructions

## GitHub Pages Deployment

This project is configured with GitHub Actions for automatic deployment to GitHub Pages.

### Setup Steps:

1. **Push to GitHub:**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin https://github.com/YOUR_USERNAME/vocab.git
   git push -u origin main
   ```

2. **Enable GitHub Pages:**
   - Go to your repository on GitHub
   - Navigate to `Settings` → `Pages`
   - Under "Source", select `GitHub Actions`
   - The workflow will automatically trigger

3. **Update Configuration:**
   - In `vocab_frontend/package.json`, update the `homepage` field:
     ```json
     "homepage": "https://YOUR_USERNAME.github.io/vocab"
     ```
   - In `vocab_frontend/src/App.js`, update the GitHub link

### What the CI/CD Does:

1. **Testing:**
   - Runs Django backend tests
   - Runs React frontend tests
   - Validates migrations and code quality

2. **Building:**
   - Builds the React application for production
   - Creates static JSON files to simulate API responses
   - Optimizes assets for deployment

3. **Deployment:**
   - Deploys to GitHub Pages automatically
   - Available at: `https://YOUR_USERNAME.github.io/vocab`

### Manual Deployment (Alternative):

If you prefer manual deployment:

```bash
cd vocab_frontend
npm run build
npm install -g serve
serve -s build -l 3000
```

### Environment Variables:

For production deployment, you may want to set:

```bash
# In GitHub Secrets
DJANGO_SECRET_KEY=your-secret-key
DATABASE_URL=your-database-url
```

### Backend Deployment:

The frontend will work on GitHub Pages, but for a full-stack deployment, consider:

- **Railway.app** (recommended for Django)
- **Heroku**
- **DigitalOcean App Platform**
- **AWS/GCP/Azure**

Update the API URLs in the React app to point to your deployed backend.

### Troubleshooting:

1. **Build Fails:**
   - Check GitHub Actions logs
   - Ensure all dependencies are listed in package.json
   - Verify no syntax errors in code

2. **Page Not Loading:**
   - Verify GitHub Pages is enabled
   - Check that homepage URL in package.json is correct
   - Ensure PUBLIC_URL environment variable is set correctly

3. **API Not Working:**
   - GitHub Pages only serves static files
   - The demo uses static JSON files for GitHub Pages
   - Deploy backend separately for full functionality

### Development vs Production:

- **Development:** Uses Django backend at localhost:8000
- **Production (GitHub Pages):** Uses static JSON files
- **Production (Full Stack):** Deploy backend separately and update API URLs
