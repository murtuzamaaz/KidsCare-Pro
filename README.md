# KidsCare Pro

**KidsCare Pro** is an AI-powered child health management platform with a 95% accuracy Machine Learning model. It helps parents and doctors make informed health decisions, track milestones, and manage child health effectively.

## Key Features
- **ML-Driven Health Predictions**: 95% accurate health predictions based on child data.
- **User Authentication**: Secure login for parents and doctors using AWS Cognito.
- **Health Predictor**: Used  Fine-tuned Llamma model on medical data for medical advise.
- **Appointments**: Book healthcare appointments easily.
- **Dashboard**: Visualized health insights and trends.
- **Child Profile Management**: Store and manage child health records with AWS DynamoDB.
- **Milestones Tracking**: Track developmental milestones for timely intervention.
- **Doctor's Portal**: Tools for healthcare providers to manage child profiles.

## Tech Stack
- **Frontend**: [Streamlit](https://streamlit.io/)
- **Backend**: Python
- **Machine Learning**: 95% accuracy model
- **Data Visualization**: Matplotlib, Seaborn, Plotly
- **AWS**: Cognito (User Authentication), DynamoDB (Data Storage), Boto3 (AWS SDK)
- **Image Processing**: Pillow
- **Navigation**: `streamlit_option_menu`

1. ![389246845-d4ebcd36-8031-4827-a4c2-63903e0bdcdb](https://github.com/user-attachments/assets/d0547268-c7a5-4c9e-bedb-4d790bffd2be)
2. ![389246847-3df819b0-b3a7-48ca-9640-f4e431b8998b](https://github.com/user-attachments/assets/cd30dffb-ecab-41e4-a1b2-a9b16a8f1974)
3. ![389246848-d494135a-bf64-4787-99f4-f705ca6e547c](https://github.com/user-attachments/assets/aedefe2f-dc7a-4e7b-8940-cdbadd3015f9)
4. ![389246850-4b6dafef-e9dc-4ed7-bc55-b4bb4b9855be](https://github.com/user-attachments/assets/5bfa5b92-091f-4578-a1ce-817d940a120d)
5. ![389246853-4b1353dd-0bb4-463e-8784-7de13712738c](https://github.com/user-attachments/assets/5f4becd1-5429-4702-8b04-8e7c6c77572c)
6. ![389246856-c48cc32c-8c23-4fdf-9d59-fb10b2cc749f](https://github.com/user-attachments/assets/5e8891f0-9cf5-4c51-9d25-ddee4264c4de)
7. ![389246854-f252d992-0985-41dc-a272-dcf8d3c279d4](https://github.com/user-attachments/assets/3f49320d-cd34-46b9-8fe5-fa4e02d0bb29)
8. ![389246855-af10ebad-7733-4747-b313-92f57c56f333](https://github.com/user-attachments/assets/21df217a-1dd1-46d7-8567-c461b957cec7)
9. ![389246857-07eaf58d-9c88-47e0-92ea-10ee51afe170 (1)](https://github.com/user-attachments/assets/bc39383c-4aa7-4a5b-a361-f50c7669b0f6)


## Installation

### 1. Clone the Repository
```bash
git clone[ https://github.com/Sa1f27/child_growth.git
cd child_growth
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Set Up AWS Cognito and DynamoDB (Optional)
To use AWS Cognito for user authentication and DynamoDB for storing data, follow these steps:

#### **Step 1: Set Up AWS Cognito**
1. **Create a User Pool**:  
   - Go to the AWS Cognito console and create a User Pool.
   - Note down the **User Pool ID** and **App Client ID**.

2. **Configure the App Client**:
   - In the User Pool settings, under "App clients," create a new App Client.
   - Disable client secret for easier integration with Streamlit.
   - Note the **App Client ID**.

#### **Step 2: Set Up DynamoDB**
1. **Create a DynamoDB Table**:  
   - Go to the DynamoDB console and create a table for storing child health data (e.g., `ChildHealthRecords`, `Appointments`).
   - Configure the primary key (e.g., `child_id`, `ID` as the partition key).

2. **Set Permissions**:  
   - Ensure your AWS user has permissions for accessing Cognito and DynamoDB.

#### **Step 3: Set AWS Credentials**
Set your AWS access keys and configure your AWS region. You can do this by adding environment variables:

```bash
export AWS_ACCESS_KEY=<YourAccessKey>
export AWS_SECRET_KEY=<YourSecretKey>
export AWS_REGION=<YourRegion>
export AWS_USER_POOL_ID=<YourUserPoolID> 
export AWS_APP_CLIENT_ID=<YourAppClientID> 
```

### 4. Run the Application
```bash
streamlit run app.py
```

## File Structure
```
KidsCarePro/
├── app/
│   ├── app.py              # Main Streamlit app
│   ├── appointments.py     # Appointment booking
│   ├── dashboard.py        # Dashboard functionality
│   ├── doctor_portal.py    # Doctor's portal functionality
│   ├── home.py             # Home page logic
│   ├── ai_model.py         # ML model for health predictions
│   ├── growth.py           # Child profile management
│   ├── milestone.py        # Milestone tracking
│   ├── show_analytics.py   # Analytics dashboard
│   └── symptoms.py         # Health predictor
├── model/
│   ├── child_dataset.csv
│   ├── eda_report.html
│   ├── model.ipynb 
│   └── symptom_predictor.pkl
├── README.md
├── requirements.txt  # Documentation
```


## Machine Learning Model
- **Accuracy**: 95% on test data
- **Features**: Age, weight, height, BMI, symptoms, health history
- **Personalized Insights**: Health recommendations based on input data.

## Customization
- **ML Model**: Update `ai_model.py` for improved accuracy or additional features.
- **UI**: Modify the CSS in `app.py` for custom styling.
- **AWS Integration**: Enable DynamoDB and Cognito in `app.py`.

## Dependencies
- **Streamlit**: Interactive web interface
- **Scikit-learn**: ML model implementation
- **Matplotlib/Seaborn/Plotly**: Data visualization
- **Pillow**: Image handling
- **Boto3**: AWS SDK for Python
- **Numpy**: Numerical computations

