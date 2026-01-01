"""
Curated database of technical skills organized by category.
Used by the NLP extractor for pattern matching and categorization.
"""

SKILLS_DATABASE = {
    "programming_languages": [
        "Python", "JavaScript", "TypeScript", "Java", "C++", "C#", "Go", "Golang",
        "Rust", "Ruby", "PHP", "Swift", "Kotlin", "Scala", "R", "MATLAB",
        "Perl", "Dart", "Elixir", "Haskell", "Clojure", "F#", "Objective-C",
        "Shell", "Bash", "PowerShell", "SQL", "PL/SQL", "T-SQL", "VBA",
        "Assembly", "C", "Fortran", "COBOL", "Lua", "Groovy", "Julia",
        "Racket", "Scheme", "Erlang", "OCaml", "Ada", "Pascal", "Delphi",
    ],

    "frameworks": [
        # Web Frameworks
        "React", "React.js", "ReactJS", "Angular", "AngularJS", "Vue", "Vue.js",
        "Svelte", "Next.js", "NextJS", "Nuxt", "Nuxt.js", "Gatsby",
        "Django", "Flask", "FastAPI", "Express", "Express.js", "NestJS",
        "Spring", "Spring Boot", "ASP.NET", ".NET", "ASP.NET Core", "Ruby on Rails", "Rails",
        "Laravel", "Symfony", "CodeIgniter", "CakePHP", "Yii",
        "Phoenix", "Gin", "Echo", "Fiber", "Beego",

        # Mobile Frameworks
        "React Native", "Flutter", "Ionic", "Xamarin", "SwiftUI", "UIKit",
        "Jetpack Compose", "Cordova", "Capacitor", "NativeScript",

        # Testing Frameworks
        "Jest", "Mocha", "Chai", "Jasmine", "Karma", "Cypress", "Selenium",
        "pytest", "unittest", "JUnit", "TestNG", "RSpec", "Enzyme",
        "Playwright", "Puppeteer", "WebdriverIO",

        # Others
        "TensorFlow", "PyTorch", "Keras", "Scikit-learn", "Pandas", "NumPy",
        "Apache Spark", "Hadoop", "Streamlit", "Gradio",
    ],

    "databases": [
        # Relational
        "PostgreSQL", "MySQL", "MariaDB", "Oracle", "SQL Server", "SQLite",
        "Amazon RDS", "Amazon Aurora", "Azure SQL", "Google Cloud SQL",

        # NoSQL
        "MongoDB", "Cassandra", "CouchDB", "DynamoDB", "Firebase",
        "Redis", "Memcached", "Elasticsearch", "Neo4j", "ArangoDB",
        "RavenDB", "Couchbase", "HBase", "ScyllaDB",

        # Data Warehouses
        "Snowflake", "BigQuery", "Redshift", "Databricks", "Teradata",
        "Amazon Athena", "Presto", "Apache Hive", "ClickHouse",
    ],

    "cloud_platforms": [
        # AWS
        "AWS", "Amazon Web Services", "EC2", "S3", "Lambda", "ECS", "EKS",
        "CloudFormation", "CloudWatch", "RDS", "DynamoDB", "SQS", "SNS",
        "API Gateway", "Elastic Beanstalk", "CloudFront", "Route 53",

        # Azure
        "Azure", "Microsoft Azure", "Azure DevOps", "Azure Functions",
        "Azure Kubernetes Service", "AKS", "Azure SQL", "Azure Cosmos DB",
        "Azure Storage", "Azure Active Directory",

        # Google Cloud
        "GCP", "Google Cloud Platform", "Google Cloud", "Compute Engine",
        "Cloud Functions", "Cloud Run", "GKE", "BigQuery", "Cloud Storage",
        "Firebase", "Cloud Firestore",

        # Other Cloud
        "Heroku", "Vercel", "Netlify", "Railway", "Render", "DigitalOcean",
        "Linode", "Vultr", "Cloudflare", "Supabase", "PlanetScale",
    ],

    "devops_tools": [
        # Containers & Orchestration
        "Docker", "Kubernetes", "K8s", "Helm", "OpenShift", "Rancher",
        "Podman", "containerd", "Docker Compose", "Docker Swarm",

        # CI/CD
        "Jenkins", "GitLab CI", "GitHub Actions", "CircleCI", "Travis CI",
        "Azure Pipelines", "Bamboo", "TeamCity", "ArgoCD", "Flux",

        # Infrastructure as Code
        "Terraform", "Ansible", "Puppet", "Chef", "CloudFormation",
        "Pulumi", "Vagrant", "SaltStack", "CDK",

        # Monitoring & Logging
        "Prometheus", "Grafana", "Datadog", "New Relic", "Splunk",
        "ELK Stack", "Elasticsearch", "Logstash", "Kibana", "Fluentd",
        "Sentry", "PagerDuty", "Nagios", "Zabbix",

        # Version Control
        "Git", "GitHub", "GitLab", "Bitbucket", "SVN", "Mercurial",
    ],

    "web_technologies": [
        # Frontend
        "HTML", "HTML5", "CSS", "CSS3", "SASS", "SCSS", "Less", "Stylus",
        "Tailwind", "Tailwind CSS", "Bootstrap", "Material-UI", "MUI",
        "Ant Design", "Chakra UI", "Semantic UI", "Bulma", "Foundation",
        "jQuery", "Ajax", "WebSockets", "GraphQL", "REST", "RESTful",
        "Webpack", "Vite", "Rollup", "Parcel", "esbuild", "Babel",
        "ESLint", "Prettier", "TypeDoc", "Storybook",

        # Backend
        "Node.js", "Deno", "Bun", "gRPC", "WebRTC", "Socket.io",
        "OAuth", "JWT", "SAML", "OpenID Connect", "Auth0", "Okta",
        "Passport.js", "bcrypt", "SSL", "TLS", "HTTPS",

        # APIs
        "REST API", "RESTful API", "GraphQL API", "Swagger", "OpenAPI",
        "Postman", "Insomnia", "Apollo", "Hasura", "tRPC",
    ],

    "data_science": [
        "Machine Learning", "ML", "Deep Learning", "Neural Networks",
        "Natural Language Processing", "NLP", "Computer Vision", "CV",
        "Artificial Intelligence", "AI", "Generative AI", "GenAI",
        "Data Analysis", "Data Visualization", "Statistical Analysis",
        "A/B Testing", "Hypothesis Testing", "Regression", "Classification",
        "Clustering", "Dimensionality Reduction", "Feature Engineering",

        # Libraries/Tools
        "TensorFlow", "PyTorch", "Keras", "Scikit-learn", "XGBoost",
        "LightGBM", "CatBoost", "Pandas", "NumPy", "SciPy", "Matplotlib",
        "Seaborn", "Plotly", "Bokeh", "Jupyter", "Jupyter Notebook",
        "Google Colab", "Tableau", "Power BI", "Looker", "Metabase",
        "Apache Airflow", "MLflow", "Kubeflow", "DVC", "Weights & Biases",
        "Hugging Face", "spaCy", "NLTK", "OpenCV", "YOLO", "BERT", "GPT",
    ],

    "mobile_development": [
        "iOS", "Android", "React Native", "Flutter", "Xamarin", "Ionic",
        "Swift", "SwiftUI", "UIKit", "Kotlin", "Java", "Jetpack Compose",
        "Objective-C", "Cordova", "Capacitor", "Expo", "Android Studio",
        "Xcode", "App Store", "Google Play", "Firebase", "push notifications",
        "Core Data", "Realm", "SQLite", "Room", "In-App Purchases",
    ],

    "design_tools": [
        "Figma", "Sketch", "Adobe XD", "InVision", "Zeplin", "Marvel",
        "Photoshop", "Illustrator", "After Effects", "Blender",
        "UI/UX", "User Experience", "User Interface", "Wireframing",
        "Prototyping", "Design Systems", "Accessibility", "WCAG", "ARIA",
    ],

    "methodologies": [
        "Agile", "Scrum", "Kanban", "Lean", "Waterfall", "SAFe",
        "TDD", "Test-Driven Development", "BDD", "Behavior-Driven Development",
        "CI/CD", "Continuous Integration", "Continuous Deployment",
        "DevOps", "DevSecOps", "GitOps", "Microservices", "Monolithic",
        "Event-Driven", "Domain-Driven Design", "DDD", "SOLID", "Clean Code",
        "Pair Programming", "Code Review", "Sprint Planning", "Retrospectives",
        "Stand-ups", "Daily Standups",
    ],

    "security": [
        "Cybersecurity", "Information Security", "Application Security",
        "Network Security", "Penetration Testing", "Ethical Hacking",
        "OWASP", "OWASP Top 10", "XSS", "CSRF", "SQL Injection",
        "Authentication", "Authorization", "Encryption", "Cryptography",
        "SSL/TLS", "PKI", "OAuth", "SAML", "MFA", "2FA",
        "Firewalls", "IDS", "IPS", "SIEM", "WAF", "DDoS Protection",
        "Security Audits", "Compliance", "GDPR", "HIPAA", "PCI DSS",
        "SOC 2", "ISO 27001", "Vulnerability Assessment",
    ],

    "blockchain": [
        "Blockchain", "Cryptocurrency", "Bitcoin", "Ethereum", "Solidity",
        "Smart Contracts", "Web3", "Web3.js", "Ethers.js", "DeFi",
        "NFT", "Consensus Algorithms", "Proof of Work", "Proof of Stake",
        "Distributed Ledger", "Hyperledger", "Truffle", "Hardhat",
        "Metamask", "Wallet Integration", "IPFS",
    ],

    "game_development": [
        "Unity", "Unreal Engine", "Godot", "CryEngine", "GameMaker",
        "Cocos2d", "Phaser", "Three.js", "WebGL", "OpenGL", "DirectX",
        "Vulkan", "Metal", "Game Design", "3D Modeling", "Animation",
        "Physics Engine", "Multiplayer", "Networking",
    ],

    "business_intelligence": [
        "Business Intelligence", "BI", "Data Warehousing", "ETL",
        "Data Pipeline", "Data Integration", "Reporting", "Dashboards",
        "KPIs", "Metrics", "Analytics", "Tableau", "Power BI", "Looker",
        "QlikView", "Sisense", "Domo", "Apache Superset", "Metabase",
        "Google Analytics", "Google Data Studio", "SAP", "Oracle BI",
    ],

    "soft_skills": [
        "Communication", "Leadership", "Teamwork", "Problem Solving",
        "Critical Thinking", "Analytical Skills", "Attention to Detail",
        "Time Management", "Project Management", "Collaboration",
        "Adaptability", "Creativity", "Innovation", "Mentoring",
        "Presentation Skills", "Written Communication", "Verbal Communication",
        "Stakeholder Management", "Customer Service", "Conflict Resolution",
        "Decision Making", "Strategic Thinking", "Emotional Intelligence",
    ],
}


def get_all_skills():
    """Returns a flat list of all skills across all categories"""
    all_skills = []
    for category, skills in SKILLS_DATABASE.items():
        all_skills.extend(skills)
    return all_skills


def get_category_for_skill(skill_name: str) -> str:
    """Returns the category for a given skill name"""
    skill_lower = skill_name.lower()
    for category, skills in SKILLS_DATABASE.items():
        if any(skill.lower() == skill_lower for skill in skills):
            return category
    return "other"


def get_skills_by_category(category: str):
    """Returns all skills for a given category"""
    return SKILLS_DATABASE.get(category, [])
