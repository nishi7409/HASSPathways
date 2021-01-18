[![Netlify Status](https://api.netlify.com/api/v1/badges/5f319796-9a6d-4747-9269-c2bd33bbdf72/deploy-status)](https://app.netlify.com/sites/hasspathways/deploys)
# Master Deployment
https://hasspathways.netlify.app/

# Frontend Developmental Setup (use cmd prompt, not wsl)
- Clone the repository to your computer
- Install Nodejs - https://nodejs.org/en/download/
- `cd` to `/frontend` directory of `HASSPathways` and type `npm install` into your console
- Once everything is installed (ignore warnings), type `npm run serve`
- Visit the specified website (localhost/IP address) the console spits out


# BRANCH/PR
To maintain an individual's credibility towards this project and order, we'll be using branches and pull requests. Branches will separate our work from one another preventing each other from overwriting someone else's work. Pull requests is more of a formaility before it goes to production. I will be handling all pull requests.

The ideal format for a branch name in this project is `issueNumber-&-issueNumber/FirstName`
For example, your branch would be called `3-&-16/Chris`. You'd base your branch off the `all-frontend` or `all-backend` branch depending on what *type* (frontend or backend) issue you've been assigned.

When you're completely done with your tasks, push to your specific branch then create a pull request to the your main-stack's branch (`all-frontend` or `all-backend`).

From there, I'll handle the PR and if everything fits, I'll commit to the stack's branch AND push your code to the master branch.
