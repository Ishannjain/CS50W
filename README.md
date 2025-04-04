# CS50 Web Projects

This repository contains web applications developed as part of the CS50 Web Programming with Python and JavaScript course. These projects showcase my skills in building dynamic web applications using Django, JavaScript, and HTML/CSS, implementing RESTful APIs, CRUD operations, and user authentication.

## Projects

### 1. Wikipedia
A web-based encyclopedia that allows users to:
- View existing Wikipedia-style pages
- Search for articles
- Create, edit, and save new pages using Markdown
- Randomly access an article

### 2. Mail
A front-end for an email client that interacts with a RESTful API, enabling users to:
- Send and receive emails
- Mark emails as read/unread
- Archive/unarchive messages
- Implement user authentication and session management

### 3. Auction House
An online auction platform where users can:
- List new auction items with starting bids
- Place bids on existing listings
- Comment on items
- Watchlist items of interest
- Close auctions and declare winners
- Implement authentication and authorization

### 4. Social Network
A simple social networking platform allowing users to:
- Create and edit posts
- Like/unlike posts
- Follow/unfollow other users
- View personalized feeds
- Utilize a RESTful API for seamless user interaction

## Technologies Used
- **Back-end:** Django (Python)
- **Front-end:** HTML, CSS, JavaScript
- **Database:** SQLite (Django ORM)
- **APIs:** RESTful API implementation
- **Authentication:** Django's built-in user authentication system

## Installation & Setup
1. Clone the repository:
   ```sh
   git clone https://github.com/your-username/cs50-web-projects.git
   cd cs50-web-projects
   ```
2. Create a virtual environment and install dependencies:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   pip install -r requirements.txt
   ```
3. Apply migrations and start the development server:
   ```sh
   python manage.py migrate
   python manage.py runserver
   ```
4. Open your browser and visit `http://127.0.0.1:8000/` to interact with the applications.

## Future Improvements
- Enhance UI/UX with Bootstrap or Tailwind CSS
- Implement WebSockets for real-time interactions
- Add more robust testing


