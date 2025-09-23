# Lab 2 Report: Git Version Control and Flet GUI Development

**Student Name:** Ayelyn Janne F. Panliboton  
**Student ID:** 231002287  
**Section:** 3A  
**Date:** August 27, 2025

## Git Configuration

### Repository Setup
- **GitHub Repository:** https://github.com/vapieee/cccs106-projects-
- **Local Repository:** ✅ Initialized and connected
- **Commit History:** 5+ commits with descriptive messages

### Git Skills Demonstrated
- ✅ Repository initialization and configuration  
- ✅ Adding, committing, and pushing changes  
- ✅ Branch creation and merging  
- ✅ Remote repository management  

## Flet GUI Applications

### 1. hello_flet.py
- **Status:** ✅ Completed  
- **Features:** Interactive greeting, student info display, dialog boxes  
- **UI Components:** Text, TextField, Buttons, Dialog, Containers  
- **Notes:** No major issues, I just experienced difficulties in instaling the flet since it always shows "pip not recognized" in cmd. Fortunately, GUI launched successfully.

### 2. personal_info_gui.py
- **Status:** ✅ Completed  
- **Features:** Form inputs, dropdowns, radio buttons, profile generation  
- **UI Components:** TextField, Dropdown, RadioGroup, Containers, Scrolling  
- **Error Handling:** Input validation and user feedback  
- **Notes:** Required extra effort on layout alignment and dropdown logic.

## Technical Skills Developed

### Git Version Control
- Understood Git repo setup  
- Learned staging and committing files  
- Used branches for testing features  
- Practiced merging and pushing to GitHub  

### Flet GUI Development
- Used Flet 0.28.3 components and layout tools  
- Created user-friendly pages with input validation  
- Handled events (button clicks, text input)  
- Built interactive and scrollable UIs

## Challenges and Solutions

- **Git Remote Error:** Initially got “remote repository not found.” Fixed it by correcting GitHub URL and ensuring proper access.  
- **Branch Deletion:** Couldn’t delete remote branch at first. Realized it was set as default, so renamed and cleaned up.  
- **GUI Alignment:** Struggled with container layouts. Solved by using `Column`, `Row`, and `expand` parameters.

## Learning Outcomes

- I now understand how Git helps manage code history and work with branches.  
- I learned how to write clean commit messages and push changes to GitHub.  
- I gained hands-on experience with Flet, which makes building UIs with Python easier and more visual.  
- This lab improved my confidence in project structure, GUI design, and debugging.

## Screenshots

### Git Repository
- ![\[ \] GitHub repository showing latest commits ](lab2_screenshots/git_commits.png) 
- ![ \] Screenshot of `git log` or `git status`](lab2_screenshots/git_log.png)  

### GUI Applications
- ![Screenshot of `hello_flet.py` running](lab2_screenshots/hello_flet_output.png)
- ![Screenshot of `personal_info_gui.py` with completed form  ](lab2_screenshots/personal_info_gui_output.png)

## Future Enhancements

- Add real-time validation for form fields  
- Save user input data to a local file  
- Add a reset button to clear the form  
- Create a fully working calculator GUI with operations