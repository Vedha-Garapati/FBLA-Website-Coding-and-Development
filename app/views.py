import nltk
import random
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.metrics.pairwise import cosine_similarity

# Download NLTK data
nltk.download('punkt')
nltk.download('stopwords')

#Import statement allows django to render HTML pages
from django.shortcuts import render

#Import statement allows django to return a physical response in the HTML page
from django.http import HttpResponse

#Import statement allows this file to access the 'Application' class in which all the data types for the job application have been initialized.
from .models import Application

# Create your views here.
from app.functions import handle_uploaded_file  
#Primary method is commonly reffered to as the 'index' method and the 'request' parameter refers to where the method will be grabbing data from.
def main(request):
    return render(request,'index.html')
def index(request):
    #Runs a condition asking if the data was written by a user, or 'POST' data, run the following code beneath.
    if request.method=="POST":
        
        #Creates a constructor using the application class
        apply = Application()

        #Grabs the user input data from the input box that has the name of 'name' on it and stores it in this variable
        firstName=request.POST.get('firstName')

        #Stores the variable we initalized earlier in this code segement and stores it in the 'name' section of the Application dataset
        apply.firstName=firstName

        lastName=request.POST.get('lastName')

        apply.lastName=lastName

        position=request.POST.get('position')

        apply.position=position

        address=request.POST.get('address')

        apply.address=address

        city=request.POST.get('city')

        apply.city=city

        state=request.POST.get('state')

        apply.state=state

        zip=request.POST.get('zip')

        apply.zip=zip

        phone=request.POST.get('phone')

        apply.phone=phone

        email=request.POST.get('email')

        apply.email=email

        reference1Name=request.POST.get('reference1Name')

        apply.reference1Name=reference1Name

        reference1Relationship=request.POST.get('reference1Relationship')

        apply.reference1Relationship=reference1Relationship

        reference1Phone=request.POST.get('reference1Phone')

        apply.reference1Phone=reference1Phone

        reference2Name=request.POST.get('reference2Name')

        apply.reference2Name=reference2Name

        reference2Relationship=request.POST.get('reference2Relationship')

        apply.reference2Relationship=reference2Relationship

        reference2Phone=request.POST.get('reference2Phone')

        apply.reference2Phone=reference2Phone

        reasonForApplying=request.POST.get('reasonForApplying')

        apply.reasonForApplying=reasonForApplying

        years=request.POST.get('years')

        apply.years=years

        certifications=request.POST.get('certifications')

        apply.certifications=certifications

        availability=request.POST.get('availability')

        apply.availability=availability

        taxKnowledge=request.POST.get('taxKnowledge')

        apply.taxKnowledge=taxKnowledge

        taxSoftware=request.POST.get('taxSoftware')

        apply.taxSoftware=taxSoftware

        recentStartDate=request.POST.get('recentStartDate')

        apply.recentStartDate=recentStartDate

        recentEndDate=request.POST.get('recentEndDate')

        apply.recentEndDate=recentEndDate

        recentJobTitle=request.POST.get('recentJobTitle')

        apply.recentJobTitle=recentJobTitle

        recentCompany=request.POST.get('recentCompany')

        apply.recentCompany=recentCompany

        recentCity=request.POST.get('recentCity')

        apply.recentCity=recentCity

        recentState=request.POST.get('recentState')

        apply.recentState=recentState

        recentReasonForLeaving=request.POST.get('recentReasonForLeaving')

        apply.recentReasonForLeaving=recentReasonForLeaving

        recentJobDescription=request.POST.get('recentJobDescription')

        apply.recentJobDescription=recentJobDescription

        extraInfo=request.POST.get('extraInfo')

        apply.extraInfo=extraInfo

        overallScore=random.randrange(70,90,1)

        apply.overallScore=overallScore



        #Saves the current version of the application class in the admin database 
        apply.save()

        #If everything went well and all the data was saved, the program will take you to the thank you page
        return render(request, 'thank_you.html')
        

    #Will always keep this page operating whether or not the application data was grabbed successfully.
    return render(request, 'index.html')

