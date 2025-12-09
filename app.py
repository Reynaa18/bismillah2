import streamlit as st
import json
import os

# ================================
# DATABASE
# ================================
DATA_FILE = "database.json"

def load_db():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            data = json.load(f)
        if "konseling" not in data:
            data["konseling"] = []
        if "solusi" not in data:
            data["solusi"] = {}
        return data
    return {"konseling": [], "solusi": {}}

def save_db(db):
    with open(DATA_FILE, "w") as f:
        json.dump(db, f, indent=4)

db = load_db()

# ================================
# AKUN GURU
# ================================
GURU_ACCOUNTS = {
    "dewi@guru.com": "12345",
    "ika@guru.com": "12345",
    "maya@guru.com": "12345",
    "muna@guru.com": "12345",
    "pandan@guru.com": "12345",
    "pipit@guru.com": "12345"
}

# ================================
# SIDEBAR NAVIGASI
# ================================
st.sidebar.title("Navigation")
menu = st.sidebar.radio(
    "Pilih Halaman:",
    ["Halaman Utama", "Profil Guru", "Materi BK", "Program BK", "Siswa", "Guru"]
)

# ================================
# HOME
# ================================
if menu == "Halaman Utama":
    st.title("𝐖𝐞𝐛𝐬𝐢𝐭𝐞 𝐁𝐢𝐦𝐛𝐢𝐧𝐠𝐚𝐧 𝐊𝐨𝐧𝐬𝐞𝐥𝐢𝐧𝐠")
    # List foto
    images = ["images/sekolah1.png", "images/sekolah2.png"]
# Slider untuk geser foto
    slide = st.slider("Bimbingan Konseling SMAN 24 Bandung", 0, len(images)-1, 0)
# Tampilkan foto sesuai posisi slider
    st.image(images[slide], use_container_width=True)
    st.header("𝐒𝐞𝐥𝐚𝐦𝐚𝐭 𝐃𝐚𝐭𝐚𝐧𝐠 𝐃𝐢 𝐛𝐢𝐦𝐛𝐢𝐧𝐠𝐚𝐧 𝐊𝐨𝐧𝐬𝐞𝐥𝐢𝐧𝐠")
    st.write("Selamat datang di Portal Layanan BK Sekolah, platform terpadu yang dirancang untuk membantu siswa dalam mengakses layanan konseling secara lebih mudah, cepat, dan aman.")
    st.write("Melalui sistem ini, siswa dapat melakukan konsultasi online maupun offline, sementara guru BK dapat memantau permintaan, memberikan layanan, dan menyusun catatan konseling secara lebih terstruktur.")
    st.subheader("𝐓𝐮𝐣𝐮𝐚𝐧 𝐏𝐥𝐚𝐭𝐟𝐨𝐫𝐦")
    st.markdown("""
    1. Mempermudah siswa mengajukan konseling kapan saja dan di mana saja.
    2. Mempercepat proses pengelolaan janji temu antara siswa dan guru BK.
    3. Menyediakan dokumentasi layanan konseling secara digital.
    4. Membangun komunikasi yang lebih responsif antara siswa dan guru.
    """)
    st.subheader("𝐋𝐚𝐲𝐚𝐧𝐚𝐧 𝐲𝐚𝐧𝐠 𝐓𝐞𝐫𝐬𝐞𝐝𝐢𝐚")
    st.markdown("1. Konseling Online")
    st.write("Cocok untuk siswa yang ingin menyampaikan permasalahan tanpa harus bertemu langsung. Siswa dapat menjelaskan situasi, memilih jenis masalah, dan guru akan memberikan respons serta solusi secara digital")
    st.markdown("2. Konseling Offline")
    st.write("Layanan pertemuan langsung di ruang BK. Siswa dapat memilih tanggal, hari, dan jam yang diinginkan, lalu guru akan menerima notifikasi untuk meninjau permintaan tersebut.")
    st.subheader("𝐀𝐤𝐬𝐞𝐬 𝐮𝐧𝐭𝐮𝐤 𝐒𝐢𝐬𝐰𝐚 𝐝𝐚𝐧 𝐆𝐮𝐫𝐮 𝐁𝐊")
    st.markdown("Siswa")
    st.markdown("""
    1. Mengisi identitas
    2. Memilih layanan
    3. Menjelaskan permasalahan atau menjadwalkan konsultasi
    4. Menunggu solusi atau konfirmasi jadwal
    """)
    st.markdown("Guru BK")
    st.markdown(""""
    1. Login menggunakan akun terdaftar
    2. Melihat daftar permintaan konseling terbaru
    3. Memberikan solusi (untuk layanan online)
    4. Mencatat hasil pertemuan (offline)
    5. Menerima notifikasi otomatis dari siswa
    """)
    st.subheader("𝐂𝐚𝐫𝐚 𝐌𝐞𝐧𝐠𝐠𝐮𝐧𝐚𝐤𝐚𝐧 𝐖𝐞𝐛𝐬𝐢𝐭𝐞")
    st.markdown("""
    1. Buka menu Login sebagai Siswa/Guru
    2. Pilih role yang sesuai
    3. Isi formulir dengan lengkap
    4. Klik Kirim Permintaan
    5. Guru BK akan menerima notifikasi otomatis
    6. Lihat status layanan di dashboard
    """)
    st.subheader("𝐏𝐞𝐧𝐲𝐢𝐦𝐩𝐚𝐧𝐚𝐧 𝐃𝐚𝐭𝐚 𝐃𝐢𝐠𝐢𝐭𝐚𝐥")
    st.write("Semua data layanan tersimpan aman dalam sistem dan hanya dapat diakses oleh pihak yang berwenang. Data meliputi")
    st.markdown("""
    1. Identitas pemohon layanan
    2. Permintaan konsultasi
    3. Jadwal tatap muka
    4. Solusi dari guru BK
    5. Riwayat layanan
    """)
    st.subheader("𝐊𝐨𝐦𝐢𝐭𝐦𝐞𝐧 𝐊𝐚𝐦𝐢")
    st.write("Kami berkomitmen untuk menghadirkan layanan BK yang:")
    st.markdown("""
    1. Responsif
    2. Profesional
    3. Aman dan rahasia
    4. Mudah digunakan oleh seluruh siswa
    """)
    st.info("Data disimpan lokal pada file data.json.")


