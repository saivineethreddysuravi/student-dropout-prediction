# Student Dropout Prediction System

A machine learning web application that predicts student dropout, enrollment, and graduation outcomes to help universities identify at-risk students early and implement targeted interventions.

## 🎯 Project Overview

**Problem:** Universities face 25-30% dropout rates, impacting institutional reputation and student futures.

**Solution:** A full-stack ML web application using real academic data to predict student outcomes with 89% accuracy.

**Impact:** Enable early identification of at-risk students for proactive support and intervention.

## ✨ Features

- 🔐 **User Authentication System** - Secure registration and login
- 📊 **ML Prediction Engine** - Real-time predictions using Random Forest model
- 📈 **Prediction History** - Track and analyze past predictions
- ℹ️ **Field Information Guide** - Understand all 36 input variables
- 👨‍💼 **Admin Dashboard** - System management and analytics
- 📱 **Responsive Web Interface** - Works on desktop and mobile

## 🏗️ Technology Stack

| Component | Technology |
|-----------|-----------|
| **Backend** | Django 4.2.1 (Python) |
| **Frontend** | HTML5, CSS3, Bootstrap 5 |
| **Database** | SQLite (Development), PostgreSQL (Production) |
| **ML Engine** | scikit-learn 1.6.1 |
| **Data Processing** | Pandas 2.3.3 |
| **Serialization** | Joblib 1.5.2 |

## 📊 Dataset & Features

- **Source:** UCI Machine Learning Repository
- **Dataset:** Predict Students Dropout and Academic Success
- **Features:** 36 input variables across multiple categories
- **Outcomes:** 3 classes (Dropout, Enrolled, Graduate)
- **Records:** Thousands of student enrollment records

### Feature Categories

1. **Personal Information (5)** - Gender, marital status, age, nationality, displacement
2. **Education Background (6)** - Previous qualifications, parents' education/occupation
3. **Enrollment Details (6)** - Course, application mode, admission grade, attendance type
4. **Academic Performance (12)** - Semester 1 & 2 credits, grades, evaluations
5. **Financial & Social (6)** - Debtor status, scholarship, tuition, special needs
6. **Economic Factors (3)** - Unemployment rate, inflation, GDP

## 🤖 Machine Learning Model

### Model Selection
- **Tested:** Logistic Regression, Random Forest, Gradient Boosting, SVM
- **Selected:** Random Forest (200 trees)
- **Accuracy:** 89% on test data
- **Inference Time:** < 100ms per prediction

### Model Training Process
1. Data preprocessing and feature engineering
2. 80/20 stratified train-test split
3. Model training with hyperparameter tuning
4. Evaluation using multiple metrics (accuracy, precision, recall, F1)
5. Serialization to pickle file for deployment

## 🚀 Getting Started

### Prerequisites
- Python 3.10+
- pip or conda
- Virtual environment (recommended)

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/student-dropout-prediction.git
cd student-dropout-prediction
```

2. **Create virtual environment**
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Navigate to Django project**
```bash
cd student_dropout_project/student_dropout_project
```

5. **Run migrations**
```bash
python manage.py migrate
```

6. **Start development server**
```bash
python manage.py runserver
```

7. **Access the application**
Open browser to: `http://127.0.0.1:8000`

### Demo Credentials

**Application User:**
- Username: `vineethreddy_app12`
- Password: `Welcome12@`

**Admin User:**
- Username: `vineethreddy`
- Password: `vineethreddy@123`

## 📚 Usage

### Making a Prediction

1. Login to the application
2. Click "Predict" in navigation
3. Fill the 36-field form with student information
4. Submit the form
5. View instant prediction (Dropout, Enrolled, or Graduate)
6. Check prediction history to track patterns

### Viewing Predictions

- Go to "History" page to see all past predictions
- Click on any prediction to view details
- Track prediction outcomes over time

### Learning Resources

- Click "Field Info" to understand each input variable
- Read documentation for feature explanations

## 📁 Project Structure

