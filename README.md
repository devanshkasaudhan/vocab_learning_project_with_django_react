# 📚 Vocabulary Learning App

A full-stack vocabulary learning application built with Django REST Framework and React. Help users improve their English vocabulary through daily word exposure and structured learning.

![Python](https://img.shields.io/badge/python-v3.11+-blue.svg)
![Django](https://img.shields.io/badge/django-v4.x-green.svg)
![React](https://img.shields.io/badge/react-v19.1.0-blue.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

## 🎯 Features

- **📖 Word of the Day**: Get a random vocabulary word with definition and example
- **📊 Difficulty Levels**: Words categorized as Beginner, Intermediate, or Advanced
- **🔧 Admin Interface**: Easy word management through Django admin
- **📱 Responsive Design**: Clean, modern UI built with React
- **🚀 REST API**: Scalable backend with Django REST Framework
- **⚡ Auto-Population**: Management commands for bulk word import

## 🛠️ Technology Stack

### Backend
- **Django 4.x** - Web framework
- **Django REST Framework** - API development
- **SQLite** - Database (development)
- **django-cors-headers** - CORS handling

### Frontend
- **React 19.1.0** - UI framework
- **Axios** - HTTP client
- **Create React App** - Build tooling

## 📁 Project Structure

```
vocab/
├── 🗄️ Backend (Django)
│   ├── vocab_backend/          # Project settings
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   └── vocab/                  # Main app
│       ├── models.py           # Word data model
│       ├── serializers.py      # API serialization
│       ├── views.py            # API endpoints
│       ├── urls.py             # URL routing
│       ├── admin.py            # Admin configuration
│       └── management/         # Custom commands
│           └── commands/
│               ├── populate_words.py
│               └── fetch_words.py
├── ⚛️ Frontend (React)
│   └── vocab_frontend/
│       ├── src/
│       │   ├── App.js
│       │   └── components/
│       │       └── WordOfTheDay.js
│       └── package.json
├── 📊 Data
│   ├── db.sqlite3
│   └── sample_words.json
└── 📄 Documentation
    └── README.md
```

## 🚀 Quick Start

### Prerequisites

- Python 3.11+
- Node.js 18+
- Git
- Code editor (VS Code recommended)

### 🔧 Local Development Setup

#### 1. Clone and Setup Repository
```bash
git clone https://github.com/devanshkasaudhan/vocab_learning_project_with_django_react.git
cd vocab_learning_project_with_django_react
```

#### 2. Backend Setup (Django)

**Create and activate virtual environment:**
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python -m venv venv
source venv/bin/activate
```

**Install Python dependencies:**
```bash
pip install -r requirements.txt
```

**Setup Django application:**
```bash
# Create migrations
python manage.py makemigrations vocab
python manage.py migrate

# Create superuser for admin access
python manage.py createsuperuser

# Populate with sample vocabulary words
python manage.py populate_words

# Start Django development server
python manage.py runserver
```

#### 3. Frontend Setup (React)

**In a new terminal, navigate to frontend:**
```bash
cd vocab_frontend
```

**Install Node.js dependencies:**
```bash
npm install
```

**Start React development server:**
```bash
npm start
```

### 🌐 Access Your Application

After setup, your application will be available at:
- **📱 Frontend (React)**: http://localhost:3000
- **🔧 Backend API**: http://localhost:8000/api/
- **⚙️ Django Admin**: http://localhost:8000/admin/

### ⚡ Quick Commands

```bash
# Backend commands
python manage.py runserver              # Start Django server
python manage.py populate_words         # Add sample words
python manage.py populate_words --clear # Clear and reload words
python manage.py test                   # Run Django tests

# Frontend commands
npm start                               # Start React dev server
npm test                               # Run React tests
npm run build                          # Build for production
```

## 🚀 GitHub Pages Deployment

This project includes automated CI/CD for GitHub Pages deployment.

### Automatic Deployment Setup

1. **Fork or create repository on GitHub**

2. **Update configuration files:**
   
   In `vocab_frontend/package.json`, update the homepage:
   ```json
   "homepage": "https://devanshkasaudhan.github.io/vocab_learning_project_with_django_react"
   ```

3. **Push to GitHub:**
   ```bash
   git add .
   git commit -m "Initial commit"
   git push origin main
   ```

4. **Enable GitHub Pages:**
   - Go to repository **Settings** → **Pages**
   - Under **Source**, select **GitHub Actions**
   - The deployment will trigger automatically

5. **Your app will be live at:**
   ```
   https://devanshkasaudhan.github.io/vocab_learning_project_with_django_react
   ```

### 🔄 CI/CD Features

The automated workflow will:
- ✅ Run Django and React tests
- 🏗️ Build optimized production version
- 🚀 Deploy to GitHub Pages automatically
- 📊 Create mock API data for demo

### Manual Deployment (Alternative)

If you prefer manual deployment:
```bash
cd vocab_frontend
npm run build
# Deploy the 'build' folder to your hosting service
```

## 📖 API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/words/` | GET | Get all vocabulary words |
| `/api/word-of-the-day/` | GET | Get a random word of the day |

### Example Response

```json
{
  "id": 1,
  "word": "Serendipity",
  "definition": "The occurrence and development of events by chance in a happy or beneficial way",
  "example": "A fortunate stroke of serendipity led her to discover the hidden talent.",
  "level": "Advanced",
  "created_at": "2025-07-21T10:30:00Z"
}
```

## 💾 Data Management

### 🎯 Adding Vocabulary Words

#### Option 1: Django Admin Interface (Recommended for Manual Entry)

1. **Access admin panel:**
   ```bash
   # Make sure Django server is running
   python manage.py runserver
   ```

2. **Navigate to:** http://localhost:8000/admin/

3. **Login** with your superuser credentials

4. **Add words:**
   - Click on **Words** under the **VOCAB** section
   - Click **Add Word** button
   - Fill in: Word, Definition, Example, and Level
   - Save and continue adding

#### Option 2: Management Commands (Recommended for Bulk Import)

**Load pre-built sample words:**
```bash
python manage.py populate_words
```

**Load from custom JSON file:**
```bash
python manage.py populate_words --file path/to/your/words.json
```

**Clear existing and reload:**
```bash
python manage.py populate_words --clear
```

**Simulate API word fetching:**
```bash
python manage.py fetch_words --count 10 --level Advanced
```

#### Option 3: JSON File Import

Create a JSON file with this structure:
```json
[
  {
    "word": "Serendipity",
    "definition": "The occurrence and development of events by chance in a happy or beneficial way",
    "example": "A fortunate stroke of serendipity led her to discover the hidden talent.",
    "level": "Advanced"
  },
  {
    "word": "Eloquent",
    "definition": "Fluent or persuasive in speaking or writing",
    "example": "The speaker delivered an eloquent speech that moved the audience to tears.",
    "level": "Intermediate"
  }
]
```

Then import it:
```bash
python manage.py populate_words --file your_words.json
```

### 📊 Available Management Commands

| Command | Purpose | Example |
|---------|---------|---------|
| `populate_words` | Load sample vocabulary words | `python manage.py populate_words` |
| `populate_words --clear` | Clear all words and reload | `python manage.py populate_words --clear` |
| `populate_words --file <path>` | Load from JSON file | `python manage.py populate_words --file words.json` |
| `fetch_words` | Simulate API word fetching | `python manage.py fetch_words --count 5 --level Beginner` |

## 🎨 Screenshots

### Word of the Day
![Word of the Day Interface](screenshots/word-of-day.png)

### Admin Interface
![Django Admin Panel](screenshots/admin-panel.png)

## 🔧 Configuration & Environment

### Development Environment

Create a `.env` file in the root directory for environment variables:

```env
# Django Settings
SECRET_KEY=your-secret-key-here-replace-in-production
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# Database (SQLite for development)
DATABASE_URL=sqlite:///db.sqlite3

# CORS Settings (for React frontend)
CORS_ALLOW_ALL_ORIGINS=True
```

### Production Environment

For production deployment, update these settings:

```env
SECRET_KEY=your-secure-production-secret-key
DEBUG=False
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
DATABASE_URL=postgresql://user:password@host:port/database
CORS_ALLOW_ALL_ORIGINS=False
CORS_ALLOWED_ORIGINS=https://yourdomain.com,https://www.yourdomain.com
```

### Frontend Configuration

The React app automatically detects the environment:

- **Development**: Uses Django API at `http://localhost:8000`
- **Production**: Uses static JSON files for GitHub Pages demo
- **Custom Backend**: Update API URLs in `WordOfTheDay.js`

### Database Configuration

**SQLite (Default - Development):**
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

**PostgreSQL (Production):**
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'vocab_db',
        'USER': 'your_username',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

## 🚀 Production Deployment Options

### 📱 Frontend-Only (GitHub Pages)
- ✅ **Free hosting**
- ✅ **Automatic CI/CD**
- ✅ **Perfect for demos**
- ❌ **Static data only**

### 🌐 Full-Stack Deployment

#### Backend Hosting Options:

**1. Railway.app (Recommended)**
```bash
# Install Railway CLI
npm install -g @railway/cli

# Login and deploy
railway login
railway init
railway up
```

**2. Heroku**
```bash
# Install Heroku CLI and login
heroku create your-vocab-app
git push heroku main
```

**3. DigitalOcean App Platform**
- Connect GitHub repository
- Auto-deploy on push
- Built-in database options

**4. PythonAnywhere**
- Great for Django applications
- Free tier available
- Easy Django setup

#### Frontend Hosting Options:

**1. Netlify**
```bash
cd vocab_frontend
npm run build
# Drag and drop 'build' folder to Netlify
```

**2. Vercel**
```bash
npm install -g vercel
cd vocab_frontend
vercel --prod
```

**3. GitHub Pages (Current Setup)**
- Automatic deployment via GitHub Actions
- Free for public repositories

### 🔄 Full Deployment Workflow

1. **Deploy Backend** to Railway/Heroku
2. **Update API URLs** in React app
3. **Deploy Frontend** to Netlify/Vercel
4. **Configure CORS** in Django settings

### 📦 Production Dependencies

**Backend (requirements.txt):**
```txt
Django>=4.2.0,<5.0.0
djangorestframework>=3.14.0
django-cors-headers>=4.0.0
gunicorn>=21.0.0
whitenoise>=6.5.0
psycopg2-binary>=2.9.0  # For PostgreSQL
```

**Frontend (package.json):**
```json
{
  "scripts": {
    "build": "react-scripts build",
    "deploy": "npm run build && gh-pages -d build"
  }
}
```

## 🛠️ Development Guide

### � Testing

**Run Django tests:**
```bash
python manage.py test
python manage.py test vocab  # Test specific app
python manage.py test vocab.tests.WordModelTest  # Test specific class
```

**Run React tests:**
```bash
cd vocab_frontend
npm test                     # Interactive mode
npm test -- --coverage      # With coverage report
npm test -- --watchAll=false # Single run
```

### 🐛 Debugging

**Django Debug Mode:**
```bash
# In settings.py
DEBUG = True

# View detailed error pages
python manage.py runserver --verbosity=2
```

**React Debug Mode:**
```bash
# Start with debug info
REACT_APP_DEBUG=true npm start

# View in browser console
console.log('API Response:', response.data);
```

### 📝 Code Quality

**Django Code Quality:**
```bash
# Check for issues
python manage.py check

# Validate migrations
python manage.py makemigrations --check --dry-run

# Code formatting (optional)
pip install black flake8
black .
flake8 .
```

**React Code Quality:**
```bash
# ESLint is included with Create React App
npm run lint  # If configured

# Prettier formatting (optional)
npm install --save-dev prettier
npx prettier --write src/
```

### 🔄 Development Workflow

1. **Feature Development:**
   ```bash
   git checkout -b feature/new-feature
   # Make changes
   python manage.py test  # Test backend
   cd vocab_frontend && npm test  # Test frontend
   git commit -m "Add new feature"
   git push origin feature/new-feature
   ```

2. **Code Review & Merge:**
   - Create Pull Request
   - CI/CD runs automatically
   - Review and merge to main
   - Auto-deployment triggers

### 📚 Adding New Features

**Adding a new Django model:**
```bash
# 1. Update models.py
# 2. Create migrations
python manage.py makemigrations
python manage.py migrate

# 3. Update admin.py, serializers.py, views.py
# 4. Add tests
python manage.py test
```

**Adding a new React component:**
```bash
# 1. Create component file
# 2. Add tests
# 3. Import and use in App.js
npm test
```

## 🚨 Troubleshooting

### Common Issues & Solutions

**🔧 Backend Issues:**

```bash
# ModuleNotFoundError: No module named 'rest_framework'
pip install djangorestframework django-cors-headers

# Migration issues
python manage.py makemigrations vocab
python manage.py migrate

# Port already in use (Windows)
netstat -ano | findstr :8000
# Kill the process or use different port
python manage.py runserver 8001

# Database locked error
rm db.sqlite3  # or del db.sqlite3 on Windows
python manage.py migrate
python manage.py populate_words

# CORS errors
# Ensure django-cors-headers is installed and configured
# Check CORS_ALLOW_ALL_ORIGINS in settings.py
```

**⚛️ Frontend Issues:**

```bash
# npm install fails
rm -rf node_modules package-lock.json  # or rmdir /s node_modules on Windows
npm cache clean --force
npm install

# API connection issues
# 1. Check if Django server is running: http://localhost:8000/api/
# 2. Verify API URLs in WordOfTheDay.js
# 3. Check browser console for CORS errors

# Build fails
npm run build -- --verbose  # Get detailed error information
# Common fix: Set CI=false in environment
CI=false npm run build  # or set CI=false in package.json

# React app not loading
# Check port conflicts (default: 3000)
# Clear browser cache and cookies
# Check console for JavaScript errors
```

**🌐 Deployment Issues:**

```bash
# GitHub Pages not updating
# 1. Check GitHub Actions tab for build errors
# 2. Verify homepage URL in package.json matches your repo
# 3. Ensure GitHub Pages source is set to "GitHub Actions"
# 4. Check if workflow files are in .github/workflows/

# CI/CD pipeline failing
# 1. Check .github/workflows/deploy.yml syntax
# 2. Verify all required files are committed and pushed
# 3. Check GitHub repository permissions for Actions
# 4. Review failed step logs in GitHub Actions tab

# Environment variables not working
# 1. Check if .env file is in .gitignore (it should be)
# 2. Set environment variables in GitHub repository secrets
# 3. Update workflow files to use secrets
```

### 🔍 Debug Commands

**Check Django setup:**
```bash
python manage.py check --verbose
python manage.py showmigrations
python manage.py shell
>>> from vocab.models import Word
>>> Word.objects.count()
```

**Check React setup:**
```bash
cd vocab_frontend
npm run build  # Test if build works
npm list        # Check installed packages
npm outdated    # Check for outdated packages
```

**Check API endpoints:**
```bash
# Test Django API directly
curl http://localhost:8000/api/words/
curl http://localhost:8000/api/word-of-the-day/

# Or use Python requests
python -c "import requests; print(requests.get('http://localhost:8000/api/words/').json())"
```

### 📞 Getting Help

- **🐛 Bug Reports**: [Create an issue](https://github.com/devanshkasaudhan/vocab_learning_project_with_django_react/issues)
- **💡 Feature Requests**: [Start a discussion](https://github.com/devanshkasaudhan/vocab_learning_project_with_django_react/discussions)  
- **❓ Questions**: Check existing issues or create a new one
- **📧 Direct Contact**: Create an issue for complex problems

## ❓ Frequently Asked Questions

### **Q: Can I use this project for commercial purposes?**
A: Yes! This project is under MIT license, which allows commercial use.

### **Q: How do I add my own vocabulary words?**
A: You have several options:
- Use Django admin interface (http://localhost:8000/admin)
- Create a JSON file and use `python manage.py populate_words --file yourfile.json`
- Add them programmatically via Django shell

### **Q: Can I deploy the backend somewhere other than the suggested platforms?**
A: Absolutely! The Django backend can run on any platform that supports Python. Just update the API URLs in the React frontend.

### **Q: Why doesn't the GitHub Pages version have a real backend?**
A: GitHub Pages only serves static files, so we use mock JSON data for the demo. For full functionality, deploy the Django backend to a separate service.

### **Q: How do I customize the UI design?**
A: The React components use inline styles for simplicity. You can:
- Modify the styles in `WordOfTheDay.js` and `App.js`
- Add CSS framework like Bootstrap or Material-UI
- Create separate CSS files

### **Q: Can I add user accounts and authentication?**
A: Yes! You can extend the project with Django's built-in authentication or use packages like `django-allauth` or `djangorestframework-simplejwt`.

### **Q: How do I integrate with real dictionary APIs?**
A: Update the management commands in `vocab/management/commands/` to call real APIs like:
- Merriam-Webster Dictionary API
- Oxford Dictionary API
- WordsAPI
- Cambridge Dictionary API

### **Q: Is this suitable for production use?**
A: The codebase provides a solid foundation, but for production you should:
- Add proper error handling and logging
- Implement security best practices
- Use a production database (PostgreSQL)
- Add user authentication
- Implement proper testing coverage
- Add monitoring and analytics

## 🎯 Future Enhancements

- [ ] User authentication and profiles
- [ ] Word quizzes and flashcards
- [ ] Progress tracking and analytics
- [ ] Mobile app development
- [ ] Audio pronunciation
- [ ] Spaced repetition algorithm
- [ ] Social features and word sharing
- [ ] Integration with external dictionary APIs
- [ ] Advanced search and filtering
- [ ] Dark/light theme toggle

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Devansh Kasaudhan**
- GitHub: [@devanshkasaudhan](https://github.com/devanshkasaudhan)
- LinkedIn: [Devansh Kasaudhan](https://www.linkedin.com/in/devansh-kasaudhan-a071a4204/)
- Email: devanshkasaudhan1234@gmail.com

## 🙏 Acknowledgments

- [Django Documentation](https://docs.djangoproject.com/)
- [React Documentation](https://reactjs.org/docs/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- Sample vocabulary words from various educational sources

## 📊 Project Stats

![GitHub repo size](https://img.shields.io/github/repo-size/devanshkasaudhan/vocab_learning_project_with_django_react)
![GitHub contributors](https://img.shields.io/github/contributors/devanshkasaudhan/vocab_learning_project_with_django_react)
![GitHub last commit](https://img.shields.io/github/last-commit/devanshkasaudhan/vocab_learning_project_with_django_react)
![GitHub issues](https://img.shields.io/github/issues/devanshkasaudhan/vocab_learning_project_with_django_react)

---

⭐ **Star this repository if you found it helpful!**
