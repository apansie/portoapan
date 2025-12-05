from flask import Flask, render_template

app = Flask(__name__)

# Data Portfolio berdasarkan CV
portfolio_data = {
    'personal_info': {
        'name': 'Muhammad Andrean Javantara',
        'title': 'Full Stack Developer & Data Analyst',
        'location': 'Surabaya, Jawa Timur, Indonesia',
        'email': 'ajavantara@gmail.com',
        'phone': '+62 856 4205 8221',
        'linkedin': 'https://www.linkedin.com/in/muhammad-andrean-javantara-514484250',
        'bio': 'Mahasiswa Teknik Informatika Universitas Negeri Surabaya dengan fokus pada Data Science, Software Engineering, dan Cybersecurity. Berpengalaman dalam pengembangan aplikasi full-stack, analisis data berbasis machine learning, penetration testing, serta manajemen proyek IT.'
    },
    
    'competencies': [
        {
            'icon': 'laptop-code',
            'title': 'Full-Stack Development',
            'description': 'Pengembangan aplikasi frontend dan backend'
        },
        {
            'icon': 'chart-line',
            'title': 'Data Science & Analytics',
            'description': 'Analisis statistik dan predictive modeling'
        },
        {
            'icon': 'robot',
            'title': 'Machine Learning',
            'description': 'Model ML untuk prediksi dan automasi'
        },
        {
            'icon': 'shield-alt',
            'title': 'Cybersecurity',
            'description': 'Penetration testing & vulnerability assessment'
        },
        {
            'icon': 'video',
            'title': 'Video Production',
            'description': 'Editing profesional dan content creation'
        },
        {
            'icon': 'bullhorn',
            'title': 'Digital Marketing',
            'description': 'Campaign management dan social media'
        },
        {
            'icon': 'tasks',
            'title': 'Project Management',
            'description': 'Metodologi Agile dan koordinasi tim'
        },
        {
            'icon': 'cogs',
            'title': 'Business Process',
            'description': 'Optimasi workflow dan efisiensi'
        }
    ],
    
    'skills': {
        'programming': ['JavaScript', 'Python', 'HTML/CSS', 'C++'],
        'frontend': ['React.js', 'Bootstrap', 'Responsive Design', 'UI/UX Design'],
        'backend': ['Node.js', 'MySQL', 'RESTful APIs', 'Firebase'],
        'data_analysis': ['Python (Pandas, NumPy)', 'Matplotlib', 'R Studio', 'SPSS', 'Excel', 'Matlab'],
        'video_editing': ['Adobe Premiere Pro', 'DaVinci Resolve', 'VN Editor', 'Alight Motion', 'CapCut'],
        'project_management': ['Agile Methodology', 'Scrum', 'Trello', 'Asana'],
        'digital_marketing': ['Social Media Marketing', 'Campaign Management', 'SEO'],
        'tools': ['Figma', 'Canva', 'WordPress', 'Microsoft Office']
    },
    
    'experience': [
        {
            'title': 'Studi Independen — Cybersecurity & Penetration Testing',
            'company': 'PT VINIX SEVEN AURUM',
            'period': '2025 (Ongoing)',
            'location': '',
            'descriptions': [
                'Melakukan vulnerability assessment pada target legal menggunakan Burp Suite dan tools pentesting lainnya',
                'Mengerjakan modul kerentanan: XSS, SQL Injection, CSRF, Directory Traversal, Authentication Bypass',
                'Membangun laporan serangan profesional untuk kebutuhan industri',
                'Melakukan simulasi eksploitasi menggunakan metode black box & grey box',
                'Menganalisis traffic jaringan dan struktur aplikasi web untuk menemukan celah keamanan',
                'Membuat proof-of-concept serangan berbasis web dan automasi pemindaian dasar'
            ]
        },
        {
            'title': 'Sales Marketing & Finance',
            'company': 'KS&K',
            'period': '2019 - Sekarang',
            'location': 'Surabaya',
            'descriptions': [
                'Mengembangkan sistem pengarsipan data yang meningkatkan efisiensi pengambilan data hingga 40%',
                'Membuat strategi digital marketing multi-platform yang menaikkan engagement rate hingga 35%',
                'Koordinasi tim lintas divisi untuk kelancaran operasional dan pencapaian target',
                'Berkontribusi pada pertumbuhan revenue year-over-year melalui optimasi proses bisnis',
                'Mengelola campaign management dengan ROI tracking yang terukur'
            ]
        },
        {
            'title': 'Freelance Video Editor',
            'company': 'LDR Agency',
            'period': '2021 - 2023',
            'location': 'Remote',
            'descriptions': [
                'Editing konten short-form yang meningkatkan retention rate hingga 50%',
                'Membuat template standar untuk branding consistency di semua platform',
                'Mengoptimalkan workflow editing agar lebih efisien dengan mengurangi production time 30%',
                'Menghasilkan 100+ video konten berkualitas tinggi untuk berbagai platform media sosial'
            ]
        },
        {
            'title': 'Freelance Video Editor',
            'company': 'AF Agency',
            'period': '2022 - 2023',
            'location': 'Remote',
            'descriptions': [
                'Membuat template video reusable yang mempercepat proses produksi hingga 40%',
                'Mengubah long-form ke short-form untuk kebutuhan marketing dengan engagement rate tinggi',
                'Quality control konten sebelum distribusi dengan tingkat approval 95%',
                'Kolaborasi dengan tim creative untuk menghasilkan konten yang align dengan brand identity'
            ]
        },
        {
            'title': 'Editor & Administrator',
            'company': 'Class',
            'period': '2019 - 2023',
            'location': 'Surabaya',
            'descriptions': [
                'Mengelola produksi video dari konsep hingga publikasi dengan timeline yang ketat',
                'Membuat dokumentasi dan laporan kerja terstruktur untuk tracking progress proyek',
                'Implementasi sistem manajemen data internal yang meningkatkan efisiensi tim 25%',
                'Supervisi terhadap 5+ project concurrent dengan success rate 100%'
            ]
        },
        {
            'title': 'Administrasi Asisten (Freelance)',
            'company': 'PT Jodya Wood Furniture',
            'period': '2014 - 2017',
            'location': '',
            'descriptions': [
                'Mengelola pencatatan keuangan dan payroll untuk 20+ karyawan dengan akurasi 100%',
                'Memastikan ketepatan laporan finansial dan budget tracking secara real-time',
                'Mengkoordinasikan alur data administrasi antar departemen',
                'Implementasi sistem filing yang terorganisir untuk kemudahan akses dokumen'
            ]
        }
    ],
    
    'projects': [
        {
            'title': 'Sistem Prediksi Cuaca Berbasis Machine Learning',
            'period': '2025',
            'descriptions': [
                'Membangun model prediksi cuaca dengan akurasi 85% menggunakan algoritma machine learning',
                'Mengolah dataset 50+ titik data meteorologi menggunakan Python (Pandas, NumPy, Scikit-learn)',
                'Membuat dashboard UI interaktif untuk visualisasi hasil prediksi real-time',
                'Melakukan dokumentasi lengkap untuk publikasi dan reproducibility',
                'Implementasi data preprocessing dan feature engineering untuk optimasi model'
            ],
            'tech': ['Python', 'Machine Learning', 'Data Analytics', 'Statistical Modeling', 'Pandas', 'NumPy']
        },
        {
            'title': 'Pengembangan Aplikasi Edukasi BelajarIN',
            'period': 'Februari 2025 - Mei 2025',
            'descriptions': [
                'Membangun aplikasi edukasi dengan fitur multi-role (guru, siswa, orang tua)',
                'Implementasi forum diskusi real-time, presensi digital, nilai, dan manajemen tugas',
                'Integrasi Firebase Authentication & Firestore untuk data management',
                'Melakukan testing dan perbaikan berkelanjutan dengan user feedback loop',
                'Mendukung 20+ pengguna aktif secara bersamaan dengan performa optimal',
                'Mencapai user satisfaction rate 80% melalui UX design yang user-centered'
            ],
            'tech': ['React.js', 'Node.js', 'Firebase', 'Full Stack Development', 'UX Design']
        },
        {
            'title': 'Penjualan & Administrasi Organisasi Siswa (OSIS)',
            'period': 'Agustus 2017 - Februari 2020',
            'descriptions': [
                'Membuat strategi fundraising yang meningkatkan pemasukan organisasi sebesar 45%',
                'Memimpin pelaksanaan acara sekolah skala besar dengan 500+ peserta',
                'Mengelola dana organisasi dengan transparan dan akuntabilitas penuh',
                'Koordinasi dengan 10+ divisi untuk sinkronisasi program kerja',
                'Implementasi sistem pelaporan keuangan digital untuk transparansi'
            ],
            'tech': ['Event Management', 'Financial Planning', 'Team Leadership', 'Fundraising']
        },
        {
            'title': 'Inisiatif Marketing Produk Kreatif',
            'period': 'Januari 2019 - Juni 2019',
            'descriptions': [
                'Mengembangkan strategi marketing yang compelling dengan fokus customer engagement',
                'Mengeksekusi transaksi penjualan profesional dengan customer-centric approach',
                'Mencapai rating kepuasan pelanggan tinggi melalui excellent service',
                'Implementasi teknik dialog pelanggan yang efektif untuk closing rate optimal',
                'Analisis feedback pelanggan untuk continuous improvement produk dan layanan'
            ],
            'tech': ['Customer Engagement', 'Sales Excellence', 'Marketing Strategy']
        }
    ],
    
    'education': [
        {
            'degree': 'Teknik Informatika',
            'school': 'Universitas Negeri Surabaya',
            'period': '2023 - Sekarang',
            'descriptions': [
                'Mempertahankan performa akademik yang kuat sambil aktif berpartisipasi dalam proyek tim',
                'Mengkoordinasikan multiple proyek pengembangan software dengan tim lintas fungsi',
                'Mengembangkan metodologi problem-solving lanjutan melalui pengalaman hands-on',
                'Fokus pembelajaran: Data Science, Software Engineering, dan Cybersecurity'
            ]
        },
        {
            'degree': 'SMA Wachid Hasyim 5 Surabaya',
            'school': 'SMA Wachid Hasyim 5',
            'period': 'Juli 2020 - Mei 2023',
            'descriptions': [
                'Mendemonstrasikan keterampilan koordinasi yang luar biasa sebagai project leader OSIS',
                'Memfasilitasi distribusi materi edukasi yang efektif antara guru dan siswa',
                'Aktif dalam berbagai kegiatan organisasi dan kepemimpinan'
            ]
        }
    ],
    
    'achievements': [
        'SEMI FINALIS Business Proposal - Kompetisi Noble National UNESA FMIPA (2025)',
        'Kompetisi Karya Tulis Ilmiah Nasional - LKTIN FMIPA Unesa (2024)',
        'Sertifikasi Perencanaan Karir IT (2024)',
        'Program Pengembangan Kepemimpinan - LKMM-TD (2024)',
        'Sertifikasi Public Speaking & Entrepreneurship (2024)',
        'Program Pengembangan Future Entrepreneur FEST (2024)'
    ]
}

@app.route('/')
def home():
    return render_template('index.html', data=portfolio_data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