def application(request):
    return render(request, 'app.html')

def applyHere(request):
    return render(request, 'work.html')

def AI(request):
    return render(request, 'AI.html')

def services(request):
    return render(request, 'services.html')


# def preprocess_text(text):
#     # Tokenize the text
#     tokens = word_tokenize(text.lower())
#     # Remove stop words and non-alphabetic tokens
#     filtered_tokens = [token for token in tokens if token.isalpha() and token not in stopwords.words('english')]
#     return ' '.join(filtered_tokens)

# def transform_similarity_score(score):
#     if score >= 0.6:
#         return 85 + int((score - 0.8) * 10)  # Scale the top scores around 85-90
#     elif score >= 0.35:
#         return 55 + int((score - 0.6) * 10)  # Scale mid scores around 55-60
#     else:
#         return 5 + int(score * 10)  # Scale low scores around 5-10

# def compute_similarity(applicant_info, combined_job_description):
#     # Preprocess the texts
#     applicant_processed = preprocess_text(applicant_info)
#     combined_job_description_processed = preprocess_text(combined_job_description)

#     # Combine texts for TF-IDF vectorization
#     documents = [applicant_processed, combined_job_description_processed]

#     # Create TF-IDF vectorizer
#     vectorizer = TfidfVectorizer()
#     tfidf_matrix = vectorizer.fit_transform(documents)

#     # Compute cosine similarity
#     similarity_matrix = cosine_similarity(tfidf_matrix)

#     # The similarity score is the value at index (0, 1)
#     similarity_score = similarity_matrix[0, 1]

#     # Transform the similarity score
#     transformed_score = transform_similarity_score(similarity_score)

#     return transformed_score

# def collect_applicant_info(years_experience, software_experience, certifications, availability, tax_knowledge):
#     info = f"""
#     Years of Tax Preparation Experience: {years_experience}
#     Tax Software Experience: {software_experience}
#     Tax Certifications: {certifications}
#     Availability during Tax Season: {availability}
#     Describe Your Tax Knowledge: {tax_knowledge}
#     """
#     return info

# # Define the job descriptions
# job_descriptions = [
#     {
#         "title": "Tax Preparer",
#         "text": """
#         Strong sales and marketing skills to attract new clients.
#         In-depth knowledge of tax laws, regulations, and procedures.
#         Ability to analyze financial data and identify potential tax deductions or credits.
#         Strong organizational skills to manage multiple client accounts simultaneously.
#         Excellent typing skills for efficient data entry.
#         """
#     },
#     {
#         "title": "Tax Accountant",
#         "text": """
#         CPA designation and/or advanced degree.
#         Experience in life/health, property/casualty, and/or general corporate taxation.
#         Possesses extensive tax knowledge to identify complex tax issues, research solutions, and develop appropriate recommendations.
#         Self-motivated with strong critical-thinking skills and keen attention to detail.
#         Able to work independently to guarantee the accurate and timely completion of tasks.
#         """
#     },
#     {
#         "title": "Tax Advisor",
#         "text": """
#         The minimum qualifications necessary to become a CPA Tax Advisor are a background in the filing of over 30 individual 1040 tax returns for both federal and state purposes for at least two years, utilizing commercial tax preparation software.
#         An EA, CPA, or practicing attorney with an unrestricted certification and comprehensive tax preparation expertise plus advanced knowledge of tax regulations is required for a position at our organization.
#         Profound dedication to guiding clients through the intricacies of taxation reflects your unwavering commitment to service excellence.
#         """
#     }
# ]

# # Combine all job descriptions into one text
# combined_job_description = " ".join([job['text'] for job in job_descriptions])

# # Example of an applicant
# years_experience = years
# software_experience = taxSoftware
# certifications = certifications
# availability = availability
# tax_knowledge = taxKnowledge

# applicant_info = collect_applicant_info(
#     years_experience,
#     software_experience,
#     certifications,
#     availability,
#     tax_knowledge
# )

# # Compute similarity score
# match_score = compute_similarity(applicant_info, combined_job_description)
# print(f"Match Score: {match_score:.2f}")

