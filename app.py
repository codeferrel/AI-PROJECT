import os

# 1. Database jadwal kamu (bisa dikembangkan pakai database beneran nanti)
JADWAL_SAYA = {
    "senin": "Senin malam kamu jadwalnya belajar Cyber Security (Penetration Testing/OSINT).",
    "selasa": "Selasa malam waktunya coding project aplikasi desktop + penetration testing .",
    "rabu": "Rabu malam fokus review materi jaringan dan persiapan sertifikasi.",
    "kamis": "Kamis malam penetration testing, lanjutin project RentBike.",
    "jumat": "Jumat malam belahar penetration testing , jangan lupa push commit ke GitHub!",
    "sabtu": "Sabtu belajar penetration testing + cari bug di vdp.",
    "minggu": "Minggu malam persiapan untuk evaluasi mingguan kuliah + belajar cyber dan pentesting ."
}

def ai_assistant(pertanyaan):
    # Mengubah input pertanyaan menjadi huruf kecil semua agar mudah dicocokkan
    pertanyaan = pertanyaan.lower()
    
    # Logika pencarian hari di dalam pertanyaan
    hari_ditemukan = None
    for hari in JADWAL_SAYA.keys():
        if hari in pertanyaan:
            hari_ditemukan = hari
            break
            
    # Respon dari AI
    if hari_ditemukan:
        return f"🤖 AI: {JADWAL_SAYA[hari_ditemukan]}"
    else:
        return "🤖 AI: Maaf, aku tidak menangkap nama hari dalam pertanyaanmu. Coba tanya seperti: 'jadwal hari senin apa?'"

# 3. Jalankan program secara interaktif di terminal
if __name__ == "__main__":
    print("=== AI Schedule Assistant Aktif ===")
    print("Ketik 'keluar' untuk menyudahi percakapan.\n")
    
    while True:
        user_input = input("User: ")
        if user_input.lower() == 'keluar':
            print("🤖 AI: Sampai jumpa! Semangat belajarnya!")
            break
            
        jawaban = ai_assistant(user_input)
        print(jawaban)
        print("-" * 40)
