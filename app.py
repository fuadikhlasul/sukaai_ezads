import streamlit as st
import requests
import re
import json

def generate(**params):
    API_BASE_URL = 'https://internal-alb-galilei-preprod-private-221671690.ap-southeast-3.elb.amazonaws.com/v1'
    API_KEY = 'app-doqtZJT09Wlau8D1nUB3JVVB'

    headers = {
        'Authorization': f'Bearer {API_KEY}',
        'Content-Type': 'application/json'
    }

    prompt = '''
    Tolong beri maksimal 5 opsi konten iklan yang sangat cocok untuk kanal SMS atau WhatsApp.
    Pastikan keyword atau kata-katanya persuasif, mendorong audience untuk engage dengan konten, dan bisa jadi konten viral.
    Pastikan juga keyword yang digunakan sedikit clickbait dan mudah diingat dengan jargon-jargon yang sesuai dengan produk.
    Konten iklan ini dibuat untuk bisnis {} bernama "{}" dengan produknya yaitu "{}".
    Tujuan dari iklan ini yaitu "{}", kemudian gunakan bahasa yang mudah dicerna dan fit dengan target audience dengan
    segmen usia "{}".
    '''.format(params['lob'], params['biz_name'], params['ads_about'], params['ad_purpose'], params['base_segment'])

    payload = {
        'inputs': {},
        'query': prompt,
        'response_mode': 'blocking',
        'conversation_id': '',
        'user': 'sukaai_ezads_client_001',
        'files': []
    }

    response = requests.post(f'{API_BASE_URL}/chat-messages', headers=headers, json=payload, verify=False)

    if response.status_code == 200:
        return json.loads(response.text)['answer']
    else:
        return {'status': response.status_code, 'message': response.text}

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
        st.success('Berikut adalah 5 top picks konten dengan capaian iklan tertinggi: \n' + str(result))

if __name__ == '__main__':
    main()
