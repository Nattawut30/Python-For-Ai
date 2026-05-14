"""
VS code Git = Git in your editor
VS Code has Git built in.
You can do everything with clicks instead of commands.

Look at the left sidebar in VS Code. You'll see this icon:
- Source Control icon (looks like a branch)
- Shows all your changed files
- One-click commits
"""

# Basic Workflow

"""
1. See your changes

Open the Source Control panel:
- Changed files appear under “Changes”
- Click any file to see what changed
- Green lines = added
- Red lines = removed

2. Stage changes

Before committing, you “stage” files:
- Hover over a file
- Click the + icon
- Or click + next to “Changes” to stage everything

3. Commit

Once files are staged:
- Type a message in the text box
- Press Ctrl/Cmd + Enter (or click ✓)

That's a commit!

4. Push to GitHub

After committing:
- Click the … menu in Source Control
- Click “Push”
- Or click the sync icon in the bottom status bar

Visual features

5. See changes inline

- Modified files show a colored bar in the editor
- Click the bar to see what changed
- Blue = modified, Green = added, Red = deleted
"""

# Pro tips for beginners
"""
1. Commit often: Every small feature or fix
2. Write clear messages: “Fix login bug” not “changes”
3. Pull before starting: Get latest changes first
4. Don't commit secrets: Check your .gitignore

***** Never commit .env files or API keys! *****
***** Always add them to .gitignore first. *****
"""