from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Variabel untuk menyimpan skor
skor = 0

# Data kuis
kuis = {
    "Matematika": [
        {"pertanyaan": "Berapa hasil dari 5 + 3?", "jawaban": "8"},
        {"pertanyaan": "20 - 7 = ...", "jawaban": "13"}
    ],
    "IPA": [
        {"pertanyaan": "Apa fungsi daun pada tumbuhan?", "jawaban": "fotosintesis"},
        {"pertanyaan": "Sebutkan hewan yang hidup di air dan darat!", "jawaban": "katak"}
        ],
     "Seni": [
        {"pertanyaan": "Apa warna primer?", "jawaban": "merah, kuning, biru"},
        {"pertanyaan": "Apa nama alat musik tradisional dari Bali?", "jawaban": "gamelan"}
    ],
    "Bahasa Inggris": [
        {"pertanyaan": "Apa arti kata 'apple' dalam Bahasa Indonesia?", "jawaban": "apel"},
        {"pertanyaan": "Sebutkan satu nama hewan dalam Bahasa Inggris!", "jawaban": "cat"}
    
    ],
}

@app.route("/")
def home():
    return render_template("index.html", kuis=kuis.keys())

@app.route("/kategori/<kategori>", methods=["GET", "POST"])
def kategori(kategori):
    global skor
    pertanyaan_list = kuis.get(kategori, [])
    if request.method == "POST":
        jawaban = request.form.get("jawaban").lower()
        index = int(request.form.get("index"))
        if jawaban == pertanyaan_list[index]["jawaban"].lower():
            skor += 10
        if index + 1 < len(pertanyaan_list):
            return render_template("quiz.html", kategori=kategori, index=index + 1, pertanyaan=pertanyaan_list[index + 1]["pertanyaan"], skor=skor)
        return redirect(url_for("hasil"))
    return render_template("quiz.html", kategori=kategori, index=0, pertanyaan=pertanyaan_list[0]["pertanyaan"], skor=skor)

@app.route("/hasil")
def hasil():
    global skor
    hasil_skor = skor
    skor = 0  # Reset skor untuk sesi berikutnya
    return render_template("hasil.html", skor=hasil_skor)

if __name__ == "__main__":
    app.run(debug=True)
