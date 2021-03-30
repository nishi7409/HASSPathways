# HASS Pathways
[![Netlify Status](https://api.netlify.com/api/v1/badges/5f319796-9a6d-4747-9269-c2bd33bbdf72/deploy-status)](https://app.netlify.com/sites/hasspathways/deploys)
#### Project Details
This project was developed to help students navigate through Rensselaer Polytechnic Institute's newly designed HASS (humanities, arts, and social sciences) curriculum--effective for the class of 2023 and beyond--which requires students to take part in an integrated pathway. The HASS Integrative Pathways were created to enhance students' HASS Core curriculum by bringing intentionality and depth to the requirements. The themes of the pathways vary in their intentionality; some are interdisciplinary, while others focus on a single discipline, providing students with significant options for their coursework. In addition to providing a more in-depth focus to the HASS Core, many Integrative Pathways can be transformed into minors with relative ease.
#### Information in regards to the **[goals of the pathways](https://info.rpi.edu/hass-pathways/goals-pathways "source")** include:
- An Integrative Pathway provides consistency to what could otherwise be an unfocused array of courses in the HASS Core
- An Integrative Pathway augments intellectual coherence to course selection in the form of disciplinary or interdisciplinary themes
- An Integrative Pathway can enhance or enrich a major. For example, a Computer Science major following the Artificial Intelligence pathway or a Biomedical Engineering major following the Public Health pathway

# Administrator Information
#### Data Sheet
https://docs.google.com/spreadsheets/d/1w6BNcxYCE54pvCJJWHiEoE9CiMjRrVNKeUArV97qN8w/edit?usp=sharing

#### Fill Database
Update later

#### Automation
Update later

#### Server Configuration & Deployment
Update later

# Developer Information
#### Frontend Setup
- Clone the repository to your computer
- Install Nodejs - https://nodejs.org/en/download/
- Open Command Prompt by executing `cmd.exe` in the Windows Run box
- `cd` to the `/frontend` directory of `HASSPathways` and type `npm install` into your console
- Once everything is installed (ignore warnings), type `npm run serve`
- Visit the specified website the console spits out

#### Backend Setup
- Update later

#### Branches/Pull Requests
To maintain an individual's credibility towards this project and order, we'll be using branches and pull requests. Branches will separate our work from one another preventing each other from overwriting someone's work. Pull requests is more of a formaility before it goes to production. With an active pull request, it tells the other developers part of the team that a feature/issue has been newly created/resolved. Pull requests will be handled by @nishi7409

The ideal format for a branch name in this project is `issueNumber-&-issueNumber/FirstName`
For example, a possible branch name would be called `3-&-16/John`. You'd base your branch off the `all-frontend` or `all-backend` branch depending on what *stack* (frontend or backend) issue you've been assigned. All issues are created with a label assigned to them (if one hasn't been labeled, let the project leader know ASAP).

When you're completely done with your issues that have been assigned to you, push to your specific branch then create a pull request to the your main-stack's branch (`all-frontend` or `all-backend`). If the pull request is approved, you should expect to see your commits made to your stack's main branch **and** your changes should be out on the live production page.
