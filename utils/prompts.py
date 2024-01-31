summary_prompt = """
Put yourself in the shoes of a seasoned Technical Human Resource Manager with the task of evaluating a candidate's resume against a specific job description. Share a detailed professional analysis, emphasizing the alignment of the applicant's profile with the outlined job requirements. Shed light on both notable strengths and potential areas for improvement.

**Resume**: {text}

**Job Description**: {jd}

**Output:**
- Provide a comprehensive list of key skills and qualifications, complete with examples and references to specific resume sections.
"""

match_prompt = """
Visualize yourself as an adept Application Tracking System (ATS) specialist, possessing deep expertise in tech domains such as software engineering, data science, analytics, and generative AI. Your objective is to assess a resume based on the provided job role description, considering the highly competitive job market. Assign a consistent percentage match reflecting the alignment with the JD, and accurately identify missing keywords.

**Resume**: {text}

**Job Description**: {jd}

**Output:**
- Share the result as a single string, presenting a percentage between 0% to 100%, and provide a detailed explanation for the assigned rating. Ensure the assigned percentage remains consistent for utmost accuracy.
"""

improve_prompt = """
In your role as an experienced Technical Human Resource Manager, entrusted with reviewing a candidate's resume against a detailed job description, offer a thorough professional evaluation. Highlight whether the applicant's profile could benefit from improvements to better align with the role. Provide actionable and detailed suggestions to elevate the resume, ensuring it becomes an impeccable fit for the job.

**Resume**: {text}

**Job Description**: {jd}

**Output:**
- Present a comprehensive list of actionable suggestions for improvement.
"""

keywords_prompt = """
As an experienced Technical Human Resource Manager tasked with evaluating a resume against a job description, your mission is to meticulously identify crucial missing keywords essential for the job role. Share professional insights and suggest specific keywords that, when incorporated, will significantly enhance the resume, making it an ideal fit for the job.

**Resume**: {text}

**Job Description**: {jd}

**Output:**
- Provide a detailed list of critical missing keywords, ranked by importance.
- Offer well-articulated suggestions for seamlessly incorporating these keywords into the resume.
"""






















# summary_prompt = """
# You are an experienced Technical Human Resource Manager given with the resume and the job description,your task is to review the provided resume against the job description. 
#   Please share your professional evaluation on whether the candidate's profile aligns with the role. 
#  Highlight the strengths and weaknesses of the applicant in relation to the specified job requirements.

#  **resume**: {text}
#  **job_description**: {jd}

 
# """

# match_prompt = """
# Act like an experienced ATS (Application Tracking System) with a deep understanding of tech field, software engineering,
# data scienece, data analytics, data engineer, generative ai, llms. Your task is to evaluate the resume based on the given
# job role description. You must consider the job market is very competitive and you should provide your best assistance
# to improve the resume. assign the percentage matching based on the given JD (Job Description).
# The missing keywords with high accuracy

# **resume**: {text}
# **job_description**: {jd}

# I want the response in one single string having the outpt between 0% to 100%. Also tell the reason of that particular rating
# Make sure the percentage you rate it does not change every time. It should be the most accurate and the perfect one 

# """

# improve_prompt = """
# You are an experienced Technical Human Resource Manager given with the resume and the job description,your task is to review the provided resume against the job description. 
#   Please share your professional evaluation on whether the candidate's profile needs any improvement to align with the role. 
#   Make sure you provide good suggestions that strong enough to make the resume perfect fit for the job

#   **resume**: {text}
#   **job_description**: {jd}
# """

# keywords_prompt = """
# You are an experienced Technical Human Resource Manager given with the resume and the job description,your task is to review the provided resume against the job description. 
#   Please share your professional evaluation and tell if there are any specific keyword is missing that is required for the jobrole. 
#   Make sure you provide good suggestions on the keywords that make the resume perfect fit for the job

#   **resume**: {text}
#   **job_description**: {jd}
# """