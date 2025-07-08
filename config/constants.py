# Countries & major cities supported by Adzuna
COUNTRIES = {
    "gb": ["london", "manchester", "birmingham"],
    "us": ["new york", "san francisco", "chicago", "austin"],
    "at": ["vienna"],
    "au": ["sydney", "melbourne", "brisbane"],
    "be": ["brussels"],
    "br": ["sao paulo", "rio de janeiro"],
    "ca": ["toronto", "vancouver", "montreal"],
    "ch": ["zurich", "geneva"],
    "de": ["berlin", "munich", "frankfurt"],
    "es": ["madrid", "barcelona", "valencia"],
    "fr": ["paris", "lyon", "marseille"],
    "in": ["bangalore", "mumbai", "delhi", "hyderabad"],
    "it": ["rome", "milan", "naples"],
    "mx": ["mexico city", "guadalajara"],
    "nl": ["amsterdam", "rotterdam"],
    "nz": ["auckland", "wellington"],
    "pl": ["warsaw", "krakow"],
    "sg": ["singapore"],
    "za": ["johannesburg", "cape town"]
}

# High-demand job role queries across tech, business, design, etc.
QUERIES = [
    # Data & Analytics
    "data analyst", "business analyst", "financial analyst", "marketing analyst",
    "data scientist", "machine learning engineer",

    # Software & Engineering
    "software engineer", "frontend developer", "backend developer",
    "full stack developer", "cloud engineer", "devops engineer", "qa engineer",

    # Product & Project
    "product manager", "project manager", "scrum master",

    # IT & Security
    "it support", "cybersecurity analyst", "network engineer",

    # Design & Creative
    "ui ux designer", "graphic designer", "web designer",

    # Marketing & Sales
    "digital marketing", "seo specialist", "content writer", "sales associate",

    # HR, Admin & Operations
    "hr specialist", "recruiter", "operations manager", "administrative assistant",

    # Finance & Accounting
    "accountant", "bookkeeper", "risk analyst", "compliance officer"
]

PAGES = range(1, 2)  


NORMALIZATION_MAP = {
    # Programming Languages
    "py": "python",
    "python3": "python",
    "python 3": "python",
    "r programming": "r",
    "c plus plus": "c++",
    "cplusplus": "c++",

    # Data/BI Tools
    "powerbi": "power bi",
    "power-bi": "power bi",
    "power_bi": "power bi",
    "microsoft power bi": "power bi",
    "ms excel": "excel",
    "microsoft excel": "excel",
    "excel spreadsheet": "excel",
    "spreadsheet": "excel",
    "tableau software": "tableau",

    # Cloud Platforms
    "amazon web services": "aws",
    "aws cloud": "aws",
    "microsoft azure": "azure",
    "google cloud": "gcp",
    "google cloud platform": "gcp",
    "gcp cloud": "gcp",

    # ML / AI
    "ml": "machine learning",
    "ai": "artificial intelligence",
    "deep learning techniques": "deep learning",

    # DevOps / Infra
    "docker container": "docker",
    "containerization": "docker",
    "version control": "git",
    "github": "git",
    "bitbucket": "git",
    "linux environment": "linux",
    "unix": "linux",
    "bash scripting": "bash",

    # Big Data / ETL
    "apache spark": "spark",
    "pyspark": "spark",
    "etl pipeline": "etl",
    "data pipeline": "etl",
    "data pipelines": "etl",

    # Other Tools
    "jira software": "jira",
    "google sheets": "excel",
    "communication skills": "communication",
    "problem-solving": "problem solving",
    "data viz": "data visualization",
    "data visualisation": "data visualization"
}