# ================================
# PROFIL GURU
# ================================
elif menu == "Profil Guru":
    st.title("𝐏𝐫𝐨𝐟𝐢𝐥 𝐆𝐮𝐫𝐮 𝐁𝐊")
    st.image("images/budewi.jpg", use_container_width=True)
    st.image("images/buika.jpg", use_container_width=True)
    st.image("images/bumaya.jpg", use_container_width=True)
    st.image("images/bumuna.jpg", use_container_width=True)
    st.image("images/bupandan.jpg", use_container_width=True)
    st.image("images/bupipit.jpg", use_container_width=True)


# ================================
# MATERI BK
# ================================
elif menu == "Materi BK":
    st.title("📘 𝐌𝐚𝐭𝐞𝐫𝐢 𝐁𝐢𝐦𝐛𝐢𝐧𝐠𝐚𝐧 & 𝐊𝐨𝐧𝐬𝐞𝐥𝐢𝐧𝐠")

    st.subheader("1. 𝐏𝐞𝐦𝐚𝐡𝐚𝐦𝐚𝐧 𝐃𝐢𝐫𝐢")
    st.write("""
    Materi ini membantu siswa mengenal potensi, karakter, kelebihan, dan kekurangan diri.
    Tujuannya supaya siswa mampu membuat keputusan yang baik dalam belajar maupun kehidupan sehari-hari.
    """)

    st.subheader("2. 𝐏𝐞𝐫𝐞𝐧𝐜𝐚𝐧𝐚𝐚𝐧 𝐊𝐚𝐫𝐢𝐫")
    st.write("""
    Siswa dibimbing untuk mengenal minat, bakat, serta peluang karir dan pendidikan lanjutan.
    Materi ini sering mencakup pengisian angket minat, informasi jurusan, dan diskusi pilihan masa depan.
    """)

    st.subheader("3. 𝐊𝐞𝐭𝐞𝐫𝐚𝐦𝐩𝐢𝐥𝐚𝐧 𝐛𝐞𝐥𝐚𝐣𝐚𝐫")
    st.write("""
    Berisi strategi belajar efektif, manajemen waktu, cara mencatat, teknik fokus, dan persiapan ujian.
    Guru BK membantu siswa menemukan gaya belajar yang cocok.
    """)

    st.subheader("4. 𝐇𝐮𝐛𝐮𝐧𝐠𝐚𝐧 𝐒𝐨𝐬𝐢𝐚𝐥")
    st.write("""
    Membahas cara berkomunikasi yang baik, memahami perasaan orang lain, mengatasi konflik, 
    serta membangun hubungan sehat dengan teman dan keluarga.
    """)

    st.subheader("5.  𝐊𝐞𝐬𝐞𝐡𝐚𝐭𝐚𝐧 𝐌𝐞𝐧𝐭𝐚𝐥 𝐃𝐚𝐬𝐚𝐫")
    st.write("""
    Menjelaskan cara mengelola stres, kecemasan ringan, tekanan belajar, dan cara meminta bantuan ketika butuh dukungan.
    Tidak menggantikan psikolog, tetapi membantu siswa memahami tanda-tanda awal masalah emosional.
    """)

    st.subheader("6. 𝐄𝐭𝐢𝐤𝐚 𝐃𝐢𝐠𝐢𝐭𝐚𝐥 & 𝐌𝐞𝐝𝐢𝐚 𝐒𝐨𝐬𝐢𝐚𝐥l")
    st.write("""
    Membahas cara menggunakan internet secara sehat, aman, dan bertanggung jawab. Termasuk cyberbullying,
    literasi digital, dan menjaga privasi online.
    """)

    st.subheader("7. 𝐏𝐞𝐧𝐠𝐞𝐦𝐛𝐚𝐧𝐠𝐚𝐧 𝐊𝐚𝐫𝐚𝐤𝐭𝐞𝐫")
    st.write("""
    Fokus pada nilai seperti disiplin, tanggung jawab, kerja sama, menghargai perbedaan, dan empati.
    Materi ini membantu siswa membangun kepribadian positif.
    """)

