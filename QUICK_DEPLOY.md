# 🚀 Quick Deploy - 3 Easiest Options

## ⚡ FASTEST: Netlify Drop (2 minutes, no code)

### Steps:
1. Go to **https://app.netlify.com/drop**
2. Drag your entire folder into the browser
3. Done! You get a live URL instantly

**Your URL will look like:** `https://nabii-dashboard-xyz123.netlify.app`

---

## 🌟 BEST: GitHub Pages (5 minutes, professional)

### Prerequisites:
- GitHub account (create at https://github.com/signup)

### Steps:

**1. Create a new repository on GitHub:**
   - Go to https://github.com/new
   - Repository name: `nabii-dashboard`
   - Make it **Public**
   - Click "Create repository"

**2. Open Command Prompt and run these commands:**

```bash
# Navigate to your project folder
cd "C:\Users\heol\Documents\Coding\Projects\NABII Interactive Charts"

# Initialize Git
git init

# Add all files
git add .

# Commit files
git commit -m "Initial deployment of NABII Dashboard"

# Connect to GitHub (REPLACE 'YOUR-USERNAME' with your actual GitHub username)
git remote add origin https://github.com/YOUR-USERNAME/nabii-dashboard.git

# Set branch name
git branch -M main

# Push to GitHub
git push -u origin main
```

**3. Enable GitHub Pages:**
   - Go to your repository on GitHub
   - Click **Settings** (top menu)
   - Click **Pages** (left sidebar)
   - Under "Source", select **main** branch
   - Click **Save**
   - Wait 1-2 minutes

**4. Your site is live!**
   - URL: `https://YOUR-USERNAME.github.io/nabii-dashboard/`

---

## 🎯 ALTERNATIVE: Vercel (3 minutes, auto-updates)

### Steps:

**1. Create Vercel account:**
   - Go to https://vercel.com/signup
   - Sign up with GitHub (recommended)

**2. Deploy:**
   - Click "Add New..." → "Project"
   - Import your GitHub repository (if you created one)
   - OR click "Import Third-Party Git Repository"
   - Click "Deploy"

**3. Done!**
   - URL: `https://nabii-dashboard.vercel.app`
   - Every GitHub push auto-deploys!

---

## 📋 Files to Upload

**Include these:**
- ✅ `index.html`
- ✅ `map.html`
- ✅ `data/` folder (all JSON files inside)

**Exclude these:**
- ❌ `~$Deal Data Zambia.xlsx`
- ❌ `__pycache__/`
- ❌ `.git/` (if manually uploading)
- ❌ Python files (unless you want to share code)

---

## 🆘 Need Help?

### If Git push fails:
1. Make sure you're logged into GitHub
2. You may need to authenticate:
   ```bash
   git config --global user.name "Your Name"
   git config --global user.email "your.email@example.com"
   ```
3. GitHub may ask for credentials - use a Personal Access Token (not password)
   - Create token at: https://github.com/settings/tokens

### If you see 404 error:
- Wait 2-3 minutes for deployment to complete
- Check GitHub Pages settings are correct
- Verify `index.html` is in the root folder

### Charts not showing:
- Open browser console (F12)
- Check for errors
- Ensure all JSON files are in `data/` folder

---

## 🎉 After Deployment

**Share your dashboard:**
- Main Dashboard: `https://your-url.com/`
- Map View: `https://your-url.com/map.html`

**Update your dashboard:**
- **Netlify Drop**: Drag folder again
- **GitHub Pages**: Push changes with Git
- **Vercel**: Push to GitHub (auto-deploys)

---

## 💡 Pro Tips

1. **Custom Domain** (optional):
   - Buy a domain (Namecheap, Google Domains: ~$10/year)
   - Add to your hosting platform (all support custom domains)

2. **Analytics** (optional):
   - Add Google Analytics
   - Or use privacy-friendly: Plausible, Fathom

3. **Updates**:
   - Edit local files
   - Re-deploy using same method

---

**Choose your method above and get started! 🚀**
