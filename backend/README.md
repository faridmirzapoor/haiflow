# CSA UK AC Backend

Welcome! This is the backend for the CSA UK AC project. If you’re new to the team, here’s how to get started and contribute:

## Getting Started

1. **Clone the repository:**
     ```bash
     git clone git@github.com:artahaam/csa_uk_ac.git
     cd csa_uk_ac/backend
     ```

2. **Switch to the dev branch:**
     ```bash
     git switch dev
     git pull origin dev
     ```

3. **Set up your environment:**
     - Create and activate a virtual environment:
         ```bash
         python3 -m venv venv
         source venv/bin/activate
         ```
     - Install dependencies:
         ```bash
         pip install -r requirements.txt
         ```
     - Copy the `.env` file template and fill in your local settings.

4. **Apply migrations and run the server:**
     ```bash
     python manage.py migrate
     python manage.py runserver
     ```

## How to Contribute

- All changes go to the `dev` branch. Never push directly to `main`.

Work directly on the `dev` branch for all features and fixes. When your work is ready for release, open a merge request (MR) from `dev` to the `main` branch and ask for a review.

Example workflow:
```bash
git switch dev
git pull origin dev
# make your changes
git add .
git commit -m "your message"
git push origin dev
```

If you have any questions, just ask in the group chat. Happy coding!
