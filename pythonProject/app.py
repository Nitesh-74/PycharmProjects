import streamlit as st
import pickle
import string
import pandas as pd


import nltk
nltk.download('stopwords')

from nltk.corpus import stopwords
stopwords.words('english')

from nltk.stem.porter import PorterStemmer

ps = PorterStemmer()



st.sidebar.title("SMS DETECTION SYSTEM")

image_path = "/Users/nites/Downloads/sms_sidebar.png"

st.sidebar.image(image_path)


st.sidebar.markdown("<br>", unsafe_allow_html=True)

user_menu = st.sidebar.radio(
    'Select an Option',
    ('Introduction','Testing','Analysis','Register')
)


if user_menu == 'Introduction' :

    st.markdown('<h1 class="centered"><b>Smishing</b></h1>', unsafe_allow_html=True)
    st.write("Smishing is a social engineering attack that uses fake mobile text messages to trick people into downloading malware, sharing sensitive information, or sending money to cybercriminals. The term “smishing” is a combination of “SMS”—or “short message service,” the technology behind text messages—and “phishing.”Smishing is an increasingly popular form of cybercrime. According to Proofpoint’s 2023 State of the Phish report (link resides outside ibm.com), 76 percent of organizations experienced smishing attacks in 2022. Several factors have contributed to a rise in smishing. For one, the hackers perpetrating these attacks, sometimes called “smishers,” know that victims are likelier to click on text messages than other links.")

    image_path = "/Users/nites/Downloads/smishing01.jpg"
    st.image(image_path)

    st.write(" At the same time, advances in spam filters have made it harder for other forms of phishing, like emails and phone calls, to reach their targets. The increase of bring-your-own-device (BYOD) and remote work arrangements have also led to more people using their mobile devices at work, making it easier for cybercriminals to access company networks through employees’ cell phones.")
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    st.header("How smishing attacks work ")
    st.write("Smishing attacks are similar to other types of phishing attacks, in which scammers use phony messages and malicious links to fool people into compromising their mobile phones, bank accounts, or personal data. The only main difference is the medium. In smishing attacks, scammers use SMS or messaging apps to conduct their cybercrimes rather than emails or phone calls.")
    image_path = "/Users/nites/Downloads/SMISHING-ATTACK-PHASES.png"
    st.image(image_path)
    st.write(" Scammers choose smishing over other types of phishing attacks for various reasons. Perhaps most importantly, research shows that people are likelier to click links in text messages. Klaviyo reports that SMS click-through rates hover between 8.9 percent and 14.5 percent (link resides outside ibm.com). By comparison, emails have an average click rate of only 1.33 percent, according to Constant Contact (link resides outside ibm.com). In addition, scammers can increasingly mask the origins of smishing messages using tactics like spoofing phone numbers with burner phones or utilizing software to send texts via email. It's also harder to spot dangerous links on cell phones. For instance, on a computer, users can hover over a link to see where it leads, but on smartphones, they don't have that option. People are also used to banks and brands contacting them over SMS and receiving shortened URLs in text messages.In 2020, the Federal Communications Commission (FCC) mandated that telecom companies adopt the STIR/SHAKEN protocol (link resides outside ibm.com), which authenticates phone calls and is the reason why some mobile phones now display scam likely or spam likely messages when suspicious numbers call. But even though STIR/SHAKEN made scam calls easier to spot, it did not have the same effect on text messages, leading many scammers to shift their focus to smishing attacks.")

    st.header("Examples of smishing scams ")
    st.write("Like other forms of social engineering, most types of smishing attacks rely on pretexting, which involves using fake stories to manipulate victims’ emotions and trick them into doing a scammer’s bidding.Pretending to be a financial institution. Scammers may pose as the victim’s bank alerting them to a problem with their account, often through a fake notification. ")
    image_path = "/Users/nites/Downloads/smsexample.png"
    st.image(image_path)
    st.write ("If the victim clicks the link, it brings them to a fake website or app that steals sensitive financial information like PINs, login credentials, passwords, and bank account or credit card information. In 2018, a group of scammers (link resides outside ibm.com) used this method to steal USD 100,000 from Fifth Third Bank customers.Pretending to be the government.Scammers may pretend to be police officers, IRS representatives, or other government officials. These smishing texts often claim the victim owes a fine or must act to claim a government benefit. For example, at the height of the COVID-19 pandemic, the Federal Trade Commission (FTC) warned of smishing attacks (link resides outside ibm.com) that offered tax relief, free COVID tests, and similar services. When victims followed links in these texts, scammers stole their social security numbers and other information they could use to commit identity theft.")
    image_path = "/Users/nites/Downloads/smsexample03.jpg"
    st.image(image_path)
    st.write (" Pretending to be customer supportAttackers pose as customer support agents at trusted brands and retailers like Amazon, Microsoft, or even the victim’s wireless provider. They usually say there is a problem with the victim’s account or an unclaimed reward or refund. Typically, these texts send the victim to a fake website that steals their credit card numbers or banking information.Pretending to be a shipper.These smishing messages claim to come from a shipping company like FedEx, UPS, or the US Postal Service. They tell the victim there was a problem delivering a package and asks them to pay a “delivery fee” or sign in to their account to correct the issue. Of course, the scammers take the money or account information and run. These scams are common around the holidays when many people wait for packages. Pretending to be a boss or colleague.In business text compromise (similar to business email compromise, except via SMS message), hackers pretend to be a boss, coworker or colleague (e.g., vendor, attorney) who needs help with an urgent task. These scams often request immediate action and end with the victim sending money to the hackers.Pretending to text the wrong number.Scammers send a text that appears to be intended for someone other than the victim. When the victim corrects the scammer’s “mistake,” the scammer strikes up a conversation with the victim. These wrong number scams tend to be long-term, with the scammer trying to earn the victim’s friendship and trust through repeated contact over months or even years. The scammer may even pretend to develop romantic feelings for the victim. The goal is to eventually steal the victim’s money through a fake investment opportunity, a request for a loan, or a similar story.Pretending to be locked out of an account.In this scam, called multifactor authentication (MFA) fraud, a hackers who already has a victim's username and password tries to steal the verification code or one-time password required to access the victim's account. The hacker might pose as one of the victim’s friends, claim to have been locked out of their Instagram or Facebook account, and ask the victim to receive a code for them. The victim gets an MFA code—which is actually for their own account—and gives it to the hacker.Pretending to offer free apps.Some smishing scams trick victims into downloading seemingly legitimate apps—e.g., file managers, digital payment apps, even antivirus apps—that are in fact malware or ransomware.")

    st.markdown("<hr>",unsafe_allow_html=True)