# ================================
# PROGRAM BK
# ================================
elif menu == "Program BK":
    st.title("📑 𝐏𝐫𝐨𝐠𝐫𝐚𝐦 𝐁𝐢𝐦𝐛𝐢𝐧𝐠𝐚𝐧 & 𝐊𝐨𝐧𝐬𝐞𝐥𝐢𝐧𝐠 𝐒𝐞𝐤𝐨𝐥𝐚𝐡")

    st.subheader("1. 𝐋𝐚𝐲𝐚𝐧𝐚𝐧 𝐎𝐫𝐢𝐞𝐧𝐭𝐚𝐬𝐢")
    st.write("""
    Program untuk mengenalkan siswa baru kepada lingkungan sekolah, tata tertib, guru, dan fasilitas.
    Tujuannya membuat siswa merasa nyaman dan cepat beradaptasi.
    """)

    st.subheader("2. 𝐋𝐚𝐲𝐚𝐧𝐚𝐧 𝐈𝐧𝐟𝐨𝐫𝐦𝐚𝐬𝐢")
    st.write("""
    Memberikan informasi penting terkait akademik, jurusan, karir, lomba, kegiatan ekstrakurikuler,
    hingga beasiswa. Informasi diberikan dalam bentuk presentasi, poster, atau sesi konseling.
    """)

    st.subheader("3. 𝐋𝐚𝐲𝐚𝐧𝐚𝐧 𝐊𝐨𝐧𝐬𝐞𝐥𝐢𝐧𝐠 𝐈𝐧𝐝𝐢𝐯𝐝𝐮")
    st.write("""
    Guru BK membantu siswa yang ingin berdiskusi secara pribadi mengenai masalah belajar,
    pertemanan, keluarga, maupun rencana masa depan.
    """)

    st.subheader("4. 𝐋𝐚𝐲𝐚𝐧𝐚𝐧 𝐊𝐨𝐧𝐬𝐞𝐥𝐢𝐧𝐠 𝐊𝐞𝐥𝐨𝐦𝐩𝐨𝐤")
    st.write("""
    Kegiatan konseling secara berkelompok dengan topik tertentu, misalnya cara belajar, komunikasi,
    kesulitan adaptasi, atau motivasi diri.
    """)

    st.subheader("5. 𝐋𝐚𝐲𝐚𝐧𝐚𝐧 𝐁𝐢𝐦𝐛𝐢𝐧𝐠𝐚𝐧 𝐊𝐥𝐚𝐬𝐢𝐤𝐚𝐥")
    st.write("""
    Guru BK masuk kelas secara terjadwal untuk memberikan materi pengembangan diri,
    motivasi, etika digital, dan berbagai topik lain yang mendukung perkembangan siswa.
    """)

    st.subheader("6. 𝐋𝐚𝐲𝐚𝐧𝐚𝐧 𝐏𝐞𝐧𝐞𝐦𝐩𝐚𝐭𝐚𝐧 𝐝𝐚𝐧 𝐏𝐞𝐧𝐲𝐚𝐥𝐮𝐫𝐚𝐧")
    st.write("""
    Program untuk membantu siswa memilih jurusan, ekstrakurikuler, atau penempatan kegiatan yang sesuai
    dengan minat dan bakat mereka.
    """)

    st.subheader("7. 𝐋𝐚𝐲𝐚𝐧𝐚𝐧 𝐊𝐨𝐧𝐬𝐮𝐥𝐭𝐚𝐬𝐢 𝐝𝐞𝐧𝐠𝐚𝐧 𝐎𝐫𝐚𝐧𝐠 𝐓𝐮𝐚")
    st.write("""
    Guru BK bekerja sama dengan orang tua untuk berdiskusi tentang perkembangan siswa dan mencari solusi terbaik
    ketika ada masalah akademik maupun perilaku.
    """)

    st.subheader("8. 𝐏𝐫𝐨𝐠𝐫𝐚𝐦 𝐏𝐞𝐧𝐜𝐞𝐠𝐚𝐡𝐚𝐧")
    st.write("""
    Berisi kegiatan seperti penyuluhan anti-bullying, anti narkoba, edukasi keamanan digital,
    serta kampanye menjaga kesehatan mental.
    """)

