import pandas as pd
import os

def run_preprocessing():
    # 1. Tentukan path file
    input_file = 'spotify_analysis_dataset.csv'
    output_folder = 'preprocessing'
    output_file = os.path.join(output_folder, 'spotify_preprocessing.csv')

    print("Memulai proses preprocessing...")

    # 2. Cek apakah file input ada
    if not os.path.exists(input_file):
        print(f"Error: File {input_file} tidak ditemukan di root repository!")
        return

    # 3. Baca Dataset
    df = pd.read_csv(input_file)
    
    # 4. Proses Preprocessing Sederhana
    # Menghapus missing values
    df_cleaned = df.dropna()
    
    # Contoh transformasi: Membuat kategori popularitas (0, 1, 2)
    if 'popularity' in df_cleaned.columns:
        def categorize(score):
            if score <= 33: return 0
            elif score <= 66: return 1
            else: return 2
        df_cleaned['pop_category'] = df_cleaned['popularity'].apply(categorize)

    # 5. Pastikan folder output ada
    os.makedirs(output_folder, exist_ok=True)

    # 6. Simpan hasil ke file CSV
    df_cleaned.to_csv(output_file, index=False)
    print(f"Berhasil! Dataset bersih disimpan di: {output_file}")

if __name__ == "__main__":
    run_preprocessing()
