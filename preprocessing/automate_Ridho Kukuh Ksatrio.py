import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import os

def run_preprocessing(input_path, output_folder):
    # Cek apakah file input ada di root
    if not os.path.exists(input_path):
        print(f"Error: {input_path} tidak ditemukan!")
        return

    df = pd.read_csv(input_path)
    df = df.dropna()

    def categorize_popularity(score):
        if score <= 33: return 0
        elif score <= 66: return 1
        else: return 2

    df['pop_category'] = df['popularity'].apply(categorize_popularity)

    cols_to_drop = ['track_id', 'track_name', 'artist', 'album', 'release_date', 'popularity']
    df_model = df.drop(cols_to_drop, axis=1)

    X = df_model.drop('pop_category', axis=1)
    y = df_model['pop_category']

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)

    cleaned_df = pd.DataFrame(X_train_scaled, columns=X.columns)
    cleaned_df['pop_category'] = y_train.values

    # Buat folder jika belum ada
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Simpan dengan nama yang konsisten untuk YAML
    output_path = os.path.join(output_folder, 'spotify_preprocessing.csv')
    cleaned_df.to_csv(output_path, index=False)
    print(f"Berhasil! Data disimpan di: {output_path}")

if __name__ == "__main__":
    # Path ini harus sesuai dengan struktur folder di GitHub
    run_preprocessing('spotify_analysis_dataset.csv', 'preprocessing')