# ================================
# FORM SISWA
# ================================
elif menu == "Siswa":
    st.title("𝐅𝐨𝐫𝐦 𝐊𝐨𝐧𝐬𝐞𝐥𝐢𝐧𝐠 𝐒𝐢𝐬𝐰𝐚")

    st.subheader("𝐃𝐚𝐭𝐚 𝐃𝐢𝐫𝐢")
    nama = st.text_input("Nama")
    kelas = st.text_input("Kelas")
    wa = st.text_input("Nomor WA / HP")

    st.subheader("𝐏𝐢𝐥𝐢𝐡 𝐆𝐮𝐫𝐮 𝐁𝐊")
    guru = st.selectbox("Pilih Guru", ["Bu Dewi", "Bu Ika", "Bu Maya", "Bu Muna", "Bu Pandan", "Bu Pipit"])

    st.subheader("𝐏𝐢𝐥𝐢𝐡 𝐌𝐞𝐭𝐨𝐝𝐞 𝐊𝐨𝐧𝐬𝐞𝐥𝐢𝐧𝐠")
    mode = st.radio("Jenis Konseling:", ["Online", "Offline"])

    if mode == "Online":
        masalah = st.text_area("Ceritakan masalahmu:")
        tanggal = "-"
        jam = "-"
    else:
        masalah = "-"
        tanggal = st.date_input("Pilih Tanggal")
        jam = st.time_input("Pilih Jam")

    if st.button("Kirim"):
        if nama and kelas and wa:
            db["konseling"].append({
                "nama": nama,
                "kelas": kelas,
                "wa": wa,
                "guru": guru,
                "mode": mode,
                "masalah": masalah,
                "tanggal": str(tanggal),
                "jam": str(jam),
            })
            save_db(db)
            st.success("Data berhasil dikirim!")
        else:
            st.error("Harap isi semua data diri terlebih dahulu.")

    # ============================
    # TOMBOL CEK SOLUSI SISWA ONLINE
    # ============================
    if mode == "Online" and nama and kelas:
        if st.button("Cek Solusi"):
            # key konsisten: strip + lowercase
            solusi_key = f"{nama.strip().lower()}_{kelas.strip().lower()}"
            # reload database untuk memastikan solusi terbaru terbaca
            db = load_db()
            solusi_text = db.get("solusi", {}).get(solusi_key, "")
            if solusi_text:
                st.subheader("Solusi dari Guru BK:")
                st.info(solusi_text)
            else:
                st.info("Belum ada solusi dari guru untuk saat ini.")

