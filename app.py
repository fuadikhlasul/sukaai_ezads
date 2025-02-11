import streamlit as st

def generate(**params):
    return params

def main():
    st.title('EZAds Simulator')

    with st.form('calcform'):
        ad_purpose_lov = [
            'Awareness', 
            'Event', 
            'Promo Pembelian', 
            'Promo Pendaftaran', 
            'Info Pelanggan', 
            'Layanan Masyarakat',
            'Pengingat / Reminder'
        ]

        lob_lov = [
            'Travel',
            'Sport & Fitness',
            'Restaurant',
            'Retail',
            'Religious',
            'Real Estate',
            'Legal',
            'Internet',
            'Technology',
            'Home Family',
            'Events',
            'Medical & Pharmacy',
            'Finance',
            'Non Profit',
            'Entertainment',
            'Education',
            'Beauty & Spa',
            'Automotive',
            'Others'
        ]

        base_segments = [
            'Boomers',
            'Millenials',
            'Gen-Z',
            'Gen Alpha'
        ]

        biz_name = st.text_input('Nama Bisnis: ', placeholder='Mie Ayam Pak Budi')
        ads_about = st.text_input('Produk atau Layanan: ', placeholder='Kuliner')
        ad_purpose = st.selectbox('Tujuan Iklan: ', ad_purpose_lov)
        lob = st.selectbox('Bidang Bisnis: ', lob_lov)
        base_segment = st.selectbox('Segmen Dasar: ', base_segments)

        input_args = {
            'biz_name': biz_name,
            'ads_about': ads_about,
            'ad_purpose': ad_purpose,
            'lob': lob,
            'base_segment': base_segment
        }

        submitted = st.form_submit_button('Generate!')
    
    if submitted:
        result = generate(**input_args)
        st.success('Result: ' + str(result))

if __name__ == '__main__':
    main()
