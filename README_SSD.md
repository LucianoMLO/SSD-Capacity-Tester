# **SSD Capacity Tester 🛡️💾**

Este utilitário foi desenvolvido para verificar a **capacidade real** de armazenamento de SSDs, cartões SD e Pendrives.

**Note:** The English version of this documentation is available below the Portuguese section.

## **🇧🇷 Português**

### **🚩 O Problema**

Muitos dispositivos de armazenamento vendidos online a preços muito baixos são falsificados. Eles informam ao sistema que possuem, por exemplo, 2TB, mas possuem apenas 64GB. Quando você ultrapassa o limite real, o dispositivo apaga dados antigos ou corrompe os novos.

### **🛡️ Por que este script?**

Este script é **código aberto e transparente**. Você pode ler cada linha e até pedir para uma IA explicar o que ele faz, garantindo que não há vírus, ao contrário de testadores duvidosos da internet.

### **📸 Interface do Programa**

Ao rodar o script, você verá uma barra de progresso e o status em tempo real:

### **🚀 Como usar (Passo a Passo)**

#### **1\. Instalar o Python**

1. Acesse [python.org](https://www.python.org/downloads/).  
2. Baixe o instalador e **marque a caixa "Add Python to PATH"** antes de instalar.

#### **2\. Obter o Script (run\_test.py)**

* **Opção A:** Baixe o arquivo run\_test.py direto deste repositório (botão "Download raw file").  
* **Opção B:** Copie o código, cole no **Bloco de Notas** e salve como run\_test.py (selecionando "Todos os arquivos" no tipo).  
* **Importante:** Coloque o arquivo **dentro da unidade** que deseja testar.

#### **3\. Executar o Teste**

1. Na pasta do SSD, clique na barra de endereços, digite cmd e dê Enter.  
2. Digite: python run\_test.py e aperte Enter.  
3. Clique em **"Iniciar Teste"**.

### **🧹 Limpeza**

Após o teste, apague o arquivo ssd\_test\_file.bin ou formate a unidade (Botão direito no SSD \> Formatar \> Formatação Rápida).

## **🇺🇸 English**

### **🚩 The Problem**

Many storage devices sold online at very low prices are counterfeit. They report a fake capacity (e.g., 2TB) while physically having much less (e.g., 64GB). Once you exceed the real capacity, the device overwrites old data or corrupts new files.

### **🛡️ Why this script?**

This script is **open-source and transparent**. You can read every line or ask an AI to explain it, ensuring it is safe and virus-free, unlike many shady testers found online.

### **📸 Program Interface**

When running the script, you will see a progress bar and real-time status:

### **🚀 How to use (Step by Step)**

#### **1\. Install Python**

1. Go to [python.org](https://www.python.org/downloads/).  
2. Download the installer and **check the "Add Python to PATH" box** before installing.

#### **2\. Get the Script (run\_test.py)**

* **Option A:** Download the run\_test.py file directly from this repository ("Download raw file" button).  
* **Option B:** Copy the code, paste it into **Notepad**, and save it as run\_test.py (select "All Files" in the file type).  
* **Important:** Save or move the file **inside the drive** you want to test.

#### **3\. Run the Test**

1. Inside the SSD folder, click the address bar, type cmd, and press Enter.  
2. Type: python run\_test.py and press Enter.  
3. Click **"Start Test"**.

### **🧹 Cleanup**

After the test, delete the ssd\_test\_file.bin file or format the drive (Right-click SSD \> Format \> Quick Format).

## **🧠 Dica Extra / Extra Tip**

Se tiver dúvidas, cole o código no Gemini/ChatGPT / If you have doubts, paste the code into Gemini/ChatGPT:

*"Descreva por partes o que este código faz e verifique se ele é seguro."*

*"Explain step by step what this code does and verify if it is safe."*

*Criado para garantir transparência e segurança nos testes de hardware.*