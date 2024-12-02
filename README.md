
# Job Scraper Application

This is a Job Scraper application built with React for the frontend and Flask for the backend. The application allows users to search for job listings by selecting a keyword, and it scrapes job data from a backend API. The data is displayed in a table with links to the company's job listings.

## Prerequisites

Before setting up the project, make sure you have the following installed on your system:

- **Node.js**: [Download and Install Node.js](https://nodejs.org/)
- **Python**: [Download and Install Python](https://www.python.org/downloads/)
- **pip**: Python package installer (usually installed with Python)

## Setup Instructions

### 1. Clone the repository

Start by cloning the repository to your local machine:

```bash
git clone https://github.com/yourusername/DexiAI-Assignment.git
cd DexiAI-Assignment
```

### 2. Set up the Backend (Flask API)

The backend is built using **Flask** and will serve as an API to scrape job listings.

#### a. Install backend dependencies

Navigate to the `Backend` directory and create a virtual environment:

```bash
cd Backend
python -m venv venv
source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
```

#### b. Install Python dependencies

Install the required Python packages using `pip`:

```bash
pip install -r requirements.txt
```

Make sure the `requirements.txt` file contains the following dependencies:

```txt
Flask
Flask-Cors
requests
beautifulsoup4
```

#### c. Run the Flask server

Once the dependencies are installed, run the Flask backend:

```bash
python app.py
```

By default, the Flask API will run on `http://127.0.0.1:5000/`.

### 3. Set up the Frontend (React Application)

#### a. Install frontend dependencies

Navigate to the `Frontend` directory:

```bash
cd ../Frontend
```

Install the required dependencies:

```bash
npm install
```

#### b. Run the React app

Start the React development server:

```bash
npm start
```

The React app will run on `http://localhost:3000/`.

### 4. Access the Application

Once both the backend and frontend servers are running:

- Open your browser and navigate to `http://localhost:3000/` to access the Job Scraper UI.
- The UI will allow you to select a keyword and fetch job listings based on that keyword from the backend.

### 5. Example Usage

1. Choose a keyword (e.g., `software-engineer`) from the dropdown.
2. Click the "Search Jobs" button.
3. The job listings will be fetched from the backend and displayed in a table with clickable links to job postings.

## Folder Structure

```plaintext
DexiAI-Assignment/
│
├── Backend/              # Backend directory containing the Flask API
│   ├── app.py            # Flask API for scraping job data
│   ├── requirements.txt  # Backend dependencies
│
└── Frontend/             # Frontend directory containing the React app
    ├── src/
    │   ├── App.js        # Main React component
    │   ├── App.css       # Styles for the frontend
    │   └── index.js      # React entry point
    ├── package.json      # Frontend dependencies
```

## Additional Notes

- Make sure that both the frontend and backend are running on different ports to avoid conflicts. React runs by default on `http://localhost:3000/` and Flask on `http://127.0.0.1:5000/`.
- The backend scraping logic uses BeautifulSoup and requests to scrape job listings. You can modify the backend to include other scraping sources as needed.

## License

This project is licensed under the MIT License.
