import pandas as pd
import os

class LegalInfoRobot:
    def __init__(self):
        self.tax_slab_24_25 = {
            "3_to_7_lakh": 0.05,
            "7_to_10_lakh": 0.10,
            "10_to_12_lakh": 0.15,
            "12_to_15_lakh": 0.20,
            "above_15_lakh": 0.30
        }
        self.FAQS = pd.DataFrame({
            "Question": [
                "How can I file for divorce in India?",
                "What are my rights during an arrest in India?",
                "How to apply for a passport in India?",
                "What are the labor laws in India?",
                "How to draft a rental agreement in India?",
                "What is the legal drinking age in India?",
                "How to create a will in India?",
                "How to file a consumer complaint in India?",
                "What are the rules for property inheritance in India?",
                "How to register a trademark in India?",
                "What are the rights of tenants in India?",
                "How to apply for a voter ID card in India?",
                "What are the laws related to domestic violence in India?",
                "How to file for child custody in India?",
                "What are the rules for land acquisition in India?",
                "How to apply for a marriage certificate in India?",
                "What are the regulations for starting an online business in India?",
                "What are the rights of women in the workplace in India?",
                "How to claim insurance in case of a car accident in India?",
                "What are the legal requirements for starting a non-profit organization in India?",
                "How to apply for a patent in India?",
                "What are the regulations for online privacy in India?",
                "How to file a cybercrime complaint in India?",
                "What are the rules for adoption in India?",
                "How to start a small business in India?",
                "What are the legal rights of persons with disabilities in India?",
                "How to file a public interest litigation (PIL) in India?",
                "What are the legal requirements for marriage in India?",
                "How to protect intellectual property in India?",
                "How to apply for a trade license in India?"
            ],
            "Answer": [
                "To file for divorce in India, follow legal procedures under personal laws like the Hindu Marriage Act or Special Marriage Act.",
                "During an arrest in India, you have the right to remain silent and the right to legal representation. The police must inform you of the reasons for the arrest.",
                "To apply for a passport in India, visit the official Passport Seva website, fill out the application form, and schedule an appointment at a Passport Seva Kendra.",
                "Labor laws in India cover aspects like wages, working conditions, and employment contracts. Key laws include the Minimum Wages Act and Industrial Disputes Act.",
                "To draft a rental agreement, include the names of the parties, property details, lease term, rent amount, and any additional terms.",
                "The legal drinking age in India varies by state and union territory. It typically ranges from 18 to 25 years. Check the specific regulations in your location.",
                "To create a will in India, list your assets, appoint an executor, and clearly state the beneficiaries. Sign the will in the presence of witnesses. It's advisable to consult a lawyer to ensure it's legally valid.",
                "To file a consumer complaint in India, approach the district consumer forum or state/national consumer dispute redressal commission. Provide details of the grievance and supporting documents.",
                "In India, property inheritance laws vary based on religion and personal laws. Consult a legal expert to understand your specific rights and obligations concerning property inheritance.",
                "To register a trademark in India, file an application with the Trademarks Registry. Conduct a trademark search, provide necessary documents, and follow the registration process.",
                "Tenants in India have rights regarding rent control, eviction, and property maintenance. Understanding local rent laws and having a rental agreement is essential.",
                "To apply for a Voter ID card in India, visit the Electoral Registration Officer in your constituency or apply online through the National Voter's Service Portal (NVSP). Provide proof of identity and address.",
                "Domestic violence laws in India are covered under the Protection of Women from Domestic Violence Act. Victims can seek protection orders, residence orders, and maintenance.",
                "Child custody matters in India are governed by personal laws. Courts consider the child's welfare as the primary concern. Consult a family lawyer for guidance.",
                "Land acquisition in India is governed by the Land Acquisition Act. The government must follow specific procedures and compensate landowners fairly when acquiring land for public projects.",
                "To apply for a marriage certificate in India, visit the local municipal office or panchayat. Provide the required documents, including proof of marriage, and complete the formalities.",
                "Starting an online business in India involves compliance with e-commerce laws, taxation, and data protection regulations. Consult legal experts to ensure compliance.",
                "Women in the workplace in India have rights related to equal pay, sexual harassment prevention, and maternity benefits. Employers must adhere to these laws.",
                "In case of a car accident in India, inform the insurance company immediately and file a claim. Provide the necessary accident details and documents for a smooth claims process.",
                "To start a non-profit organization in India, you need to register it under the appropriate legal framework, such as the Societies Registration Act or the Companies Act. Consult with a legal expert for guidance.",
                "To apply for a patent in India, you should file a patent application with the Indian Patent Office. The application should include a detailed description of your invention. Consult with a patent attorney for assistance.",
                "Online privacy in India is governed by the Information Technology Act and the Personal Data Protection Bill. These laws regulate data protection and privacy issues online. Ensure compliance with these regulations if you operate a website or app.",
                "To file a cybercrime complaint in India, contact your local cybercrime cell or police station. Provide all necessary details and evidence of the cybercrime. Consult with a cybercrime lawyer if needed.",
                "Adoption in India is governed by the Juvenile Justice (Care and Protection of Children) Act, 2015. Prospective adoptive parents need to follow the legal adoption process through recognized agencies or authorities.",
                "Starting a small business in India involves registering your business, obtaining necessary licenses, and complying with taxation and regulatory requirements. Consult with a business lawyer or a chartered accountant for guidance.",
                "Persons with disabilities in India have legal rights protected by the Rights of Persons with Disabilities Act, 2016. These rights include accessibility, reservation in education and employment, and more.",
                "To file a public interest litigation (PIL) in India, approach the High Court or the Supreme Court. A PIL can be filed to address issues of public concern. Consult with a PIL lawyer for assistance.",
                "Legal requirements for marriage in India include age restrictions, registration, and compliance with personal laws. Different religions and regions may have specific marriage rules. Consult with a marriage lawyer for guidance.",
                "To protect intellectual property in India, you can register trademarks, copyrights, patents, and designs. Intellectual property laws provide legal protection for your creations. Consult with an intellectual property attorney for advice.",
                "To apply for a trade license in India, contact the local municipal corporation or the relevant government authority. Follow the prescribed application process and fulfill the necessary requirements for obtaining a trade license."
            ]
        })
                
        self.legal_rights = pd.DataFrame({
            "Right": [
                "Right to Freedom from Discrimination Based on Sexual Orientation in Employment",
                "Right to Adequate Nutrition",
                "Right to Clean Water and Sanitation",
                "Right to Freedom from Discrimination Based on Gender in Education",
                "Right to Privacy of Personal Finances",
                "Right to Participate in Cultural and Artistic Activities",
                "Right to Freedom from Forced Labor",
                "Right to Adequate Childcare Services",
                "Right to Freedom from Torture and Inhumane Treatment",
                "Right to Access to Public Records",
                "Right to Freedom from Discrimination Based on Genetic Information in Healthcare",
                "Right to Freedom of the Press",
                "Right to Adequate Mental Health Care",
                "Right to Freedom from Discrimination Based on Gender Identity in Housing",
                "Right to Access to Affordable Prescription Medications",
                "Right to Freedom from Discrimination Based on Citizenship Status",
                "Right to Adequate Child Protection Services",
                "Right to Freedom from Discrimination Based on Education Status",
                "Right to Freedom of Conscience and Belief",
                "Right to Adequate Legal Aid for Immigrants",
                "Right to Freedom from Discrimination Based on Economic Activities",
                "Right to Adequate Rehabilitation for Persons with Disabilities",
                "Right to Freedom from Discrimination Based on Political Affiliation",
                "Right to Access to Family Planning Services",
                "Right to Freedom from Discrimination Based on Maternity or Pregnancy",
                "Right to Adequate Refugee Protection",
                "Right to Freedom from Discrimination Based on Trade Union Membership",
                "Right to Accessible Public Parks and Recreation Areas",
                "Right to Freedom from Discrimination Based on Immigration Status in Employment",
                "Right to Adequate Cultural Heritage Preservation",
                "Right to Freedom from Discrimination Based on Disability in Education",
                "Right to Access to Mental Health Counseling Services",
                "Right to Freedom from Discrimination Based on Language in Education",
                "Right to Adequate Support for Orphans and Vulnerable Children",
                "Right to Freedom from Discrimination Based on Parental or Caregiver Status in Employment",
                "Right to Access to Clean Energy Sources",
                "Right to Freedom from Discrimination Based on Refugee Status in Housing",
                "Right to Adequate Protection for Whistleblowers",
                "Right to Freedom from Discrimination Based on Sexual Orientation in Housing",
                "Right to Access to Reproductive Health Information",
                "Right to Freedom from Discrimination Based on Socioeconomic Status in Healthcare",
                "Right to Adequate Training and Education for Workers",
                "Right to Freedom from Discrimination Based on Genetic Information in Employment",
                "Right to Access to Legal Aid for Victims of Domestic Violence",
                "Right to Freedom from Discrimination Based on Disability in Housing",
                "Right to Adequate Environmental Conservation and Protection",
                "Right to Freedom from Discrimination Based on Gender Identity in Employment",
                "Right to Access to Affordable Healthcare for Low-Income Individuals",
                "Right to Education",
                "Right to Information",
                "Right to Legal Aid",
                "Right to a Fair Trial",
                "Right to Privacy",
                "Right to Freedom of Speech",
                "Right to Equality",
                "Right to Work",
                "Right to Health",
                "Right to Housing",
                "Right to a Clean Environment",
                "Right to Marriage and Family",
                "Right to Freedom of Religion",
                "Right to Adequate Food",
                "Right to Freedom of Assembly",
                "Right to Participate in Government",
                "Right to Cultural Life",
                "Right to Adequate Standard of Living",
                "Right to Social Security",
                "Right to Non-Discrimination",
                "Right to Indigenous Peoples",
                "Right to Access to Justice",
                "Right to Privacy of Communication",
                "Right to Education for Persons with Disabilities",
                "Right to a Nationality",
                "Right to Adequate Clothing and Shelter",
                "Right to Access to the Internet",
                "Right to Equal Access to Technology",
                "Right to Freedom from Discrimination Based on Sexual Orientation and Gender Identity",
                "Right to Freedom of Thought and Expression on the Internet",
                "Right to Fair and Transparent Digital Data Practices",
                "Right to Freedom from Genetic Discrimination",
                "Right to Dignified End-of-Life Care",
                "Right to Equal Access to Online Education",
                "Right to Accessible Public Transportation",
                "Right to Freedom from Forced or Coerced Medical Procedures",
                "Right to Protection from Cyberbullying and Online Harassment",
                "Right to Freedom from Age Discrimination",
                "Right to Freedom from Discrimination Based on Disability in the Workplace",
                "Right to Rest and Leisure",
                "Right to Freedom from Human Trafficking",
                "Right to Accessible and Inclusive Public Spaces",
                "Right to Freedom from Gender-Based Violence",
                "Right to Adequate Medical Care and Treatment in Detention",
                "Right to Digital Privacy",
                "Right to Freedom from Racial Discrimination",
                "Right to Access to Affordable Housing for the Homeless",
                "Right to Freedom of Movement for Internally Displaced Persons",
                "Right to Freedom from Discrimination Based on HIV/AIDS Status",
                "Right to Freedom from Discrimination Based on Nationality",
                "Right to Freedom of Sexual Orientation and Gender Identity Expression",
                "Right to Freedom from Discrimination in Access to Goods and Services",
                "Right to Freedom from Discrimination Based on Religion or Belief",
                "Right to Cultural Diversity and Heritage",
                "Right to Freedom from Discrimination in Adoption and Fostering",
                "Right to Freedom from Discrimination Based on Language",
                "Right to Freedom from Discrimination Based on Social and Economic Status",
                "Right to Freedom of Movement for Refugees",
                "Right to Freedom from Discrimination Based on Political Opinion",
                "Right to Access to Comprehensive Sexual and Reproductive Health Education",
                "Right to Freedom from Discrimination Based on Marital Status",
                "Right to Accessible Transportation for Persons with Disabilities",
                "Right to Freedom from Discrimination Based on Socioeconomic Class",
                "Right to Freedom from Discrimination in Adoption and Fostering for LGBTQ+ Individuals",
                "Right to Freedom from Discrimination Based on Parental Status",
                "Right to Freedom from Discrimination Based on Residence or Domicile",
                "Right to Freedom from Discrimination Based on Criminal Record",
                "Right to Accessible and Inclusive Tourism",
                "Right to Freedom from Discrimination Based on Health Status",
                "Right to Accessible Information for Persons with Disabilities",
                "Right to Freedom from Discrimination Based on Refugee Status",
                "Right to Freedom from Discrimination Based on Age in Employment",
                "Right to Accessible and Inclusive Voting and Elections",
                "Right to Freedom from Discrimination Based on Military or Veteran Status",
                "Right to Accessible Information and Communication Technology for Persons with Disabilities"
            ],
            "Description": [
                "You have the right to be free from discrimination based on sexual orientation in employment.",
                "You have the right to adequate nutrition and a balanced diet.",
                "You have the right to access clean and safe drinking water and sanitation facilities.",
                "You have the right to be free from discrimination based on gender in education.",
                "You have the right to privacy of your personal financial information.",
                "You have the right to participate in cultural and artistic activities.",
                "You have the right to be free from forced or compulsory labor.",
                "You have the right to access adequate childcare services.",
                "You have the right to be free from torture and inhumane or degrading treatment or punishment.",
                "You have the right to access public records and government documents.",
                "You have the right to be free from discrimination based on genetic information in healthcare.",
                "You have the right to freedom of the press and media.",
                "You have the right to access adequate mental health care and treatment.",
                "You have the right to be free from discrimination based on gender identity in housing.",
                "You have the right to access affordable prescription medications.",
                "You have the right to be free from discrimination based on citizenship or immigration status.",
                "Children have the right to adequate protection from abuse, exploitation, and neglect.",
                "You have the right to be free from discrimination based on your educational status.",
                "You have the right to freedom of conscience and belief.",
                "Immigrants have the right to adequate legal aid and representation.",
                "You have the right to be free from discrimination based on your economic activities or profession.",
                "Persons with disabilities have the right to adequate rehabilitation services.",
                "You have the right to be free from discrimination based on your political affiliation.",
                "You have the right to access family planning and reproductive health services.",
                "You have the right to be free from discrimination based on maternity or pregnancy.",
                "Refugees have the right to adequate protection, including asylum and safe refuge.",
                "You have the right to be free from discrimination based on trade union membership.",
                "You have the right to access public parks and recreation areas that are accessible to all.",
                "You have the right to be free from discrimination based on immigration status in employment.",
                "You have the right to the preservation of your cultural heritage and historical sites.",
                "You have the right to be free from discrimination based on disability in education.",
                "You have the right to access mental health counseling and support services.",
                "You have the right to be free from discrimination based on language in education.",
                "Orphans and vulnerable children have the right to adequate support and care.",
                "You have the right to be free from discrimination based on parental or caregiver status in employment.",
                "You have the right to access clean and sustainable energy sources.",
                "You have the right to be free from discrimination based on refugee status in housing.",
                "Whistleblowers have the right to adequate protection and legal safeguards.",
                "You have the right to be free from discrimination based on sexual orientation in housing.",
                "You have the right to access information on reproductive health and family planning.",
                "You have the right to be free from discrimination based on socioeconomic status in healthcare.",
                "Workers have the right to adequate training and education to improve their skills.",
                "You have the right to be free from discrimination based on genetic information in employment.",
                "Victims of domestic violence have the right to access legal aid and support.",
                "You have the right to be free from discrimination based on disability in housing.",
                "You have the right to adequate environmental conservation and protection measures.",
                "You have the right to be free from discrimination based on gender identity in employment.",
                "Low-income individuals have the right to access affordable healthcare services.",
                "Every child has the right to free and compulsory education up to the age of 14.",
                "You have the right to access information held by public authorities.",
                "If you cannot afford legal representation, you have the right to free legal aid.",
                "You have the right to a fair and public trial within a reasonable time by an impartial tribunal.",
                "You have the right to privacy and protection of personal data.",
                "You have the right to freedom of speech and expression.",
                "All persons are equal before the law and are entitled to equal protection of the law.",
                "You have the right to work in a safe and healthy environment with fair wages.",
                "You have the right to the enjoyment of the highest attainable standard of physical and mental health.",
                "You have the right to adequate housing and protection against homelessness.",
                "You have the right to live in a clean and healthy environment.",
                "You have the right to marry and found a family without any discrimination.",
                "You have the right to freedom of thought, conscience, and religion.",
                "You have the right to adequate food and clean drinking water.",
                "You have the right to freedom of peaceful assembly and association.",
                "You have the right to take part in the government of your country.",
                "You have the right to take part in cultural, artistic, and scientific activities.",
                "You have the right to an adequate standard of living for yourself and your family.",
                "You have the right to social security and protection in times of need.",
                "You have the right to be free from discrimination based on race, color, sex, religion, and more.",
                "Indigenous peoples have the right to maintain and strengthen their distinct cultural identities.",
                "You have the right to access to justice and a fair legal process.",
                "You have the right to privacy of your communications, including mail, telephone, and electronic communications.",
                "Persons with disabilities have the right to inclusive education and reasonable accommodations.",
                "You have the right to a nationality and not to be arbitrarily deprived of your nationality.",
                "You have the right to adequate clothing and shelter as part of your right to an adequate standard of living.",
                "You have the right to access and use the internet as a means of exercising your rights to information and freedom of expression.",
                "You have the right to equal access to and benefit from advancements in technology.",
                "You have the right to be free from discrimination based on sexual orientation and gender identity.",
                "You have the right to freedom of thought and expression on the internet.",
                "You have the right to fair and transparent practices concerning your personal digital data.",
                "You have the right to be free from discrimination based on your genetic information.",
                "You have the right to receive dignified end-of-life care and the right to make decisions about your medical treatment.",
                "You have the right to equal access to online education and digital learning resources.",
                "You have the right to accessible and affordable public transportation.",
                "You have the right to be free from forced or coerced medical procedures or treatments.",
                "You have the right to protection from cyberbullying and online harassment.",
                "You have the right to be free from age discrimination.",
                "You have the right to be free from discrimination based on disability in the workplace.",
                "You have the right to rest and leisure, including reasonable working hours and periodic holidays with pay.",
                "You have the right to be free from human trafficking and modern forms of slavery.",
                "You have the right to access public spaces that are accessible and inclusive for all individuals, including those with disabilities.",
                "You have the right to be free from gender-based violence and abuse.",
                "You have the right to adequate medical care and treatment if you are in detention or incarcerated.",
                "You have the right to privacy and protection of your digital communications and data.",
                "You have the right to be free from discrimination based on race or ethnicity.",
                "You have the right to access affordable housing and support services if you are homeless.",
                "Internally displaced persons have the right to freedom of movement and the right to return to their homes.",
                "You have the right to be free from discrimination based on HIV/AIDS status.",
                "You have the right to be free from discrimination based on nationality.",
                "You have the right to freely express your sexual orientation and gender identity.",
                "You have the right to be free from discrimination in access to goods and services.",
                "You have the right to be free from discrimination based on religion or belief.",
                "You have the right to respect and protect your cultural diversity and heritage.",
                "You have the right to be free from discrimination in adoption and fostering based on various factors.",
                "You have the right to be free from discrimination based on language.",
                "You have the right to be free from discrimination based on social and economic status.",
                "Refugees have the right to freedom of movement and the right to seek asylum in other countries.",
                "You have the right to be free from discrimination based on your political opinion.",
                "You have the right to access comprehensive sexual and reproductive health education.",
                "You have the right to be free from discrimination based on marital status.",
                "Persons with disabilities have the right to accessible transportation.",
                "You have the right to be free from discrimination based on socioeconomic class.",
                "LGBTQ+ individuals have the right to be free from discrimination in adoption and fostering.",
                "You have the right to be free from discrimination based on parental status.",
                "You have the right to be free from discrimination based on your residence or domicile.",
                "You have the right to be free from discrimination based on your criminal record.",
                "You have the right to accessible and inclusive tourism and travel.",
                "You have the right to be free from discrimination based on your health status.",
                "Persons with disabilities have the right to accessible information.",
                "You have the right to be free from discrimination based on your refugee status.",
                "You have the right to be free from discrimination based on age in employment.",
                "You have the right to accessible and inclusive voting and elections.",
                "You have the right to be free from discrimination based on military or veteran status.",
                "Persons with disabilities have the right to accessible information and communication technology."
            ]
        })
        
        self.legal_glossary = pd.DataFrame({
            "Term": [
                "Arbitration",
                "Defendant",
                "Plaintiff",
                "Jurisdiction",
                "Evidence",
                "Criminal Law",
                "Affidavit",
                "Breach of Contract",
                "Civil Law",
                "Contractual Obligation",
                "Damages",
                "Due Diligence",
                "Injunction",
                "Mediation",
                "Precedent",
                "Settlement",
                "Tort",
                "Writ"
            ],
            "Definition": [
                "A method of dispute resolution where a neutral third party (an arbitrator) makes a binding decision.",
                "The party in a legal case who is accused of wrongdoing and defends against the allegations.",
                "The party in a legal case who initiates the lawsuit by filing a complaint against the defendant.",
                "The authority of a court to hear and decide legal cases within a specific geographic area or over certain types of cases.",
                "Information, documents, or materials presented in court to prove or disprove facts in a legal case.",
                "A branch of law that deals with offenses against society, and the government prosecutes individuals accused of crimes.",
                "A written statement made under oath, usually used in court as evidence.",
                "Failure to fulfill the terms of a contract, leading to a legal dispute.",
                "A branch of law dealing with disputes between individuals or organizations, as opposed to criminal law.",
                "The legal duties and responsibilities agreed upon in a contract.",
                "Compensation awarded to a party for loss or harm caused by a breach of contract or legal wrong.",
                "The process of thoroughly investigating and evaluating a business or legal situation before proceeding with a transaction or agreement.",
                "A court order requiring a person to do or refrain from doing a particular act.",
                "A form of alternative dispute resolution where a neutral third party helps parties reach a mutually acceptable agreement.",
                "A legal principle established in previous court decisions that guides judges in deciding future cases.",
                "An agreement reached between parties to resolve a dispute without going to trial.",
                "A civil wrong that causes harm or loss to another person, leading to a legal claim for damages.",
                "A written order issued by a court requiring a person to do or refrain from doing a specific action."
            ]
        })

    def display_legal_document_templates(self):
        print("\nLegal Document Templates:")
        templates = ["Contract", "Will", "Power of Attorney", "Lease Agreement", "Non-Disclosure Agreement", "Employment Agreement"]
        for i, template in enumerate(templates, 1):
            print(f"{i}. {template} Template")

        while True:
            template_choice = input("Enter the number of the template you want to access (0 to go back): ").strip()
            if template_choice == '0':
                break
            elif template_choice in map(str, range(1, len(templates) + 1)):
                method_name = f"display_{templates[int(template_choice) - 1].lower().replace(' ', '_')}_template"
                getattr(self, method_name, lambda: print("Invalid choice."))()
            else:
                print("Invalid choice. Please select a valid template.")

    def start_assistant(self):
        print("Welcome to the Legal Information Robot!")
        print("Please provide some information about yourself to get started.")
        self.disply_services()
        
    def disply_services(self):
        print("\nSelect the type of service you need:")
        print("1. Get Information About a legal Right")
        print("2. Legal FAQs")
        print("3. Get information about a Legal Advocate")
        print("4. Store a Document")
        print("5. Retrieve a Document")
        print("6. Income tax calculator")
        print("7. Legal Glossary")
        print("8. Legal Chatbot")
        print("9. Legal Compliance Checklist")
        print("10. Legal Hotline")
        print("11. Generate Legal Document")
        print("0. Go back")
        
        choice = input("Please select a command (1/2/3/4/5/6/7/8/9/10/11/0): ").strip()

        if choice == "1":
            self.display_legal_right()
        elif choice == "2":
            self.display_legal_faqs()
        elif choice == "3":
            self.get_legal_advocate_contact()
        elif choice == "4":
            self.store_document()
        elif choice == "5":
            self.retrieve_document()
        elif choice == "6":
            self.income_tax_calculator()
        elif choice == "7":
            self.display_legal_glossary()
        elif choice == "8":
            self.launch_legal_chatbot()
        elif choice == "9":
            self.legal_compliance_checklist()
        elif choice == "10":
            self.display_legal_hotlines()
        elif choice == "11":
            self.generate_legal_document()
        elif choice == "0":
            print("Thank you for using the Legal Information Robot. Goodbye!")
        else:
            print("Invalid command. Please select a valid option.")

    def get_legal_advocate_contact(self):
        print("\nSelect the type of advocate you need contact information for:")
        print("1. Intellectual Property Lawyer")
        print("2. Public Interest Lawyer")
        print("3. Tax Lawyer")
        print("4. Corporate Lawyers")
        print("5. Immigration Lawyers")
        print("6. Criminal Lawyer")
        print("7. Civil Rights Lawyer")
        print("8. Family Lawyer")
        print("0. Go back")

        choice = input("Enter the number of the type of advocate (0 to go back): ").strip()

        if choice == '0':
            return
        elif choice == '1':
            self.display_advocate_contact("Intellectual Property Lawyer", "IP Lawyer's Name", "+123-456-7890", "ip.lawyer@example.com")
        elif choice == '2':
            self.display_advocate_contact("Public Interest Lawyer", "Public Interest Lawyer's Name", "+123-456-7890", "public.interest@example.com")
        elif choice == '3':
            self.display_advocate_contact("Tax Lawyer", "Tax Lawyer's Name", "+123-456-7890", "tax.lawyer@example.com")
        elif choice == '4':
            self.display_advocate_contact("Corporate Lawyers", "Corporate Lawyer's Name", "+123-456-7890", "corporate.lawyer@example.com")
        elif choice == '5':
            self.display_advocate_contact("Immigration Lawyers", "Immigration Lawyer's Name", "+123-456-7890", "immigration.lawyer@example.com")
        elif choice == '6':
            self.display_advocate_contact("Criminal Lawyer", "Criminal Lawyer's Name", "+123-456-7890", "criminal.lawyer@example.com")
        elif choice == '7':
            self.display_advocate_contact("Civil Rights Lawyer", "Civil Rights Lawyer's Name", "+123-456-7890", "civil.rights.lawyer@example.com")
        elif choice == '8':
            self.display_advocate_contact("Family Lawyer", "Family Lawyer's Name", "+123-456-7890", "family.lawyer@example.com")
        else:
            print("Invalid choice. Please select a valid option.")

    def display_advocate_contact(self, advocate_type, name, phone, email):
        print(f"\n{advocate_type} Contact Information:")
        print(f"Name: {name}")
        print(f"Phone: {phone}")
        print(f"Email: {email}")


    def store_document(self):
        user_folder = f"{self.user_info['name'].replace(' ', '_')}_documents"
        if not os.path.exists(user_folder):
            os.mkdir(user_folder)

        document_name = input("Enter the name of the document: ")
        document_content = input("Enter the document content: ")

        file_path = os.path.join(user_folder, document_name)
        with open(file_path, 'w') as file:
            file.write(document_content)

        print(f"Document '{document_name}' has been saved successfully.")

    def retrieve_document(self):
        user_folder = f"{self.user_info['name'].replace(' ', '_')}_documents"
        if os.path.exists(user_folder):
            document_name = input("Enter the name of the document you want to retrieve: ")
            file_path = os.path.join(user_folder, document_name)

            if os.path.exists(file_path):
                with open(file_path, 'r') as file:
                    document_content = file.read()
                print(f"Document Content:\n{document_content}")
            else:
                print(f"Document '{document_name}' not found.")
        else:
            print("No documents found for this user.")



    def display_legal_hotlines(self):
        hotlines = pd.DataFrame({
            "Service": [
                "Legal Aid India Hotline",
                "National Human Rights Commission (NHRC) Helpline",
                "Women Helpline",
                "Child Helpline",
                "Anti-Corruption Helpline",
                "Consumer Helpline",
                "Domestic Violence Helpline",
                "Disability Rights Helpline",
                "National Legal Services Authority (NALSA) Helpline",
                "Labor Helpline",
                "Right to Information (RTI) Helpline",
                "Prisoner Rights Helpline",
                "Environmental Law Helpline",
                "Legal Awareness Helpline",
                "Human Trafficking Helpline"
            ],
            "Contact Number": [
                "1800-233-3330",
                "91-11-23385368",
                "181",
                "1098",
                "1860-233-3330",
                "1800-11-4000",
                "1800-180-8181",
                "1800-11-1212",
                "91-11-23384686",
                "1800-200-1577",
                "1800-110-440",
                "1800-233-7007",
                "1800-3000-4444",
                "1800-11-8222",
                "91-11-23388340"
            ]
        })
        print("\nLegal Hotlines for India:")
        print(hotlines.to_string(index=False))


    def display_legal_right(self):
        print("\nAvailable Legal Rights:")
        for idx, legal_right in enumerate(self.legal_rights['Right'], start=1):
            print(f"{idx}. {legal_right}")

        try:
            choice = int(input("Enter the number of the legal right you want information about (0 to go back): "))
            if 0 < choice <= len(self.legal_rights):
                legal_right = self.legal_rights.iloc[choice - 1]
                print(f"\n{legal_right['Right']}: {legal_right['Description']}\n")
            elif choice == 0:
                return
            else:
                print("Invalid choice. Please select a valid legal right.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    def display_legal_faqs(self):
        print("\nLegal FAQs:")
        print(self.FAQS.to_string(index=False))

    def display_legal_glossary(self):
        print("\nLegal Glossary:")
        print(self.legal_glossary.to_string(index=False))

    def generate_legal_document(self):
        print("\nLegal Document Generator:")
        print("Available Options:")
        print("1. Generate Contract")
        print("2. Generate Will")
        print("3. Generate Power of Attorney")
        print("4. Generate Lease Agreement")
        print("5. Generate Non-Disclosure Agreement")
        print("6. Generate Employment Agreement")

        while True:
            option = input("Enter the number of the option you want (0 to go back): ").strip()
            if option == '0':
                break
            elif option == '1':
                self.generate_contract()
            elif option == '2':
                self.generate_will()
            elif option == '3':
                self.generate_power_of_attorney()
            elif option == '4':
                self.generate_lease_agreement()
            elif option == '5':
                self.generate_non_disclosure_agreement()
            elif option == '6':
                self.generate_employment_agreement()
            else:
                print("Invalid choice. Please select a valid option.")

    def view_legal_glossary(self):
        print("\nLegal Glossary:")
        for index, row in self.legal_glossary.iterrows():
            print(f"{row['Term']}: {row['Definition']}")


    def legal_compliance_checklist(self):
        checklist= [
            "1. Review and understand local and national laws relevant to your situation.",
            "2. Ensure that all necessary licenses and permits are obtained.",
            "3. Maintain proper records and documentation for all business operations.",
            "4. Comply with labor laws, including employee rights and safety regulations.",
            "5. Adhere to tax regulations and file taxes timely.",
            "6. Follow environmental regulations and obtain necessary environmental clearances.",
            "7. Implement data protection measures and comply with privacy laws.",
            "8. Ensure compliance with consumer protection laws and regulations.",
            "9. Review and update contracts and agreements regularly.",
            "10. Establish procedures for handling and reporting legal disputes and claims.",
            "11. Adhere to intellectual property laws, including trademarks and copyrights.",
            "12. Implement anti-corruption and anti-bribery measures.",
            "13. Ensure compliance with health and safety standards.",
            "14. Regularly review and update company policies to ensure legal compliance.",
            "15. Stay informed about changes in laws and regulations that may affect your operations.",
            "16. Ensure that your business practices comply with industry-specific regulations.",
            "17. Conduct periodic internal audits to assess compliance with legal requirements.",
            "18. Develop and implement a compliance training program for employees.",
            "19. Consult with legal professionals for advice on complex legal matters.",
            "20. Establish a mechanism for whistleblowing and handling ethical concerns."
        ]
        print("\nLegal Compliance Checklist:")
        for item in checklist:
            print(item)

    def generate_contract(self):
        print("\nGenerating Contract:")
        
        party_a_name = input("Enter the name of Party A: ")
        party_a_address = input("Enter the address of Party A: ")
        party_b_name = input("Enter the name of Party B: ")
        party_b_address = input("Enter the address of Party B: ")
        purpose = input("Enter the purpose of the contract: ")
        payment_terms = input("Enter the payment terms: ")
        duration = input("Enter the contract duration: ")

        contract_text = f"This contract is entered into on [Date] in [City], India, between:\n"
        contract_text += f"Party A:\nName: {party_a_name}\nAddress: {party_a_address}\n\n"
        contract_text += f"Party B:\nName: {party_b_name}\nAddress: {party_b_address}\n\n"
        contract_text += f"1. Purpose of Contract:\nThis contract is for {purpose}.\n\n"
        contract_text += f"2. Terms and Conditions:\n2.1 Payment: {payment_terms}\n2.2 Duration: {duration}\n\n"
        contract_text += "3. Governing Law:\nThis contract shall be governed by and construed in accordance with the laws of India.\n\n"
        contract_text += "4. Dispute Resolution:\nAny disputes arising from or related to this contract shall be resolved through arbitration in accordance with the Arbitration and Conciliation Act, 1996, or through litigation in [Specify City or State] courts.\n\n"
        contract_text += "5. Confidentiality:\nBoth parties agree to keep confidential any proprietary or sensitive information disclosed during the course of this contract.\n\n"
        contract_text += "[Include signature lines for both parties]"


    def generate_will(self):
        print("\nGenerating Will:")
        
        testator_name = input("Enter the name of the testator: ")
        testator_address = input("Enter the address of the testator: ")
        executor_name = input("Enter the name of the executor: ")
        executor_address = input("Enter the address of the executor: ")
        bequest = input("Enter the description of the bequest: ")

        will_text = f"Last Will and Testament of {testator_name}\n\n"
        will_text += f"I, {testator_name}, residing in [City], India, being of sound mind, do hereby declare this to be my last will and testament.\n\n"
        will_text += f"1. Appointment of Executor:\nI appoint {executor_name} as the executor of this will to manage my estate and distribute my assets in accordance with my wishes.\n\n"
        will_text += f"2. Bequests:\nI bequeath the following assets to the respective beneficiaries:\n"
        will_text += f"2.1 To [Beneficiary's Name]: {bequest}\n"
        will_text += "[Add more bequests as needed]\n\n"
        will_text += "3. Debts and Taxes:\nI direct that all my debts, funeral expenses, and taxes be paid from my estate.\n\n"
        will_text += "4. Residuary Estate:\nI give the rest, residue, and remainder of my estate to [Residuary Beneficiary's Name], if living. If not, to [Alternate Beneficiary's Name].\n\n"
        will_text += "5. Revocation of Prior Wills:\nI hereby revoke all wills and codicils previously made by me.\n\n"
        will_text += "6. Governing Law:\nThis will shall be governed by and construed in accordance with the laws of India.\n\n"
        will_text += "[Include your signature and witnesses' signatures]"

    def generate_power_of_attorney(self):
        print("\nGenerating Power of Attorney:")
        
        grantor_name = input("Enter the name of the grantor: ")
        attorney_name = input("Enter the name of the attorney-in-fact: ")
        attorney_authority = input("Enter the specific authorities granted to the attorney: ")

        power_of_attorney_text = f"I, {grantor_name}, residing in [City], India, hereby appoint {attorney_name} as my attorney-in-fact to act on my behalf in the following matters:\n"
        power_of_attorney_text += f"1. To manage and transact all my financial affairs, including banking, investments, and real estate.\n"
        power_of_attorney_text += f"2. To make decisions related to my healthcare, medical treatment, and consent to medical procedures.\n"
        power_of_attorney_text += f"3. To handle legal and administrative matters, including signing documents and representing me in legal proceedings.\n"
        power_of_attorney_text += "This power of attorney is effective as of [Effective Date] and shall remain in effect unless revoked by me in writing.\n"
        power_of_attorney_text += "I affirm that I am of sound mind and under no duress or undue influence while granting this power of attorney.\n"
        power_of_attorney_text += "[Include your signature]"


    def generate_lease_agreement(self):
        print("\nGenerating Lease Agreement:")
        
        landlord_name = input("Enter the name of the landlord: ")
        tenant_name = input("Enter the name of the tenant: ")
        property_address = input("Enter the address of the property: ")
        rent_amount = input("Enter the monthly rent amount: ")
        lease_term = input("Enter the lease term (in months): ")
        security_deposit = input("Enter the security deposit amount: ")

        lease_agreement_text = f"This Lease Agreement (the 'Agreement') is entered into on [Date], between the landlord, {landlord_name}, and the tenant, {tenant_name}, for the property located at {property_address}.\n"
        lease_agreement_text += f"1. Term of Lease:\nThis lease shall commence on [Commencement Date] and continue for a period of {lease_term} months.\n"
        lease_agreement_text += f"2. Rent:\nThe monthly rent for the property is {rent_amount}, payable on or before the [Rent Due Date] of each month.\n"
        lease_agreement_text += f"3. Security Deposit:\nThe tenant shall provide a security deposit of {security_deposit} to the landlord.\n"
        lease_agreement_text += f"4. Maintenance and Repairs:\nThe landlord shall be responsible for [Specify Landlord's Responsibilities], and the tenant shall be responsible for [Specify Tenant's Responsibilities].\n"
        lease_agreement_text += f"5. Termination:\nEither party may terminate this lease by providing [Notice Period] written notice to the other party.\n"
        lease_agreement_text += "6. Governing Law:\nThis lease shall be governed by and construed in accordance with the laws of India.\n"
        lease_agreement_text += "[Include signature lines for both parties]"


    def generate_non_disclosure_agreement(self):
        print("\nGenerating Non-Disclosure Agreement:")
        
        disclosing_party_name = input("Enter the name of the disclosing party: ")
        receiving_party_name = input("Enter the name of the receiving party: ")
        confidential_information = input("Enter a description of the confidential information: ")
        duration = input("Enter the duration of the agreement: ")

        nda_text = f"This Non-Disclosure Agreement ('NDA') is entered into on [Date], between {disclosing_party_name}, located at [Address], and {receiving_party_name}, located at [Address].\n"
        nda_text += f"1. Confidential Information:\nThe 'Confidential Information' refers to any non-public information disclosed by the {disclosing_party_name} to the {receiving_party_name}.\n"
        nda_text += f"2. Obligations of the Receiving Party:\nThe {receiving_party_name} agrees to keep the Confidential Information confidential and not disclose it to third parties.\n"
        nda_text += f"3. Duration:\nThis NDA shall remain in effect for {duration} years from the date of signing.\n"
        nda_text += "4. Governing Law:\nThis NDA shall be governed by and construed in accordance with the laws of India.\n"
        nda_text += "[Include signature lines for both parties]"


    def generate_employment_agreement(self):
        print("\nGenerating Employment Agreement:")
        
        company_name = input("Enter the name of the company: ")
        employee_name = input("Enter the name of the employee: ")
        position = input("Enter the employee's position: ")
        salary_amount = input("Enter the monthly salary amount: ")
        benefits = input("Enter the benefits provided to the employee: ")
        termination_notice = input("Enter the notice period for termination: ")

        employment_agreement_text = f"This Employment Agreement ('Agreement') is entered into on [Date], between {company_name}, a company registered in India, and {employee_name}, an individual.\n"
        employment_agreement_text += f"1. Position and Responsibilities:\nThe Company agrees to employ the {employee_name} as {position} and outlines the {employee_name}'s responsibilities.\n"
        employment_agreement_text += f"2. Compensation:\nThe {employee_name} shall receive a monthly salary of {salary_amount}, subject to applicable deductions and tax.\n"
        employment_agreement_text += f"3. Benefits:\nThe {employee_name} shall be entitled to {benefits}.\n"
        employment_agreement_text += f"4. Termination:\nThis Agreement may be terminated by either party with {termination_notice} written notice or for cause as specified.\n"
        employment_agreement_text += "5. Confidentiality:\nThe {employee_name} agrees to maintain the confidentiality of the Company's proprietary information.\n"
        employment_agreement_text += "6. Governing Law:\nThis Agreement shall be governed by and construed in accordance with the laws of India.\n"
        employment_agreement_text += "[Include signature lines for both parties]"


    def calculate_income_tax(self, income):
        if income <= 300000:
            tax = 0
        elif income <= 700000:
            tax = (income - 300000) * self.tax_slab_24_25["3_to_7_lakh"]
        elif income <= 1000000:
            tax = (400000 * self.tax_slab_24_25["3_to_7_lakh"]) + (income - 700000) * self.tax_slab_24_25["7_to_10_lakh"]
        elif income <= 1200000:
            tax = (400000 * self.tax_slab_24_25["3_to_7_lakh"]) + (300000 * self.tax_slab_24_25["7_to_10_lakh"]) + (income - 1000000) * self.tax_slab_24_25["10_to_12_lakh"]
        elif income <= 1500000:
            tax = (400000 * self.tax_slab_24_25["3_to_7_lakh"]) + (300000 * self.tax_slab_24_25["7_to_10_lakh"]) + (200000 * self.tax_slab_24_25["10_to_12_lakh"]) + (income - 1200000) * self.tax_slab_24_25["12_to_15_lakh"]
        else:
            tax = (400000 * self.tax_slab_24_25["3_to_7_lakh"]) + (300000 * self.tax_slab_24_25["7_to_10_lakh"]) + (200000 * self.tax_slab_24_25["10_to_12_lakh"]) + (300000 * self.tax_slab_24_25["12_to_15_lakh"]) + (income - 1500000) * self.tax_slab_24_25["above_15_lakh"]
        
        return tax

    def income_tax_calculator(self):
        print("\nIncome Tax Calculator:")
        try:
            income = float(input("Enter your annual income: "))
            tax = self.calculate_income_tax(income)
            print(f"The calculated tax on an income of ₹{income:,.2f} is ₹{tax:,.2f}")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    robot = LegalInfoRobot()
    robot.start_assistant()