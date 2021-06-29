import streamlit as st
import streamlit.components.v1 as stc
from readExcel import get_email_rows
from sendEmails import send_email
import pandas as pd




def main():
    app_pass = st.secrets['APP_PASS']
    email_user = st.secrets['EMAIL_USER']
    email_pass = st.secrets['EMAIL_PASS']
    st.title("Send Project Emails")

    with st.form(key='enterPass'):
        t = st.empty
        t.text_input("Enter el password. Or do you not know it?", type='password')
        submit_button = st.form_submit_button(label='Submit')

    if submit_button:
        if t == app_pass:
            with st.form(key='uploadExcel'):
                excel_file = st.file_uploader("Upload Excel file", type=['xlsx'])
                submit_button = st.form_submit_button(label='Submit')

            if submit_button:
                status = st.empty()
                status.text(f'reading Excel file. Just one moment....')
                status.write(get_email_rows(excel_file))





    # with st.form(key='my_form'):
        # username_input = st.text_input('Email Username')
        # password_input = st.text_input("Email Password")
        # subject_input = st.text_input("Email Subject")
        # body_input = st.text_area("Email Body")
        # to_input = st.text_input("Email recipients")
        # submit_button = st.form_submit_button(label='Submit')

        # st.subheader("Email Username")
        # username_input = st.text_input()
        # password_input = st.text_input("somegreatpassword95")
        # subject_input = st.text_input("Please don't read my email")
        # body_input = st.text_area("Okay this has to be a large text box")
        # to_input = st.text_input("paradondequieresmandaresto@gmail.com")

        #image_file = st.file_uploader("Upload Image", type=['png', 'jpeg', 'jpg'])

        # if image_file is not None:
        #     # To See Details
        #     # st.write(type(image_file))
        #     #st.write(dir(image_file))
        #     file_details = {"Filename": image_file.name, "FileType": image_file.type, "FileSize": image_file.size}
        #     st.write(file_details)
        #
        #     img = image_file
        #
        #
        #     img = load_image(image_file)
        #     st.image(img)



if __name__ == '__main__':
    main()