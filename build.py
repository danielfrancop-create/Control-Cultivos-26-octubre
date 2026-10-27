#!/usr/bin/env python3
"""
Finca Los Sauces - Script de Ensamblado Automático de Previsualización (build.py)
Lee todas las plantillas individuales y las consolida en assembled_preview.txt
"""

import os

def assemble_preview():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    index_path = os.path.join(base_dir, 'index.txt')

    if not os.path.exists(index_path):
        print("Error: No se encontró index.txt")
        return

    index_content = open(index_path, 'r', encoding='utf-8').read()

    includes = {
        "<?!= include('Styles'); ?>": 'Styles.txt',
        "<?!= include('Header'); ?>": 'Header.txt',
        "<?!= include('ViewDashboard'); ?>": 'ViewDashboard.txt',
        "<?!= include('ViewPOS'); ?>": 'ViewPOS.txt',
        "<?!= include('ViewCashflow'); ?>": 'ViewCashflow.txt',
        "<?!= include('ViewLoans'); ?>": 'ViewLoans.txt',
        "<?!= include('ViewPersonalExpenses'); ?>": 'ViewPersonalExpenses.txt',
        "<?!= include('ViewMap'); ?>": 'ViewMap.txt',
        "<?!= include('Modals'); ?>": 'Modals.txt',
        "<?!= include('JavaScript'); ?>": 'JavaScript.txt'
    }

    assembled = index_content
    for tag, filename in includes.items():
        filepath = os.path.join(base_dir, filename)
        if os.path.exists(filepath):
            file_content = open(filepath, 'r', encoding='utf-8').read()
            assembled = assembled.replace(tag, file_content)
        else:
            print(f"Advertencia: Archivo {filename} no encontrado.")

    preview_path = os.path.join(base_dir, 'assembled_preview.txt')
    with open(preview_path, 'w', encoding='utf-8') as f:
        f.write(assembled)

    print(f"¡Éxito! assembled_preview.txt generado correctamente ({len(assembled)} bytes).")

if __name__ == '__main__':
    assemble_preview()
