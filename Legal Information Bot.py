import os
import warnings
from urllib3.exceptions import NotOpenSSLWarning

warnings.filterwarnings("ignore", category=NotOpenSSLWarning)

class LegalInfoRobot:

    def __init__(self):
        self.user_info = {}
        self.legal_rights = {
            "Right to Freedom from Discrimination Based on Sexual Orientation in Employment": "You have the right to be free from discrimination based on sexual orientation in employment.",
            "Right to Adequate Nutrition": "You have the right to adequate nutrition and a balanced diet.",
            "Right to Clean Water and Sanitation": "You have the right to access clean and safe drinking water and sanitation facilities.",
            "Right to Freedom from Discrimination Based on Gender in Education": "You have the right to be free from discrimination based on gender in education.",
            "Right to Privacy of Personal Finances": "You have the right to privacy of your personal financial information.",
            "Right to Participate in Cultural and Artistic Activities": "You have the right to participate in cultural and artistic activities.",
            "Right to Freedom from Forced Labor": "You have the right to be free from forced or compulsory labor.",
            "Right to Adequate Childcare Services": "You have the right to access adequate childcare services.",
            "Right to Freedom from Torture and Inhumane Treatment": "You have the right to be free from torture and inhumane or degrading treatment or punishment.",
            "Right to Access to Public Records": "You have the right to access public records and government documents.",
            "Right to Freedom from Discrimination Based on Genetic Information in Healthcare": "You have the right to be free from discrimination based on genetic information in healthcare.",
            "Right to Freedom of the Press": "You have the right to freedom of the press and media.",
            "Right to Adequate Mental Health Care": "You have the right to access adequate mental health care and treatment.",
            "Right to Freedom from Discrimination Based on Gender Identity in Housing": "You have the right to be free from discrimination based on gender identity in housing.",
            "Right to Access to Affordable Prescription Medications": "You have the right to access affordable prescription medications.",
            "Right to Freedom from Discrimination Based on Citizenship Status": "You have the right to be free from discrimination based on citizenship or immigration status.",
            "Right to Adequate Child Protection Services": "Children have the right to adequate protection from abuse, exploitation, and neglect.",
            "Right to Freedom from Discrimination Based on Education Status": "You have the right to be free from discrimination based on your educational status.",
            "Right to Freedom of Conscience and Belief": "You have the right to freedom of conscience and belief.",
            "Right to Adequate Legal Aid for Immigrants": "Immigrants have the right to adequate legal aid and representation.",
            "Right to Freedom from Discrimination Based on Economic Activities": "You have the right to be free from discrimination based on your economic activities or profession.",
            "Right to Adequate Rehabilitation for Persons with Disabilities": "Persons with disabilities have the right to adequate rehabilitation services.",
            "Right to Freedom from Discrimination Based on Political Affiliation": "You have the right to be free from discrimination based on your political affiliation.",
            "Right to Access to Family Planning Services": "You have the right to access family planning and reproductive health services.",
            "Right to Freedom from Discrimination Based on Maternity or Pregnancy": "You have the right to be free from discrimination based on maternity or pregnancy.",
            "Right to Adequate Refugee Protection": "Refugees have the right to adequate protection, including asylum and safe refuge.",
            "Right to Freedom from Discrimination Based on Trade Union Membership": "You have the right to be free from discrimination based on trade union membership.",
            "Right to Accessible Public Parks and Recreation Areas": "You have the right to access public parks and recreation areas that are accessible to all.",
            "Right to Freedom from Discrimination Based on Immigration Status in Employment": "You have the right to be free from discrimination based on immigration status in employment.",
            "Right to Adequate Cultural Heritage Preservation": "You have the right to the preservation of your cultural heritage and historical sites.",
            "Right to Freedom from Discrimination Based on Disability in Education": "You have the right to be free from discrimination based on disability in education.",
            "Right to Access to Mental Health Counseling Services": "You have the right to access mental health counseling and support services.",
            "Right to Freedom from Discrimination Based on Language in Education": "You have the right to be free from discrimination based on language in education.",
            "Right to Adequate Support for Orphans and Vulnerable Children": "Orphans and vulnerable children have the right to adequate support and care.",
            "Right to Freedom from Discrimination Based on Parental or Caregiver Status in Employment": "You have the right to be free from discrimination based on parental or caregiver status in employment.",
            "Right to Access to Clean Energy Sources": "You have the right to access clean and sustainable energy sources.",
            "Right to Freedom from Discrimination Based on Refugee Status in Housing": "You have the right to be free from discrimination based on refugee status in housing.",
            "Right to Adequate Protection for Whistleblowers": "Whistleblowers have the right to adequate protection and legal safeguards.",
            "Right to Freedom from Discrimination Based on Sexual Orientation in Housing": "You have the right to be free from discrimination based on sexual orientation in housing.",
            "Right to Access to Reproductive Health Information": "You have the right to access information on reproductive health and family planning.",
            "Right to Freedom from Discrimination Based on Socioeconomic Status in Healthcare": "You have the right to be free from discrimination based on socioeconomic status in healthcare.",
            "Right to Adequate Training and Education for Workers": "Workers have the right to adequate training and education to improve their skills.",
            "Right to Freedom from Discrimination Based on Genetic Information in Employment": "You have the right to be free from discrimination based on genetic information in employment.",
            "Right to Access to Legal Aid for Victims of Domestic Violence": "Victims of domestic violence have the right to access legal aid and support.",
            "Right to Freedom from Discrimination Based on Disability in Housing": "You have the right to be free from discrimination based on disability in housing.",
            "Right to Adequate Environmental Conservation and Protection": "You have the right to adequate environmental conservation and protection measures.",
            "Right to Freedom from Discrimination Based on Gender Identity in Employment": "You have the right to be free from discrimination based on gender identity in employment.",
            "Right to Access to Affordable Healthcare for Low-Income Individuals": "Low-income individuals have the right to access affordable healthcare services.",
            "Right to Education": "Every child has the right to free and compulsory education up to the age of 14.",
            "Right to Information": "You have the right to access information held by public authorities.",
            "Right to Legal Aid": "If you cannot afford legal representation, you have the right to free legal aid.",
            "Right to a Fair Trial": "You have the right to a fair and public trial within a reasonable time by an impartial tribunal.",
            "Right to Privacy": "You have the right to privacy and protection of personal data.",
            "Right to Freedom of Speech": "You have the right to freedom of speech and expression.",
            "Right to Equality": "All persons are equal before the law and are entitled to equal protection of the law.",
            "Right to Work": "You have the right to work in a safe and healthy environment with fair wages.",
            "Right to Health": "You have the right to the enjoyment of the highest attainable standard of physical and mental health.",
            "Right to Housing": "You have the right to adequate housing and protection against homelessness.",
            "Right to a Clean Environment": "You have the right to live in a clean and healthy environment.",
            "Right to Marriage and Family": "You have the right to marry and found a family without any discrimination.",
            "Right to Freedom of Religion": "You have the right to freedom of thought, conscience, and religion.",
            "Right to Adequate Food": "You have the right to adequate food and clean drinking water.",
            "Right to Freedom of Assembly": "You have the right to freedom of peaceful assembly and association.",
            "Right to Participate in Government": "You have the right to take part in the government of your country.",
            "Right to Cultural Life": "You have the right to take part in cultural, artistic, and scientific activities.",
            "Right to Adequate Standard of Living": "You have the right to an adequate standard of living for yourself and your family.",
            "Right to Social Security": "You have the right to social security and protection in times of need.",
            "Right to Non-Discrimination": "You have the right to be free from discrimination based on race, color, sex, religion, and more.",
            "Right to Indigenous Peoples": "Indigenous peoples have the right to maintain and strengthen their distinct cultural identities.",
            "Right to Access to Justice": "You have the right to access to justice and a fair legal process.",
            "Right to Privacy of Communication": "You have the right to privacy of your communications, including mail, telephone, and electronic communications.",
            "Right to Education for Persons with Disabilities": "Persons with disabilities have the right to inclusive education and reasonable accommodations.",
            "Right to a Nationality": "You have the right to a nationality and not to be arbitrarily deprived of your nationality.",
            "Right to Adequate Clothing and Shelter": "You have the right to adequate clothing and shelter as part of your right to an adequate standard of living.",
            "Right to Access to the Internet": "You have the right to access and use the internet as a means of exercising your rights to information and freedom of expression.",
            "Right to Equal Access to Technology": "You have the right to equal access to and benefit from advancements in technology.",
            "Right to Freedom from Discrimination Based on Sexual Orientation and Gender Identity": "You have the right to be free from discrimination based on sexual orientation and gender identity.",
            "Right to Freedom of Thought and Expression on the Internet": "You have the right to freedom of thought and expression on the internet.",
            "Right to Fair and Transparent Digital Data Practices": "You have the right to fair and transparent practices concerning your personal digital data.",
            "Right to Freedom from Genetic Discrimination": "You have the right to be free from discrimination based on your genetic information.",
            "Right to Dignified End-of-Life Care": "You have the right to receive dignified end-of-life care and the right to make decisions about your medical treatment.",
            "Right to Equal Access to Online Education": "You have the right to equal access to online education and digital learning resources.",
            "Right to Accessible Public Transportation": "You have the right to accessible and affordable public transportation.",
            "Right to Freedom from Forced or Coerced Medical Procedures": "You have the right to be free from forced or coerced medical procedures or treatments.",
            "Right to Protection from Cyberbullying and Online Harassment": "You have the right to protection from cyberbullying and online harassment.",
            "Right to Freedom from Age Discrimination": "You have the right to be free from discrimination based on age.",
            "Right to Freedom from Discrimination Based on Disability in the Workplace": "You have the right to be free from discrimination based on disability in the workplace.",
            "Right to Rest and Leisure": "You have the right to rest and leisure, including reasonable working hours and periodic holidays with pay.",
            "Right to Freedom from Human Trafficking": "You have the right to be free from human trafficking and modern forms of slavery.",
            "Right to Accessible and Inclusive Public Spaces": "You have the right to access public spaces that are accessible and inclusive for all individuals, including those with disabilities.",
            "Right to Freedom from Gender-Based Violence": "You have the right to be free from gender-based violence and abuse.",
            "Right to Adequate Medical Care and Treatment in Detention": "You have the right to adequate medical care and treatment if you are in detention or incarcerated.",
            "Right to Digital Privacy": "You have the right to privacy and protection of your digital communications and data.",
            "Right to Freedom from Racial Discrimination": "You have the right to be free from discrimination based on race or ethnicity.",
            "Right to Access to Affordable Housing for the Homeless": "You have the right to access affordable housing and support services if you are homeless.",
            "Right to Freedom of Movement for Internally Displaced Persons": "Internally displaced persons have the right to freedom of movement and the right to return to their homes.",
            "Right to Freedom from Discrimination Based on HIV/AIDS Status": "You have the right to be free from discrimination based on HIV/AIDS status.",
            "Right to Freedom from Discrimination Based on Nationality": "You have the right to be free from discrimination based on nationality.",
            "Right to Freedom of Sexual Orientation and Gender Identity Expression": "You have the right to freely express your sexual orientation and gender identity.",
            "Right to Freedom from Discrimination in Access to Goods and Services": "You have the right to be free from discrimination in access to goods and services.",
            "Right to Freedom from Discrimination Based on Religion or Belief": "You have the right to be free from discrimination based on religion or belief.",
            "Right to Cultural Diversity and Heritage": "You have the right to respect and protect your cultural diversity and heritage.",
            "Right to Freedom from Discrimination in Adoption and Fostering": "You have the right to be free from discrimination in adoption and fostering based on various factors.",
            "Right to Freedom from Discrimination Based on Language": "You have the right to be free from discrimination based on language.",
            "Right to Freedom from Discrimination Based on Social and Economic Status": "You have the right to be free from discrimination based on social and economic status.",
            "Right to Freedom of Movement for Refugees": "Refugees have the right to freedom of movement and the right to seek asylum in other countries.",
            "Right to Freedom from Discrimination Based on Political Opinion": "You have the right to be free from discrimination based on your political opinion.",
            "Right to Access to Comprehensive Sexual and Reproductive Health Education": "You have the right to access comprehensive sexual and reproductive health education.",
            "Right to Freedom from Discrimination Based on Marital Status": "You have the right to be free from discrimination based on marital status.",
            "Right to Accessible Transportation for Persons with Disabilities": "Persons with disabilities have the right to accessible transportation.",
            "Right to Freedom from Discrimination Based on Socioeconomic Class": "You have the right to be free from discrimination based on socioeconomic class.",
            "Right to Freedom from Discrimination in Adoption and Fostering for LGBTQ+ Individuals": "LGBTQ+ individuals have the right to be free from discrimination in adoption and fostering.",
            "Right to Freedom from Discrimination Based on Parental Status": "You have the right to be free from discrimination based on parental status.",
            "Right to Freedom from Discrimination Based on Residence or Domicile": "You have the right to be free from discrimination based on your residence or domicile.",
            "Right to Freedom from Discrimination Based on Criminal Record": "You have the right to be free from discrimination based on your criminal record.",
            "Right to Accessible and Inclusive Tourism": "You have the right to accessible and inclusive tourism and travel.",
            "Right to Freedom from Discrimination Based on Health Status": "You have the right to be free from discrimination based on your health status.",
            "Right to Accessible Information for Persons with Disabilities": "Persons with disabilities have the right to accessible information.",
            "Right to Freedom from Discrimination Based on Refugee Status": "You have the right to be free from discrimination based on your refugee status.",
            "Right to Freedom from Discrimination Based on Age in Employment": "You have the right to be free from discrimination based on age in employment.",
            "Right to Accessible and Inclusive Voting and Elections": "You have the right to accessible and inclusive voting and elections.",
            "Right to Freedom from Discrimination Based on Military or Veteran Status": "You have the right to be free from discrimination based on military or veteran status.",
            "Right to Accessible Information and Communication Technology for Persons with Disabilities": "Persons with disabilities have the right to accessible information and communication technology."
        }

        self.FAQS = {
            "1": {
                "question": "How can I file for divorce in India?",
                "answer": "To file for divorce in India, follow legal procedures under personal laws like the Hindu Marriage Act or Special Marriage Act."
            },
            "2": {
                "question": "What are my rights during an arrest in India?",
                "answer": "During an arrest in India, you have the right to remain silent and the right to legal representation. The police must inform you of the reasons for the arrest."
            },
            "3": {
                "question": "How to apply for a passport in India?",
                "answer": "To apply for a passport in India, visit the official Passport Seva website, fill out the application form, and schedule an appointment at a Passport Seva Kendra."
            },
            "4": {
                "question": "What are the labor laws in India?",
                "answer": "Labor laws in India cover aspects like wages, working conditions, and employment contracts. Key laws include the Minimum Wages Act and Industrial Disputes Act."
            },
            "5": {
                "question": "How to draft a rental agreement in India?",
                "answer": "To draft a rental agreement in India, include details of the parties, rent amount, security deposit, and terms and conditions."
            },
            "6": {
                "question": "What is the legal drinking age in India?",
                "answer": "The legal drinking age in India varies by state and union territory. It typically ranges from 18 to 25 years. Check the specific regulations in your location."
            },
            "7": {
                "question": "What are the steps for divorce in India?",
                "answer": "Divorce in India involves legal procedures under personal laws such as the Hindu Marriage Act or Special Marriage Act. Consult a family lawyer to understand the process, which includes filing a petition and court appearances."
            },
            "8": {
                "question": "How to create a will in India?",
                "answer": "To create a will in India, list your assets, appoint an executor, and clearly state the beneficiaries. Sign the will in the presence of witnesses. It's advisable to consult a lawyer to ensure it's legally valid."
            },
            "9": {
                "question": "How to file a consumer complaint in India?",
                "answer": "To file a consumer complaint in India, you can approach the district consumer forum or state/national consumer dispute redressal commission. Provide details of the grievance and supporting documents."
            },
            "10": {
                "question": "What are the rules for property inheritance in India?",
                "answer": "In India, property inheritance laws vary based on religion and personal laws. Consult a legal expert to understand your specific rights and obligations concerning property inheritance."
            },
            "11": {
                "question": "How to register a trademark in India?",
                "answer": "To register a trademark in India, file an application with the Trademarks Registry. Conduct a trademark search, provide necessary documents, and follow the registration process."
            },
            "12": {
                "question": "What are the rights of tenants in India?",
                "answer": "Tenants in India have rights regarding rent control, eviction, and property maintenance. Understanding local rent laws and having a rental agreement is essential."
            },
            "13": {
                "question": "How to apply for a voter ID card in India?",
                "answer": "To apply for a Voter ID card in India, visit the Electoral Registration Officer in your constituency or apply online through the National Voter's Service Portal (NVSP). Provide proof of identity and address."
            },
            "14": {
                "question": "What are the laws related to domestic violence in India?",
                "answer": "Domestic violence laws in India are covered under the Protection of Women from Domestic Violence Act. Victims can seek protection orders, residence orders, and maintenance."
            },
            "15": {
                "question": "How to file for child custody in India?",
                "answer": "Child custody matters in India are governed by personal laws. Courts consider the child's welfare as the primary concern. Consult a family lawyer for guidance."
            },
            "16": {
                "question": "What are the rules for land acquisition in India?",
                "answer": "Land acquisition in India is governed by the Land Acquisition Act. The government must follow specific procedures and compensate landowners fairly when acquiring land for public projects."
            },
            "17": {
                "question": "How to apply for a marriage certificate in India?",
                "answer": "To apply for a marriage certificate in India, visit the local municipal office or panchayat. Provide the required documents, including proof of marriage, and complete the formalities."
            },
            "18": {
                "question": "What are the regulations for starting an online business in India?",
                "answer": "Starting an online business in India involves compliance with e-commerce laws, taxation, and data protection regulations. Consult legal experts to ensure compliance."
            },
            "19": {
                "question": "What are the rights of women in the workplace in India?",
                "answer": "Women in the workplace in India have rights related to equal pay, sexual harassment prevention, and maternity benefits. Employers must adhere to these laws."
            },
            "20": {
                "question": "How to claim insurance in case of a car accident in India?",
                "answer": "In case of a car accident in India, inform the insurance company immediately and file a claim. Provide the necessary accident details and documents for a smooth claims process."
            },
            "21": {
                "question": "What are the legal requirements for starting a non-profit organization in India?",
                "answer": "To start a non-profit organization in India, you need to register it under the appropriate legal framework, such as the Societies Registration Act or the Companies Act. Consult with a legal expert for guidance."
            },
            "22": {
                "question": "How to apply for a patent in India?",
                "answer": "To apply for a patent in India, you should file a patent application with the Indian Patent Office. The application should include a detailed description of your invention. Consult with a patent attorney for assistance."
            },
            "23": {
                "question": "What are the regulations for online privacy in India?",
                "answer": "Online privacy in India is governed by the Information Technology Act and the Personal Data Protection Bill. These laws regulate data protection and privacy issues online. Ensure compliance with these regulations if you operate a website or app."
            },
            "24": {
                "question": "How to file a cybercrime complaint in India?",
                "answer": "To file a cybercrime complaint in India, you should contact your local cybercrime cell or police station. Provide all necessary details and evidence of the cybercrime. Consult with a cybercrime lawyer if needed."
            },
            "25": {
                "question": "What are the rules for adoption in India?",
                "answer": "Adoption in India is governed by the Juvenile Justice (Care and Protection of Children) Act, 2015. Prospective adoptive parents need to follow the legal adoption process through recognized agencies or authorities."
            },
            "26": {
                "question": "How to start a small business in India?",
                "answer": "Starting a small business in India involves registering your business, obtaining necessary licenses, and complying with taxation and regulatory requirements. Consult with a business lawyer or a chartered accountant for guidance."
            },
            "27": {
                "question": "What are the legal rights of persons with disabilities in India?",
                "answer": "Persons with disabilities in India have legal rights protected by the Rights of Persons with Disabilities Act, 2016. These rights include accessibility, reservation in education and employment, and more."
            },
            "28": {
                "question": "How to file a public interest litigation (PIL) in India?",
                "answer": "To file a public interest litigation (PIL) in India, you need to approach the High Court or the Supreme Court. A PIL can be filed to address issues of public concern. Consult with a PIL lawyer for assistance."
            },
            "29": {
                "question": "What are the legal requirements for marriage in India?",
                "answer": "Legal requirements for marriage in India include age restrictions, registration, and compliance with personal laws. Different religions and regions may have specific marriage rules. Consult with a marriage lawyer for guidance."
            },
            "30": {
                "question": "How to protect intellectual property in India?",
                "answer": "To protect intellectual property in India, you can register trademarks, copyrights, patents, and designs. Intellectual property laws provide legal protection for your creations. Consult with an intellectual property attorney for advice."
            },
            "31": {
                "question": "What are the legal rights of tenants in India?",
                "answer": "Tenants in India have rights regarding rent control, eviction, and property maintenance. Understanding local rent laws and having a rental agreement is essential."
            },
            "32": {
                "question": "How to apply for a voter ID card in India?",
                "answer": "To apply for a Voter ID card in India, visit the Electoral Registration Officer in your constituency or apply online through the National Voter's Service Portal (NVSP). Provide proof of identity and address."
            },
            "33": {
                "question": "What are the laws related to domestic violence in India?",
                "answer": "Domestic violence laws in India are covered under the Protection of Women from Domestic Violence Act. Victims can seek protection orders, residence orders, and maintenance."
            },
            "34": {
                "question": "How to file for child custody in India?",
                "answer": "Child custody matters in India are governed by personal laws. Courts consider the child's welfare as the primary concern. Consult a family lawyer for guidance."
            },
            "35": {
                "question": "What are the rules for land acquisition in India?",
                "answer": "Land acquisition in India is governed by the Land Acquisition Act. The government must follow specific procedures and compensate landowners fairly when acquiring land for public projects."
            },
            "36": {
                "question": "How to apply for a marriage certificate in India?",
                "answer": "To apply for a marriage certificate in India, visit the local municipal office or panchayat. Provide the required documents, including proof of marriage, and complete the formalities."
            },
            "37": {
                "question": "What are the regulations for starting an online business in India?",
                "answer": "Starting an online business in India involves compliance with e-commerce laws, taxation, and data protection regulations. Consult legal experts to ensure compliance."
            },
            "38": {
                "question": "What are the rights of women in the workplace in India?",
                "answer": "Women in the workplace in India have rights related to equal pay, sexual harassment prevention, and maternity benefits. Employers must adhere to these laws."
            },
            "39": {
                "question": "How to claim insurance in case of a car accident in India?",
                "answer": "In case of a car accident in India, inform the insurance company immediately and file a claim. Provide the necessary accident details and documents for a smooth claims process."
            },
            "40": {
                "question": "What are the legal requirements for starting a non-profit organization in India?",
                "answer": "To start a non-profit organization in India, you need to register it under the appropriate legal framework, such as the Societies Registration Act or the Companies Act. Consult with a legal expert for guidance."
            },
            "41": {
                "question": "How to apply for a patent in India?",
                "answer": "To apply for a patent in India, you should file a patent application with the Indian Patent Office. The application should include a detailed description of your invention. Consult with a patent attorney for assistance."
            },
            "42": {
                "question": "What are the regulations for online privacy in India?",
                "answer": "Online privacy in India is governed by the Information Technology Act and the Personal Data Protection Bill. These laws regulate data protection and privacy issues online. Ensure compliance with these regulations if you operate a website or app."
            },
            "43": {
                "question": "How to file a cybercrime complaint in India?",
                "answer": "To file a cybercrime complaint in India, you should contact your local cybercrime cell or police station. Provide all necessary details and evidence of the cybercrime. Consult with a cybercrime lawyer if needed."
            },
            "44": {
                "question": "What are the rules for adoption in India?",
                "answer": "Adoption in India is governed by the Juvenile Justice (Care and Protection of Children) Act, 2015. Prospective adoptive parents need to follow the legal adoption process through recognized agencies or authorities."
            },
            "45": {
                "question": "How to start a small business in India?",
                "answer": "Starting a small business in India involves registering your business, obtaining necessary licenses, and complying with taxation and regulatory requirements. Consult with a business lawyer or a chartered accountant for guidance."
            },
            "46": {
                "question": "What are the legal rights of persons with disabilities in India?",
                "answer": "Persons with disabilities in India have legal rights protected by the Rights of Persons with Disabilities Act, 2016. These rights include accessibility, reservation in education and employment, and more."
            },
            "47": {
                "question": "How to file a public interest litigation (PIL) in India?",
                "answer": "To file a public interest litigation (PIL) in India, you need to approach the High Court or the Supreme Court. A PIL can be filed to address issues of public concern. Consult with a PIL lawyer for assistance."
            },
            "48": {
                "question": "What are the legal requirements for marriage in India?",
                "answer": "Legal requirements for marriage in India include age restrictions, registration, and compliance with personal laws. Different religions and regions may have specific marriage rules. Consult with a marriage lawyer for guidance."
            },
            "49": {
                "question": "How to protect intellectual property in India?",
                "answer": "To protect intellectual property in India, you can register trademarks, copyrights, patents, and designs. Intellectual property laws provide legal protection for your creations. Consult with an intellectual property attorney for advice."
            },
            "50": {
                "question": "How to apply for a trade license in India?",
                "answer": "To apply for a trade license in India, contact the local municipal corporation or the relevant government authority. Follow the prescribed application process and fulfill the necessary requirements for obtaining a trade license."
            },
            "51": {
                "question": "What are the legal rights of LGBTQ+ individuals in India?",
                "answer": "LGBTQ+ individuals in India have legal rights, including protection from discrimination and the right to privacy. However, there are ongoing efforts to advocate for more comprehensive legal protections. Stay informed about the latest developments in LGBTQ+ rights in India."
            },
            "52": {
                "question": "How to register a partnership firm in India?",
                "answer": "To register a partnership firm in India, draft a partnership deed specifying the terms and conditions of the partnership. Visit the Registrar of Firms in your state and submit the deed along with the required documents for registration."
            },
            "53": {
                "question": "What are the legal requirements for starting a restaurant in India?",
                "answer": "Starting a restaurant in India involves obtaining licenses and permits related to food safety, health, and fire safety. Compliance with local and state regulations is essential. Consult with legal and regulatory authorities for guidance."
            },
            "54": {
                "question": "How to file a harassment complaint in the workplace in India?",
                "answer": "If you experience harassment in the workplace in India, report it to your employer's Internal Complaints Committee (ICC) or the Local Complaints Committee (LCC) in case of unorganized sectors. You can also file a complaint with the police or labor authorities if necessary."
            },
            "55": {
                "question": "What are the legal rights of tenants facing eviction in India?",
                "answer": "Tenants facing eviction in India have rights, including notice periods and legal proceedings. The specific rights may vary by state and locality. Consult with legal experts to understand and protect your rights."
            },
            "56": {
                "question": "How to apply for a trademark renewal in India?",
                "answer": "To renew a trademark in India, file a renewal application with the Trademarks Registry before the expiry of the trademark registration. Ensure timely renewal to maintain your trademark's protection."
            },
            "57": {
                "question": "What are the legal requirements for importing goods into India?",
                "answer": "Importing goods into India involves compliance with customs regulations, import duties, and documentation. Consult with customs authorities and legal experts to understand the specific requirements for your imports."
            },
            "58": {
                "question": "How to address workplace discrimination in India?",
                "answer": "To address workplace discrimination in India, you can approach your employer, file a complaint with the Equal Opportunity Commission, or seek legal redress. Be aware of your rights and consult with legal experts if needed."
            },
            "59": {
                "question": "What are the laws regarding child labor in India?",
                "answer": "Child labor laws in India prohibit the employment of children in certain hazardous occupations and prescribe conditions for child labor in non-hazardous sectors. Employers must comply with these laws, and violations can result in penalties."
            },
            "60": {
                "question": "How to file a complaint against a defective product in India?",
                "answer": "If you purchase a defective product in India, you can file a complaint with the manufacturer, seller, or consumer protection authorities. Document the issue and gather evidence to support your complaint."
            },
            "61": {
                "question": "How to apply for a copyright registration in India?",
                "answer": "To apply for copyright registration in India, complete the application form and submit it to the Copyright Office along with the required documents and the applicable fee. The process involves examination and registration."
            },
            "62": {
                "question": "What are the legal requirements for starting an educational institution in India?",
                "answer": "Starting an educational institution in India requires compliance with education laws, licensing, and accreditation. Consult with the relevant education authorities and legal experts for guidance."
            },
            "63": {
                "question": "How to seek legal aid in India if you cannot afford a lawyer?",
                "answer": "If you cannot afford a lawyer in India, you have the right to free legal aid. You can approach the Legal Services Authority or other organizations that provide legal aid to eligible individuals."
            },
            "64": {
                "question": "What are the rules for environmental impact assessment (EIA) in India?",
                "answer": "Environmental impact assessment (EIA) in India is governed by the Environment Impact Assessment Notification. Projects that have a significant environmental impact require EIA clearance and public consultations."
            },
            "65": {
                "question": "How to file a complaint against a builder for a delayed construction project in India?",
                "answer": "If you face delays in a construction project in India, you can file a complaint with the appropriate authority, consumer forums, or seek legal recourse. Keep records of agreements and communication with the builder."
            },
            "66": {
                "question": "What are the legal rights of victims of sexual harassment in India?",
                "answer": "Victims of sexual harassment in India have rights protected under the Sexual Harassment of Women at Workplace (Prevention, Prohibition, and Redressal) Act, 2013. Employers are required to establish Internal Complaints Committees (ICCs) for addressing such complaints."
            },
            "67": {
                "question": "How to register a non-governmental organization (NGO) in India?",
                "answer": "To register an NGO in India, you can choose from various legal structures like trusts, societies, or Section 8 companies. The registration process involves documentation and compliance with relevant laws."
            },
            "68": {
                "question": "What are the legal requirements for exporting goods from India?",
                "answer": "Exporting goods from India involves compliance with customs regulations, export licenses, and documentation. Consult with customs authorities and legal experts to understand the specific requirements for your exports."
            },
            "69": {
                "question": "How to file a complaint against medical malpractice in India?",
                "answer": "If you believe you are a victim of medical malpractice in India, you can file a complaint with the relevant medical council or approach consumer forums. Collect medical records and expert opinions as evidence."
            },
            "70": {
                "question": "What are the rights of senior citizens in India?",
                "answer": "Senior citizens in India have rights protected under the Maintenance and Welfare of Parents and Senior Citizens Act, 2007. These rights include financial support and protection against abuse."
            },
            "71": {
                "question": "How to seek legal recourse for online defamation in India?",
                "answer": "To seek legal recourse for online defamation in India, you can file a civil defamation suit or approach cybercrime authorities. Gather evidence of the defamatory content and consult with legal experts."
            },
            "72": {
                "question": "What are the legal requirements for starting a micro, small, or medium-sized enterprise (MSME) in India?",
                "answer": "Starting an MSME in India involves registration under the MSMED Act, 2006, and compliance with various government schemes and incentives. Consult with industry associations and legal experts for guidance."
            },
            "73": {
                "question": "How to address workplace harassment based on gender in India?",
                "answer": "Workplace harassment based on gender is prohibited in India. Victims can file complaints with their employers or approach the Internal Complaints Committee (ICC) or Local Complaints Committee (LCC) for redressal."
            },
            "74": {
                "question": "What are the legal requirements for importing and selling food products in India?",
                "answer": "Importing and selling food products in India requires compliance with the Food Safety and Standards Act, 2006. Businesses must obtain licenses, adhere to food safety standards, and label products correctly."
            },
            "75": {
                "question": "How to resolve disputes through mediation in India?",
                "answer": "Dispute resolution through mediation in India involves the appointment of a mediator to facilitate negotiations between parties. Mediation can be court-annexed or voluntary, and it aims to reach a mutually acceptable solution."
            },
            "76": {
                "question": "How to obtain a no-objection certificate (NOC) for property transactions in India?",
                "answer": "To obtain a no-objection certificate (NOC) for property transactions in India, approach the relevant authority or property owner. NOCs may be required for various property-related transactions, such as mortgages and transfers."
            },
            "77": {
                "question": "What are the legal requirements for hosting an event or concert in India?",
                "answer": "Hosting an event or concert in India involves obtaining necessary licenses, permissions, and ensuring safety measures. Consult with local authorities and legal experts for event planning and compliance."
            },
            "78": {
                "question": "How to address discrimination based on caste or religion in India?",
                "answer": "Discrimination based on caste or religion is prohibited in India. Victims can file complaints with the National Commission for Scheduled Castes (NCSC), National Commission for Minorities (NCM), or other relevant authorities."
            },
            "79": {
                "question": "What are the legal requirements for starting an e-commerce business in India?",
                "answer": "Starting an e-commerce business in India involves compliance with e-commerce regulations, taxation, and data protection laws. Consult legal experts and industry associations for guidance on e-commerce compliance."
            },
            "80": {
                "question": "How to address sexual harassment in educational institutions in India?",
                "answer": "Educational institutions in India are required to establish Internal Complaints Committees (ICCs) for addressing sexual harassment complaints. Victims can report incidents to the ICC or the police."
            }}

        self.legal_glossary = {
            "Arbitration": "A method of dispute resolution where a neutral third party (an arbitrator) makes a binding decision.",
            "Defendant": "The party in a legal case who is accused of wrongdoing and defends against the allegations.",
            "Plaintiff": "The party in a legal case who initiates the lawsuit by filing a complaint against the defendant.",
            "Jurisdiction": "The authority of a court to hear and decide legal cases within a specific geographic area or over certain types of cases.",
            "Evidence": "Information, documents, or materials presented in court to prove or disprove facts in a legal case.",
            "Criminal Law": "A branch of law that deals with offenses against society, and the government prosecutes individuals accused of crimes.",
            "Civil Law": "A branch of law that deals with disputes between individuals, organizations, or entities, and the injured party typically files a lawsuit seeking compensation.",
            "Common Law": "A legal system based on precedent and past court decisions rather than written laws.",
            "Statute": "A written law passed by a legislative body, such as a parliament or congress.",
            "Contract": "A legally binding agreement between two or more parties that defines their rights and obligations.",
            "Tort": "A civil wrong or wrongful act that results in harm or injury to another party, leading to a legal liability.",
            "Injunction": "A court order that requires a party to do or refrain from doing a specific action.",
            "Lien": "A legal claim or right over a property or asset to secure a debt or obligation.",
            "Habeas Corpus": "A legal writ that requires a person under arrest to be brought before a judge or into court to secure their release unless lawful grounds are shown for their detention.",
            "Due Process": "The legal requirement that the government must respect all legal rights of a person, including the right to a fair trial.",
            "Probate": "The legal process of proving the validity of a will and settling the estate of a deceased person.",
            "Deposition": "The testimony of a witness taken under oath outside of the courtroom, typically used in pre-trial proceedings.",
            "Allegation": "A statement of a fact that a party claims to be true, especially one that is disputed or unproven.",
            "Indictment": "A formal accusation of a serious crime, typically issued by a grand jury.",
            "Precedent": "A legal decision or case that serves as an authoritative example or reference for future cases.",
            "Adjudication": "The legal process of resolving a dispute or controversy by making a formal decision or judgment.",
            "Inadmissible": "Evidence or information that is not allowed to be presented in court due to legal rules or objections.",
            "Lawsuit": "A legal dispute between two or more parties that is resolved through a formal court process.",
            "Solicitor": "A legal professional who provides legal advice, prepares legal documents, and represents clients in certain legal matters.",
            "Bailiff": "A court officer responsible for maintaining order in the courtroom and executing court orders.",
            "Notary Public": "A public officer authorized to witness the signing of important documents and administer oaths.",
            "Affidavit": "A written statement made under oath and signed in the presence of a notary public or other authorized official.",
            "Lawsuit": "A legal dispute between two or more parties that is resolved through a formal court process.",
            "Solicitor": "A legal professional who provides legal advice, prepares legal documents, and represents clients in certain legal matters.",
            "Bailiff": "A court officer responsible for maintaining order in the courtroom and executing court orders.",
            "Notary Public": "A public officer authorized to witness the signing of important documents and administer oaths.",
            "Affidavit": "A written statement made under oath and signed in the presence of a notary public or other authorized official.",
            "Liability": "Legal responsibility or obligation for one's actions or debts.",
            "Executor": "A person appointed to carry out the terms of a will and administer the estate of a deceased person.",
            "Intestate": "The condition of dying without a valid will, resulting in the distribution of assets according to state law.",
            "Grand Jury": "A group of citizens convened to review evidence and decide whether to issue indictments in criminal cases.",
            "Writ": "A formal written order issued by a court, typically used to command a specific action.",
            "Perjury": "The act of intentionally lying or making false statements while under oath in a legal proceeding.",
            "Subpoena": "A legal order requiring a person to attend a deposition, produce documents, or testify in a legal proceeding.",
            "Custody": "The legal right and responsibility to care for and make decisions on behalf of a child.",
            "Acquittal": "A legal judgment that declares a defendant not guilty of the charges brought against them.",
            "Class Action": "A lawsuit filed by a group of individuals with similar claims or grievances against a common defendant.",
        }

    def display_legal_document_templates(self):
            print("\nLegal Document Templates:")
            print("1. Contract Template")
            print("2. Will Template")
            print("3. Power of Attorney Template")
            print("4. Lease Agreement Template")
            print("5. Non-Disclosure Agreement Template")
            print("6. Employment Agreement Template")

            while True:
                template_choice = input("Enter the number of the template you want to access (0 to go back): ").strip()
                if template_choice == '0':
                    break
                elif template_choice == '1':
                    self.display_contract_template()
                elif template_choice == '2':
                    self.display_will_template()
                elif template_choice == '3':
                    self.display_power_of_attorney_template()
                elif template_choice == '4':
                    self.display_lease_agreement_template()
                elif template_choice == '5':
                    self.display_non_disclosure_agreement_template()
                elif template_choice == '6':
                    self.display_employment_agreement_template()
                else:
                    print("Invalid choice. Please select a valid template.")

    def start_assistant(self):
        print("Welcome to the Legal Information Robot!")
        print("Please provide some information about yourself to get started.")
        self.collect_user_info()

    def collect_user_info(self):
        print("\nUser Information:")
        self.user_info["name"] = input("Name: ")
        self.user_info["age"] = input("Age: ")
        self.user_info["language"] = input("Preferred language: ")
        self.display_services()

    def display_services(self):
        print("\nSelect the type of service you need:")
        print("1. Get Information About a Legal Right")
        print("2. Legal FAQs")
        print("3. Get Information About a Legal Advocate")
        print("4. Store a Document")
        print("5. Retrieve a Document")
        print("6. Income Tax Calculator")
        print("7. Legal Glossary")
        print("8. Legal Chatbot")
        print("9. Legal Compliance Checklist")
        print("10. Legal Hotline")
        print("11. Generate Legal Document")
        print("0. Go back")

        choice = input("Please select a command (1/2/3/4/5/6/7/8/9/10/11/0): ").strip()

        if choice == "1":
            self.get_information_about_legal_right()
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

    def launch_legal_chatbot(self):
        print("\nLaunching the Legal Chatbot...")
        print("You can now interact with the Legal Chatbot for legal assistance.")
        while True:
            user_input = input("You: ")
            if user_input.lower() in ['exit', 'quit', 'bye']:
                print("Legal Chatbot: Goodbye!")
                break
            response = self.generate_response(user_input)
            print(f"Legal Chatbot: {response}")

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



    def generate_legal_document(self):
        print("\nLegal Document Generator:")
        print("Available Document Types:")
        print("1. Contract")
        print("2. Will")
        print("3. Power of Attorney")
        print("4. Lease Agreement")
        print("5. Non-Disclosure Agreement")
        print("6. Employment Agreement")

        while True:
            document_type = input("Enter the number of the document type you want to generate (0 to go back): ").strip()
            if document_type == '0':
                break
            elif document_type == '1':
                self.generate_contract()
            elif document_type == '2':
                self.generate_will()
            elif document_type == '3':
                self.generate_power_of_attorney()
            elif document_type == '4':
                self.generate_lease_agreement()
            elif document_type == '5':
                self.generate_non_disclosure_agreement()
            elif document_type == '6':
                self.generate_employment_agreement()
            else:
                print("Invalid choice. Please select a valid document type.")


    def display_legal_hotlines(self):
        print("\nLegal Hotlines for India:")
        print("1. Legal Aid India Hotline: 1800-123-4567")
        print("2. National Human Rights Commission (NHRC) Helpline: 14433")
        print("3. Women Helpline: 1091")
        print("4. Child Helpline: 1098")
        print("5. Anti-Corruption Helpline: 1031")
        print("6. National Legal Services Authority (NALSA) Helpline: 15100")
        print("7. Cyber Crime Helpline: 155260")
        print("8. National Commission for Women (NCW) Helpline: 7217735372")
        print("9. National Consumer Helpline: 1800-11-4000")
        print("10. Human Rights Law Network (HRLN) Helpline: +91-11-2437 4910")
        print("11. National Commission for Protection of Child Rights (NCPCR) Helpline: 1800-11-5433")
        print("12. National Women's Helpline (NWH): 181")
        print("13. Senior Citizens Helpline: 1291")
        print("14. Anti-Discrimination and Equality Helpline: 011-23387508")
        print("15. Labour Helpline: 155214")
        print("16. Legal Services Authority of India: 15100")
        print("17. National Human Rights Commission (NHRC) Toll-Free Complaint Number: 14433")
        print("18. National Legal Aid Services: 15100")
        print("19. National Legal Services Authority (NALSA) Helpline for Free Legal Aid: 15100")
        print("20. National Commission for Scheduled Castes (NCSC) Toll-Free Helpline: 1800-180-6763")
        print("21. National Commission for Scheduled Tribes (NCST) Helpline: 1800-11-6565")
        print("22. Drug De-Addiction and Rehabilitation Helpline: 1800-11-0031")
        print("23. National Disaster Management Helpline: 1078")
        print("24. Women's Helpline for Domestic Violence: 181")
        print("25. National Commission for Minorities (NCM) Helpline: 1800-11-0088")
        print("26. Environment Helpline: 1800-11-2515")
        print("27. Mental Health Helpline: 1860-2662-345")
        print("28. Helpline for Persons with Disabilities: 1800-11-7708")
        print("29. HIV/AIDS Helpline: 1097")
        print("30. Legal Services Authority for Juveniles: 15103")
        print("31. Legal Services Authority for Senior Citizens: 15110")
        print("32. National Anti-Doping Agency (NADA) Helpline: 1800-11-0000")
        print("33. Trafficking in Persons (TIP) Helpline: 1800-123-6600")
        print("34. Cyber Security Helpline: 155260")
        print("35. Road Safety Helpline: 1033")
        print("36. Corruption Complaints Helpline: 1031")
        print("37. Financial Fraud Helpline: 155260")
        print("38. Narcotics Control Bureau (NCB) Helpline: 1800-11-2436")
        print("39. National Commission for Protection of Child Rights (NCPCR) Toll-Free Helpline: 1800-121-2830")
        print("40. District Legal Services Authority (DLSA): Varies by district")
        print("41. National Commission for Safai Karamcharis (NCSK) Helpline: 1800-11-7766")
        print("42. Legal Aid Clinic for Women: Varies by location")
        print("43. Women's Helpline for Police Assistance: 1096")
        print("44. National Legal Services Authority (NALSA) Childline: 1098")
        print("45. National Disaster Management Authority (NDMA) Helpline: 1078")
        print("46. National Commission for Women (NCW) WhatsApp Helpline: 7217735372")
        print("47. Senior Citizens Welfare Helpline: 1291")
        print("48. Women's Legal Aid Cell: Varies by location")
        print("49. Child Rights and You (CRY) Helpline: 1800-11-7552")
        print("50. National Legal Services Authority (NALSA) Mental Health Helpline: 15102")
        print("51. National Commission for Minorities (NCM) WhatsApp Helpline: 9868396148")
        print("52. Senior Citizens Helpline for Legal Aid: 1800-180-1253")
        print("53. Human Rights Law Network (HRLN) Toll-Free Helpline: 1800-274-1288")
        print("54. Child Rights Helpline for Adoption: 011-23077824")
        print("55. Domestic Violence Support Helpline: 1091")
        print("56. Legal Aid Helpline for Tribal Communities: Varies by state")
        print("57. Legal Services Authority for the Disabled: 15106")
        print("58. National Human Rights Commission (NHRC) WhatsApp Helpline: 9868104901")
        print("59. Women's Legal Support Helpline: 011-23713607")
        print("60. Road Accident Helpline: 1073")
        print("61. Legal Aid Helpline for Minorities: Varies by state")
        print("62. National Commission for Safai Karamcharis (NCSK) WhatsApp Helpline: 9811049634")
        print("63. National Commission for Women (NCW) Legal Aid Helpline: 011-23954732")
        print("64. Legal Services Authority for Senior Citizens (WhatsApp): 9519840144")
        print("65. Human Trafficking Helpline: 1800-11-6878")
        print("66. National Anti-Doping Agency (NADA) WhatsApp Helpline: 8826631271")
        print("67. Consumer Rights Helpline: 1800-11-4000")
        print("68. Juvenile Justice Legal Aid Helpline: Varies by location")
        print("69. Child Labor Helpline: 1098")
        print("70. Domestic Violence Legal Support: Varies by state")
        print("71. Women and Child Support Helpline: 1091")
        print("72. Helpline for Missing and Exploited Children: 1098")
        print("73. Right to Information (RTI) Helpline: 155300")
        print("74. Cyberbullying and Online Harassment Helpline: Varies by state")
        print("75. Environmental Legal Aid Helpline: 1800-11-3155")
        print("76. Legal Services Authority for LGBTQ+ Community: Varies by location")
        print("77. Mental Health Support Helpline: 1800-233-3330")
        print("78. National Commission for Safai Karamcharis (NCSK) Legal Aid Helpline: 011-2467 2927")
        print("79. Legal Services Authority for Persons with Disabilities (WhatsApp): 8800447997")
        print("80. National Commission for Women (NCW) WhatsApp Helpline for Cyberbullying: 7217735372")
        print("81. Employment and Labor Rights Helpline: Varies by location")
        print("82. Legal Aid Helpline for Farmers: Varies by state")
        print("83. National Commission for Scheduled Castes (NCSC) WhatsApp Helpline: 9868233842")
        print("84. Child Protection Helpline: 1098")
        print("85. Anti-Trafficking Helpline: 1800-11-8484")
        print("86. Legal Services Authority for Persons with Disabilities: 15107")
        print("87. Legal Services Authority for Senior Citizens (WhatsApp): 9519840144")
        print("88. Human Rights Law Network (HRLN) WhatsApp Helpline: 8587980173")
        print("89. Legal Aid Helpline for HIV/AIDS Patients: Varies by state")
        print("90. Helpline for Orphans and Destitute Children: 1098")
        print("91. Women and Child Support Helpline for Pregnancy Assistance: 1091")
        print("92. Helpline for the Visually Impaired: 155204")
        print("93. Legal Aid Helpline for Persons with Mental Disabilities: Varies by location")
        print("94. National Commission for Women (NCW) Child Support Helpline: 1098")
        print("95. Helpline for Elderly Abuse: 1253")
        print("96. Legal Services Authority for Persons with Autism: Varies by location")
        print("97. Legal Aid Helpline for Human Rights Violations: 011-2435 9527")
        print("98. Child Helpline for Street Children: 1098")
        print("99. Helpline for Persons with Intellectual Disabilities: 1800-111-550")
        print("100. Legal Services Authority for Animal Welfare: Varies by location")


    def legal_compliance_checklist(self):
        print("\nLegal Compliance Checklist:")
        compliance_items = [
            "1. Review and understand local and national laws relevant to your situation.",
            "2. Ensure that any legal documents or contracts are drafted and executed correctly.",
            "3. Comply with tax laws and report income accurately.",
            "4. Protect sensitive information and respect confidentiality agreements.",
            "5. Be aware of your legal rights and responsibilities.",
            "6. Obtain necessary permits and licenses for your business or activities.",
            "7. Keep accurate and organized financial records.",
            "8. Comply with labor laws and employment regulations.",
            "9. Ensure workplace safety and adhere to occupational health standards.",
            "10. Maintain proper documentation for employee hiring and termination.",
            "11. Adhere to environmental protection laws and regulations.",
            "12. Comply with data protection and privacy laws (e.g., GDPR, CCPA).",
            "13. Respect copyright and intellectual property rights.",
            "14. Implement anti-discrimination and anti-harassment policies.",
            "15. Follow antitrust and competition laws.",
            "16. Adhere to advertising and marketing regulations.",
            "17. Comply with food safety and hygiene standards (if applicable).",
            "18. Ensure product labeling and packaging meet legal requirements.",
            "19. Abide by import/export laws and trade regulations.",
            "20. Handle and dispose of hazardous materials safely.",
            "21. Maintain proper records for tax deductions and credits.",
            "22. Comply with zoning and land use regulations.",
            "23. Report and pay any applicable excise or customs duties.",
            "24. Adhere to securities and financial market regulations (if applicable).",
            "25. Comply with intellectual property licensing agreements.",
            "26. Follow legal requirements for employee benefits and insurance.",
            "27. Protect consumer rights and ensure fair business practices.",
            "28. Comply with healthcare regulations (if applicable).",
            "29. Adhere to building codes and construction permits (if applicable).",
            "30. Respect indigenous land rights and cultural heritage (if applicable).",
            "31. Comply with international trade sanctions (if applicable).",
            "32. Follow anti-money laundering and anti-corruption laws.",
            "33. Ensure proper disposal of electronic waste (e-waste).",
            "34. Abide by export control restrictions (if applicable).",
            "35. Comply with bankruptcy and insolvency laws (if applicable).",
            "36. Adhere to immigration laws for hiring foreign workers (if applicable).",
            "37. Protect employee and customer personal data.",
            "38. Comply with contract and agreement terms.",
            "39. Follow industry-specific regulations (e.g., healthcare, aviation).",
            "40. Ensure fair and transparent pricing practices.",
            "41. Adhere to real estate laws and property rights.",
            "42. Comply with import safety and product standards.",
            "43. Follow transportation and shipping regulations (if applicable).",
            "44. Protect whistleblowers and provide a safe reporting mechanism.",
            "45. Comply with tax filing deadlines and requirements.",
            "46. Ensure fair lending and financial services practices (if applicable).",
            "47. Abide by e-commerce and online business regulations (if applicable).",
            "48. Maintain compliance with workplace diversity and inclusion standards.",
            "49. Comply with cybersecurity and data breach notification laws.",
            "50. Follow any legal requirements related to disaster preparedness and recovery."

        ]
        for item in compliance_items:
            print(item)


    def display_legal_glossary(self):
        print("\nLegal Glossary")

        while True:
            term = input("Enter a legal term to look up (or '0' to go back): ").strip()
            if term == '0':
                break
            elif term in self.legal_glossary:
                definition = self.legal_glossary[term]
                print(f"{term}: {definition}")
            else:
                print("Term not found in the glossary. Please enter a valid legal term.")

    def income_tax_calculator(self):
        print("\nIncome Tax Calculator")
        try:
            income = float(input("Enter your annual income: "))
            if income < 0:
                print("Income cannot be negative.")
                return


            tax_rate = 0.2  
            tax_amount = income * tax_rate

            print(f"Tax Amount: {tax_amount}")
        except ValueError:
            print("Invalid input. Please enter a valid income amount.")

    def get_information_about_legal_right(self):
        print("\nAvailable Legal Rights:")
        for idx, legal_right in enumerate(self.legal_rights, start=1):
            print(f"{idx}. {legal_right}")

        try:
            choice = int(input("Enter the number of the legal right you want information about (0 to go back): "))
            if 0 < choice <= len(self.legal_rights):
                legal_right = list(self.legal_rights.keys())[choice - 1]
                info = self.legal_rights[legal_right]
                print(f"{legal_right}: {info}")
            elif choice == 0:
                return
            else:
                print("Invalid choice. Please select a valid legal right.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    def display_legal_faqs(self):
        print("\nCommon Legal FAQs:")
        for key, value in self.FAQS.items():
            print(f"{key}. {value['question']}")

        while True:
            question_number = input("Enter the number of the FAQ you want to view, or '0' to go back: ")
            if question_number == '0':
                break
            if question_number in self.FAQS:
                print(self.FAQS[question_number]['answer'])
            else:
                print("Invalid FAQ number. Please enter a valid FAQ number.")

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


if __name__ == "__main__":
    legal_info_robot = LegalInfoRobot()
    legal_info_robot.start_assistant()  