```
student-dropout-prediction/
├── README.md
├── requirements.txt
├── .gitignore
├── data.csv (UCI dataset)
├── SaiVineeth_ML_Model.ipynb (Model training notebook)
│
└── student_dropout_project/
    └── student_dropout_project/ (Django project root)
        ├── manage.py
        ├── db.sqlite3
        │
        ├── student_dropout_project/ (settings)
        │   ├── settings.py
        │   ├── urls.py
        │   ├── wsgi.py
        │   └── asgi.py
        │
        ├── predictor/ (main app)
        │   ├── models.py (Database models)
        │   ├── views.py (Business logic)
        │   ├── forms.py (Form definitions)
        │   ├── urls.py (URL routing)
        │   ├── admin.py (Admin interface)
        │   └── ml_models/
        │       └── best_student_dropout_model.pkl
        │
        └── templates/
            └── predictor/
                ├── base.html
                ├── login.html
                ├── register.html
                ├── predict_form.html
                ├── prediction_result.html
                ├── history.html
                └── field_info.html
```

## 🔐 Security Features

✅ Password hashing using Django's built-in system
✅ CSRF protection on all forms
✅ SQL injection prevention via ORM
✅ Login-required decorators on sensitive views
✅ User data isolation (users only see their own predictions)
✅ Session management and authentication
✅ Server-side input validation

## 📈 Performance

| Operation | Time |
|-----------|------|
| Model Loading | < 1 second |
| Prediction | < 100 milliseconds |
| Database Query | < 50 milliseconds |
| Total Response | < 1 second |
| Form Validation | < 100 milliseconds |

## 🚀 Deployment

### Production Deployment

1. **Change settings for production:**
   - Set `DEBUG = False`
   - Configure `ALLOWED_HOSTS`
   - Use strong `SECRET_KEY`

2. **Use production database:**
   - Migrate from SQLite to PostgreSQL
   - Configure database credentials in environment

3. **Set up web server:**
   - Use Gunicorn (WSGI server)
   - Configure Nginx as reverse proxy
   - Enable HTTPS/SSL

4. **Deploy to cloud:**
   - Options: AWS, Heroku, Azure, DigitalOcean
   - Set up monitoring and logging
   - Configure automated backups

### Docker (Optional)

```dockerfile
FROM python:3.11
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
```

## 📊 Results & Impact

- **Prediction Accuracy:** 89% on real student data
- **Response Time:** < 1 second per prediction
- **Features Analyzed:** 36 comprehensive student attributes
- **Outcomes Predicted:** 3 distinct student trajectories
- **Real-World Application:** Institutional dropout prevention

## 🎓 Learning Outcomes

This project demonstrates:

✅ Full-stack web development with Django
✅ Machine learning model deployment
✅ Database design and SQL
✅ User authentication and security
✅ Form validation and error handling
✅ Model serialization and loading
✅ System architecture and design
✅ Professional documentation

## 📝 Model Training (Jupyter Notebook)

The ML model was trained using `SaiVineeth_ML_Model.ipynb`:

1. Data loading and preprocessing
2. Feature engineering and selection
3. Model comparison (4 algorithms)
4. Hyperparameter tuning
5. Evaluation and metrics
6. Model serialization to pickle file

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📜 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 📞 Contact

**Student:** Sai Vineeth Reddy Suravi
**Project:** Student Dropout Prediction System
**Term:** Fall 2025

## 🙏 Acknowledgments

- UCI Machine Learning Repository for the dataset
- Django framework and community
- scikit-learn for machine learning tools
- Open source community for tools and libraries

---

## 🎯 Next Steps

- [ ] Deploy to production cloud service
- [ ] Add real-time data integration
- [ ] Build mobile app companion
- [ ] Create API for external integrations
- [ ] Add advanced analytics dashboard
- [ ] Implement student intervention tracking
- [ ] Add multi-language support
- [ ] Create admin report generation

---

**Project Status:** ✅ Complete & Production-Ready

Built with ❤️ for academic excellence and student success.
