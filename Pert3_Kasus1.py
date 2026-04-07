import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

barang_terjual = ctrl.Antecedent(np.arange(0, 101, 1), 'barang_terjual')
permintaan = ctrl.Antecedent(np.arange(0, 301, 1), 'permintaan')
harga_satuan = ctrl.Antecedent(np.arange(0, 100001, 1), 'harga_satuan')
keuntungan = ctrl.Antecedent(np.arange(0, 4000001, 1), 'keuntungan')
rekomendasi_stok = ctrl.Consequent(np.arange(0, 1001, 1), 'rekomendasi_stok')

barang_terjual['rendah'] = fuzz.trimf(barang_terjual.universe, [0, 0, 40])
barang_terjual['sedang'] = fuzz.trimf(barang_terjual.universe, [30, 50, 70])
barang_terjual['tinggi'] = fuzz.trimf(barang_terjual.universe, [60, 100, 100])

permintaan['rendah'] = fuzz.trimf(permintaan.universe, [0, 0, 100])
permintaan['sedang'] = fuzz.trimf(permintaan.universe, [50, 150, 250])
permintaan['tinggi'] = fuzz.trimf(permintaan.universe, [200, 300, 300])

harga_satuan['murah'] = fuzz.trimf(harga_satuan.universe, [0, 0, 40000])
harga_satuan['sedang'] = fuzz.trimf(harga_satuan.universe, [30000, 50000, 80000])
harga_satuan['mahal'] = fuzz.trimf(harga_satuan.universe, [60000, 100000, 100000])

keuntungan['rendah'] = fuzz.trimf(keuntungan.universe, [0, 0, 1000000])
keuntungan['sedang'] = fuzz.trimf(keuntungan.universe, [1000000, 2000000, 2500000])
keuntungan['banyak'] = fuzz.trapmf(keuntungan.universe, [1500000, 2500000, 4000000,4000000])

rekomendasi_stok['sedang'] = fuzz.trimf(rekomendasi_stok.universe, [100, 500, 900])
rekomendasi_stok['banyak'] = fuzz.trimf(rekomendasi_stok.universe, [600, 1000, 1000])

rule1 = ctrl.Rule(barang_terjual['tinggi'] & permintaan['tinggi'] & harga_satuan['murah'] & keuntungan['banyak'], rekomendasi_stok['banyak'])
rule2 = ctrl.Rule(barang_terjual['tinggi'] & permintaan['tinggi'] & harga_satuan['murah'] & keuntungan['sedang'], rekomendasi_stok['sedang'])
rule3 = ctrl.Rule(barang_terjual['tinggi'] & permintaan['sedang'] & harga_satuan['murah'] & keuntungan['sedang'], rekomendasi_stok['sedang'])
rule4 = ctrl.Rule(barang_terjual['sedang'] & permintaan['tinggi'] & harga_satuan['murah'] & keuntungan['sedang'], rekomendasi_stok['sedang'])
rule5 = ctrl.Rule(barang_terjual['sedang'] & permintaan['tinggi'] & harga_satuan['murah'] & keuntungan['banyak'], rekomendasi_stok['banyak'])
rule6 = ctrl.Rule(barang_terjual['rendah'] & permintaan['rendah'] & harga_satuan['sedang'] & keuntungan['sedang'], rekomendasi_stok['sedang'])

sistem_stok = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6])
simulasi_stok = ctrl.ControlSystemSimulation(sistem_stok)

simulasi_stok.input['barang_terjual'] = 80
simulasi_stok.input['permintaan'] = 255
simulasi_stok.input['harga_satuan'] = 25000
simulasi_stok.input['keuntungan'] = 3500000

simulasi_stok.compute()

hasil_rekomendasi_stok = simulasi_stok.output['rekomendasi_stok']
print("--- HASIL PERHITUNGAN LOGIKA FUZZY ---")
print(f"Barang Terjual : 80")
print(f"Permintaan : 255")
print(f"Harga per Item : 25.000")
print(f"Profit : 3.500.000")
print("--------------------------------------")
print(f"Jumlah Stok Makanan yang Direkomendasikan: {hasil_rekomendasi_stok:.2f} unit")

barang_terjual.view(sim=simulasi_stok)
permintaan.view(sim=simulasi_stok)
harga_satuan.view(sim=simulasi_stok)
keuntungan.view(sim=simulasi_stok)
rekomendasi_stok.view(sim=simulasi_stok)