import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import random

# Download NLTK data
nltk.download('punkt')
nltk.download('stopwords')

# Import necessary modules for Django
from django.shortcuts import render
from django.http import HttpResponse
from .models import Application

def preprocess_text(text):
    tokens = word_tokenize(text.lower())
    filtered_tokens = [token for token in tokens if token.isalpha() and token not in stopwords.words('english')]
    return ' '.join(filtered_tokens)

def transform_similarity_score(score):
    return round(score * 100, 2)

def compute_similarity(years_experience, software_experience, certifications, availability, tax_knowledge, combined_job_description):
    applicant_processed = preprocess_text(f"Years of Tax Preparation Experience: {years_experience} Tax Software Experience: {software_experience} Tax Certifications: {certifications} Availability during Tax Season: {availability} Describe Your Tax Knowledge: {tax_knowledge}")
    combined_job_description_processed = preprocess_text(combined_job_description)
    documents = [applicant_processed, combined_job_description_processed]
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(documents)
    similarity_matrix = cosine_similarity(tfidf_matrix)
    similarity_score = similarity_matrix[0, 1]
    transformed_score = transform_similarity_score(similarity_score)
    return transformed_score

def collect_applicant_info(years_experience, software_experience, certifications, availability, tax_knowledge):
    info = f"""
    Years of Tax Preparation Experience: {years_experience}
    Tax Software Experience: {software_experience}
    Tax Certifications: {certifications}
    Availability during Tax Season: {availability}
    Describe Your Tax Knowledge: {tax_knowledge}
    """
    return info

def main(request):
    return render(request,'index.html')

def index(request):
    if request.method == "POST":
        apply = Application()
        apply.firstName = request.POST.get('firstName')
        apply.lastName = request.POST.get('lastName')
        apply.position = request.POST.get('position')
        apply.address = request.POST.get('address')
        apply.city = request.POST.get('city')
        apply.state = request.POST.get('state')
        apply.zip = request.POST.get('zip')
        apply.phone = request.POST.get('phone')
        apply.email = request.POST.get('email')
        apply.years = request.POST.get('years')
        apply.certifications = request.POST.get('certifications')
        apply.availability = request.POST.get('availability')
        apply.taxKnowledge = request.POST.get('taxKnowledge')
        apply.taxSoftware = request.POST.get('taxSoftware')
        apply.recentStartDate = request.POST.get('recentStartDate')
        apply.recentEndDate = request.POST.get('recentEndDate')
        apply.recentJobTitle = request.POST.get('recentJobTitle')
        apply.recentCompany = request.POST.get('recentCompany')
        apply.recentCity = request.POST.get('recentCity')
        apply.recentState = request.POST.get('recentState')
        apply.WhyTheyWantToJoin = request.POST.get('recentReasonForLeaving')
        apply.recentJobDescription = request.POST.get('recentJobDescription')
        apply.extraInfo = request.POST.get('extraInfo')

        # Collect applicant information
        years_experience = apply.years
        software_experience = apply.taxSoftware
        certifications = apply.certifications
        availability = apply.availability
        tax_knowledge = apply.taxKnowledge

        # Define job descriptions
        job_descriptions = [
            {
                "title": "Tax Preparer",
                "text": """
                Strong sales and marketing skills to attract new clients.
                In-depth knowledge of tax laws, regulations, and procedures.
                Ability to analyze financial data and identify potential tax deductions or credits.
                Strong organizational skills to manage multiple client accounts simultaneously.
                Excellent typing skills for efficient data entry.
                """
            },
            {
                "title": "Tax Accountant",
                "text": """
                CPA designation and/or advanced degree.
                Experience in life/health, property/casualty, and/or general corporate taxation.
                Possesses extensive tax knowledge to identify complex tax issues, research solutions, and develop appropriate recommendations.
                Self-motivated with strong critical-thinking skills and keen attention to detail.
                Able to work independently to guarantee the accurate and timely completion of tasks.
                """
            },
            {
                "title": "Tax Advisor",
                "text": """
                The minimum qualifications necessary to become a CPA Tax Advisor are a background in the filing of over 30 individual 1040 tax returns for both federal and state purposes for at least two years, utilizing commercial tax preparation software.
                An EA, CPA, or practicing attorney with an unrestricted certification and comprehensive tax preparation expertise plus advanced knowledge of tax regulations is required for a position at our organization.
                Profound dedication to guiding clients through the intricacies of taxation reflects your unwavering commitment to service excellence.
                """
            }
        ]

        # Combine all job descriptions into one text
        combined_job_description = " ".join([job['text'] for job in job_descriptions])

        # Compute similarity score
        match_score = compute_similarity(years_experience, software_experience, certifications, availability, tax_knowledge, combined_job_description)

        # Assign computed score to the overallScore field
        apply.overallScore = match_score

        # Save the application data
        apply.save()

        # If everything went well, redirect to the thank you page
        return render(request, 'thank_you.html')

    # Render the index.html page if it's a GET request
    return render(request, 'index.html')

def application(request):
    return render(request, 'app.html')

def applyHere(request):
    return render(request, 'work.html')

def AI(request):
    return render(request, 'AI.html')

def services(request):
    return render(request, 'services.html')