if user_menu == 'Testing':
    def transform_text(text):
        text = text.lower()
        text = nltk.word_tokenize(text)

        y = []
        for i in text:
            if i.isalnum():
                y.append(i)

        text = y[:]
        y.clear()

        for i in text:
            if i not in stopwords.words('english') and i not in string.punctuation:
                y.append(i)

        text = y[:]
        y.clear()

        for i in text:
            y.append(ps.stem(i))

        return " ".join(y)


    tfidf = pickle.load(open('vectorizer2.pkl', 'rb'))
    model = pickle.load(open('model2.pkl', 'rb'))

    st.title("SMS Spam Classifier")


    input_sms = st.text_area("Enter the message")

    if st.button('Predict'):

        # 1. preprocess
        transformed_sms = transform_text(input_sms)
        # 2. vectorize
        vector_input = tfidf.transform([transformed_sms])
        # 3. predict
        result = model.predict(vector_input)[0]
        # 4. Display
        if result == 1:
            st.header("Spam")
        else:
            st.header("Not Spam")

if user_menu == 'Analysis':
    st.header("Country Wise Frauds")
    image_path = "/Users/nites/Downloads/c.jpg"
    st.image(image_path)
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    st.header("State SMS frauds")
    image_path = "/Users/nites/Downloads/statewisefraud.png"
    st.image(image_path)




if user_menu == 'Register':
    st.markdown(
        """
        <style>
            body {
                background-image: url('');
                background-size: cover;
            }
        </style>
        """,
        unsafe_allow_html=True
    )
    st.header("Register Your Sms")
    st.markdown("<br>", unsafe_allow_html=True)

    with st.form("Text Input Form"):
        # Add a text input widget to the form
        # Add a text input widget for name with placeholder
        name = st.text_input("Enter your name", help="e.g., Aryan pikkhan")

        # Add a text input widget for email with placeholder
        email = st.text_input("Enter your email", help="e.g., aryanpikkhan@gmail.com")

        # Add a text input widget for contact number with placeholder
        contact_number = st.text_input("Enter your contact number", help="e.g., +1234567890")

        text_input = st.text_area("Enter your SMS:")
        # Add a submit button to the form
        submit_button = st.form_submit_button("Submit")
        if submit_button:
            # Process the user input when the form is submitted

            st.markdown(
                """
                <style>
                    [data-testid="stFormSubmitButton"] {
                        color: green !important;
                    }
                </style>
                """,
                unsafe_allow_html=True
            )
            st.write("User Information:")
            user_data = {'Name': [name], 'Email': [email], 'Contact Number': [contact_number] , 'SMS': [text_input]}
            user_df = st.table(user_data)