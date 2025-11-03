# Deployment Guide - NABII Interactive Charts

## Quick Deployment Options

### Option 1: GitHub Pages (Recommended - FREE)

#### Step-by-Step Instructions:

1. **Create GitHub Account**
   - Go to https://github.com
   - Sign up if you don't have an account

2. **Create New Repository**
   - Click the "+" icon → "New repository"
   - Name it: `nabii-dashboard` (or any name you prefer)
   - Make it **Public** (for free hosting)
   - Don't initialize with README (we already have files)

3. **Upload Files**

   **Option A: Using Git (Command Line)**
   ```bash
   # Initialize git in your project folder
   cd "C:\Users\heol\Documents\Coding\Projects\NABII Interactive Charts"
   git init
   git add .
   git commit -m "Initial commit - NABII Dashboard"

   # Connect to GitHub (replace USERNAME and REPO with your details)
   git remote add origin https://github.com/USERNAME/nabii-dashboard.git
   git branch -M main
   git push -u origin main
   ```

   **Option B: Using GitHub Website (Easier)**
   - In your new repository, click "uploading an existing file"
   - Drag and drop ALL files and folders EXCEPT:
     - ~$Deal Data Zambia.xlsx (temporary Excel file)
     - .git folder (if exists)
   - Commit the files

4. **Enable GitHub Pages**
   - Go to repository Settings → Pages
   - Under "Source", select "main" branch
   - Click Save
   - Wait 1-2 minutes
   - Your site will be live at: `https://USERNAME.github.io/nabii-dashboard/`

5. **Share the Link!**
   - Share: `https://USERNAME.github.io/nabii-dashboard/`
   - Map page: `https://USERNAME.github.io/nabii-dashboard/map.html`

---

### Option 2: Netlify (FREE - Drag & Drop)

#### Step-by-Step Instructions:

1. **Create Netlify Account**
   - Go to https://www.netlify.com
   - Sign up (free account)

2. **Deploy Site**
   - Click "Add new site" → "Deploy manually"
   - Drag and drop your ENTIRE project folder
   - Netlify will deploy instantly

3. **Get Your Link**
   - You'll get a URL like: `https://random-name-12345.netlify.app`
   - You can customize this in Site Settings → Domain Management

4. **Update Site**
   - To update, just drag and drop the folder again in "Deploys" tab

**Pros:**
- Instant deployment
- Custom domain support
- Automatic HTTPS
- Built-in forms and functions

---

### Option 3: Vercel (FREE - Fast & Modern)

#### Step-by-Step Instructions:

1. **Create Vercel Account**
   - Go to https://vercel.com
   - Sign up with GitHub (easiest)

2. **Import Project**
   - Click "Add New" → "Project"
   - If connected to GitHub, select your repository
   - OR use "Import Third-Party Git Repository"

3. **Deploy**
   - Click "Deploy"
   - Site goes live at: `https://project-name.vercel.app`

4. **Updates**
   - Every GitHub push auto-deploys
   - Instant updates!

---

### Option 4: Azure Static Web Apps (FREE for Microsoft users)

#### Step-by-Step Instructions:

1. **Azure Account**
   - Go to https://azure.microsoft.com
   - Free tier available

2. **Create Static Web App**
   - Search for "Static Web Apps"
   - Click "Create"
   - Connect to GitHub or upload files

3. **Configure**
   - Set app location to "/"
   - No build command needed
   - Deploy

---

## Comparison Table

| Platform | Setup Difficulty | Custom Domain | Best For |
|----------|-----------------|---------------|----------|
| **GitHub Pages** | Easy | Free (paid for custom) | Public projects, portfolios |
| **Netlify** | Very Easy | Free | Quick deploys, no-code users |
| **Vercel** | Easy | Free | Modern apps, auto-deploy |
| **Azure** | Medium | Free | Enterprise, Microsoft ecosystem |

---

## File Checklist for Deployment

Make sure these files are included:
- ✅ `index.html` (main dashboard)
- ✅ `map.html` (map page)
- ✅ `data/` folder with all JSON files:
  - `sankey_data.json`
  - `treemap_data.json`
  - `sectoral_data.json`
  - `sdg_data.json`
  - `capital_source_data.json`
  - `instrument_timeline.json`
  - `top_deals.json`

**DO NOT upload:**
- ❌ `~$Deal Data Zambia.xlsx` (temporary file)
- ❌ `__pycache__/` (Python cache)
- ❌ `.git/` (Git internals - unless using Git)

---

## Troubleshooting

### Charts not loading?
- Check browser console (F12)
- Ensure all JSON files are in the `data/` folder
- Verify file paths are relative (not absolute)

### 404 Error?
- Check that `index.html` is in the root directory
- Verify GitHub Pages is enabled on the correct branch

### Styling looks different?
- Clear browser cache (Ctrl + Shift + Delete)
- Check that fonts are loading from Google Fonts CDN

---

## Security Notes

✅ **Safe to share publicly:**
- HTML files
- JSON data files
- CSS/JavaScript

⚠️ **Consider privacy:**
- If data is sensitive, use private repositories (GitHub paid) or password-protected hosting
- Remove any confidential company information before deploying

---

## Next Steps After Deployment

1. **Share the link** with stakeholders
2. **Set up analytics** (Google Analytics, Plausible)
3. **Custom domain** (optional - buy from Namecheap, Google Domains)
4. **SSL Certificate** (automatic on all platforms)
5. **Monitor usage** through platform dashboards

---

## Questions?

- GitHub Pages Docs: https://pages.github.com/
- Netlify Docs: https://docs.netlify.com/
- Vercel Docs: https://vercel.com/docs

Good luck with your deployment! 🚀
