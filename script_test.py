import os
import time
import threading
import tkinter as tk
from tkinter import ttk, messagebox

# --- CONFIGURAÇÕES DO TESTE / TEST SETTINGS ---
BLOCK_SIZE = 16 * 1024 * 1024  # 16MB blocks / Blocos de 16MB
TEST_FILE = "ssd_test_file.bin"

class SSDTester:
    def __init__(self, root):
        self.root = root
        self.root.title("SSD Capacity Tester")
        self.root.geometry("450x220")

        # Centralizar elementos / UI Layout
        self.main_frame = tk.Frame(root, padx=20, pady=20)
        self.main_frame.pack(expand=True, fill="both")

        self.progress = ttk.Progressbar(self.main_frame, length=400, mode='determinate')
        self.progress.pack(pady=10)

        self.label = tk.Label(self.main_frame, text="Pronto / Ready", font=("Arial", 10))
        self.label.pack(pady=5)

        self.start_button = tk.Button(self.main_frame, text="Iniciar Teste / Start Test", command=self.start_test, bg="#e1e1e1", padx=10)
        self.start_button.pack(pady=10)

    def generate_block(self, index):
        """
        Gera um bloco único para evitar compressão.
        Generates a unique block to prevent drive compression/caching.
        """
        pattern = f"BLOCK_{index}_SSD_TEST_DATA_VERIFICATION".encode()
        data = pattern * (BLOCK_SIZE // len(pattern) + 1)
        return data[:BLOCK_SIZE]

    def run_test(self):
        total_written = 0
        start_time = time.time()
        
        # Bloquear botão / Disable button
        self.start_button.config(state="disabled")

        try:
            # FASE 1: GRAVAÇÃO / PHASE 1: WRITING
            self.label.config(text="Gravando... / Writing...")
            with open(TEST_FILE, "wb") as f:
                while True:
                    data = self.generate_block(total_written)
                    try:
                        f.write(data)
                        f.flush() 
                    except OSError:
                        # Disco cheio / Disk full
                        break
                    
                    total_written += 1
                    self.progress["value"] = total_written % 100
                    self.label.config(text=f"Bloco / Block {total_written} (~{ (total_written * 16) / 1024:.2f} GB)")
                    self.root.update()

            # FASE 2: VERIFICAÇÃO / PHASE 2: VERIFICATION
            self.label.config(text="Verificando... / Verifying...")
            self.progress["value"] = 0
            self.root.update()
            
            first_error = None
            with open(TEST_FILE, "rb") as f:
                for i in range(total_written):
                    expected = self.generate_block(i)
                    data = f.read(BLOCK_SIZE)

                    if data != expected and first_error is None:
                        first_error = i

                    self.progress["value"] = (i / total_written) * 100 if total_written > 0 else 100
                    self.root.update()

            # RESULTADOS / RESULTS
            size_gb = (total_written * BLOCK_SIZE) / (1024**3)
            
            if first_error is not None:
                real_gb = (first_error * BLOCK_SIZE) / (1024**3)
                res_pt = f"⚠️ Possível SSD Falso!\nCapacidade real: {real_gb:.2f} GB"
                res_en = f"⚠️ Possible Fake SSD!\nReal capacity: {real_gb:.2f} GB"
            else:
                res_pt = f"✅ Sucesso! {size_gb:.2f} GB verificados."
                res_en = f"✅ Success! {size_gb:.2f} GB verified."

            messagebox.showinfo("Resultado / Result", f"{res_pt}\n\n{res_en}")

        except Exception as e:
            messagebox.showerror("Erro / Error", str(e))
        
        finally:
            self.label.config(text="Finalizado / Finished")
            self.start_button.config(state="normal")
            self.progress["value"] = 0

    def start_test(self):
        thread = threading.Thread(target=self.run_test, daemon=True)
        thread.start()

if __name__ == "__main__":
    root = tk.Tk()
    app = SSDTester(root)
    root.mainloop()