# ================================
# HALAMAN GURU (LOGIN + DASHBOARD)
# ================================
elif menu == "Guru":
    st.title("𝐋𝐨𝐠𝐢𝐧 𝐆𝐮𝐫𝐮 𝐁𝐊")

    # Inisialisasi session state
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False
    if "guru_email" not in st.session_state:
        st.session_state.guru_email = ""

    # LOGIN
    if not st.session_state.logged_in:
        email = st.text_input("Email")
        pwd = st.text_input("Password", type="password")

        if st.button("Login"):
            if email in GURU_ACCOUNTS and GURU_ACCOUNTS[email] == pwd:
                st.session_state.logged_in = True
                st.session_state.guru_email = email
                st.success("Login berhasil!")
            else:
                st.error("Email atau password salah!")

    # DASHBOARD GURU
    if st.session_state.logged_in:
        guru_login = st.session_state.guru_email
        st.success(f"Login sebagai: {guru_login}")

        map_guru = {
            "dewi@guru.com": "Bu Dewi",
            "ika@guru.com": "Bu Ika",
            "maya@guru.com": "Bu Maya",
            "muna@guru.com": "Bu Muna",
            "pandan@guru.com": "Bu Pandan",
            "pipit@guru.com": "Bu Pipit"
        }
        nama_guru = map_guru.get(guru_login, "")

        st.subheader("Siswa Konseling untuk Anda:")

        data_saya = [d for d in db["konseling"] if d["guru"] == nama_guru]

        if len(data_saya) == 0:
            st.info("Belum ada siswa yang memilih Anda.")
        else:
            if "solusi" not in db:
                db["solusi"] = {}

            for i, d in enumerate(data_saya):
                with st.expander(f"{d['nama']} - ({d['mode']})"):
                    st.write("Nama:", d["nama"])
                    st.write("Kelas:", d["kelas"])
                    st.write("Nomor WA:", d["wa"])
                    st.write("Mode:", d["mode"])
                    st.write("Permasalahan:", d["masalah"])
                    st.write("Tanggal:", d["tanggal"])
                    st.write("Jam:", d["jam"])

                    # Memberi solusi (online)
                    if d["mode"] == "Online":
                        st.write("### Berikan Solusi untuk Siswa ini")
                        solusi_key = f"{d['nama'].strip().lower()}_{d['kelas'].strip().lower()}"

                        if f"solusi_text_{i}" not in st.session_state:
                            st.session_state[f"solusi_text_{i}"] = db["solusi"].get(solusi_key, "")

                        st.session_state[f"solusi_text_{i}"] = st.text_area(
                            "Tulis solusi:",
                            value=st.session_state[f"solusi_text_{i}"],
                            key=f"solusi_text_area_{i}"   # <-- FIX ID DUPLIKAT
                        )

                        # Tombol simpan solusi unik
                        if st.button(f"Simpan Solusi {i}"):
                            # pastikan session state terambil saat tombol ditekan
                            solusi_isi = st.session_state[f"solusi_text_{i}"]
                            db["solusi"][solusi_key] = solusi_isi
                            save_db(db)
                            st.success("Solusi berhasil disimpan!")
                            st.rerun()  # reload agar solusi siswa langsung bisa baca

                        # Tampilkan solusi jika sudah ada
                        if solusi_key in db["solusi"]:
                            st.info(f"Solusi yang sudah diberikan:\n{db['solusi'][solusi_key]}")

        # Logout
        if st.button("Logout"):
            st.session_state.logged_in = False
            st.session_state.guru_email = ""
            st.rerun()